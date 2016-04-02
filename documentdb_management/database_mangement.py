import pydocumentdb.documents as documents
import pydocumentdb.errors as errors

class DatabaseManagement:

    @staticmethod
    def find_database(client, id):
        print('1. Query for Database')

        databases = list(client.QueryDatabases({
            "query": "SELECT * FROM r WHERE r.id=@id",
            "parameters": [
                { "name":"@id", "value": id }
            ]
        }))

        if len(databases) > 0:
            print('Database with id \'{0}\' was found'.format(id))
        else:
            print('No database with id \'{0}\' was found'. format(id))
        
    @staticmethod
    def create_database(client, id):
        print("\n2. Create Database")
        
        try:
            client.CreateDatabase({"id": id})
            print('Database with id \'{0}\' created'.format(id))

        except errors.DocumentDBError as e:
            if e.status_code == 409:
               print('A database with id \'{0}\' already exists'.format(id))
            else: 
                raise errors.HTTPFailure(e.status_code)               
    
    @staticmethod
    def read_database(client, id):
        print("\n3. Get a Database by id")

        try:
            # All DocumentDB resources are addressable via a link
            # This link is constructed from a combination of resource hierachy and 
            # the resource id. 
            # Eg. The link for database with an id of Foo would be dbs/Foo
            database_link = 'dbs/' + id

            database = client.ReadDatabase(database_link)
            print('Database with id \'{0}\' was found, it\'s _self is {1}'.format(id, database['_self']))

        except errors.DocumentDBError as e:
            if e.status_code == 404:
               print('A database with id \'{0}\' does not exist'.format(id))
            else: 
                raise errors.HTTPFailure(e.status_code)    

    @staticmethod
    def list_databases(client):
        print("\n4. List all Databases on an account")
        
        print('Databases:')
        
        databases = list(client.ReadDatabases())
        
        if not databases:
            return

        for database in databases:
            print(database['id'])          

    @staticmethod
    def delete_database(client, id):
        print("\n5. Delete Database")
        
        try:
           database_link = 'dbs/' + id
           client.DeleteDatabase(database_link)

           print('Database with id \'{0}\' was deleted'.format(id))

        except errors.DocumentDBError as e:
            if e.status_code == 404:
               print('A database with id \'{0}\' does not exist'.format(id))
            else: 
                raise errors.HTTPFailure(e.status_code)


