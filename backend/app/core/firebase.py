import os
from .config import settings
import firebase_admin
from firebase_admin import credentials

if os.path.exists("/etc/secrets/firebase-adminsdk.json"):
    firebase_cred_path = "/etc/secrets/firebase-adminsdk.json"
else:
    firebase_cred_path = settings.firebase_cred_path

cred = credentials.Certificate(firebase_cred_path)
firebase_admin.initialize_app(cred)