from django import forms

class addTriple(forms.Form):
    subject = forms.CharField(label='subject', max_length=100)
    predicate = forms.CharField(label='predicate', max_length=100)
    object = forms.CharField(label='object', max_length=100)

class editTriple(forms.Form):
    subject = forms.CharField(label='subject', max_length=100, required=True)
    predicate = forms.CharField(label='predicate', max_length=100, required=True)
    object = forms.CharField(label='object', max_length=100, required=True)

