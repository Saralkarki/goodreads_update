import os

def credentials():
    un = os.environ.get('GOODREADS_USER')
    pwd = os.environ.get('GOODREADS_PASS')
    return un,pwd
