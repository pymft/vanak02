mass = input("mass (in kgs) : ")
height = input("height (m) : ")

mass_float = float(mass)
height_float = float(height)

bmi = mass_float / height_float ** 2

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
else:
    print("obese")
