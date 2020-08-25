from ipay_sdk.gateway import Ipay


class BaseTest:
    @classmethod
    def setup_class(cls):
        cls.hash_key = "demoCHANGED"
        cls.vid = "demo"
        cls.instance = Ipay(cls.hash_key)
