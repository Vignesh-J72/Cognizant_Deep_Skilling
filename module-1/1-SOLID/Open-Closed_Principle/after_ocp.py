class Student:
    def __init__(self,name,subjects,marks):
        self.subjects=subjects
        self.marks=marks
        self.name=name

class TotalFinder(Student):
    def FindTotal(self):
        return sum(self.marks)

class SubjectBook(Student):
    def GetSubjects(self):
        return self.subjects

class StudentDetails(Student):
    def GetName(self):
        return self.name
if __name__=="__main__":
    subjects=['English','Maths','Social Science']
    marks=[89,90,95]
    name="Anush"
    
    student_1_marks=TotalFinder(name,subjects,marks)
    student_1_sub=SubjectBook(name,subjects,marks)
    student_1_det=StudentDetails(name,subjects,marks)
    print("Total",student_1_marks.FindTotal())
    print("Subjects:",student_1_sub.GetSubjects())
    print("Details:",student_1_det.GetName())