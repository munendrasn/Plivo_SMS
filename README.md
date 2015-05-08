## Introduction
Plivo has a powerful API and helper libraries that let you build awesome SMS and voice apps. I have built a web application powered by Django that lets you send a text message to a number of your choice. It also shortens URL's found in the message using TinyURL service.

## Getting Started
In the `utils.py` file present in the `communication` folder, replace the existing AUTH_ID and AUTH_TOKEN with yours.

Staying in the root directory, execute the following commands :
```
python manage.py migrate
python manage.py syncdb

python manage.py runserver

```

This should start the server running on your localhost
Point your browser to the link specified below
[http://localhost:8000/communication/send/sms](http://localhost:8000/communication/send/sms)

where you can find the fields to enter a phone number, a text box to specify the message and a submit button, which on clicking sends the message

## Contact
For any queries, feel free to reach me at  *sn.munendra52 [at] gmail [dot] com*