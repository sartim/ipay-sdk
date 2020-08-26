from ipay_sdk.gateway import Ipay


class BaseTest:
    @classmethod
    def setup_class(cls):
        cls.hash_key = "demoCHANGED"
        cls.vid = "demo"
        cls.order_id = "1234"
        cls.test_number = "000000000000"
        cls.test_email = "write2sartim@gmail.com"
        cls.instance = Ipay(cls.hash_key)
        cls.callback_url = ""
        kwargs = dict(
            live=0, oid=cls.order_id, inv=cls.order_id,
            amount=10.00, tel=cls.test_number, eml=cls.test_email, vid=cls.vid,
            curr="KES", p1="", p2="", p3="", p4="", cbk=cls.callback_url,
            cst=1, crl=0
        )
        cls.instance.initiator_request(**kwargs)
