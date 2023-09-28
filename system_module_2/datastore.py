from google.cloud import datastore
from config import PROJECT_ID

def init_app(app):
    """
    Configuration of firestore as datastore
    """
    app.datastore_client = datastore.Client(PROJECT_ID)