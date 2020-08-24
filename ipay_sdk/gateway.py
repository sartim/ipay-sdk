from ipay_sdk.helpers import make_request
from ipay_sdk.config import BaseConfig


constants = BaseConfig


class Ipay:
    def __init__(self, hash_key):
        self.hash_key = hash_key

    def generated_hash(self):
        pass

    def initiator_request(self):
        params = dict(
            method="POST",
            url=constants.INITIATOR_URL,
            data=self.generated_hash()
        )
        response = make_request(**params)
        if response.status_code == 200:
            return response.json()
        return None
