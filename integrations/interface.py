import aiohttp

from schema import Data


class External:
    def __init__(self, base_url: str, auth_endpoint: str, data_endpoint: str, username: str, password: str):
        self.base_url = base_url
        self.auth_url = f'{base_url}/{auth_endpoint}'
        self.data_url = f'{base_url}/{data_endpoint}'
        self.username = username
        self.password = password
        self.token = None

    async def authenticate(self):
        raise NotImplementedError

    async def send_data(self, data: Data):
        raise NotImplementedError
