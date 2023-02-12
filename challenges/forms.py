from django import forms

# this is the standard input form for challenges, with the text area's (i.e. where the code input happens) size defined
class InputForm(forms.Form):
    challenge_input = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        fields = ['challenge_input']