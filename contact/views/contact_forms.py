from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ValidationError

from contact.models import Contact
from django import forms

class ContactForm(forms.ModelForm):  #modelform: baseado num model, no caso o model ja existente pra contato
    class Meta:
        model = Contact
        fields = 'first_name','last_name', 'phone',

    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        self.add_error('first_name', ValidationError('Mensagem de erro', code='invalid'))
        return super().clean()


def create(request):
    if request.method == 'POST':
        # print(request.POST.get('first_name'))

        context = {
            'form': ContactForm(request.POST)
        }

        return render(
            request,
            'contact/create.html',
            context
        )

    context = {
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )