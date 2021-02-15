# base image from which my image will be created
FROM httpd

# copy the index.html to htdocs directory
COPY ./index.html /usr/local/apache2/htdocs/

# expose port 80 for listening for incoming requests
EXPOSE 80

# run apache in foreground
CMD apachectl -D FOREGROUND
