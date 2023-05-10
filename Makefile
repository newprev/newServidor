##Parâmetros importantes
PASSWORD=senha

##Iniciar o servidor
run-dev:
	@python3.8 manage.py runserver
run-aws:
	@python3.8 manage.py runserver 0:8080
access-aws:
	@cd ../Documentos && ssh -i "NewPrevDev.pem" ubuntu@ec2-3-139-65-128.us-east-2.compute.amazonaws.com


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
deletaRecriaAtualiza: recriaBanco clearAllMigrations makeAllMigrations updateDB-Backup run-dev ## Deleta banco de dados, recria, deleta todos os arquivos de migração, recria, completa a migração,  popula o banco com o último backup feito e reinicia o servidor.


## @ Migracoes
makeAllMigrations: ## Cria todos os arquivos de migração e completa a migração
	@echo 'Makemigrations'
	@python3.8 manage.py makemigrations advogado
	@python3.8 manage.py makemigrations escritorios
	@python3.8 manage.py makemigrations ferramentas
	@python3.8 manage.py makemigrations informacoes
	@python3.8 manage.py makemigrations sincron
	@python3.8 manage.py makemigrations newMails
	@python3.8 manage.py migrate


## @ Banco de dados
updateDB-Backup: ## Atualiza o banco baseado nos arquivos de backup criados 
	@echo 'Atualizando todas as tabelas'
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/carenciasLei91.sql
	@echo '--> Carências da Lei de 91 está atualizado'
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/convMon.sql
	@echo '--> Conversões Monetárias está atualizada'
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/expectativaSobrevida.sql
	@echo '--> Expectativas de sobrevida estão atualizadas'
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/indicadores.sql
	@echo '--> Indicadores do CNIS estão atualizados'
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/salarioMinimo.sql
	@echo '--> Salários Minimos estão atualizados'
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/tetosPrev.sql
	@echo '--> Tetos previdenciarios estão atualizados'
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/indicesAtuMonetaria.sql
	@echo '--> Índices de atualização monetária estão atualizados'
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/TipoBeneficio.sql
	@echo '--> Tipo de benefícios estão atualizados'
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/especieTipo.sql
	@echo '--> Tipos de espécies de benefícios estão atualizados'

updateDB-Tabela: ## Atualiza apenas uma tabela baseado no arquivo de backup criado
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/indicesAtuMonetaria.sql

recriaBanco: ## Deleta o banco GIDEON, recria o banco e apresenta os bancos criados nessa base
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" -e "DROP DATABASE GIDEON; CREATE DATABASE GIDEON; SHOW DATABASES;"
