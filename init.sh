#!/bin/sh

# Iniciando ambiente virtual
echo 'Iniciando ambiente virtual *****************'
echo '    '
python3 -m venv prevServEnv
source prevServEnv/bin/activate
pip install --upgrade pip
echo '    '
echo '    '
echo 'Instalando dependencias do projeto **************'
echo '    '
pip install -r requirements.txt

# Criando projeto do Django
echo '    '
echo '    '
echo 'Criando projeto do Django *********************'
echo '    '
django-admin startproject newPrevServ .

# Criando pastas importantes
echo 'Criando pastas importantes *******************'
echo '    '
mkdir datasource
mkdir -p logs/historicoLogs
mkdir templates