# Especifica a imagem de origem
FROM python:3

# Instala as dependências
ADD helloworld.py /
RUN pip install flask
RUN pip install flask_restful
 
# Expõe a porta do apache
EXPOSE 3333
 
# Executa o apache
CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]
