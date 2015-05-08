from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView

from models import SendSMS
from forms import SendSMSForm
from utils import send_plivo_message

from django.core.urlresolvers import reverse_lazy

class SendSmsCreateView(CreateView):
    model = SendSMS
    form_class = SendSMSForm
    template_name = 'communication/sendsms_form.html'
    success_url = reverse_lazy('send_sms')
 
    def form_valid(self, form):
        if form.is_valid():
            number = form.cleaned_data['to_number']
            body = form.cleaned_data['body']
            # call plivo
            sent = send_plivo_message(number, body)
 
            return super(SendSmsCreateView, self).form_valid(form)
