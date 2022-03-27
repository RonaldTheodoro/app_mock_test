class Secret:
    storage = {}

    def __call__(self, secret_id, field):
        return self.get_secret(secret_id, field)

    def get_secret(self, secret_id, field):
        if secret_id not in self.storage:
            payload = self.get_secret_from_aws(secret_id)

            self.storage[secret_id] = payload

        if field not in self.storage[secret_id]:
            raise Exception(f'{field} not in {secret_id}')

        return self.storage[secret_id][field]

    def get_secret_from_aws(self, secret_id):
        payload = {
            'db_host': 'localhost',
            'db_port': '3699',
            'db_password': 'password',
            'db_user': 'user',
        }
        return payload