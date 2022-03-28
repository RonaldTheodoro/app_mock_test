from unittest import mock

import pytest


@pytest.fixture
def settings(settings_base):
    params = {
        'STAGE': 'prod',
    }
    with mock.patch.multiple(settings_base, **params):
        yield settings_base


def test_settings_stage_is_equal_prod(settings):
    assert settings.STAGE == 'prod'


def test_settings_stage_prod_is_not_local(settings):
    assert not settings.is_local


def test_settings_stage_prod_is_not_dev(settings):
    assert not settings.is_dev


def test_settings_stage_prod_is_not_homolog(settings):
    assert not settings.is_homolog


def test_settings_stage_is_prod(settings):
    assert settings.is_prod


def test_settings_stage_prod_is_aws(settings):
    assert settings.is_aws


def test_settings_stage_name_is_prod(settings):
    assert settings.stage_name == 'prod'


def test_settings_db_host_prod(settings):
    assert settings.db_host == 'localhost'


def test_settings_db_port_prod(settings):
    assert settings.db_port == '3699'


def test_settings_db_user_prod(settings):
    assert settings.db_user == 'user_prod'


def test_settings_db_password_prod(settings):
    assert settings.db_password == 'prod_token'


def test_settings_db_database_prod(settings):
    assert settings.db_database == 'db_prod'


def test_settings_db_url_prod(settings):
    db_url = 'mysql://user_prod:prod_token@localhost:3699/db_prod'
    assert settings.db_url == db_url


def test_settings_chromedriver_prod(settings):
    assert settings.chromedriver == '/usr/bin/chromedriver'


def test_settings_chromium_executable_prod(settings):
    assert settings.chromium_executable == '/usr/bin/chromium-browser'


def test_settings_geckodriver_prod(settings):
    assert settings.geckodriver == '/usr/bin/geckodriver'


def test_settings_firefox_executable_prod(settings):
    assert settings.firefox_executable == '/usr/bin/firefox'
