class SSM:
    storage = {}

    def __call__(self, ssm_id, field):
        return self.get_ssm(ssm_id, field)

    def get_ssm(self, ssm_id, field):
        if ssm_id not in self.storage:
            payload = self.get_ssm_from_aws(ssm_id)

            self.storage[ssm_id] = payload

        if field not in self.storage[ssm_id]:
            raise Exception(f'{field} not in {ssm_id}')

        return self.storage[ssm_id][field]

    def get_ssm_from_aws(self, ssm_id):
        payload = {
            'db_host': 'localhost',
            'db_port': '3699',
            'db_password': 'password',
            'db_user': 'user',
        }
        return payload