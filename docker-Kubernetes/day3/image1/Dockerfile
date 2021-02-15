FROM httpd

WORKDIR /usr/local/apache2/htdocs/

COPY ./index.html .

ADD ./files.zip /usr/local/apache2/htdocs/

EXPOSE 80

CMD apachectl -D FOREGROUND
