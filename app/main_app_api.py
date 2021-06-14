#!/usr/bin/python
import getopt
import sys

from requests import Session

SOURCE_USERS_URL = 'https://gorest.co.in/public-api/users'
SOURCE_USERS_RUD_URL = 'https://gorest.co.in/public-api/users/123'

session = Session()


def create_user(url, **kwargs):
    session.post(url, **kwargs)


def modify_user(url, **kwargs):
    session.put(url, **kwargs)


def remove_user(url, **kwargs):
    session.delete(url, **kwargs)


def main(argv):
    if not argv:
        sys.exit('Available arguments: -u \'{"name":"", "gender":"", "email":"", "status":""}\'')
    data = {}
    try:
        opts, args = getopt.getopt(argv, 'u:')
    except getopt.GetoptError:
        sys.exit('Available arguments: -u \'{"name":"", "gender":"", "email":"", "status":""}\'')
    for opt, arg in opts:
        if opt == 'u':
            data = arg
    create_user(SOURCE_USERS_URL, data=data)
    print('User is created')
    modify_user(SOURCE_USERS_RUD_URL, data=data)
    print('User is modified')
    remove_user(SOURCE_USERS_RUD_URL, data=data)
    print('User is removed')


if __name__ == "__main__":
    main(sys.argv[1:])
