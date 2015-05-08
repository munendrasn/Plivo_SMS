from django.conf import settings

import re
import urllib2 
import plivo
 
def tiny_url(url):
    apiurl = "http://tinyurl.com/api-create.php?url="
    tinyurl = urllib2.urlopen(apiurl + url).read()
    return tinyurl
 
def content_tiny_url(content):
    regex_url = r'http:\/\/([\w.]+\/?)\S*'
    for match in re.finditer(regex_url, content):
        url = match.group(0)
        content = content.replace(url,tiny_url(url))
 
    return content 

def send_plivo_message(to_number, body):
	p = plivo.RestAPI('MAZWU5ZWVKNMU4MZG1N2','YWMzMzk5NmIzNzc2MTAyZDI4ZTIwYzYzMWZhOTM0')
	flag = content_tiny_url(body)
	params = {
    'src': '+919686798312', # Caller Id
    'dst' : to_number, # User Number to Call
    'text' : flag,
    'type' : "sms",
	}

	response = p.send_message(params)
	return response