from django import forms


class InputForm(forms.Form):
    challenge_input = forms.CharField(widget=forms.Textarea(attrs={"rows":30, "cols":50}))