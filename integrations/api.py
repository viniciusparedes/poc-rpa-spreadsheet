import aiohttp

from integrations.interface import External
from schema import Data


class ExternalApi(External):
    async def authenticate(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    self.auth_url,
                    json={"username": self.username, "password": self.password}
            ) as response:
                response.raise_for_status()
                self.token = (await response.json())['token']

    async def send_data(self, data: Data):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    self.data_url,
                    json=data,
                    headers={"Authorization": f"Bearer {self.token}"}
            ) as response:
                response.raise_for_status()
                return await response.json()
