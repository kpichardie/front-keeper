from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label='Your search', max_length=100)


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
    validate = "valid"

class EditForm(forms.Form):
    info = forms.CharField(widget=forms.Textarea(attrs={'cols': 160,
                                                        'rows': 30,
                                                        'style': 'width: auto;'
                                                        }))
    validate = "valid"


class ReadForm(forms.Form):

    filename = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    #def loadcontent(filename):
    #    passkeeperpath = '/opt/mypasskeeper/'
    #    fd = os.open(os.path.join(passkeeperpath, filename), os.O_RDONLY)
    #    content = os.read(fd)
    #    os.close(fd)
    #    info = forms.CharField(widget=forms.Textarea(attrs={'cols': 160,
    #                                                        'rows': 30,
    #                                                        'style': 'width: auto;',
    #                                                        'content': content
    #                                                        }))
    #    validate = "valid"
