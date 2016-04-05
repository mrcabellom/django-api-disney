from documentdb_management.document_management import DocumentManagement
from documentdb_management.client_connection import ConnectionDDB
import pdb
import time
from app.utils import date_to_string
import urllib

class AttractionsDao:

     @staticmethod
     def find_aggregate_attractions_between_date(attractions, start_date, end_date):

        with ConnectionDDB() as client:
            query = u'''select * 
                    from c where c.date >= "{0}" 
                    and c.date <= "{1}" 
                    and c.attractionId in ({2})'''.format(date_to_string(start_date),
                                                        date_to_string(end_date),
                                                        ','.join(["'"+urllib.unquote(attraction)+"'" for attraction in attractions]))
            docs = DocumentManagement.find_document(client,'attractionswaittimeaggregation',query);
        return docs.fetch_items()


     @staticmethod
     def find_attractions():

        with ConnectionDDB() as client:
            query = u'''select top 1 * from c ORDER BY c.createdAt DESC'''
            docs = DocumentManagement.find_document(client,'attractionswaittime',query)
            for doc in docs:
                first_element = doc

            query_attractions = u'''select * 
                    from c where c.createdAt = "{0}"'''.format(first_element['createdAt'])
            docs_attractions = DocumentManagement.find_document(client,'attractionswaittime',query_attractions);

        return docs_attractions.fetch_items()

        


