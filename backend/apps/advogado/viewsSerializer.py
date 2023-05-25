from dateutil.relativedelta import relativedelta

from rest_framework import viewsets, generics, filters, status
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend

from random import randint

from apps.newMails.views import primeiroAcessoAdvogado, trocouSenhaAdvogado
from utils.enums.loginEnums import TipoTrocaSenha
from .models import Advogado, TrocaSenha
from .serializers import AdvogadoSerializer, ConfirmaAdvogadoSerializer, AuthAdvogadoSerializer, TrocaSenhaSerializer

from logging import error, info, warning


class AdvogadosViewSet(viewsets.ModelViewSet):
    """Exibindo todos advogados cadastrados"""
    http_method_names = ['patch', 'get']

    try:
        info("GET::api/advogados")
        queryset = Advogado.objects.all()
        serializer_class = AdvogadoSerializer
        filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
        ordering_fields = ['nomeAdvogado']
        search_fields = ['numeroOAB', 'email']
        filterset_fields = ['ativo']

    except Exception as err:
        warning("GET::api/advogados")

    def patch(self, request, *args, **kwargs):
        try:
            senha = request.data['senhaEnviada']
            advogadoId = request.data['advogadoId']

            advogado: Advogado = get_object_or_404(Advogado, advogadoId=advogadoId)
            advogado.senha = senha
            advogado.dataUltAlt = timezone.now()
            advogado.confirmado = True
            advogado.save()
            info(f"UPDATE::AdvogadosConfirmacaoViewSet - {advogado=}")
            return HttpResponse("Advogado atualizado", status=201)

        except Exception as err:
            error(f"api/advogados - {err}")
            print(f"{err=}")
            return HttpResponse('', status=500)

class AdvogadosConfirmacaoViewSet(generics.RetrieveUpdateAPIView):
    """Exibindo senha provisória de advogado ainda não confirmado"""
    def get_queryset(self):
        queryset = None
        try:
            if len(self.kwargs) != 0:
                advogadoId = self.kwargs['pk']
                info(f"GET::api/advogados/{advogadoId}/confirmacao/")
                queryset = Advogado.objects.filter(advogadoId=advogadoId)

            return queryset
        except Exception as err:
            error(f"{err=}::api/advogados/<advogadoId>/confirmacao/")
            return HttpResponse(status=510)

    def get_object(self):
        return get_object_or_404(Advogado, pk=self.kwargs['pk'])

    def patch(self, request, *args, **kwargs):
        try:
            info(f"PATCH::api/advogados/<advogadoId>/confirmacao/")
            advModel = self.get_object()
            advogado = ConfirmaAdvogadoSerializer(advModel, data=request.data, partial=True)
            if advogado.is_valid():
                info(f"UPDATE::AdvogadosConfirmacaoViewSet - {advModel.advogadoId=}")
                advogado.save()
                return JsonResponse(status=201, data=advogado.data)
            return JsonResponse(status=400, data="Parâmetros errados")
        except Exception as err:
            error(f"err::api/advogados/<advogadoId>/confirmacao/")
            return HttpResponse(status=510)

    serializer_class = ConfirmaAdvogadoSerializer
    http_method_names = ['get', 'patch']

class ListaAdvogadosByEscritorio(generics.ListAPIView):
    """Exibindo os(as) advogados(as) de determinado escritório"""

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    # ordering_fields = ['login']
    filterset_fields = ['confirmado', 'ativo']

    def get_queryset(self):
        queryset = None
        if len(self.kwargs) != 0:
            try:
                escritorioId = self.kwargs['pk']
                queryset = Advogado.objects.filter(escritorioId_id=escritorioId)
                info(f"api/escritorio/{escritorioId}/advogado")
                return queryset

            except Exception as err:
                error(f"api/escritorio/<int:pk>/advogado::{err}")
                return HttpResponse(status=510)


    serializer_class = AdvogadoSerializer

class AuthAdvogado(generics.RetrieveUpdateAPIView):
    """Autenticando usuário do PrevCliente"""

    search_fields = ['numeroOAB', 'email']
    serializer_class = AuthAdvogadoSerializer
    http_method_names = ['patch', 'get']

    def patch(self, request, *args, **kwargs):
        try:
            info(f"PATCH::api/advogados/auth/", extra={'teste': True})
            body: dict = request.data
            if 'senha' not in body.keys() or len(body['senha']) == 0:
                return HttpResponse(410, "Autenticação sem senha")

            senhaAdv = body['senha']

            if 'numeroOAB' in body.keys() and len(body['numeroOAB']) != 0:
                numeroOab = int(body['numeroOAB'])
                advogado = get_object_or_404(
                    Advogado,
                    numeroOAB=numeroOab,
                    senha=senhaAdv,
                    ativo=True,
                    confirmado=True,
                )
                modeloRetorno = AuthAdvogadoSerializer(advogado).data
                return JsonResponse(modeloRetorno, status=status.HTTP_202_ACCEPTED)
            elif 'cpf' in body.keys() and len(body['cpf']) != 0:
                cpfAdv = body['cpf']
                advogado = get_object_or_404(
                    Advogado,
                    cpf=cpfAdv,
                    senha=senhaAdv,
                    ativo=True,
                    confirmado=True,
                )
                modeloRetorno = AuthAdvogadoSerializer(advogado).data
                return JsonResponse(modeloRetorno, status=status.HTTP_202_ACCEPTED)
            elif 'email' in body.keys() and len(body['email']) != 0:
                emailAdv = body['email']
                advogado = get_object_or_404(
                    Advogado,
                    email=emailAdv,
                    senha=senhaAdv,
                    ativo=True,
                    confirmado=True,
                )
                modeloRetorno = AuthAdvogadoSerializer(advogado).data
                return JsonResponse(modeloRetorno, status=status.HTTP_202_ACCEPTED)
            else:
                warning("Erro ao tentar autenticar advogado")
                return HttpResponse("Erro ao tentar autenticar advogado", status=404)

        except Http404 as err:
            warning(err)
            return HttpResponse("Falha no login. Nenhum advogado encontrado", status=404)

        except Exception as err:
            error(f"PATCH::api/advogados/auth/ ________ {err}")
            print(f"patch(AuthAdvogado): {err=}")
            return HttpResponse(status=510)

    def get_object(self):
        try:
            login = self.kwargs['login']
            if login is not None:
                if login.isdecimal():
                    info(f'OAB::api/advogados/auth/{login}')
                    return get_object_or_404(Advogado, numeroOAB=self.kwargs['login'])
                else:
                    info(f'Email::api/advogados/auth/{login}')
                    return get_object_or_404(Advogado, email=self.kwargs['login'], ativo=True)
            else:
                info(f'api/advogados/auth/{login}')
                JsonResponse(status=400, data="Parâmetros errados")
        except Exception as err:
            error(f'api/advogados/auth/<login>')
            return HttpResponse(status=510)

    def get_queryset(self):
        queryset = self.get_object()
        return queryset

class TrocaSenhaViewSet(generics.RetrieveUpdateAPIView):
    """Primeiro acesso do advogado pelo PrevCliente"""

    serializer_class = TrocaSenhaSerializer
    http_method_names = ['post', 'get']

    def verificaTipoBool(self, variavel) -> bool:
        if isinstance(variavel, bool):
            return variavel
        elif isinstance(variavel, str):
            return variavel == 'True'
        else:
            return False

    def post(self, request, **kwargs):
        try:
            info(f"POST::api/advogados/auth/trocaSenha")
            if request.data is not None:
                if 'esqueceuSenha' in request.data.keys():
                    esqueceuSenha = self.verificaTipoBool(request.data['esqueceuSenha'])
                else:
                    esqueceuSenha = False

                if 'info' in request.data.keys() and request.data['info'] is not None:
                    login = request.data['info']
                    if login is not None:
                        advogado: Advogado = self.get_object(login, esqueceuSenha=esqueceuSenha)
                        if advogado is not None:
                            trocaSenha = TrocaSenha()
                            trocaSenha.advogadoId = advogado
                            trocaSenha.primAcesso = not esqueceuSenha
                            trocaSenha.codAcesso = randint(10000, 99999)

                            if esqueceuSenha:
                                trocaSenha.tipoTroca = TipoTrocaSenha.EsqueceuSenha.value
                                advogado.confirmado = True
                                trocouSenhaAdvogado(advogado, trocaSenha)
                            else:
                                advogado.confirmado = False
                                trocaSenha.tipoTroca = TipoTrocaSenha.PrimeiroAcesso.value
                                primeiroAcessoAdvogado(advogado, trocaSenha)

                            advogado.save()
                            trocaSenha.save()
                            return JsonResponse({"advogadoId": advogado.advogadoId})
                        else:
                            return HttpResponse("Nenhum advogado encontrado", status=310)
                    else:
                        return HttpResponse("Não foi possível carregar o CPF/E-mail enviado", status=300)
        except Exception as err:
            print(err)
            error(f'POST::api/advogados/auth/trocaSenha/')
            return HttpResponse(status=510)

    def get_object(self, infoRequest: str, esqueceuSenha: bool = False):
        info = infoRequest
        if info.isnumeric():
            queryset = get_object_or_404(Advogado, cpf=info, confirmado=esqueceuSenha)
        else:
            queryset = get_object_or_404(Advogado, email=info, confirmado=esqueceuSenha)

        return queryset

class AutenticaPrimeiroAcesso(generics.RetrieveUpdateAPIView):
    """Faz a autenticação do primeiro acesso por meio do código de acesso enviado por email"""

    serializer_class = TrocaSenhaSerializer
    http_method_names = ['patch', 'get']

    def get_queryset(self):
        queryset = None
        try:
            info(f"GET::api/advogados/auth/autenticaCodAcesso/<int:codAcesso>")
            queryset = TrocaSenha.objects.filter(verificado=True)

            return queryset
        except Exception as err:
            error(f"api/advogados/auth/autenticaCodAcesso/<int:codAcesso>")
            return HttpResponse(status=510)

    def patch(self, request, **kwargs):
        try:
            info(f"PATCH::api/advogados/auth/autenticaCodAcesso/<int:codAcesso>")

            if 'codigo' not in request.data.keys():
                error(f'api/advogados/auth/autenticaCodAcesso/<int:codAcesso>')
                return HttpResponse(status=410)
            else:
                codigo = int(request.data['codigo'])
                if codigo is not None:
                    primAcesso: TrocaSenha = self.get_object(codigo)
                    if primAcesso is not None:
                        tempoDecorrido: relativedelta = relativedelta(timezone.now(), primAcesso.dataCadastro)
                        if tempoDecorrido.minutes > 10:
                            return HttpResponse("Tempo excedido. Tente novamente.", status=406)
                        else:
                            primAcesso.verificado = True
                            primAcesso.save()
                            return HttpResponse("Código de acesso confirmado.", status=201)
                else:
                    return HttpResponse("Chave incorreta", status=310)
        except Exception as err:
            print(err)
            error(f'api/advogados/auth/autenticaCodAcesso/<int:codAcesso>')
            return HttpResponse(status=510)

    def get_object(self, codigo: int):
        return get_object_or_404(TrocaSenha, codAcesso=codigo, verificado=False)

