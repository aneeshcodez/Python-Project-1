#Positional Argument
def introduce(name, age, city):
    print(name, age, city)

introduce("Ram", 25, "Chennai")

# Keyword Argument

def introduce1(name, age, city):
    print(name, age, city)

introduce1(name="Sam" , age=27 , city="Salem")
introduce1(city="Trichy", name="Samuel" , age=29 )