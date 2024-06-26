import datetime
import json
from time import sleep
from typing import List, Generator

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models import QuerySet
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages, auth

from apps.advogado.models import Advogado, EnderecoAdvogado, Contato
from apps.escritorio.models import Escritorio
from apps.gerenciamento.models import ChaveAcesso
from utils.enums.imgManipulacaoEnum import ImgManipulacao
from utils.helpers import getEstadosDict, campoAlterado, buscaAdvNaLista
from utils.imageManager import redimensionarImagem
from utils.validators import validaTelefone, validaEmail


def advogadosCadastrados(request):
    contexto: dict = {
        'dashboard': True,
    }
    try:
        if not request.user.is_authenticated:
            auth.logout(request)
            redirect('login')

        escritorio: Escritorio = request.user
        listaAdvogados: List[dict] = []

        if Advogado.objects.filter(escritorioId=escritorio).exists():
            queryAdvogados = Advogado.objects.filter(escritorioId=escritorio)

            for adv in queryAdvogados.all():
                dictInfoPessoal: dict = adv.toDict(enviaEscritorio=False)
                dictEndereco: dict = None
                dictContato: dict = None

                if EnderecoAdvogado.objects.filter(advogadoId=adv).exists():
                    endereco = EnderecoAdvogado.objects.get(advogadoId=adv)
                    dictEndereco = endereco.toDict(enviaAdvogado=False)

                if Contato.objects.filter(advogadoId=adv).exists():
                    contato = Contato.objects.get(advogadoId=adv)
                    dictContato = contato.toDict(enviaAdvogado=False)

                listaAdvogados.append({
                    'pessoal': dictInfoPessoal,
                    'endereco': dictEndereco,
                    'contato': dictContato
                })

            for adv in listaAdvogados:
                print(f"{adv['pessoal']['advogadoId']} **************************************** ")
                for chave, valor in adv.items():
                    print(f"{chave}: {valor}")
                print('---------------------------------\n\n')

        if len(listaAdvogados) <= 0:
            contexto['listaAdvogados'] = None
        else:
            contexto['listaAdvogados'] = listaAdvogados

        return render(request, 'advCadastrados.html', contexto)

    except Exception as err:
        print(f"advogadosCadastrados - err:{err=}")
        return render(request, 'advCadastrados.html', {})


def avaliaCadastroAdvogado(request):
    if request.method == 'POST':
        contextForm: dict = {}

        try:
            # Criação do contexto
            contextForm["nomeFantasia"] = request.POST.get('primeiroNome')
            contextForm["sobrenome"] = request.POST.get('sobrenome')
            contextForm["cpf"] = request.POST.get('cpf')
            contextForm["oab"] = request.POST.get('oab')
            contextForm["telefone"] = request.POST.get('celular')
            contextForm["email"] = request.POST.get('email')
            contextForm["cep"] = request.POST.get('cep')
            contextForm["cidade"] = request.POST.get('cidade')
            contextForm["bairro"] = request.POST.get('bairro')
            contextForm["endereco"] = request.POST.get('endereco')
            contextForm["numero"] = request.POST.get('numero')
            contextForm["complemento"] = request.POST.get('complemento')
            contextForm["senha"] = request.POST.get('password')
            contextForm["is-whatsapp"] = request.POST.get('password')
            contextForm["is-telegram"] = request.POST.get('password')

            request.session['requestFormAdv'] = request.POST

            # Dados pessoais do advogado
            primeiroNome = request.POST.get('primeiroNome')
            sobrenome = request.POST.get('sobrenome')
            cpf = request.POST.get('cpf')
            oab = request.POST.get('oab')
            email = validaEmail(request.POST.get('email'))

            # Dados de contato
            telefone = validaTelefone(request.POST.get('celular'))
            isWhatsapp = bool(request.POST.get('is-whatsapp'))
            isTelegram = bool(request.POST.get('is-telegram'))

            # Dados residenciais do advogado
            cep = request.POST.get('cep')
            cidade = request.POST.get('cidade')
            bairro = request.POST.get('bairro')
            endereco = request.POST.get('endereco')
            estado = request.POST.get('estados')
            numero = request.POST.get('numero')
            complemento = request.POST.get('complemento')
            senha = request.POST.get('password')

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
                numeroOAB=oab,
                email=email,
            )
            # advogado.save()

            if cep is not None and cep != '':
                endereco: EnderecoAdvogado = EnderecoAdvogado.objects.create(
                    advogadoId=advogado,
                    endereco=endereco,
                    cidade=cidade,
                    estado=estado,
                    bairro=bairro,
                    cep=cep,
                    numero=numero,
                    complemento=complemento
                )

            if telefone != '':
                contato: Contato = Contato.objects.create(
                    advogadoId=advogado,
                    telefone=telefone,
                    isWhatsapp=isWhatsapp,
                    isTelegram=isTelegram
                )

            messages.success(request, "Advogado cadastrado com sucesso!")
            request.session['requestFormAdv'] = None

        except ValidationError as err:
            if err.message == 'telefone':
                print(f"avaliaCadastroAdvogado - {err=}")
                messages.warning(request, 'Telefone informado possui caracteres não numéricos. Verifique e tente novamente.')
            return redirect('cadastroAdvogado')

        except IntegrityError as err:
            messages.warning(request, 'Número da OAB já cadastrado. Verifique e tente novamente.')
            print(f"avaliaCadastroAdvogado - {err=}")
            return redirect('cadastroAdvogado')

        except Exception as err:
            print(f"avaliaCadastroAdvogado - {err=}")
            if advogado is not None:
                advogado.delete()

            if endereco is not None:
                endereco.delete()

            if contato is not None:
                contato.delete()

            return redirect('cadastroAdvogado')

        return redirect('dashboard')
    else:
        return HttpResponse('<h1>Não funcionou</h1>')


def atualizaCadastro(request, **kwargs):
    contexto: dict = {}

    if kwargs is None or len(kwargs.items()) == 0:
        messages.error(request, 'Não foi possível buscar as informações do advogado. Entre em contato com o suporte.')
        return redirect('dashboard')

    else:
        advogadoId: int = kwargs['advogadoId']

    try:
        advogado: Advogado = Advogado.objects.get(advogadoId=advogadoId)
        contexto['advogado'] = advogado.toDict()

        endereco: EnderecoAdvogado = None
        if EnderecoAdvogado.objects.filter(advogadoId=advogadoId).exists():
            endereco = EnderecoAdvogado.objects.filter(advogadoId=advogadoId).get()

        contatoAdvogado: Contato = None
        if Contato.objects.filter(advogadoId=advogado).exists():
            contatoAdvogado = Contato.objects.get(advogadoId=advogado)
            print('\n\nEntrou aqui!\n\n')

        contexto['endereco'] = endereco.toDict() if endereco is not None else None
        contexto['contato'] = contatoAdvogado.toDict(enviaAdvogado=False) if contatoAdvogado is not None else None
        contexto['cadastro'] = True
        contexto['dashboard'] = True
        contexto['atualizacao'] = True
        contexto['estados'] = getEstadosDict()
        contexto['headers'] = {'HX-Trigger': 'testandoHtmx'}

    except Exception as err:
        messages.error(request, err)
        print(f"atualizaCadastro - err:{err=}")
        return redirect('dashboard')

    return render(request, 'atualizacaoAdv.html', context=contexto)


def buscaAdvogados(request):
    contexto: dict = {
        'temChaves': False,
        'primeiroAdvogado': True,
        'chaves': []
    }
    temChaves: bool = False

    try:
        escritorio: Escritorio = request.user

        chavesAcesso: QuerySet = ChaveAcesso.objects.filter(escritorioId=escritorio, ativo=True)
        temChaves = chavesAcesso.count() != 0

    except ChaveAcesso.DoesNotExist:
        contexto['temChaves'] = False

    if temChaves:
        advogadoIdsChaves: Generator = (chave.advogadoId for chave in chavesAcesso.all())
        listaAdvogados: List[Advogado] = Advogado.objects.filter(advogadoId__in=advogadoIdsChaves).order_by('-ativo', 'primeiroNome').all()
        contexto['primeiroAdvogado'] = len(listaAdvogados) == 0

        for chave in chavesAcesso.all():
            dictChave: dict = chave.toDict()

            if chave.advogadoId is not None:
                dictChave['advogadoId'] = buscaAdvNaLista(listaAdvogados, chave.advogadoId).toDict(enviaEscritorio=False)
            else:
                dictChave['advogadoId'] = None

            contexto['chaves'].append(dictChave)
        # print('\n\n')
        #
        # for chave in contexto['chaves']:
        #     for c, v in chave.items():
        #         if c == 'chaveId':
        #             print(f"chaveId: {v} *****************************")
        #         else:
        #             print(f"{c}: {v}")
        #     print('-------------------------\n\n')

        contexto['aCadastrar'] = chavesAcesso.count() > len(listaAdvogados)

    return render(request, 'gridAdvogados.html', contexto)


def cadastroAdvogado(request, **kwargs):
    if not request.user.is_authenticated:
        redirect('login')

    if request.method == 'GET':
        # escritorio: Escritorio = request.user
        # qtdChavesLivres: int = ChaveAcesso.objects.filter(escritorioId=escritorio.escritorioId, advogadoId=None).count()
        # if qtdChavesLivres < 1:
        #     headers = {"HX-Trigger": json.dumps({'semChaves': "Não há chaves disponíveis. Adquira mais em 'Gerenciar chaves'"})}
        #     return HttpResponse(status=204, headers=headers)

        contexto: dict = {
            'cadastro': True,
            'dashboard': True,
            'estados': getEstadosDict()
        }
        sessaoAnterior: dict = request.session.get('requestFormAdv')

        if sessaoAnterior is not None and len(sessaoAnterior.keys()) != 0:
            contexto['info'] = restauraCampos(request, sessaoAnterior)

    else:
        print('Entrou com dificuldade')

    return render(request, 'cadastroAdv.html', context=contexto)


def desAtivaAdvogado(request, advogadoId: int):
    if not request.user.is_authenticated:
        redirect('login')

    advogado: Advogado = get_object_or_404(Advogado, advogadoId=advogadoId)
    advogado.ativo = not advogado.ativo
    advogado.dataUltAlt = datetime.datetime.now()
    advogado.save()

    if advogado.ativo:
        mensagem: str = f"Advogado(a) {advogado.primeiroNome} ativado(a) com sucesso."
    else:
        mensagem: str = f"Advogado(a) {advogado.primeiroNome} desativado(a) com sucesso."

    headers: dict = {'HX-Trigger': json.dumps({'desAtivaAdvogado': mensagem})}

    return HttpResponse(status=204, headers=headers)


def efetivaAtualizaCadastro(request):

    if request.method == 'POST':
        enviouEndereco: bool = False
        criarEndereco: bool = False
        alterouEndereco: bool = False
        alterouDadoPessoal: bool = False


        # Dados pessoais
        advogadoId = request.POST.get('advogadoId')
        primeiroNome = request.POST.get('primeiroNome')
        sobrenome = request.POST.get('sobrenome')
        cpf = request.POST.get('cpf')
        oab = request.POST.get('oab')
        email = validaEmail(request.POST.get('email'))

        # Dados de contato
        telefone = validaTelefone(request.POST.get('celular'))
        isWhatsapp = bool(request.POST.get('is-whatsapp'))
        isTelegram = bool(request.POST.get('is-telegram'))

        # Dados residenciais do advogado
        cep = request.POST.get('cep')
        cidade = request.POST.get('cidade')
        bairro = request.POST.get('bairro')
        endereco = request.POST.get('endereco')
        estado = request.POST.get('estados')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        senha = request.POST.get('password')

        advogado: Advogado = Advogado.objects.get(advogadoId=advogadoId)

        if Contato.objects.filter(advogadoId=advogado).exists():
            contato: Contato = Contato.objects.get(advogadoId=advogado)
        else:
            contato = None

        if 'foto-advogado' in request.FILES:
            advogado.fotoPath = request.FILES['foto-advogado']

        if campoAlterado(advogado.primeiroNome, primeiroNome):
            alterouDadoPessoal = True
            advogado.primeiroNome = primeiroNome

        if campoAlterado(advogado.sobrenome, sobrenome):
            alterouDadoPessoal = True
            advogado.sobrenome = sobrenome

        if campoAlterado(advogado.cpf, cpf):
            alterouDadoPessoal = True
            advogado.cpf = cpf

        if campoAlterado(advogado.oab, oab):
            alterouDadoPessoal = True
            advogado.numeroOAB = oab

        if campoAlterado(advogado.email, email):
            alterouDadoPessoal = True
            advogado.email = email

        if campoAlterado(advogado.senha, senha):
            alterouDadoPessoal = True
            advogado.senha = senha

        # Se enviou e/já cadastrou endereço
        if cep is not None and cep != '':
            enviouEndereco = True
            enderecoAdv: EnderecoAdvogado = EnderecoAdvogado.objects.filter(cep=cep, advogadoId=advogado.advogadoId)
            if not enderecoAdv.exists():
                criarEndereco = True
            else:
                enderecoAdv = enderecoAdv.get()

        if contato is None or campoAlterado(contato.telefone, telefone) or campoAlterado(contato.isTelegram, isTelegram) or campoAlterado(contato.isWhatsapp, isWhatsapp):
            if contato is None:
                contato: Contato = Contato.objects.create(
                    advogadoId=advogado,
                    telefone=telefone,
                    isWhatsapp=isWhatsapp,
                    isTelegram=isTelegram
                )
            else:
                contato.telefone = telefone
                contato.isWhatsapp = isWhatsapp
                contato.isTelegram = isTelegram
                contato.dataUltAlt = datetime.datetime.now()
                contato.save()

        if enviouEndereco:
            if criarEndereco:
                novoEndereco: EnderecoAdvogado = EnderecoAdvogado.objects.create(
                    advogadoId=advogado,
                    cep=cep,
                    endereco=endereco,
                    cidade=cidade,
                    bairro=bairro,
                    estado=estado,
                    numero=numero,
                    complemento=complemento
                )
                novoEndereco.save()
            else:
                if campoAlterado(enderecoAdv.cep, cep):
                    alterouEndereco = True
                    enderecoAdv.cep = cep

                if campoAlterado(enderecoAdv.endereco, endereco):
                    alterouEndereco = True
                    enderecoAdv.endereco = endereco

                if campoAlterado(enderecoAdv.bairro, bairro):
                    alterouEndereco = True
                    enderecoAdv.bairro = bairro

                if campoAlterado(enderecoAdv.cidade, cidade):
                    alterouEndereco = True
                    enderecoAdv.cidade = cidade

                if campoAlterado(enderecoAdv.estado, estado):
                    alterouEndereco = True
                    enderecoAdv.estado = estado

                if campoAlterado(enderecoAdv.numero, numero):
                    alterouEndereco = True
                    enderecoAdv.numero = numero

                if campoAlterado(enderecoAdv.complemento, complemento):
                    alterouEndereco = True
                    enderecoAdv.complemento = complemento

                if alterouEndereco:
                    enderecoAdv.dataUltAlt = datetime.datetime.now()
                    enderecoAdv.save()

        if alterouDadoPessoal:
            advogado.dataUltAlt = datetime.datetime.now()
            advogado.save()

        if redimensionarImagem(advogado.fotoPath.path) == ImgManipulacao.ok:
            print('Ok........................')

        messages.success(request, "Advogado atualizado com sucesso")
        return redirect('dashboard')
    else:
        print('Tá fazendo merdaaaa..........: efetivaAtualizaCadastro')


def excluiAdvogado(request, advogadoId: int):
    if not request.user.is_authenticated:
        return redirect('login')

    advogado: Advogado = get_object_or_404(Advogado, advogadoId=advogadoId)

    chaveAcesso: ChaveAcesso = get_object_or_404(ChaveAcesso, advogadoId=advogadoId, escritorioId=advogado.escritorioId)
    chaveAcesso.advogadoId = None
    chaveAcesso.dataUltAlt = datetime.datetime.now()
    chaveAcesso.save()

    advogado.delete()

    return redirect('dashboard')


def restauraCampos(request, sessaoAnterior) -> dict:
    dictSessaoAnterior = {
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
    return dictSessaoAnterior

