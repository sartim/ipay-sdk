from ipay_sdk.gateway import Ipay


class BaseTest:
    @classmethod
    def setup_class(cls):
        cls.hash_key = "demoCHANGED"
        cls.vid = "demo"
        cls.order_id = "1234CVK"
        cls.test_number = "000000000000"
        cls.test_email = "write2sartim@gmail.com"
        cls.instance = Ipay(cls.hash_key)
        cls.callback_url = "http://path/to/callback"
        kwargs = dict(
            live=0, oid=cls.order_id, inv=cls.order_id,
            amount=10.00, tel=cls.test_number, eml=cls.test_email, vid=cls.vid,
            curr="KES", p1="0", p2="123", p3="456", p4="789",
            cbk=cls.callback_url, cst=1
        )
        response = cls.instance.initiator_request(**kwargs)
        data = {
            'sid': '123DEM31518159851494053188904DEMO', 'oid': '1234CVK',
            'amount': '10.0', 'account': 'AT0239105540M',
            'payment_channels': [{'name': 'MPESA', 'paybill': '510800'},
                                 {'name': 'AIRTEL', 'paybill': '510800'},
                                 {'name': 'EQUITEL', 'paybill': '510800'}],
            'hash': '022c72242321211acc1f3aa65243a20dac10c357f99d50257c397968cd09609c'}
        assert response["header_status"] == 200
        assert response["status"] == 1
        assert response["data"] == data
        cls.sid = response["data"]["sid"]
