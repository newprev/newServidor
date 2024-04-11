## @ Ambiente do Linux
atualiza-apt: ## Atualizando repositórios apt
	@echo "Atualizando repositorios apt"
	@sudo apt-get upgrade -y
	@sudo apt-get update -y
	@sudo apt upgrade -y
	@sudo apt update -y

# -----------------------------------


## @ Limpeza de migrações
clearAllMigrations: ## Exclui todos os arquivos de migração gerados pelo sistema
	@echo 'Limpando as migrações'
	@rm -f apps/advogado/migrations/*.py && echo "---> apps/advogado/migrations"
	@rm -f apps/escritorios/migrations/*.py && echo "---> apps/escritorios/migrations"
	@rm -f apps/ferramentas/migrations/*.py && echo "---> apps/ferramentas/migrations"
	@rm -f apps/informacoes/migrations/*.py && echo "---> apps/informacoes/migrations"
	@rm -f apps/sincron/migrations/*.py && echo "---> apps/sincron/migrations"
	@rm -f apps/sincron/migrations/*.py && echo "---> apps/newMails/migrations"


recriaAllMigrations: clearAllMigrations makeAllMigrations ## Exclui todos os arquivos de migração, recria todos e completa todas as migrações
recriaAtualiza: recriaAllMigrations updateDB-Backup ## Deleta banco de dados, recria, deleta todos os arquivos de migração, recria, completa a migração e popula o banco com o último backup feito.


## @ Migracoes
makeAllMigrations: ## Cria todos os arquivos de migração e completa a migração
	@echo 'Makemigrations'
	@python manage.py makemigrations escritorio
	@python manage.py makemigrations advogado
	@python manage.py makemigrations ferramentas
	@python manage.py makemigrations informacoes
	@python manage.py makemigrations gerenciamento
	@python manage.py makemigrations sincron
	@python manage.py makemigrations newMails
	@python manage.py migrate


## @ Banco de dados
updateDB-Backup: ## Atualiza o banco baseado nos arquivos de backup criados 
	@echo 'Atualizando todas as tabelas'
	@mysql -h localhost -u NEWPREV -p GIDEON < ../backup/carenciasLei91.sql
	@echo '--> Carências da Lei de 91 está atualizado'
	@mysql -h localhost -u NEWPREV -p GIDEON < ../backup/convMon.sql
	@echo '--> Conversões Monetárias está atualizada'
	@mysql -h localhost -u NEWPREV -p GIDEON < ../backup/expectativaSobrevida.sql
	@echo '--> Expectativas de sobrevida estão atualizadas'
	@mysql -h localhost -u NEWPREV -p GIDEON < ../backup/indicadores.sql
	@echo '--> Indicadores do CNIS estão atualizados'
	@mysql -h localhost -u NEWPREV -p GIDEON < ../backup/salarioMinimo.sql
	@echo '--> Salários Minimos estão atualizados'
	@mysql -h localhost -u NEWPREV -p GIDEON < ../backup/tetosPrev.sql
	@echo '--> Tetos previdenciarios estão atualizados'
	@mysql -h localhost -u NEWPREV -p GIDEON < ../backup/indicesAtuMonetaria.sql
	@echo '--> Índices de atualização monetária estão atualizados'
	@mysql -h localhost -u NEWPREV -p GIDEON < ../backup/TipoBeneficio.sql
	@echo '--> Tipo de benefícios estão atualizados'
	@mysql -h localhost -u NEWPREV -p GIDEON < ../backup/especieTipo.sql
	@echo '--> Tipos de espécies de benefícios estão atualizados'

updateDB-Tabela: ## Atualiza apenas uma tabela baseado no arquivo de backup criado
	@mysql -h localhost -u NEWPREV -p GIDEON < ../backup/indicesAtuMonetaria.sql


# -----------------------------------

# @ Instalação do pip e poetry
install-pip: ## Instala gerenciador de dependências do Python
	@sudo apt install python3-pip -y

# @ Instalação de ferramentas
install-poetry: ## Instalação do gerenciador de ambiente
	@pip install --upgrade pip
	@sudo -S apt install pipx -y
	@pipx install poetry
	@pipx ensurepath

# @ Instala bibliotecas necessarias do projeto
install-libs: ## Instala libs do Python com Poetry
	@exec bash -l
	@poetry install

# -----------------------------------

## @ Instalação do sistema
instala-mysql: ## Instala mysql e dependências
	@sudo -S apt-get install python3-dev default-libmysqlclient-dev build-essential libssl-dev -y
	@sudo -S apt install python3-dev default-libmysqlclient-dev build-essential libssl-dev -y
	@sudo -S apt-get install mysql-server -y

libera-porta-mysql: ## Libera porta do banco ded dados para acesso externo
	@echo "Liberando porta do mysql para acesso externo"
	@sudo -S chmod ug+rw /etc/mysql/mysql.conf.d/mysqld.cnf
	@sudo python3 instalacao/liberaBancoMysql.py
	@sudo -S ufw allow 3306
	@sudo systemctl restart mysql
	@sudo -S mysql_secure_installation
	@sudo -S mysql -h 'localhost' < instalacao/usuarioSQL.sql


install: atualiza-apt install-pip install-poetry instala-mysql libera-porta-mysql ## Instala tudo
makeEverything: install install-libs recriaAtualiza ## Instala tudo necessário para iniciar o sistema
