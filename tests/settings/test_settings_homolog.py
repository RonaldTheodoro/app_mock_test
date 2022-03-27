from unittest import mock

import pytest


@pytest.fixture
def settings(settings_base):
    params = {
        'STAGE': 'homolog',
    }
    with mock.patch.multiple(settings_base, **params):
        yield settings_base


def test_settings_stage_is_equal_homolog(settings):
    assert settings.STAGE == 'homolog'


def test_settings_stage_homolog_is_not_local(settings):
    assert not settings.is_local


def test_settings_stage_homolog_is_not_dev(settings):
    assert not settings.is_dev


def test_settings_stage_is_homolog(settings):
    assert settings.is_homolog


def test_settings_stage_homolog_is_not_prod(settings):
    assert not settings.is_prod


def test_settings_stage_homolog_is_aws(settings):
    assert settings.is_aws


def test_settings_stage_name_is_homolog(settings):
    assert settings.stage_name == 'homolog'


def test_settings_db_host_homolog(settings):
    assert settings.db_host == 'localhost'


def test_settings_db_port_homolog(settings):
    assert settings.db_port == '3699'


def test_settings_db_user_homolog(settings):
    assert settings.db_user == 'user_homolog'


def test_settings_db_database_homolog(settings):
    assert settings.db_database == 'db_homolog'
