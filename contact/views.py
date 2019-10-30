from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import ContactReciver
from .models import EmailSetting
from datetime import datetime
from django.core.mail import send_mail
from django.template.loader import render_to_string


def index(request):
    n = []
    if request.method == 'POST':
        form = ContactReciver(request.POST)
        if form.is_valid():
            ins = form.save(commit=False)
            ins.created_date = datetime.now()
            ins.user_info = request.META['REMOTE_ADDR']
            ins.save()
            sendit(ins.name, ins.email, ins.comment)
            return redirect('contact:index')

        else:
            err = form.errors
            return HttpResponse(err)
    else:
        form1 = ContactReciver()
        return render(request, 'contact.html', {'form': form1})


# change this part by your settings
def sendit(name, email, comment):
    setting = EmailSetting.objects.get(id=1)
    msg_plain = render_to_string(
        'email.txt', {'name': name, 'email': email, 'comment': comment})
    msg_html = render_to_string(
        'email.html', {'name': name, 'email': email, 'comment': comment})
    send_mail(
        subject=setting.subject,
        message=msg_plain,
        from_email=setting.from_email,
        recipient_list=[setting.recipients_email, ],
        html_message=msg_html,
        fail_silently=False,
    )
