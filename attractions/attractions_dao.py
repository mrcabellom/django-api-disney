from documentdb_management.document_management import DocumentManagement
from documentdb_management.client_connection import ConnectionDDB
import pdb
import time

class AttractionsDao:

     @staticmethod
     def find_aggregate_attractions_between_date(attraction_id, start_date, end_date):

        with ConnectionDDB() as client:
            query = u'''select * 
                    from c where c.date >= "{0}" 
                    and c.date <= "{1}" 
                    and c.attractionId = "{2}"'''.format(start_date.isoformat(),
                                                        end_date.isoformat(),
                                                        attraction_id)
            docs = DocumentManagement.find_document(client,'attractionswaittimeaggregation',query);
        return docs.fetch_items()

        


