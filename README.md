# __Educaton__
Project to support programming classes. A website developed taking into account the theory of multiple intelligences.

## __To run__

### Setup mysql server
- Install mysql server from oracle.
- create a database and a user with admin privileges for testing purposes with the following settings :

        - DATABASE NAME: educaton
        - USER: testuser
        - PASSWORD: 01020304050607
        - HOST: localhost
        - PORT: 3306

### Clone the project

```
git clone https://github.com/joaopedro02/educaton.git

```
### Install dependencies & activate virtualenv
    
- open a terminal in the destination folder and run these commands(the pip tool is needed):

```
pip install pipenv
pipenv install
pipenv shell
```
### Initialize the project
- Open a terminal on the project folder  `\educaton` and run the following commands:
    - `py manage.py migrate`
    - `py manage.py add_questions_answers_data` , to initialize the databank with data (mysql server must be running).   
    - `py manage.py runserver` , to start a server to acess the website. This server is only for test purposes.

- the website can be acessed by the adrees given by the `py manage.py runserver` command where the server is running.

___
## __Para Rodar__

### Configure o mysql server
- instale o mysql server distribuído pela oracle
- crie um database e um usuário com privilégios de administrador com as seguintes configurações: 

        - DATABASE NAME: educaton
        - USUARIO : testuser
        - SENHA : 01020304050607
        - HOST: localhost
        - PORT: 3306

### Clone o projeto

```
git clone https://github.com/joaopedro02/educaton.git

```
### Instale as dependências & ative o virtualenv
- Abra um terminal na pasta de destino e rode esses comandos (a ferramenta pip é necessária) :
```
pip install pipenv
pipenv install
pipenv shell
```
### Inicialize o projeto
- Abra um terminal no diretório `\educaton` e rode os seguintes comandos:
    - `py manage.py migrate`
    - `py manage.py add_questions_answers_data` , para inicializar o banco de dados ( o mysql server precisa estar em execução).   
    - `py manage.py runserver` , para iniciar um servidor para o website. Esse servidor só é indicado para testes.
- O website pode ser acessado pelo endereço dado pelo comando `py manage.py runserver` onde o servidor está sendo executado.