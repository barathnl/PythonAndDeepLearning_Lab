import sys

#python_student_list=['Barath','Shilan','Dev']
print("Enter list of student attending python : ")
python_student_list=sys.stdin.readline().strip('\n').split(" ")

#web_student_list =['Shilan','Nikhila','Barath']
print("Enter list of student attending web development : ")
web_student_list=sys.stdin.readline().strip('\n').split(" ")

'''
Sorting both list so that comparsion time is less 
'''
python_student_list.sort()
web_student_list.sort()

'''
Finding common student who are attending from both class
'''
list_common = []
for a, b in zip(python_student_list, web_student_list):
    if a == b:
        list_common.append(a)
print("Common student who are attending from both class :: ",list_common)

'''
Finding uncommon student who are not attending both class
'''
list_uncommon = []
for a, b in zip(python_student_list, web_student_list):
    if a != b:
        list_uncommon.append(a)
        list_uncommon.append(b)
print("Uncommon student who are not attending both class :: ",list_uncommon)