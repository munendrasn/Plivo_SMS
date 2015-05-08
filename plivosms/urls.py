from django.conf.urls import patterns, url
 
from communication.views import SendSmsCreateView
 
urlpatterns = patterns('',
    url(r'^communication/send/sms/$',SendSmsCreateView.as_view(),name='send_sms'
    ),
)