# Especifica a imagem de origem
FROM python:3

# Copia o programa para a imagem
ADD helloworld.py /

# Instala na imagem os pacotes necessários para o código
RUN pip install flask
RUN pip install flask_restful
 
# Expõe a porta da aplicação
EXPOSE 3333
 
# Roda o programa Python
CMD [ "python", "./helloworld.py"]
