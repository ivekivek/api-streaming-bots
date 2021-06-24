import webbrowser

import httplib2
from oauth2client import client
from oauth2client.file import Storage

flow = client.flow_from_clientsecrets(
    'client_secrets.json',
    scope=['https://www.googleapis.com/auth/youtube', 'https://www.googleapis.com/auth/youtube.force-ssl'],
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')

import sys

args = sys.argv

#auth_code = input("auth code: ")
auth_code = args [1]
credentials = flow.step2_exchange(auth_code)
http_auth = credentials.authorize(httplib2.Http())
storage = Storage("oauth_creds")
storage.put(credentials)