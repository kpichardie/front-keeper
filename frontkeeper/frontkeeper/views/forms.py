from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label='Search in password', max_length=100)


class PasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())


class SubmitForm(forms.Form):
    validate = "valid"


class NewForm(forms.Form):
    filename = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    info = forms.CharField(widget=forms.Textarea(attrs={'cols': 160,
                                                        'rows': 30,
                                                        'style': 'width: auto;'
                                                        }))
    rawfile = forms.CharField(label='This file is a raw file',
                              widget=forms.CheckboxInput)
    validate = "valid"


class EditForm(forms.Form):
    info = forms.CharField(widget=forms.Textarea(attrs={'cols': 160,
                                                        'rows': 30,
                                                        'style': 'width: auto;'
                                                        }))
    validate = "valid"


class CustomForm(forms.Form):
    validate = "valid"


class ReadForm(forms.Form):

    filename = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
