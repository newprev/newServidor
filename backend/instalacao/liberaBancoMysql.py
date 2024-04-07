import re
from pathlib import Path
from copy import deepcopy
from os import chmod
import stat

def main():
    try:
        pathMysql: Path = Path("/etc/mysql/mysql.conf.d/mysqld.cnf")
        reBindAdress: str = "bind-address[\s]{0,20}=[\s]{0,2}[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
        ipAntigo: str = ''
        arquivoTotal: str = ''

        if pathMysql.exists():

            with pathMysql.open(mode='r', encoding='utf-8') as f:
                conteudoArquivo = f.read()
                if len(re.findall(reBindAdress, conteudoArquivo)) != 0:
                    ipAntigo = re.findall(reBindAdress, conteudoArquivo)[0]
                    arquivoTotal = deepcopy(conteudoArquivo)
                    arquivoTotal = arquivoTotal.replace(ipAntigo, 'bind-address\t\t= 0.0.0.0')
                    f.flush()

            if ipAntigo != '':
                with pathMysql.open('w', encoding='utf-8') as f:
                    f.write(arquivoTotal)
                    f.flush()

            print(f"Arquivo {pathMysql} alterado com sucesso!")
            exit(0)

        else:
            print("Não funfou...")
            exit(1)
    except Exception as err:
        print(err)
        exit(1)

main()
