from typing import List

frequenciaPlano = [
    ('ME', 'Mensal'),
    ('AN', 'Anual'),
    ('VI', 'Vitalicio'),
]


def buscaAdvNaLista(listaAdvogados: List, advogadoId: int):
    for adv in listaAdvogados:
        if adv.advogadoId == advogadoId:
            return adv

    return None


def listaFrequenciaPlanos():
    return frequenciaPlano

def getEstados():
    return [
        ('AC', 'Acre'),
        ('AL','Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ]

def getEstadosDict() -> List:
    return [
        {'nome': 'São Paulo', 'uf': 'SP'},
        {'nome': 'Acre', 'uf': 'AC'},
        {'nome': 'Alagoas', 'uf': 'AL'},
        {'nome': 'Amapá', 'uf': 'AP'},
        {'nome': 'Amazonas', 'uf': 'AM'},
        {'nome': 'Bahia', 'uf': 'BA'},
        {'nome': 'Ceará', 'uf': 'CE'},
        {'nome': 'Distrito Federal', 'uf': 'DF'},
        {'nome': 'Espírito Santo', 'uf': 'ES'},
        {'nome': 'Goiás', 'uf': 'GO'},
        {'nome': 'Maranhão', 'uf': 'MA'},
        {'nome': 'Mato Grosso', 'uf': 'MT'},
        {'nome': 'Mato Grosso do Sul', 'uf': 'MS'},
        {'nome': 'Minas Gerais', 'uf': 'MG'},
        {'nome': 'Pará', 'uf': 'PA'},
        {'nome': 'Paraíba', 'uf': 'PB'},
        {'nome': 'Paraná', 'uf': 'PR'},
        {'nome': 'Pernambuco', 'uf': 'PE'},
        {'nome': 'Piauí', 'uf': 'PI'},
        {'nome': 'Rio de Janeiro', 'uf': 'RJ'},
        {'nome': 'Rio Grande do Norte', 'uf': 'RN'},
        {'nome': 'Rondônia', 'uf': 'RO'},
        {'nome': 'Roraima', 'uf': 'RR'},
        {'nome': 'Santa Catarina', 'uf': 'SC'},
        {'nome': 'Sergipe', 'uf': 'SE'},
        {'nome': 'Tocantins', 'uf': 'TO'},
    ]


def getTipoAuth() -> List:
    return [
        ('E', 'Escritorio'),
        ('A', 'Advogado'),
        ('S', 'Super')
    ]


def campoAlterado(campoOriginal, campoAlterado) -> bool:
    if campoAlterado is None or campoAlterado == '':
        return False
    return campoOriginal != campoAlterado