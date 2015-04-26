# Module for sending an email
import shelve
import os


def getCred():
    username = input('Everything before the @: ') + '@gmail.com'
    password = input('Password: ')
    shelf = shelve.open('cred_store')
    shelf['pass'] = password
    shelf['user'] = username
    shelf.close()


def sGmail(to, message):
    # TODO: send an email

