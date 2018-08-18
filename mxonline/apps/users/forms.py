# -*- coding: utf-8 -*-
#!/usr/bin/python

__author__ = 'envisocy'
__date__ = '2018/8/10 14:25'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
	username = forms.CharField(required=True, min_length=3)
	password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True, min_length=6)
	captcha = CaptchaField()
