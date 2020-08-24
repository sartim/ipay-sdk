import hashlib


def hash_string(text):
    """Hash string with sha1"""
    return hashlib.sha1(text.encode()).hexdigest()
