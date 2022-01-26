from django import forms

from blog.models import Content


class ContentForm(forms.ModelForm):
    OPTIONS = ((False, "Draft"), (True, "Publish"))
    publish = forms.ChoiceField(choices=OPTIONS)

    class Meta:
        model = Content
        exclude = ("slug", "publish")
