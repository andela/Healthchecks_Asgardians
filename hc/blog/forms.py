from django import forms


class PostForm(forms.Form):
    author = forms.CharField(max_length=30)
    category = forms.CharField(max_length=30)
    content = forms.CharField()
    title = forms.CharField()


