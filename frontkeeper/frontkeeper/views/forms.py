#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    All specifics forms used in frontkeeper
"""
from django import forms


class SearchForm(forms.Form):
    """
        Form with a charfield
    """
    search = forms.CharField(label='Search in password', max_length=100)


class PasswordForm(forms.Form):
    """
        Form with a password
    """
    password = forms.CharField(widget=forms.PasswordInput())


class EmptyForm(forms.Form):
    """
        Empty form
    """
    validate = "valid"


class NewForm(forms.Form):
    """
        Form with one charfield for name of the new file
        Charfield to fill the password and info need
        Checkbox to determine it's a raw file
    """
    filename = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    info = forms.CharField(widget=forms.Textarea(attrs={'cols': 160,
                                                        'rows': 30,
                                                        'style': 'width: auto;'
                                                        }))
    rawfile = forms.CharField(label='This file is a raw file',
                              widget=forms.CheckboxInput)
    validate = "valid"


class EditForm(forms.Form):
    """
        Form to edit password on a charfield
    """
    info = forms.CharField(widget=forms.Textarea(attrs={'cols': 160,
                                                        'rows': 30,
                                                        'style': 'width: auto;'
                                                        }))
    validate = "valid"
