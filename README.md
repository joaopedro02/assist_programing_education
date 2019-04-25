# Educaton
Project to support programming classes. A website developed taking into account the theory of multiple intelligences.
___
>__To run__

 - Setup mysql server
    - Install mysql server from oracle.
    - create a database and a user with admin privileges for testing purposes with the following settings :

            - DATABASE NAME: educaton
            - USER: testuser
            - PASSWORD: 01020304050607
            - HOST: localhost
            - PORT: 3306

- Install python 3.7.
- Install Django 2.2.
- Open a terminal on the project folder  `\educaton` and run the following commands:
    - `py manage.py add_questions_answers_data` , to initialize the databank with data (mysql server must be running).   
    - `py manage.py runserver` , to start a server to acess the website. This server is only for test purposes.

- the website can be acessed by the adrees given by the `py manage.py runserver` command where the server is running.

___
>__Para Rodar__

- Configure o mysql server
    - instale o mysql server distribuído pela oracle
    - crie um database e um usuário com privilégios de administrador com as seguintes configurações: 

            - DATABASE NAME: educaton
            - USUARIO : testuser
            - SENHA : 01020304050607
            - HOST: localhost
            - PORT: 3306

    - instale python 3.7
    - instale Django 2.2
    - Abra um terminal no diretório `\educaton` e rode os seguintes comandos:
        - `py manage.py add_questions_answers_data` , para inicializar o banco de dados ( o mysql server precisa estar em execução).   
        - `py manage.py runserver` , para iniciar um servidor para o website. Esse servidor só é indicado para testes.
    - O website pode ser acessado pelo endereço dado pelo comando `py manage.py runserver` onde o servidor está sendo executado.