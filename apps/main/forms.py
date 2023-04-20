from django import forms 

from auths.models import ClientCustomUser


# class ClientForm(forms.ModelForm):
#     """Client form."""

#     class Meta:
#         model = ClientCustomUser
#         fields = ['email', 'first_name', 'last_name', 'password']