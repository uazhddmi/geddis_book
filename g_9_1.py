dict1 = {
    'CS101':3004,
    'CS102':4501,
    'CS103': 6755,
    'CS104': 1244,
    'CS105': 1411
}

dict2 = {
    'CS101': "Heyns",
    'CS102': "Alvarados",
    'CS103': "Rich",
    'NT110': 'Berk',
    'CM241': 'Lee'
}

dict3 = {
    'CS101': '8:00',
    'CS102': '9:00',
    'CS103': '10:00',
    'NT110': '11:00',
    'CM241': '13:00'
}

course = input("Enter your course name: ").upper()

print(f"Room number is {dict1[course]}" if course in dict1 else 'there are no such course')
print(f"Lector is {dict2[course]}" if course in dict2 else 'there are no such course')
print(f"Course starts at {dict3[course]}" if course in dict3 else 'there are no such course')
