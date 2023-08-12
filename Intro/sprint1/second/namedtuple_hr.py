from collections import namedtuple

attributes = 'ID,MARKS,CLASS,NAME'
Sheet = namedtuple('Students', attributes)
student_sheet = Sheet(ID = [], MARKS = [], CLASS = [], NAME=[])
order = []
student_nr = int(input())

for i in range(student_nr+1):
    if i == 0: 
        passed_attr = input().split()
        order = {attributes.split(',').index(k): k for k in passed_attr}
        continue
    student = input().split()
    for i,o in enumerate(order.items()):
        student_attr = student[i]
        if o[1] != 'NAME': student_attr = int(student_attr)
        student_sheet[o[0]].append(student_attr)

results = sum(getattr(student_sheet, 'MARKS'))/student_nr
print("%.2f" % results)


nr = int(input())
a = namedtuple('Students', input().split())
summarized = sum([float(a(*input().split()).MARKS) for x in range(nr)])/nr
print(a)