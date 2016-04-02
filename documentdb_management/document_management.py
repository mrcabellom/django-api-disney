import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client
import pydocumentdb.errors as errors
from django.conf import settings

database_link = 'dbs/' + settings.DOC_DB['database_id']

class DocumentManagement:
               
    @staticmethod
    def create_document(client,collection_name,object):
               
        try:
            client.CreateDocument(database_link + '/colls/{0}'.format(collection_name), object)
            print('Document with id \'{0}\' created'.format(id))

        except errors.DocumentDBError as e:
            raise errors.HTTPFailure(e.status_code)
        
    @staticmethod
    def find_document(client,collection_name,query):
               
        try:
            doc = client.QueryDocuments(database_link + '/colls/{0}'.format(collection_name), query)
            return doc            

        except errors.DocumentDBError as e:
            raise errors.HTTPFailure(e.status_code)               
       
       

