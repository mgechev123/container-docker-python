## Dockerfile

Exemplo de como criar um container usando Dockerfile, que vai rodar um programa "Hello, World!" em Python.

Os passos serão:
<pre>
-Criar um arquivo com o código fonte do programa Python
-Criar um arquivo Dockerfile
-Criar a imagem docker usando o build
-Rodar a imagem dentro de um container
</pre>

1. Primeiro, baixar os arquivos "Dockerfile" e "helloworld.py" (que contém o código do programa) para a máquina local. Se estiver usando o terminal da VM da Amazon, podem baixar os arquivos pra lá também. Um jeito fácil de fazer isso é usar o comando "wget" para baixar o conteúdo "raw" da página aqui do github, onde se encontra o código dos arquivos e transformá-los em arquivos dentro da VM. (Também, é possível usar o Nano para criar os arquivos direto na máquina e copiar/colar o conteúdo, porém isso irá quebrar a formatação das linhas, e será preciso editá-las manualmente).

<pre>
wget https://raw.githubusercontent.com/mgechev123/container-docker-python/main/Dockerfile
wget https://raw.githubusercontent.com/mgechev123/container-docker-python/main/helloworld.py
</pre>

2. Após esse passo, use o comando "ls" para confirmar que os arquivos foram criados no diretório. Use o comando "cat" para checar se o conteúdo dos arquivos está correto.

<pre>
cat Dockerfile
cat helloworld.py
</pre>

3. Agora, vamos entrar no diretório onde se encontram os arquivos e vamos criar uma imagem docker a partir do Dockerfile, usando o comando build:

<pre>
docker build -t "nome_imagem" -f Dockerfile .
</pre>

Listar as imagens:

<pre>
docker images
</pre>

Executar o container:

<pre>
docker run -t -d -p 80:80 webserver
</pre>

Para testar, se estiver executando o container localmente, acesar diretamente o endereço localhost:

* http://localhost
