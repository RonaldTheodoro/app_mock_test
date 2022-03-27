from unittest import mock

import pytest


@pytest.fixture
def settings(settings_base):
    params = {
        'STAGE': 'dev',
    }
    with mock.patch.multiple(settings_base, **params):
        yield settings_base


def test_settings_stage_is_equal_dev(settings):
    assert settings.STAGE == 'dev'


def test_settings_stage_dev_is_not_local(settings):
    assert not settings.is_local
    

def test_settings_stage_is_dev(settings):
    assert settings.is_dev


def test_settings_stage_dev_is_not_homolog(settings):
    assert not settings.is_homolog


def test_settings_stage_dev_is_not_prod(settings):
    assert not settings.is_prod


def test_settings_stage_dev_is_aws(settings):
    assert settings.is_aws


def test_settings_stage_name_is_dev(settings):
    assert settings.stage_name == 'dev'


def test_settings_db_host_dev(settings):
    assert settings.db_host == 'localhost'


def test_settings_db_port_dev(settings):
    assert settings.db_port == '3699'


def test_settings_db_user_dev(settings):
    assert settings.db_user == 'user_dev'


def test_settings_db_password_dev(settings):
    assert settings.db_password == 'dev_token'


def test_settings_db_database_dev(settings):
    assert settings.db_database == 'db_dev'
