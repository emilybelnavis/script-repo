#-*- coding: utf-8 -*-

import argparse
import base64
import string
import secrets
import sys, os

parser = argparse.ArgumentParser(description="Secure String Generator")

parser.add_argument("str_length", help="Length of string in chars/bytes", type=int)
parser.add_argument("-b","--bytes", action="store_true", help="Generate a random string of bytes")
parser.add_argument("-B","--base64", action="store_true", help="Generate a random string encoded in base64")
parser.add_argument("-H","--hex", action="store_true", help="Generate a random string of hex characters")
parser.add_argument("-a", "--alphanumeric", action="store_true", help="Generate a random string of alphanumeric characters")

args = vars(parser.parse_args())


def gen_bytes(length):
    str = secrets.token_bytes(length)
    print(str)


def gen_b64(length):
    str = bytes(secrets.token_urlsafe(length), 'utf-8')
    str = base64.b64encode(str)
    print(str.decode('utf-8'))


def gen_alpha(length):
    str = secrets.token_urlsafe(length)
    str = str.replace('_','')
    str = str.replace('-','')
    print(str)


def gen_hex(length):
    str = secrets.token_hex(length)
    print(str)


if args["bytes"]:
    gen_bytes(args["str_length"])
elif args["base64"]:
   gen_b64(args["str_length"])
elif args["hex"]:
    gen_hex(args["str_length"])
elif args["alphanumeric"]:
    gen_alpha(args["str_length"])
else:
    print("No option selected. Use -h for help.")