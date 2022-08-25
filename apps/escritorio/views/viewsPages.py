from time import sleep
from typing import List, Tuple, Generator

from django.shortcuts import render, redirect, Http404, HttpResponse
from django.contrib import auth, messages
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from apps.escritorio.models import Escritorio
from apps.gerenciamento.models import ChaveAcesso
from apps.advogado.models import Advogado

from logging import error, info, warning
from utils.validators import validaSenha, validaEmail, validaTelefone
from utils.enums.exceptionCodesEnums import NewValidationError
from utils.helpers import getEstadosDict


def avaliaCadastro(request):

    if request.method == 'POST':
        contextForm: dict = {}
        try:
            # Dados do escritório
            nomeFantasia = request.POST.get('nomeFantasia')
            cnpj = request.POST.get('cnpj')
            telefone = validaTelefone(request.POST.get('celular'))
            email = validaEmail(request.POST.get('email'))

            # Endereço do escritório
            cep = request.POST.get('cep')
            cidade = request.POST.get('cidade')
            bairro = request.POST.get('bairro')
            endereco = request.POST.get('endereco')
            numero = request.POST.get('numero')
            complemento = request.POST.get('complemento')
            senha = request.POST.get('password')
            confirmaSenha = request.POST.get('secondPassword')

            # Criação do contexto
            contextForm["nomeFantasia"] = nomeFantasia
            contextForm["cnpj"] = cnpj
            contextForm["telefone"] = telefone
            contextForm["email"] = email
            contextForm["cep"] = cep
            contextForm["cidade"] = cidade
            contextForm["bairro"] = bairro
            contextForm["endereco"] = endereco
            contextForm["numero"] = numero
            contextForm["complemento"] = complemento
            contextForm["senha"] = senha
            contextForm["confirmaSenha"] = confirmaSenha

            request.session['requestForm'] = request.POST

            # Verifica senhas
            senhaValida: bool = validaSenha(senha) is not None
            if not senhaValida:
                messages.error(request, "Senha não segue o padrão requisitado. Tente novamente.")
                request.session['requestForm'] = request.POST
                return redirect('cadastro')

            if not senha == confirmaSenha:
                messages.error(request, "As senhas digitadas precisam ser iguais. Tente novamente.")
                request.session['requestForm'] = request.POST
                return redirect('cadastro')

            usrJaExiste = Escritorio.objects.filter(email=email).exists()
            if usrJaExiste:
                messages.warning(request, 'E-mail já cadastrado. Caso precise, clique em "Esqueci a senha"')
                request.session['requestForm'] = request.POST
                return redirect('cadastro')

            escritorio: Escritorio = Escritorio.objects.create_user(
                nomeFantasia=nomeFantasia,
                password=senha,
                username=email,
                cnpj=cnpj,
                telefone=telefone,
                email=email,
                cep=cep,
                cidade=cidade,
                bairro=bairro,
                endereco=endereco,
                numero=numero,
                complemento=complemento
            )

            if 'imagem-logo' in request.FILES:
                escritorio.logoPath = request.FILES['imagem-logo']

            escritorio.save()

            auth.login(request, escritorio)
            messages.success(request, "Escritório cadastrado com sucesso!")

            return redirect('dashboard')

        except ValidationError as err:
            auth.logout(request)

            if err.message == NewValidationError.emailInvalido.value:
                erroMessage = 'E-mail inválido. Tente novamente.'
                messages.warning(request, erroMessage)

            elif err.message == NewValidationError.telefoneInvalido.value:
                erroMessage: str = 'Telefone inválido. Tente novamente.'
                messages.warning(request, erroMessage)
            else:
                erroMessage = 'Senhas não conferem ou não seguem o padrão necessário. Tente novamente.'
                messages.warning(request, erroMessage)

            request.session['requestForm'] = request.POST
            return redirect('cadastro')

        except IntegrityError:
            auth.logout(request)

            messages.warning(request, 'Não foi possível completar o cadastro, pois alguma das informações já possui cadastro no nosso banco.')

            request.session['requestForm'] = request.POST
            return redirect('cadastro')

    else:
        auth.logout(request)
        return redirect('cadastro')


def cadastro(request):
    metodo: str = request.method
    contexto: dict = {
        'cadastro': True,
        'estados': getEstadosDict()
    }

    if metodo == 'POST':
        print(f"{request.POST.get('email', 'DeuBosta')=}")
    else:
        sessaoAnterior: dict = request.session.get('requestForm')

        if sessaoAnterior is not None and len(sessaoAnterior.keys()) != 0:
            contexto['info'] = {
                'nomeFantasia': sessaoAnterior['nomeFantasia'],
                'cnpj': sessaoAnterior['cnpj'],
                'celular': sessaoAnterior['celular'],
                'email': sessaoAnterior['email'],
                'password': sessaoAnterior['password'],
                'secondPassword': sessaoAnterior['secondPassword'],
                'cep': sessaoAnterior['cep'],
                'cidade': sessaoAnterior['cidade'],
                'bairro': sessaoAnterior['bairro'],
                'endereco': sessaoAnterior['endereco'],
                'numero': sessaoAnterior['numero'],
                'complemento': sessaoAnterior['complemento'],
            }
            request.session['requestForm'] = None

    return render(request, 'cadastro.html', contexto)

def dashboard(request):
    contexto: dict = {
        'dashboard': True,
        'semChaves': True
    }

    if request.user.is_authenticated:
        escritorio: Escritorio = request.user
        contexto['escritorio'] = escritorio.toDict()


        chavesAcesso: ChaveAcesso = ChaveAcesso.objects.filter(escritorioId=escritorio)
        contexto['qtdChavesTotais'] = chavesAcesso.count()

        qtdChavesUtilizadas: List = []
        for c in chavesAcesso.all():
            if c.advogadoId is not None:
                qtdChavesUtilizadas.append(c)

        contexto['qtdChaves'] = len(qtdChavesUtilizadas)
        contexto['aCadastrar'] = contexto['qtdChavesTotais'] > contexto['qtdChaves']

        return render(request, "dashboard/dashboardMain.html", context=contexto)

    else:
        return HttpResponse(Http404)

def esqSenha(request):
    print('\n\n*******Clicou no esqueci senha*******\n\n')
    return login(request)

def fazerLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        psw = request.POST.get('password')

        try:
            escritorioModel: Escritorio = Escritorio.objects.get(email=email)
            if not escritorioModel.check_password(psw):
                messages.error(request, 'Usuário ou senha não encontrados')
                return redirect('login')

            auth.login(request, escritorioModel)
            # messages.success(request, 'Escritório logado com sucesso!')
            return redirect('dashboard')

        except Escritorio.DoesNotExist as err:
            messages.error(request, 'Usuário não encontrado')
            return redirect('login')
        except Exception as err:
            error(f'fazerLogin - err: {err}')

def fazerLogout(request):
    auth.logout(request)

    contexto = { 'dashboard': False }

    return render(request, 'login.html', context=contexto)

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    return redirect('login')

def login(request, *args, **kwargs):
    if request.method == 'POST':
        try:
            info('POST::/cadastro')
            email = validaEmail(request.POST['email'])
            senha = request.POST['senha']
            
        except Exception as err:
            print(f'----------- err: {err=}')

    context: dict = {
        'dashboard': False,
        'mostraNomeEscritorio': False,
        'login': True,
        'user': {
            'email': ''
        }
    }
    if request.user.is_authenticated:
        context['user']['email'] = request.user.email
        auth.logout(request)

    return render(request, 'login.html', context)