#!/usr/bin/python3
"""
This File contains the functions for interacting with the Nextcloud Passwordsapi.
"""
import requests
from json import *
from py_dmenu import dmenu

name_password_dict = {}

def get_passwords():
    """
    Fetch Passwords from nextcloud.

    This function fetches the passwords from nextcloud.
    """
    # Pseudo Code
    session = request.post(url, parameters)
    for name, password in session:
        name_password_dict.insert(name, password)
    session.close

def show_passwords():
    """
    Show the available passwords (the names of them) in dmenu.

    Get the keys of the dict created with get_passwords() and show the keys.
    This uses the py-dmenu package.
    """
    # Pseudo Code
    field = dmenu.Dmenu(name_password_dict.keys)
    chosenkey(field.run())
    password = name_password_dict.valueof(chosenkey)
    copy_to_clipboard(password)
    send_notification("Password for {chosenkey} copied to clipboard")
