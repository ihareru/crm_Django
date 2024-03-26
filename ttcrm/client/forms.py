from django import forms

from .models import Client, Comment, ClientFile


class AddClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'contact_person', 'phone', 'email', 'address', 'description',)


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class AddFileForm(forms.ModelForm):
    class Meta:
        model = ClientFile
        fields = ('file',)
