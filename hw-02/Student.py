# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0, year=0):
        self.name = name
        self.gpa = gpa
        self.year = year
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
        
    def enroll(self, courses): 
        '''
        This function enrolls students in courses and sets them as attributes
        '''
        self.courses = courses
        
    def display_courses(self):
        '''
        This function takes the course attributes and prints them
        '''
        print('I am enrolled in:', self.courses)
        
    def years_until_graduation(self): 
        '''
        This function prints the number of years a student has left until they graduate
        '''
        years_for_degree = 4
        print('I will graduate in', years_for_degree-self.year, 'years')

class Spartan(Student):
    '''
    This class is designed to inherit the Student class and include methods for the school's motto and school spirit
    '''
    
    def __init__(self, name= '', motto = ''):
        self.name = name
        self.motto = motto
        
    def set_motto(self,motto):
        '''
        This function takes a string input and sets it as the class motto
        '''
        self.motto = motto 

    def school_spirit(self):
        '''
        This function prints a Spartan's name and the class motto
        '''
        print('My name is', self.name)
        print('I am a Spartan. My motto is', self.motto)