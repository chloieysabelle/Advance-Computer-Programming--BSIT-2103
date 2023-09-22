english_grade = float(input ("Enter English Grade: "))
filipino_grade= float(input("Enter Flipino Grade: "))
science_grade= float(input ("Enter Science Grade: "))
math_grade= float(input("Enter Math Grade: "))
araling_panlipunan_grade = float(input ("Enter Araling panlipunan Grade: "))
physical_grade= float(input("Enter Physical Education Grade: "))

total_grade=(
english_grade+filipino_grade+science_grade+math_grade+araling_panlipunan_grade+physical_grade
)
average_grade=total_grade / 6

print("Your Average grade is: ",average_grade)
