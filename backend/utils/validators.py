from validate_docbr import CPF, CNPJ
import re as regex
from django.core.exceptions import ValidationError

from utils.enums.exceptionCodesEnums import NewValidationError


def validaCpf(numeroCpf: str):
    cpf = CPF()
    return cpf.validate(numeroCpf)


def validaCNPJ(numeroCNPJ: str):
    cnpj = CNPJ()
    return cnpj.validate(numeroCNPJ)

def validaEmail(email: str):
    padrao: str = "[a-z0-9.]+@[a-z0-9]+.[a-z]+.([a-z]+)?"
    if email is not None and regex.match(padrao, email) is None:
        raise ValidationError(NewValidationError.emailInvalido.value)
    else:
        return email


def validaApenasNumero(numero: str):
    if isinstance(numero, int) or (isinstance(numero, str) and numero.isdecimal()):
        return numero

    else:
        raise ValidationError("Digite apenas números")


def validaSenha(senha: str):
    padraoMinuscula: str = "(?=.*[a-z])"
    padraoMaiuscula: str = "(?=.*[A-Z])"
    padraoNumero: str = "(?=.*?[0-9])"
    padraoEspecial1: str = "(?=.*[!@#$%¨&*()_-])"
    padraoEspecial2: str = "(?=.*[=+ ;:|><'.,])"

    verificaMinuscula: bool = regex.match(padraoMinuscula, senha) is not None
    verificaMaiuscula: bool = regex.match(padraoMaiuscula, senha) is not None
    verificaNumero: bool = regex.match(padraoNumero, senha) is not None
    verificaEspecial1: bool = regex.match(padraoEspecial1, senha) is not None
    verificaEspecial2: bool = regex.match(padraoEspecial2, senha) is not None
    verificaQtd: bool = len(senha) > 7

    if verificaQtd and (verificaEspecial1 or verificaEspecial2) and verificaMaiuscula and verificaNumero and verificaMinuscula:
        return senha
    else:
        raise ValidationError("Senha não contém caracteres necessários")


def validaTelefone(telefone: str) -> str:
    if telefone is None or (isinstance(telefone, int) and len(str(telefone)) > 13):
        raise ValidationError(NewValidationError.telefoneInvalido.value)

    if not telefone.isnumeric():
        raise ValidationError(NewValidationError.telefoneInvalido.value)

    return telefone