from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html')


def contacts(request):
    return render(request, 'core/contacts.html')


def mail(request):
    return render(request, 'core/mail.html')


def chat(request):
    return render(request, 'core/chat.html')


def phone(request):
    return render(request, 'core/phone.html')
