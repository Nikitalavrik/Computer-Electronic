from django import forms

class BlockForm(forms.Form):
    ip = forms.CharField(max_length=30)
    mask  = forms.CharField(max_length=20)
