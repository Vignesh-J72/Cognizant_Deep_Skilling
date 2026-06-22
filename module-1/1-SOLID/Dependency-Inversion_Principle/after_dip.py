class DatabaseBlueprint:
    def runquery(self):
        pass

class DB(DatabaseBlueprint):
    def runquery(self):
        return "Sample data"

class CloudDB(DatabaseBlueprint):
    def runquery(self):
        return "Cloud data"

class DBAccess:
    def __init__(self, db_instance: DatabaseBlueprint):
        self.db = db_instance
    
    def GetData(self):
        data = self.db.runquery()
        print("Data retrieved")

if __name__ == "__main__":
    database_1 = DB()
    access_1 = DBAccess(database_1)
    access_1.GetData()

    database_2 = CloudDB()
    access_2 = DBAccess(database_2)
    access_2.GetData()