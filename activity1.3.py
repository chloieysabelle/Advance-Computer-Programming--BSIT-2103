from datetime import datetime

father_name = input("Enter your father's name: ") 
birthplace = input("Enter your father's birthplace: ")
birthday_str = input("Enter your father's birthday (YYYY-MM-DD): ")

birthday = datetime.strptime(birthday_str, "%Y-%m-%d")

current_year = datetime.now().year
father_age = current_year - birthday.year
print( "_____________________________________________")
print("\n         ---Father's Information---")
print( "_____________________________________________")
print(f"|Name: {father_name}                                  ")
print(f"|Birthplace: {birthplace}                            ")
print(f"|Birthday: {birthday.strftime('%Y-%m-%d')}                      ")
print(f"|Age: {father_age} years                               ")
print( "|___________________________________________")
