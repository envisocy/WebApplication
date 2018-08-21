# -*- coding: utf-8 -*-
#!/usr/bin/python

__author__ = 'envisocy'
__date__ = '2018/8/10 14:25'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
	username = forms.CharField(required=True, min_length=3)
	password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True, min_length=6)
	captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
	
	
class ForgetForm(forms.Form):
	email = forms.EmailField(required=True)
	captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ResetForm(forms.Form):
	password = forms.CharField(required=True, min_length=6)


class ModifyPwdForm(forms.Form):
	password1 = forms.CharField(required=True, min_length=6)
	password2 = forms.CharField(required=True, min_length=6)
