score = int(input("Score: "))

if 90 <= score <= 100:   #combine inequalities
    print("Grade A")
elif score >= 80:
    print("Grade B")
else:
    print("Try Again!")