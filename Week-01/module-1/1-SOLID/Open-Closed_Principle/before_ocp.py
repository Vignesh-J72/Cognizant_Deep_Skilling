class Student:
    def __init__(self,subjects,marks):
        self.subjects=subjects
        self.marks=marks
    
    def FindTotal(self):
        return sum(self.marks)
    
    def GetSubjects(self):
        return self.subjects

if __name__=="__main__":
    subjects=['English','Maths','Social Science']
    marks=[89,90,95]
    student_1=Student(subjects,marks)
    print("Total",student_1.FindTotal())
    print("Subjects:",student_1.GetSubjects())