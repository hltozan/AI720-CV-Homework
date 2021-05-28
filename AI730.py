from prettytable import PrettyTable


cv1 = {"�sim": "Halit Ozan",
"E-posta": "developer@outlook.com",
"Telefon numaras�": "11111111111",
"E�itim": "Dicle Universtiy Computer Programming",
"�� Deneyimi": "Datasoft Dogus Bilgisayar (1 month internship)",
"Projeler": "Reporting application with C# and Crystal reporting",
"Kurslar & Sertifikalar": "Global AI Introduction to Python",
"Beceriler": "C#, Python, SQL",
"�lgi Alanlar�": "Math, Programming, Algorithm"}

cv2 = {"�sim": "�brahim Rona",
"E-posta": "pythoner@outlook.com",
"Telefon numaras�": "22222222222",
"E�itim": "Ataturk Universtiy MIS",
"�� Deneyimi": "Mercedes Computing (1 month internship)",
"Projeler": "E-commerce automation",
"Kurslar & Sertifikalar": "Global AI Introduction to Python",
"Beceriler": "C#, Python, HTML&CSS, SQL",
"�lgi Alanlar�": "Data science"}

cv3 = {"�sim": "Faruk Demir",
"E-posta": "abc@outlook.com",
"Telefon numaras�": "33333333333",
"E�itim": "Yildiz Technical Universtiy Math Engineering",
"�� Deneyimi": "Turkcell (6 month internship)",
"Projeler": "-",
"Kurslar & Sertifikalar": "Global AI Introduction to Python",
"Beceriler": "C#, Python, Java",
"�lgi Alanlar�": "Math, Statistics"}

cv4 = {"�sim": "Nihat Balban",
"E-posta": "def@outlook.com",
"Telefon numaras�": "44444444444",
"E�itim": "Istanbul Technical University Computer Engineering",
"�� Deneyimi": "Turk Telekom (6 month internship)",
"Projeler": "Neural networks",
"Kurslar & Sertifikalar": "Global AI Introduction to Python",
"Beceriler": "C#, Python, Java",
"�lgi Alanlar�": "Neural networks"}

cv5 = {"�sim": "Ay�e Y�ksek",
"E-posta": "ghi@outlook.com",
"Telefon numaras�": "55555555555",
"E�itim": "Ataturk University",
"�� Deneyimi": "-",
"Projeler": "E-commerce system",
"Kurslar & Sertifikalar": "Global AI Introduction to Python",
"Beceriler": "HTML&CSS, JavaScript, Angular, React",
"�lgi Alanlar�": "Web Programming"}

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
  all_cvs[cv_list[i1]["�sim"]] = cv_list[i1]

table = PrettyTable()
columns = key_list
name_list = getList(all_cvs)

for i3 in range(len(key_list)):
    for i4 in range(len(all_cvs)):
      column.append((all_cvs[name_list[i4]])[key_list[i3]])
    table.add_column(columns[i3], column)
    column.clear()
print(table)
