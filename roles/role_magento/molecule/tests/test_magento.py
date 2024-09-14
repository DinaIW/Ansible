def test_magento_page(host):
    cmd = host.run("curl http://localhost")
    assert "Magento" in cmd.stdout
