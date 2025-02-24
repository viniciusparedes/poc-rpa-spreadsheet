import aiohttp


class ExternalApplication:
    def __init__(self, auth_url, data_endpoint, username, password):
        self.auth_url = auth_url
        self.data_endpoint = data_endpoint
        self.username = username
        self.password = password
        self.token = None

    async def authenticate(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    self.auth_url,
                    json={"username": self.username, "password": self.password}
            ) as response:
                response.raise_for_status()
                self.token = (await response.json())['token']

    async def send_data(self, data):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    self.data_endpoint,
                    json=data,
                    headers={"Authorization": f"Bearer {self.token}"}
            ) as response:
                response.raise_for_status()
                return await response.json()
