import re
from pathlib import Path
from copy import deepcopy
from os import chmod
import stat

def main():
    pathMysql: Path = Path("/etc/mysql/mysql.conf.d/mysqld.cnf")
    reBindAdress: str = "bind-address[\s]{0,20}=[\s]{0,2}[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
    ipAntigo: str = ''
    arquivoTotal: str = ''

    if pathMysql.exists():
        # print(f"{stat.S_IRUSR=}")
        # print(f"{stat.S_IRGRP=}")
        # print(f"{stat.S_IROTH=}")
        # chmod(pathMysql, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)

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
        exit(1)

    else:
        print("Não funfou...")
        exit(0)

main()
