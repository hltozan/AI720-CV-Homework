from prettytable import PrettyTable


cv1 = {"Ýsim": "Halit Ozan",
"E-posta": "developer@outlook.com",
"Telefon numarasý": "11111111111",
"Eðitim": "Dicle Universtiy Computer Programming",
"Ýþ Deneyimi": "Datasoft Dogus Bilgisayar (1 month internship)",
"Projeler": "Reporting application with C# and Crystal reporting",
"Kurslar & Sertifikalar": "Global AI Introduction to Python",
"Beceriler": "C#, Python, SQL",
"Ýlgi Alanlarý": "Math, Programming, Algorithm"}

cv2 = {"Ýsim": "Ýbrahim Rona",
"E-posta": "pythoner@outlook.com",
"Telefon numarasý": "22222222222",
"Eðitim": "Ataturk Universtiy MIS",
"Ýþ Deneyimi": "Mercedes Computing (1 month internship)",
"Projeler": "E-commerce automation",
"Kurslar & Sertifikalar": "Global AI Introduction to Python",
"Beceriler": "C#, Python, HTML&CSS, SQL",
"Ýlgi Alanlarý": "Data science"}

cv3 = {"Ýsim": "Faruk Demir",
"E-posta": "abc@outlook.com",
"Telefon numarasý": "33333333333",
"Eðitim": "Yildiz Technical Universtiy Math Engineering",
"Ýþ Deneyimi": "Turkcell (6 month internship)",
"Projeler": "-",
"Kurslar & Sertifikalar": "Global AI Introduction to Python",
"Beceriler": "C#, Python, Java",
"Ýlgi Alanlarý": "Math, Statistics"}

cv4 = {"Ýsim": "Nihat Balban",
"E-posta": "def@outlook.com",
"Telefon numarasý": "44444444444",
"Eðitim": "Istanbul Technical University Computer Engineering",
"Ýþ Deneyimi": "Turk Telekom (6 month internship)",
"Projeler": "Neural networks",
"Kurslar & Sertifikalar": "Global AI Introduction to Python",
"Beceriler": "C#, Python, Java",
"Ýlgi Alanlarý": "Neural networks"}

cv5 = {"Ýsim": "Ayþe Yüksek",
"E-posta": "ghi@outlook.com",
"Telefon numarasý": "55555555555",
"Eðitim": "Ataturk University",
"Ýþ Deneyimi": "-",
"Projeler": "E-commerce system",
"Kurslar & Sertifikalar": "Global AI Introduction to Python",
"Beceriler": "HTML&CSS, JavaScript, Angular, React",
"Ýlgi Alanlarý": "Web Programming"}

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
  all_cvs[cv_list[i1]["Ýsim"]] = cv_list[i1]

table = PrettyTable()
columns = key_list
name_list = getList(all_cvs)

for i3 in range(len(key_list)):
    for i4 in range(len(all_cvs)):
      column.append((all_cvs[name_list[i4]])[key_list[i3]])
    table.add_column(columns[i3], column)
    column.clear()
print(table)
