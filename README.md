## Dockerfile

Exemplo de como criar um container usando Dockerfile, que vai rodar um programa "Hello, World!" em Python.


Primeiro, baixar os arquivos "Dockerfile" e "helloworld.py" (que contém o código do programa) para a máquina local. Se estiver usando o terminal da VM da Amazon, podem baixar os arquivos pra lá também. Um jeito fácil de fazer isso é usar o comando "wget" para baixar o conteúdo "raw" da página aqui do github, onde se encontra o código dos arquivos e transformá-los em arquivos dentro da VM.

Exemplo:
<pre>
wget https://raw.githubusercontent.com/mgechev123/container-docker-python/main/Dockerfile
wget https://raw.githubusercontent.com/mgechev123/container-docker-python/main/helloworld.py
</pre>

Após esse passo, use o comando "ls" para confirmar que os arquivos foram criados no diretório. Use o comando "cat" para confirmar o conteúdo.

<pre>
cat Dockerfile
cat helloworld.py
</pre>

Entrar no diretório onde se encontra o arquivo Dockerfile e criar uma imagem:

<pre>
docker build -t webserver .
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
