class student:
    school_name="cbse SCHOOL"
    def __init__ (self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
s1=student("jeni",1)
s2=student("eva",2)
print(s1.school_name)
print(s2.school_name)
student.school_name="stateboard school"
print(s1.school_name)
print(s2.school_name)


