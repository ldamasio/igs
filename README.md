# Teste de Desenvolvimento Django

## Introdução

O objetivo deste teste de programação é demonstrar minhas habilidades e conhecimento em Python, e mais especificamente no framework web Django.

Utilizamos o docker, contendo dois containers: um para o banco de dados PostgreSQL e outro para o projeto Django (API).

## INSTALAÇÃO
Testado no Ubuntu 20.10

### Removendo outras versões do docker

sudo snap remove --purge docker
sudo apt purge docker.io
sudo apt remove docker-compose

### Instalação uma versão funcional

sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
 echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose
sudo docker --version
sudo docker-compose --version

### Usar o docker sem o sudo

sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

### Buildar e subir todos os containers:

docker-compose up -d --build

## Requisição Principal

```
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```

## Resposta

```
[
  {
    "name": "Jose da Silva",
    "email": "jose.silva@igs-software.com.br",
    "department": "Tester"
  },
  {
    "name": "Jose dos Santos",
    "email": "jose.santos@igs-software.com.br",
    "department": "Developer"
  },
  {
    "name": "Jose Lima",
    "email": "jose.lima@igs-software.com.br",
    "department": "RH"
  }
]
```

## Todas as rotas

A aplicação roda na porta 8000. Utilize os métodos HTTP corretos:

 - `GET /overview`: Detalhes da API, se conexão leitura e escritura com a base de dados está OK, horário da última vez que o CRON foi executado, tempo online e uso de memória.
 - `POST /employee/create/`: Insere o registro de um novo colaborador.
 - `PUT /employee/:<pk>`: Será responsável por atualizar o registro de um colaborador.
 - `DELETE /employee/:<pk>`: Remove um colaborador da base de dados.
 - `GET /employee/:<pk>`: Obter a informação somente de um colaborador da base de dados.
 - `GET /employee`: Listar todos os colabodores (com paginação).
 - `POST /department/create/`: Insere o registro de um novo departamento.
 - `PUT /department/:<pk>`: Será responsável por atualizar o registro de um departamento.
 - `DELETE /department/:<pk>`: Remove um departamento da base de dados.
 - `GET /department/:<pk>`: Obter a informação somente de um departamento da base de dados.
 - `GET /department`: Listar todos os departamentos (com paginação).

## Bonus

Utilizei o Django Rest Framework (DRF) para maior agilidade no desenvolvimento.
Este recurso também facilita a manutenção / expansão da API.
O DRF também automatiza parte do processo de validação dos campos.
Aliado ao DRF, optamos por acrescentar paginação nas rotas de listagem, seja dos colaboradores, seja dos departamentos.

Além disso, criamos uma rota para monitoramento básico da saúde da API

### Rota para monitoramento da API

```
curl -H "Content-Type: application/javascript" http://localhost:8000/overview/
```
