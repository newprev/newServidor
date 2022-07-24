from django.shortcuts import render


def cadastro(request, *args, **kwargs):
    return render(request, 'cadastro.html')
