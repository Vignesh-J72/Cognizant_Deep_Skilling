class portal:
    def login(self):
        pass
    def authorize(self):
        pass
    def request(self):
        pass
    def modify(self):
        pass

class StudentPortal(portal):
    def login(self,user_id):
        print("Logging into user_id:",user_id)
    def request(self,details):
        print("Submitting request to view:",details)
    
class StaffPortal(portal):
    def login(self,user_id):
        print("Logging into user_id:",user_id)
    def request(self,details):
        print("Submitting request to view:",details)
    def authorize(self,user_id):
        print("Authorizing user id:",user_id)
    def modify(self,details):
        print("Opening modification page for:",details)

if __name__=="__main__":
    student_1=StudentPortal()
    student_1.login("21134")
    student_1.request("Marks")

    staff_1=StaffPortal()
    staff_1.login("1235")
    staff_1.authorize("21134")