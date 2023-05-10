#!/bin/bash

FIRST_PARAM="$1"
SENHA="$2"
MANUAL="""
Ajuda para ações comuns na instalação do NewPrev.

--help                       Apresenta opções de ajuda
-h 

--installAll                 Parâmetro que instala MySQL server, cria o usuário NEWPREV e libera a porta do serviço
--lib-port <senha su>        Parâmetro para liberar a porta do banco de dados para acesso fora do localhost
--fix-mysql                  Ajusta erro Mysql(Mariadb) no Ubuntu 
--cria-usuario-sql           Roda o script que cria o usuário NEWPREV no banco e dá as permissões necessárias
--install-mysql              Instala o Mysql e abre na configuração do usuário SUPER (su)
--install-python3.8          Instala o Python 3.8
--purge-mysql                Desinstala completemante o servidor do MySQL
"""


case $FIRST_PARAM in
	"-h")
		echo "$MANUAL"
	;;

	"--help")
		echo "$MANUAL"
	;;

	"")
		echo "$MANUAL"
	;;

	"--lib-port")
		sudo -S chmod ug+rw /etc/mysql/mysql.conf.d/mysqld.cnf
		python3.8 liberaBancoMysql.py
		echo -e "$SENHA" | sudo -S ufw allow 3306
	;;

	"--fix-mysql")
		sudo -S apt-get install python3-dev default-libmysqlclient-dev build-essential -y
		pip install --upgrade pip
	;;

	"--cria-usuario-sql")
		sudo -S mysql -h 'localhost' < usuarioSQL.sql
	;;

	"--install-mysql")
		sudo -S apt-get remove mysql-server -y
		sudo -S apt-get remove mysql-client -y
		sudo -S apt-get remove mysql-common -y
		sudo -S apt-get remove phpmyadmin -y
		sudo -S apt autoremove

		sudo -S apt-get install mysql-server -y
	;;

	"--install-python3.8")
		sudo -S add-apt-repository ppa:deadsnakes/ppa
		sudo -S apt-get update
		sudo -S apt-get install python3.8 -y
		sudo -S apt-get install python3.8-venv -y
		sudo -S apt-get install python3.8-dev -y
		sudo -S apt-get install default-libmysqlclient-dev -y
		sudo -S apt-get install build-essential -y
		sudo -S apt-get install python3-pip -y
	;;

	"--installAll")
		sudo -S apt-get install python3-dev default-libmysqlclient-dev build-essential -y
		pip install --upgrade pip

		sudo -S apt-get install mysql-server -y
		sudo -S mysql_secure_installation

		sudo -S mysql -h 'localhost' < usuarioSQL.sql
	;;

	"--purge-mysql")
		sudo -S systemctl stop mysql
		sudo apt-get clean -y
		sudo apt-get purge mysql-server-8.0 -y
		sudo apt-get purge mysql-server* -y
		sudo apt purge mysql-server mysql-client mysql-common mysql-server-core-* mysql-client-core-* -y
		sudo -S rm -rf /etc/mysql /var/lib/mysql /var/log/mysql
		sudo apt autoremove -y
		sudo apt autoclean -y

		sudo apt-get update -y
		sudo apt-get install -f
		sudo apt-get install mysql-server-8.0 -y
		sudo apt-get dist-upgrade -y
	;;

	"--teste")
		sudo apt-get clean
		sudo apt-get purge 'mysql*'
		sudo apt-get update
		sudo apt-get install -f
		sudo apt-get install mysql-server-8.0
		sudo apt-get dist-upgrade
	;;
esac
