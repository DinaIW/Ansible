import testinfra

def test_mysql_running_and_enabled(host):
    # Vérifier si le service MySQL est en cours d'exécution et activé
    mysql = host.service("mysql")
    assert mysql.is_running
    assert mysql.is_enabled

def test_mysql_user_fabien_exists(host):
    # Vérifier si l'utilisateur 'Fabien' existe dans MySQL
    cmd = host.run("mysql -u root -e 'SELECT User FROM mysql.user WHERE User = \"Fabien\";'")
    assert "Fabien" in cmd.stdout

def test_mysql_listening(host):
    # Vérifier si le port 3306 (MySQL) est ouvert
    mysql_port = host.socket("tcp://0.0.0.0:3306")
    assert mysql_port.is_listening

def test_nginx_running_and_enabled(host):
    # Vérifier si Nginx est en cours d'exécution et activé
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

def test_nginx_listening(host):
    # Vérifier si le port 80 (HTTP) est ouvert pour Nginx
    nginx_port = host.socket("tcp://0.0.0.0:80")
    assert nginx_port.is_listening
