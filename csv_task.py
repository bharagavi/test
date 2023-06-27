'''
import csv

with open(r'C:\\Users\\DELL\\Downloads\\employees.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)        
'''

        

import csv
def read_csv_file(filepath):
    with open(filepath, 'r')as file:
        csvreader = csv.reader(file)
        data = list(csvreader)
    return data

filepath = r'C:\\Users\\DELL\\Downloads\\employees.csv'
csv_data = read_csv_file(filepath)

dept = []
for i in csv_data:
    if i in csv_data:
       dept.append(i[5])
#print(dept)       
print("Total no. of emps:", dept.count("Human Resource"))  
print("Total no. of emps:", dept.count("Product"))
sal1 = []
sal2 = []
for i in csv_data[1:]:
    if i[5]  == "Human Resource":
        sal1.append(int(i[8]))
    else:
        sal2.append(int(i[8]))
print("Avg salary of Human Resource Department EE's is:", sum(sal1)/dept.count("Human Resource"))

print("Avg salary of Product Department EE's is:", sum(sal2)/dept.count("Product"))
employee_name = []
for i in csv_data[1::]:
    if int(i[7]) > 10:
        employee_name.append(i[0]+" "+i[1])
print(employee_name)        

