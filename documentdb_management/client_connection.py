from django.conf import settings
import pydocumentdb.document_client as document_client

class ConnectionDDB():
    """ A context manager to automatically close an object with a close method
    in a with statement. """
    
    def __init__(self):
        self.obj = document_client.DocumentClient(settings.DOC_DB['host'],{'masterKey': settings.DOC_DB['master_key']})

    def __enter__(self):
        return self.obj

    def __exit__(self, exception_type, exception_val, trace):
        # extra cleanup in here
        self.obj = None