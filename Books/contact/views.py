from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    send_mail('Hello from SteblinaEE', 
              'Hello there. This is an automated message.', 
              'steblinaee@gmail.com', 
              ['egorinkas@gmail.com'], 
              fail_silently=False)
    return render(request, 'contact/index.html')

def contact_form(request):
    #errors = []
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message = request.POST['message']
        message_email = request.POST['message-email']

        # send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['egorinkas@gmail.com'], # To Email
            )

        return render(request, 'contact/contact_form.html', {'message_name': message_name,
                                                             'message_email': message_email})
    else:
        return render(request, 'contact/contact_form.html', {})

            #if not request.POST.get('subject', ''):
            #errors.append('Введите тему.')
       #if not request.POST.get('message', ''):
           # errors.append('Введите сообщение.')
        #if not request.POST.get('e-mail') and '@' not in request.POST['e-mail']:
           # errors.append('Введите правильный адрес e-mail.')
        #if not errors:
           # send_mail(