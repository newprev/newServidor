from apps.escritorios.models import Escritorio
from apps.advogado.models import Advogado, TrocaSenha

from django.core.mail import send_mail

from prevEnums import TipoLog, Prioridade


def emailBoasVindas(escritorio: Escritorio) -> True:
    try:
        send_mail(
            f'Seja bem vindo(a), {escritorio.nomeFantasia}',
            f'Olá!\nÉ um prazer ter você conosco. Abaixo estão alguns dos seus dados. Pedimos que confirme-os e, se tudo estiver correto, é só acessar nossa plataforma e '
            f'cadastrar os advogados que trabalharão na {escritorio.nomeFantasia}!',
            'thomas.anderson@newprev.dev.br',
            [escritorio.email],
            fail_silently=False
        )
        # logPrioridade("E-mail::emailBoasVindas", tipoLog=TipoLog.rest)
        return True
    except Exception as err:
        print(f"apps/newMail/views/cadastro: {err}")
        # logPrioridade(f"E-mail::emailBoasVindas::{err}", tipoLog=TipoLog.rest, priodiade=Prioridade.erro)
        return False


def primeiroAcessoAdvogado(advogado: Advogado, primAcessoModel: TrocaSenha) -> True:
    try:
        send_mail(
            f'Seja bem vindo(a), {advogado.nomeAdvogado}',
            f'Olá!\nÉ um prazer ter você conosco. Abaixo estão alguns dos seus dados. Pedimos que confirme-os e, se tudo estiver correto, insira o código de acesso e defina a sua senha.\n\nCódigo de acesso: {primAcessoModel.codAcesso}',
            'thomas.anderson@newprev.dev.br',
            [advogado.email],
            fail_silently=False
        )
        # logPrioridade("E-mail::primeiroAcessoAdvogado", tipoLog=TipoLog.rest)
        return True
    except Exception as err:
        print(err)
        # logPrioridade(f"E-mail::primeiroAcessoAdvogado::{err}", tipoLog=TipoLog.erro, priodiade=Prioridade.erro)

    return True

def trocouSenhaAdvogado(advogado: Advogado, primAcessoModel: TrocaSenha) -> True:
    try:
        send_mail(
            f'Troca de senha',
            f'Olá, {advogado.nomeAdvogado}! \n\nPara trocar sua senha, use o código gerado abaixo. Caso não tenha sido você que pediu para trocar a senha, entre em contato com a equipe de suporte o mais rápido possível.\n\nCódigo de acesso: {primAcessoModel.codAcesso}',
            'thomas.anderson@newprev.dev.br',
            [advogado.email],
            fail_silently=False
        )
        # logPrioridade("E-mail::trocaDeSenhaAdvogado", tipoLog=TipoLog.rest)
        return True
    except Exception as err:
        print(err)
        # logPrioridade(f"E-mail::trocaDeSenhaAdvogado::{err}", tipoLog=TipoLog.erro, priodiade=Prioridade.erro)

    return True
