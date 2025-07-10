student_data={'kai':[89,98,78,67,78],'fanum':[78,89,98,66,77],'ray':[88,98,98,95,78] }
for name,marks in student_data.items():
    print(name,marks)
    Total=0
    for mark in marks:

        Total=Total+mark

    print(f",{name} got a total of {Total} marks")  # Formatted string
