import hashlib
import logging
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def make_request(**kwargs):
    try:
        req = requests.request(**kwargs)
    except Exception as e:
        logger.exception("Request Error: {}".format(str(e)))
        return None
    else:
        return req


def hash_string(text):
    """Hash string with sha1"""
    return hashlib.sha1(text.encode()).hexdigest()
