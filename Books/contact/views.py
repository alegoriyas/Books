from django.core.mail import send_mail

from django.shortcuts import render

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Введите тему.')
        if not request.POST.get('message', ''):
            errors.append('Введите сообщение.')
        if not request.POST.get('e-mail') and '@' not in request.POST['e-mail']:
            errors.append('Введите правильный адрес e-mail.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('e-mail', 'noreply@example.com'),
                ['siteowner@example.com'],
                )
        return render(request, '/contact/thanks/')
    return render(request, 'contact/contact_form.html', {'errors': errors})