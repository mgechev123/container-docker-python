## Dockerfile

Exemplo de como criar um container usando Dockerfile, que vai rodar um programa "Hello, World!" em Python.

Os passos serão:
<pre>
-Criar um arquivo com o código fonte do programa Python
-Criar um arquivo Dockerfile
-Criar a imagem docker usando o build
-Rodar a imagem dentro de um container usando o run
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

3. Agora, vamos entrar no diretório onde se encontram os arquivos e vamos criar uma imagem docker a partir do Dockerfile, usando o comando "build":

<pre>
docker build -t "nome_imagem" -f Dockerfile .
</pre>

4. Listar as imagens para verificar se a nossa imagem foi criada:

<pre>
docker images
</pre>

5. Vamos usar o comando "run" para executar a imagem no container. A porta mapeada será a 3333:

<pre>
docker run -d -p 3333:3333 "nome_imagem"
</pre>

6. Para testar, há algumas maneiras. 

Caso esteja utilizando o ambiente da Amazon, acesse o endereço IP público da máquina virtual através do seu browser, adicionando a porta ao final do endereço:
<pre>
ec2-54-89-206-156.compute-1.amazonaws.com:3333
</pre>

Se quiser testar dentro do terminal mesmo, use o comando curl para verificar a mensagem de sucesso:
<pre>
docker curl http://localhost:3333
</pre>

Se estiver executando o container localmente, acessar diretamente o endereço localhost no seu browser:
<pre>
http://localhost:3333
</pre>
