def test_mysql_is_running(host):
    service = host.service("mysql")
    assert service.is_running
    assert service.is_enabled

def test_mysql_port_listening(host):
    socket = host.socket("tcp://0.0.0.0:3306")
    assert socket.is_listening
