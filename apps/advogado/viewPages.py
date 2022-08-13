from django.shortcuts import render, redirect, Http404, HttpResponse
from django.contrib import auth, messages
from logging import error, info, warning

from apps.advogado.models import Advogado
from apps.escritorio.models import Escritorio
from apps.gerenciamento.models import ChaveAcesso
from utils.helpers import getEstadosDict
from utils.validators import validaTelefone, validaEmail, validaSenha


def cadastroAdvogado(request):
    
    if request.method == 'GET':
        contexto: dict = {
            'dashboard': True,
            'estados': getEstadosDict()
        }
        sessaoAnterior: dict = request.session.get('requestFormAdv')

        if sessaoAnterior is not None and len(sessaoAnterior.keys()) != 0:
            contexto['info'] = {
                'primeiroNome': sessaoAnterior['primeiroNome'],
                'sobrenome': sessaoAnterior['sobrenome'],
                'cpf': sessaoAnterior['cpf'],
                'oab': sessaoAnterior['oab'],
                'celular': sessaoAnterior['celular'],
                'email': sessaoAnterior['email'],
                'password': sessaoAnterior['password'],
                'cep': sessaoAnterior['cep'],
                'cidade': sessaoAnterior['cidade'],
                'bairro': sessaoAnterior['bairro'],
                'endereco': sessaoAnterior['endereco'],
                'numero': sessaoAnterior['numero'],
                'complemento': sessaoAnterior['complemento'],
            }
            request.session['requestFormAdv'] = None

    else:
        print('Entrou com dificuldade')

    return render(request, 'cadastroAdv.html', context=contexto)


def avaliacadastroAdvogado(request):
    if request.method == 'POST':
        contextForm: dict = {}

        try:
            # Dados pessoais do advogado
            primeiroNome = request.POST.get('primeiroNome')
            sobrenome = request.POST.get('sobrenome')
            cpf = request.POST.get('cpf')
            oab = request.POST.get('oab')
            telefone = validaTelefone(request.POST.get('celular'))
            email = validaEmail(request.POST.get('email'))

            # Dados residenciais do advogado
            cep = request.POST.get('cep')
            cidade = request.POST.get('cidade')
            bairro = request.POST.get('bairro')
            endereco = request.POST.get('endereco')
            numero = request.POST.get('numero')
            complemento = request.POST.get('complemento')
            senha = request.POST.get('password')

            # Criação do contexto
            contextForm["nomeFantasia"] = primeiroNome
            contextForm["sobrenome"] = sobrenome
            contextForm["cpf"] = cpf
            contextForm["oab"] = oab
            contextForm["telefone"] = telefone
            contextForm["email"] = email
            contextForm["cep"] = cep
            contextForm["cidade"] = cidade
            contextForm["bairro"] = bairro
            contextForm["endereco"] = endereco
            contextForm["numero"] = numero
            contextForm["complemento"] = complemento
            contextForm["senha"] = senha

            request.session['requestFormAdv'] = request.POST

            usrJaExiste = Advogado.objects.filter(cpf=cpf).exists()
            if usrJaExiste:
                messages.warning(request, 'Advogado já cadastrado. Verifique a aba "Advogados"')
                request.session['requestForm'] = request.POST
                return redirect('cadastroAdvogado')

            escritorio: Escritorio = request.user

            advogado: Advogado = Advogado.objects.create(
                escritorioId=escritorio,
                primeiroNome=primeiroNome,
                sobrenome=sobrenome,
                senha=senha,
                cpf=cpf,
                oab=oab,
                email=email,
            )
            advogado.save()

            ChaveAcesso.objects.create(
                escritorioId=escritorio,
                advogadoId=advogado,
            )

            messages.success(request, "Advogado cadastrado com sucesso!")

        except Exception as err:
            print(f"{err=}")
            return redirect('cadastroAdvogado')

        return redirect('dashboard')
    else:
        return HttpResponse('<h1>Não funcionou</h1>')
