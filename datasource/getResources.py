from pathlib import Path
import os
import json
from utils.enums.conexoes import TipoConexao


def getDatabase(conexao: TipoConexao):
    pathSource: Path

    if conexao == TipoConexao.magic:
        pathSource = Path('.') / 'datasource' / 'magic.json'
    elif conexao == TipoConexao.hearthstone:
        pathSource: Path = Path('.') / 'datasource' / 'hearthstone.json'
    else:
        pathSource = Path('.')

    if pathSource.exists() and pathSource.is_file():
        banco = json.loads(pathSource.read_text(encoding='utf8'))
    else:
        raise Exception('Não foi possível encontrar as informações para conexão com o banco de dados.')

    return banco


def getEmailServer() -> dict:
    strPathSource: str = os.path.join(os.getcwd(), 'datasource', 'marioCart.json')

    with open(strPathSource, encoding='utf-8', mode='r') as cacheLogin:
        banco = json.load(cacheLogin)

    return banco

def getLoggingPsd():
    strPathSource: str = os.path.join(os.getcwd(), 'datasource', 'sentryPsd.txt')

    with open(strPathSource, encoding='utf-8', mode='r') as urlSentry:
        dsn: str = urlSentry.read()

    return dsn


