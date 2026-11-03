from django import forms

class NameForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    address = forms.CharField(widget=forms.Textarea(attrs={'cols':15,'rows':5}))
    gender = forms.MultipleChoiceField(choices=[('MALE','MALE'),('FEMALE','FEMALE')],widget=forms.CheckboxSelectMultiple)
    