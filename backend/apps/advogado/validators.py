from validate_docbr import CPF


def validaCpf(numeroCpf: str):
    cpf = CPF()
    return cpf.validate(numeroCpf)


def validaTamanhoNumOAB(numeroOAB: str):
    return len(numeroOAB) == 9


def validaApenasNumerosOAB(numeroOAB: str):
    return numeroOAB.isdecimal()


def validaNomeAdvogado(nomeAdvogado: str):
    return nomeAdvogado.isalpha()


def validaSobrenomeAdvogado(sobrenomeAdvogado: str):
    return sobrenomeAdvogado.isalpha()
