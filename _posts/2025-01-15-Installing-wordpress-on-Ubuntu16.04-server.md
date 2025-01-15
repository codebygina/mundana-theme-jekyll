---
layout: post
title:  "WordPress Installation on Ubuntu 16.04"
author: Snowdiamond
categories: [ Jekyll, tutorial ]
image: assets/images/wordpress/wordpress-logo.jpg
tags: [Networking]
---
## Wordpress Installation on Ubuntu 16.04
Ubuntu 16.04 is quite old and requires the installation of some dependencies for WordPress installation and proper functionality.

## STEPS

**- SYSTEM UPDATE AND UPGRADE**  
  ```
  sudo apt update && sudo apt upgrade -y
  ```  
**- Apache Installation**
  ```
  sudo apt install apache2 -y
  ```
**- PHP INSTALLATION**
WordPress requires PHP to function but Ubuntu16.04's highest version of PHP is 7.0, which is not sufficient. So we are installing 7.4 using a third-party library.

```
sudo add-apt-repository ppa:jczaplicki/xenial-php74-temp
sudo apt-get update
sudo apt install php7.4
```

**- PHP MYSQLI EXTENSION INSTALLATION**

```
sudo apt install php7.4-mysql
sudo phpenmod mysqli
sudo systemctl restart apache2
```
**- UNINSTALLING PHP7.0 IF ALREADY INSTALLED**
```
sudo a2dismod php7.0
sudo a2enmod php7.4
sudo systemctl restart apache2
```
**- MYSQL INSTALLATION**
```
sudo apt update
sudo apt update
sudo apt install mysql-server -y
sudo mysql_secure_installation
```
**- MYSQL LOGIN AND DB CREATION**
`
sudo mysql -u root -p
`

**WORDPRESS DB CREATION**
```
CREATE DATABASE wordpress;
CREATE USER 'wordpressuser'@'localhost' IDENTIFIED BY 'password'; (replace 'wordpressuser with your desired username and 'password' with your desired password.
GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpressuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
**- WORDPRESS INSTALLATION**
```
sudo apt update
wget https://wordpress.org/latest.tar.gz
tar -xvzf latest.tar.gz
sudo mv wordpress /var/www/html/

```
**- SET PERMISSIONS**
```
sudo chown -R www-data:www-data /var/www/html/wordpress
sudo chmod -R 755 /var/www/html/wordpress

```
**- Apache Configuration**
  ```
  sudo nano /etc/apache2/sites-available/wordpresss.conf
  ```
  **ENTER THE BELOW CONFIGURATION CAREFULLY**
  ```
  <VirtualHost *:80>
    ServerName enter you server ip or domain here" e.g ServerName 192.168.300.6
    DocumentRoot /var/www/html/wordpress

    <Directory /var/www/html/wordpress>
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
  ```
  **SAVE CONFIGURATION**
  ```
  sudo a2ensite wordpress.conf
  sudo a2enmod rewrite
  sudo systemctl restart apache2
  ```
**NOTE:** There is a possibility of typing this wrongly and getting error when you are about to restart the server. use `sudo apachectl configtest` to trace the error.

**- LOGIN TO YOUR WORDPRESS WEBSITE**
Access your wordpress website using `http://your_server_ip` example `http://192.168.300.6`
