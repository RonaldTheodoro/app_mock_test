class RDS:

    def __call__(self, host, port, user):
        return self.generate_token(host, port, user)

    def generate_token(self, host, port, user):
        return 'password'
