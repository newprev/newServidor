import datetime
import json
from time import sleep
from typing import List, Generator

from django.contrib import messages, auth
from django.db.models import QuerySet
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.decorators.http import require_POST, require_GET

from apps.advogado.models import Advogado
from apps.escritorio.models import Escritorio
from apps.gerenciamento.models import Planos, ChaveAcesso


def addChaves(request):
    contexto: dict = {}
    contexto['dashboard'] = True
    contexto['cadastro'] = True

    return render(request, 'addChaves.html', contexto)

def atualizaCarrinho(request):
    contexto: dict = {
        'dashboard': True,
        'valorTotal': 0.0,
        'qtdPlanosAdquiridos': 0,
        'listaPlanos': []
    }

    if request.method in ('GET', 'get', 'delete', 'DELETE'):
        escritorio: Escritorio = request.user
        carrinhoChaves = []
        if 'carrinhoChaves' in request.session:
            carrinhoChaves = request.session['carrinhoChaves']

        if 'listaAdvogados' not in contexto.keys():
            contexto['listaAdvogados']: List[Advogado] = Advogado.objects.filter(escritorioId=escritorio.escritorioId, ativo=True, confirmado=True).all()

        contexto['carrinhoChaves'] = carrinhoChaves

        contexto['qtdPlanosAdquiridos'] = len(carrinhoChaves)

        return render(request, 'detalhesCompra.html', contexto)
    else:
        return render(request, 'detalhesCompra.html', {})


def avaliaAddChave(request, planoId: int):
    if request.user.is_authenticated:
        try:
            escritorio: Escritorio = request.user
            plano: Planos = get_object_or_404(Planos, planoId=planoId)
            chave: ChaveAcesso = ChaveAcesso(
                escritorioId=escritorio,
                planoId=plano,
            )

            # headers: dict = {'HX-Trigger': json.dumps({'chaveAdicionada': 'Chave adquirida com sucesso!'})}
            carrinhoChaves = []
            if 'carrinhoChaves' in request.session and request.session['carrinhoChaves'] is not None:
                carrinhoChaves = request.session['carrinhoChaves']
                # request.session['carrinhoChaves'] = None

                carrinhoChaves.append(chave.toDict())

            request.session['carrinhoChaves'] = carrinhoChaves

            # return HttpResponse(status=204, headers=headers)
            return redirect('atualizaCarrinho')

        except Exception as err:
            messages.error(request, 'Aconteceu um erro inesperado!')
            print(f"avaliaAddChave - {err=}")
    else:
        headers: dict = {'HX-Trigger': json.dumps({'naoAutorizado': 'A aquisição de novas chaves não foi permitida. Refaça o login e tente novamente.'})}

        return HttpResponse(status=401, headers=headers)


def buscaMinhasChaves(request):
    contexto: dict = {'dashboard': True}

    try:
        if request.user.is_authenticated:
            escritorio: Escritorio = request.user
            chaves: QuerySet = ChaveAcesso.objects.filter(
                escritorioId=escritorio.escritorioId,
            ).order_by('advogadoId', 'ativo', 'dataAquisicao')

            listaChavesAdvogadosPlanos: List[dict] = []

            for chave in chaves.all():
                infoConjugada = chave.toDict()

                plano: Planos = chave.planoId
                infoConjugada['planoId'] = plano.toDict()

                if chave.advogadoId is not None:
                    advogado: Advogado = get_object_or_404(Advogado, advogadoId=chave.advogadoId)
                    infoConjugada['advogadoId'] = advogado.toDict()

                else:
                    infoConjugada['advogadoId'] = None

                listaChavesAdvogadosPlanos.append(infoConjugada)

            contexto['chaves'] = listaChavesAdvogadosPlanos
            return render(request, 'localHtmls/_rowChaves.html', contexto)

        else:
            return redirect('login')
    except Exception as err:
        print(f"minhasChaves - {err=}")


def buscaMinhasUltimasAquisicoes(request):
    contexto: dict = {'dashboard': True}
    temChaveSemAdvogado: bool = False
    advogadosChavesId: List[int] = []

    try:
        if request.user.is_authenticated:
            escritorio: Escritorio = request.user
            chaves: QuerySet = ChaveAcesso.objects.filter(
                escritorioId=escritorio.escritorioId,
            ).order_by('advogadoId', 'ativo', 'dataAquisicao')

            listaChavesAdvogadosPlanos: List[dict] = []

            for chave in chaves.all()[:5]:
                infoConjugada = chave.toDict()

                plano: Planos = chave.planoId
                infoConjugada['planoId'] = plano.toDict()

                if chave.advogadoId is not None:
                    advogado: Advogado = get_object_or_404(Advogado, advogadoId=chave.advogadoId)
                    infoConjugada['advogadoId'] = advogado.toDict()
                    advogadosChavesId.append(advogado.advogadoId)

                else:
                    temChaveSemAdvogado = True
                    infoConjugada['advogadoId'] = None

                listaChavesAdvogadosPlanos.append(infoConjugada)

            if temChaveSemAdvogado:
                listaAdvogados: QuerySet = Advogado.objects.filter(escritorioId=escritorio, ativo=True, confirmado=True).exclude(advogadoId__in=advogadosChavesId)
                contexto['listaAdvogados'] = listaAdvogados.all()

            contexto['chaves'] = listaChavesAdvogadosPlanos

            return render(request, 'localHtmls/_cardUltimasAquisicoes.html', contexto)

        else:
            return redirect('login')
    except Exception as err:
        print(f"minhasChaves - {err=}")


def buscaPlanos(request):
    contexto: dict = {}
    try:
        listaPlanosQueryset: Planos = Planos.objects.filter(
            ativo=True, dataInicio__gte=datetime.datetime.now()
        ).order_by('-valor')
        listaPlanos: List[dict] = [plano.toDict() for plano in listaPlanosQueryset.all()]


        contexto['planos'] = listaPlanos
    except Exception as err:
        print(f"buscaPlanos - {err=}")
    finally:
        return render(request, 'cardPlano.html', contexto)


def deletaChaveCarrinho(request, uuid: str):
    print(f"{request.method=}")
    print(f"{uuid=}")

    carrinhoChaves: List[dict] = request.session['carrinhoChaves']
    if carrinhoChaves is None:
        return HttpResponse(status=204)

    carrinhoChaves = [chave for chave in carrinhoChaves if chave['uuid'] != uuid]
    request.session['carrinhoChaves'] = carrinhoChaves

    return redirect('atualizaCarrinho')

@require_POST
def efetivaAssociacao(request):

    if not request.user.is_authenticated:
        auth.logout(request)
        return redirect('login')

    try:
        escritorio: Escritorio = request.user
        advogadoId: int = int(request.POST.get('advogadoSelecionado'))
        advogado: Advogado = Advogado.objects.get(advogadoId=advogadoId, escritorioId=escritorio)
        chaveId: int = int(request.POST.get('chaveId'))

        if ChaveAcesso.objects.filter(advogadoId=advogadoId, escritorioId=escritorio).exists():
            messages.warning(request, 'Advogado já está associado a um plano.')
            return redirect('minhasChaves')

        chave: ChaveAcesso = ChaveAcesso.objects.get(chaveId=chaveId)
        chave.advogadoId = advogadoId
        chave.dataUltAlt = datetime.datetime.now()
        chave.save()

        messages.success(request, f"Advogado {advogado.primeiroNome} {advogado.sobrenome} associado ao plano {chave.planoId.titulo} com sucesso.")
        return redirect('minhasChaves')

    except Exception as err:
        print(f"efetivaAssociacao - {err=}")
        messages.warning(request, '')
        return redirect('minhasChaves')

@require_POST
def efetivaCompraPlanos(request):
    carrinho = request.session['carrinhoChaves']
    headers: dict = {}

    try:
        for chave in carrinho:
            advogadoId = request.POST.get(chave['uuid'])
            chave['advogadoId'] = advogadoId if advogadoId != '' else None

            novaChave: ChaveAcesso = ChaveAcesso().fromDict(chave)
            novaChave.save()

        headers['HX-Trigger'] = json.dumps({
            'chavesAdquiridas': f"{len(carrinho) if carrinho is not None else 0} chaves adquiridas com sucesso"
        })

        request.session['carrinhoChaves'] = None
        request.session['qtdPlanosAdquiridos'] = 0
        messages.success(request, f"{len(carrinho) if carrinho is not None else 0} chaves adquiridas com sucesso")
        return redirect('dashboard')

        # return HttpResponse(status=200, headers=headers)

    except Exception as err:
        print(f"efetivaCompraPlanos - err:{err=}")
        # headers['HX-Trigger'] = json.dumps({
        #     'erroAquisicao': f"Não foi possível adicionar as chaves ao seu cadastro"
        # })
        messages.error(request, f"Não foi possível adicionar as chaves ao seu cadastro")
        return redirect('minhasChaves')


def minhasChaves(request):
    contexto: dict = {'dashboard': True}

    try:
        if request.user.is_authenticated:
            return render(request, 'minhasChaves.html', contexto)

        else:
            return redirect('login')
    except Exception as err:
        print(f"minhasChaves - {err=}")
        return redirect('login')
