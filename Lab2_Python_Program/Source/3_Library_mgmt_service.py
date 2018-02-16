#parent class
class Person:
    # constructor for person
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def display(self):
        print("Name: ", self.name)
        print("Email: ", self.email)

#child class 1
class Student(Person):
    StudentCount = 0
    # constructor for student
    def __init__(self,name,email,student_id):
        Person.__init__(self,name,email)
        self.student_id = student_id
        Student.StudentCount +=1
    def displayCount(self):
        print("Total Number of Students:", Student.StudentCount)
    def display(self):
        print("Student Details:")
        #calling parent method
        Person.display(self)
        print("Student Id: ",self.student_id)

#child class 2
class Librarian(Person):
    StudentCount = 0
    def __init__(self,name,email,employee_id):
        super().__init__(name,email)
        self.employee_id = employee_id
    def display(self):
        print("Employee Details:")
        Person.display(self)
        print("Employee Id: ",self.employee_id)

class Book():
    def __init__(self,book_name,author,book_id):
        self.book_name = book_name
        self.author = author
        self.book_id = book_id
    def display(self):
        print("Book Details")
        print("Book_Name: ", self.book_name)
        print("Author: ", self.author)
        print("Book_ID: ", self.book_id)

#multiple inhertience
class Lend_Book(Student,Book):
    def __init__(self,name,email,student_id,book_name,author,book_id):
        #constructor for student
        Student.__init__(self,name,email,student_id)
        # constructor for book
        Book.__init__(self,book_name,author,book_id)
    def display(self):
        print("Borrowed Book Details:")
        Student.display(self)
        Book.display(self)

LibRecords = []
LibRecords.append(Student('Barath','barath323@gmail.com',123))
LibRecords.append(Librarian('Peter','df43d@gmail.com',789))
LibRecords.append(Book('Algorithm Book','leo',123456))
LibRecords.append(Book('Java Book','leo',123456))
LibRecords.append(Lend_Book('Phani','abc@gmail.com',456,'Network book','Petter',67890))

for obj, item in enumerate(LibRecords):
    item.display()
    print("\n")
    if obj == len(LibRecords)-1:
        item.displayCount()