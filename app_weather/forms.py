from django import forms


class LocateForm(forms.Form):
    locate = forms.CharField(max_length=50)




