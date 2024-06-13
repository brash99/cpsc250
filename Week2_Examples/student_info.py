firstname = "Alicia"
lastname = "Smith"
student_id = 10345302
street_number = 908
street = "Promenade Lane"
city = "Williamsburg"
state = "VA"
zip_code = 23185
address = [street_number, street, city, state, zip_code]
grades = {"HW": 94.2, "Quiz": 75.8, "Tests": 88.4, "Final": 71.2}


student_info = [firstname, lastname, student_id, address, grades]

print(student_info)
print(student_info[4]['HW'])