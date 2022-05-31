# get marks from user to display. If >90, display A; if > 80, display b; if < 50, display fail

grade = int(raw_input("Enter the grade: "))

if grade > 90:
    print("Grade A")
elif grade > 80:
    print("Grade B")
elif grade > 70:
    print("Grade C")
elif grade > 60:
    print("Grade D")
elif grade > 50:
    print("Grade E")
elif grade <=50:
    print("You are failed")