class Student:
    schoolname='St. Patrick Higher Secondary School'
    def setname(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def marks(self,eng,tam,mat,sci,soc):
        self.eng=eng
        self.tam=tam
        self.mat=mat
        self.sci=sci
        self.soc=soc
class Total(Student):
    def totalmarks(self,a,b,c,d,e):
        self.total=a+b+c+d+e
        print(fname+lname)
        print('Total ')
s1=Student()
s1.setname('John','Wick')
s1.marks(99,97,96,95,100)




