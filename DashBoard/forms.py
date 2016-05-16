# coding: utf-8
__author__ = 'Lorgan Sherwood'

from django.forms import Form, ModelForm
from django.forms import inlineformset_factory
from django.contrib.auth.models import User

from .models import *

class UserForm(ModelForm):
   class Meta:
       model = User
       fields = ['username', 'email']

UserProBaseInline = inlineformset_factory(
    User,
    ProfileBasic,
    fields = ('realname', 'dob', 'gender',  'minority', 'party', 'department', 'firstwt', 'phone', 'address'),
)
