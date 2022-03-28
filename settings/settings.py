import pathlib

from decouple import config
from decouple import Choices

from aws.rds import RDS
from aws.secrets import Secret


class Settings:
    rds = RDS()
    secret = Secret()

    STAGE = config('STAGE', cast=Choices(['local', 'dev', 'homolog', 'prod']))
    BASE_DIR = pathlib.Path(__file__).parent.parent

    CHROMIUM_EXECUTABLE = '/usr/bin/chromium-browser'
    FIREFOX_EXECUTABLE = '/usr/bin/firefox'

    @property
    def stage_name(self):
        return 'dev' if self.STAGE == 'local' else self.STAGE

    @property
    def is_local(self):
        return self.STAGE == 'local'

    @property
    def is_dev(self):
        return self.STAGE == 'dev'

    @property
    def is_homolog(self):
        return self.STAGE == 'homolog'

    @property
    def is_prod(self):
        return self.STAGE == 'prod'

    @property
    def is_aws(self):
        return any([self.is_dev, self.is_homolog, self.is_prod])

    @property
    def db_host(self):
        return self.secret(f'db_{self.stage_name}', 'db_host')

    @property
    def db_port(self):
        return self.secret(f'db_{self.stage_name}', 'db_port')

    @property
    def db_user(self):
        return self.secret(f'db_{self.stage_name}', 'db_user')

    @property
    def db_password(self):
        return self.rds(self.db_host, self.db_port, self.db_user)

    @property
    def db_database(self):
        return self.secret(f'db_{self.stage_name}', 'db_database')

    @property
    def db_url(self):
        host = self.db_host
        port = self.db_port
        user = self.db_user
        password = self.db_password
        database = self.db_database
        return f'mysql://{user}:{password}@{host}:{port}/{database}'

    @property
    def chromedriver(self):
        if self.is_aws:
            return '/usr/bin/chromedriver'
        return str(pathlib.Path.home() / '.local/bin/chromedriver')

    @property
    def geckodriver(self):
        if self.is_aws:
            return '/usr/bin/geckodriver'
        return str(pathlib.Path.home() / '.local/bin/geckodriver')
