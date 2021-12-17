from prettytable import PrettyTable

cv1 = {"Name": "Halit Ozan",
"E-mail": "developer@outlook.com",
"Phone number": "11111111111",
"Education": "Anadolu University Computer Programming",
"Work experience": "Datasoft Dogus Bilgisayar (1 month internship)",
"Projects": "Reporting application with C# and Crystal reporting",
"Courses&Certificates": "Global AI Introduction to Python",
"Skills": "C#, Python, SQL",
"Areas of interest": "Math, Programming, Algorithm"}

cv2 = {"Name": "İbrahim Rona",
"E-mail": "pythoner@outlook.com",
"Phone number": "22222222222",
"Education": "Ataturk University MIS",
"Work experience": "Mercedes Computing (1 month internship)",
"Projects": "E-commerce automation",
"Courses&Certificates": "Global AI Introduction to Python",
"Skills": "C#, Python, HTML&CSS, SQL",
"Areas of interest": "Data science"}

cv3 = {"Name": "Faruk Demir",
"E-mail": "abc@outlook.com",
"Phone number": "33333333333",
"Education": "Yildiz Technical University Math Engineering",
"Work experience": "Turkcell (6 month internship)",
"Projects": "-",
"Courses&Certificates": "Global AI Introduction to Python",
"Skills": "C#, Python, Java",
"Areas of interest": "Math, Statistics"}

cv4 = {"Name": "Nihat Balban",
"E-mail": "def@outlook.com",
"Phone number": "44444444444",
"Education": "Istanbul Technical University Computer Engineering",
"Work experience": "Turk Telekom (6 month internship)",
"Projects": "Neural networks",
"Courses&Certificates": "Global AI Introduction to Python",
"Skills": "C#, Python, Java",
"Areas of interest": "Neural networks"}

cv5 = {"Name": "Ayşe Yüksek",
"E-mail": "ghi@outlook.com",
"Phone number": "55555555555",
"Education": "Ataturk University",
"Work experience": "-",
"Projects": "E-commerce system",
"Courses&Certificates": "Global AI Introduction to Python",
"Skills": "HTML&CSS, JavaScript, Angular, React",
"Areas of interest": "Web Programming"}

cv_list = [cv1, cv2, cv3, cv4, cv5]
name_list = []
key_list = []
all_CVs = {}
column = []

def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list
key_list = getList(cv1)

for i1 in range(len(cv_list)):
  all_CVs[cv_list[i1]["Name"]] = cv_list[i1]

table = PrettyTable()
columns = key_list
name_list = getList(all_CVs)

for i3 in range(len(key_list)):
    for i4 in range(len(all_CVs)):
      column.append((all_CVs[name_list[i4]])[key_list[i3]])
    table.add_column(columns[i3], column)
    column.clear()
print(table)
