from django import forms

from models import SendSMS

class SendSMSForm(forms.ModelForm):
    class Meta:
        model = SendSMS
        fields = ('to_number', 'body')