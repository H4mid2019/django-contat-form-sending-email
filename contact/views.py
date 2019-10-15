from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactReciver
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

n = []


def index(request):
    global n
    if request.method == 'POST':
        form = ContactReciver(request.POST)
        if form.is_valid():
            ins = form.save(commit=False)
            ins.created_date = datetime.now()
            n.append(request.POST.get('name'))
            n.append(request.POST.get('email'))
            n.append(request.POST.get('comment'))
            ins.save()
            sendit(n)
            return redirect('contact:index')

        else:
            err = form.errors
            return HttpResponse(err)
    else:
        form1 = ContactReciver()
        return render(request, 'contact.html', {'form': form1})


# change this part by your settings
def sendit(name):
    mm = '-'.join(name)
    message = MIMEMultipart()
    message["from"] = 'info@foo.com'
    message["to"] = 'john@gmail.com'
    message["subject"] = 'Hello Wolrd'
    message.attach(MIMEText(mm))

    with smtplib.SMTP(host='mail.foo.com', port=26) as smtp:
        smtp.ehlo()
        # smtp.starttls() # uncomment for tls connection
        smtp.login('username', 'secretpass')
        smtp.send_message(message)
