from unittest import mock

import pytest

from aws.rds import RDS
from aws.secrets import Secret
from aws.ssm import SSM
from settings.settings import Settings


PAYLOAD = {
    'db_dev': {
        'db_host': 'localhost',
        'db_port': '3699',
        'db_user': 'user_dev',
        'db_database': 'db_dev',
    },
    'db_homolog': {
        'db_host': 'localhost',
        'db_port': '3699',
        'db_user': 'user_homolog',
        'db_database': 'db_homolog',
    },
    'db_prod': {
        'db_host': 'localhost',
        'db_port': '3699',
        'db_user': 'user_prod',
        'db_database': 'db_prod',
    },
}


def get_secret(secret_id, field):
    return PAYLOAD[secret_id][field]


def get_ssm(ssm_id, field):
    return PAYLOAD[ssm_id][field]


def generate_token(host, port, user):
    payload = {
        ('localhost', '3699', 'user_dev'): 'dev_token',
        ('localhost', '3699', 'user_homolog'): 'homolog_token',
        ('localhost', '3699', 'user_prod'): 'prod_token',
    }
    return payload[(host, port, user)]


@pytest.fixture
def secret():
    with mock.patch.object(Secret, 'get_secret', side_effect=get_secret):
        yield Secret()


@pytest.fixture
def ssm():
    with mock.patch.object(SSM, 'get_ssm', side_effect=get_ssm):
        yield SSM()


@pytest.fixture
def rds():
    with mock.patch.object(RDS, 'generate_token', side_effect=generate_token):
        yield RDS()


@pytest.fixture
def settings_base(rds, secret):
    params = {
        'rds': rds,
        'secret': secret,
    }
    with mock.patch.multiple(Settings, **params):
        yield Settings()
