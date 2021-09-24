# for BMI you must get weight and height of user 
print(" we want estimate your BMI")
weight = input("plz enter yr weight in kg :")
height = input("plz enter yr height in m :")
height = float(height)
weight = float(height)
bmi = weight / (height * height)
print(round(bmi,2)) 
if bmi < 18.5 :
    print(" you are underweight")
elif bmi >= 18.5 and bmi < 25 :
    print(" you are normal")
elif bmi >= 25 and bmi < 30 :
    print(" you are overweight")
elif bmi >= 30 :
    print(" you are obese")
else :
    print("somethimg went wrong")

