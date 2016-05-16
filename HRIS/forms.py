# coding: utf-8
__author__ = 'Lorgan Sherwood'

from django.forms import Form, CharField, PasswordInput, TextInput


class LoginForm(Form):
    username = CharField(
        required = True,
        label = '用户名',
        max_length = 100,
        error_messages = {'required':'请输入用户名'},
        widget = TextInput(
            attrs = {
                'placeholder':'用户名',
                'class': 'form-control',
            }
        ),
    )
    password = CharField(
        required = True,
        label = '密码',
        error_messages = {'required':'请输入密码'},
        widget = PasswordInput(
            attrs = {
                'placeholder':'密码',
                'class': 'form-control',
            }
        ),
    )
