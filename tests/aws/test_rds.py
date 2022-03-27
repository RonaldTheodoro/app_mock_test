def test_rds(secret, rds):
    host = secret('db_prod', 'db_host')
    port = secret('db_prod', 'db_port')
    user = secret('db_prod', 'db_user')
    assert rds(host, port, user) == 'prod_token'
