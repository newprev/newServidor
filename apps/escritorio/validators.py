from validate_docbr import CNPJ

def validaCNPJ(numeroCNPJ: str):
    cnpj = CNPJ()
    return cnpj.validate(numeroCNPJ)

