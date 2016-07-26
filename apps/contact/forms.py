from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea())
    sender = forms.EmailField(required=True)
