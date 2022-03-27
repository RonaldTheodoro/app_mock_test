
def test_ssm(ssm):
    assert ssm('db_homolog', 'db_host') == 'localhost'
    assert ssm('db_homolog', 'db_port') == '3699'
    assert ssm('db_homolog', 'db_user') == 'user_homolog'
