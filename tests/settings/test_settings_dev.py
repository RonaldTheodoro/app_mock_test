import pathlib
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


def test_settings_db_url_dev(settings):
    db_url = 'mysql://user_dev:dev_token@localhost:3699/db_dev'
    assert settings.db_url == db_url


def test_settings_chromedriver_dev(settings):
    assert settings.chromedriver == '/usr/bin/chromedriver'


def test_settings_chromium_executable_dev(settings):
    assert settings.chromium_executable == '/usr/bin/chromium-browser'


def test_settings_geckodriver_dev(settings):
    assert settings.geckodriver == '/usr/bin/geckodriver'


def test_settings_firefox_executable_dev(settings):
    assert settings.firefox_executable == '/usr/bin/firefox'
