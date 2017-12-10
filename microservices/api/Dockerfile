FROM php:5.6-apache
RUN docker-php-ext-install mysqli

# Add default apache listener
COPY app/conf/apache-config.conf /etc/apache2/sites-enabled/000-default.conf
COPY app/conf/ports.conf /etc/apache2/ports.conf
COPY app/src /var/www/html/