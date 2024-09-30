# Ansible

TO DO:
- Sécuriser le fichier instance_state.py
- Faire regle de sécurité pour le SHH "Ip public restreinte" (mais comme ma VM change d'ip tout les 3 heures... NO)

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