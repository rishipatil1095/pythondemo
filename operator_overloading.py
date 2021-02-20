class Student:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self,other):
        m1 = self.a + other.a
        m2 = self.b + other.b
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):
        m1 = self.a + self.b
        m2 = other.a + other.b
        if m1 > m2 :
            return True
        elif m2 > m1:
            return False

    def __str__(self):
        return '{} {}'.format(self.a,self.b)

s1 = Student(24,56)
s2 = Student(56,25)

s3 = s1+s2
print(s3.a,s3.b)

if s1 > s2:
    print('S1 wins')
else:
    print('S2 wins')

print(s3)