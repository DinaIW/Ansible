# Ansible
## Readme.
Magento est bien acessible, en revanche il y a des problemes avec le css. Je pense qu'il s'agit de permission.

sudo chown -R ubuntu:www-data /var/www/html/magento2-2.4.5
sudo find /var/www/html/magento2-2.4.5 -type d -exec chmod 775 {} \;
sudo find /var/www/html/magento2-2.4.5 -type f -exec chmod 664 {} \;



TO DO:
- Sécuriser le fichier instance_state.py
- Faire regle de sécurité pour le SHH "Ip public restreinte" (mais comme ma VM change d'ip tout les 3 heures... NO)

-- Adie debug
permission du fichier vendor : (insuufisant )
sudo chown -R www-data:www-data /var/www/html/magento2-2.4.5
sudo chmod -R 755 /var/www/html/magento2-2.4.5
Il faut ajouter l'utilisateur :
sudo chown -R ubuntu:www-data /var/www/html/magento2-2.4.5
sudo chmod -R 775 /var/www/html/magento2-2.4.5
ou faire un SUDO !!!

------
CREATE USER 'Fabien'@'%' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON fab_magento_db.* TO 'Fabien'@'%';
FLUSH PRIVILEGES;

-------
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
bind-address = 0.0.0.0

GRANT ALL PRIVILEGES ON fab_magento_db.* TO 'Fabien'@'%' IDENTIFIED BY 'password123';
FLUSH PRIVILEGES;


privilege de l'instance magento
dans le root avec l'ip de magento :
CREATE USER 'Fabien'@'35.180.186.138' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'Fabien'@'35.180.186.138' WITH GRANT OPTION;
FLUSH PRIVILEGES;

----------

# Nom de l'utilisateur sans mot de passe
username=ubuntu
# Créer l'utilisateur sans mot de passe
sudo adduser --gecos "" --disabled-password $username
# Ajouter l'utilisateur au groupe sudo pour les privilèges administratifs
sudo usermod -aG sudo $username
# Créer le répertoire .ssh pour l'utilisateur 'ubuntu' et copier la clé SSH autorisée
sudo mkdir /home/$username/.ssh/
sudo cp /home/ubuntu/.ssh/authorized_keys /home/$username/.ssh/authorized_keys
# Changer les permissions du fichier 'authorized_keys' pour appartenir à 'ubuntu'
sudo chown -R $username:$username /home/$username/.ssh/
sudo chmod 700 /home/$username/.ssh/
sudo chmod 600 /home/$username/.ssh/authorized_keys
pour les fichier statiques :
sudo find var pub/static pub/media app/etc -type f -exec chmod 644 {} \;
sudo find var pub/static pub/media app/etc -type d -exec chmod 755 {} \;
sudo chmod -R 777 var pub/static pub/media generated

-------

apres installation de magento :

verifier les permission du sossier public.
fichier statique de mangeto :
php bin/magento setup:static-content:deploy
permission magento :
sudo find var generated vendor pub/static pub/media app/etc -type f -exec chmod 664 {} \;
sudo find var generated vendor pub/static pub/media app/etc -type d -exec chmod 775 {} \;
sudo chmod u+x bin/magento
sudo chown -R www-data:www-data .
sudo chown -R www-data:www-data var/ generated/ pub/static/ pub/media/ app/etc
sudo chmod -R 775 var/ generated/ pub/static/ pub/media/ app/etc
sudo chown -R www-data:www-data var/
sudo chmod -R 775 var/
sudo systemctl stop apparmor

------
sudo nano /etc/php/8.1/fpm/php.ini
Vérifiez les paramètres suivants dans le fichier php.ini pour vous assurer qu'ils sont adaptés pour Magento :
memory_limit : Magento recommande généralement 2 Go de mémoire. Recherchez cette ligne et ajustez-la si nécessaire :
makefile
Copier le code
memory_limit = 2G
max_execution_time : Augmentez cette valeur à au moins 180 ou 300.
makefile
Copier le code
max_execution_time = 300
zlib.output_compression : Assurez-vous que la compression est activée.
graphql
Copier le code
zlib.output_compression = On
deployer les fichier static en sudo -u www-data php bin/magento setup:static-content:deploy -f
