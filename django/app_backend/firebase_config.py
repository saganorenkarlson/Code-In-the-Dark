import firebase_admin
import os
from firebase_admin import credentials

cred = credentials.Certificate({
  "type": os.environ['FIREBASE_ACCOUNT_TYPE'],
  "project_id": os.environ['FIREBASE_PROJECT_ID'],
  "private_key_id": os.environ['FIREBASE_PRIVATE_KEY_ID'],
  "private_key": os.environ['FIREBASE_PRIVATE_KEY'].replace('\\n', '\n'),
  "client_email": os.environ['FIREBASE_CLIENT_EMAIL'],
  "client_id": os.environ['FIREBASE_CLIENT_ID'],
  "auth_uri": os.environ['FIREBASE_AUTH_URI'],
  "token_uri": os.environ['FIREBASE_TOKEN_URI'],
  "auth_provider_x509_cert_url": os.environ['FIREBASE_AUTH_PROVIDER_X509_CERT_URL'],
  "client_x509_cert_url": os.environ['FIREBASE_CLIENT_X509_CERT_URL']
})

firebase_app = firebase_admin.initialize_app(cred)