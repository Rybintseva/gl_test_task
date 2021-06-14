#!/usr/bin/python
import crypt
import getopt
import os
import sys


def create_user(username, _password):
    _enc_password = crypt.crypt(_password, "22")
    return os.system(f'sudo useradd -p {_enc_password} {username}')


def modify_user(username, new_username):
    return os.system(f'sudo usermod -l {new_username} {username}')


def remove_user(username):
    return os.system(f'sudo deluser {username}')


def main(argv):
    if not argv:
        sys.exit('Available arguments: -u <username> -p <password>')
    username = ''
    new_username = ''
    _password = ''
    try:
        opts, args = getopt.getopt(argv, 'u:p:')
    except getopt.GetoptError:
        sys.exit('Available arguments: -u <username> -p <password>')
    for opt, arg in opts:
        if opt == 'u':
            username = arg
            new_username = f'new_{username}'
        if opt == 'p':
            _password = arg
    create_user(username, _password)
    print('User is created')
    modify_user(username, new_username)
    print('User is modified')
    remove_user(new_username)
    print('User is removed')


if __name__ == "__main__":
    main(sys.argv[1:])
