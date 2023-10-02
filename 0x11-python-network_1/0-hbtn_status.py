#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as results:
        info = results.read()
        print("Body response:")
        print("\t- type: {}".format(type(info)))
        print("\t- content: {}".format(type(info)))
        print("\t- utf8 content: {}".format(info.decode('utf-8')))
