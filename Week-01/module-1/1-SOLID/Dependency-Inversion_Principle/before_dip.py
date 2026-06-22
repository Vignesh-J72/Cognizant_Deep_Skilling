class DBAccess:
    def __init__(self):
        self.db=DB()
    
    def GetData(self):
        data=self.db.runquery()
        print("Data retrieved from database.")

class DB:
    def runquery(self):
        return "Sample data"

if __name__=="__main__":
    
    access_1=DBAccess()
    access_1.GetData()