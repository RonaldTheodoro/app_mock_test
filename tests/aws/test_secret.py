
def test_secret(secret):
    assert secret('db_dev', 'db_host') == 'localhost'
    assert secret('db_dev', 'db_port') == '3699'
    assert secret('db_dev', 'db_user') == 'user_dev'
