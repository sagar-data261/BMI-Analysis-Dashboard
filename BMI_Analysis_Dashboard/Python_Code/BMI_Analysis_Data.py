def height_cm(H):
    height=H/100
    return height

def BMI_calculator(weight_kg,height_m):
    return weight_kg/height_m**2

def categories(BMI_value):
    if(BMI_value<18.5):
        return "Underweight"
    elif(18.5<=BMI_value<=24.9):
        return "Normal"
    elif(24.9<BMI_value<=30):
        return "Overweight"
    else:
        return "Obese"
    
import random
import csv

data=[]

first_names = ["Aarav", "Rahul", "John", "Emma", "Sophia", "Liam", "Noah", "Aisha"]
last_names = ["Sharma", "Smith", "Khan", "Brown", "Patel", "Singh", "Lee"]
gender_choice=["M","F"]
country_choice=["USA","India","Canada","Russia","China","Australia","UK","Bangladesh","Sri Lanka","UAE"]
activity_level_choice=["L","M","H"]


for _ in range(100):
    name=random.choice(first_names)+" "+random.choice(last_names)
    height=round(random.uniform(150.0,190.0),2)
    height_m=height_cm(height)
    weight_kg=round(random.uniform(40.0,100.0),1)
    age=random.randint(18,70)
    gender=random.choice(gender_choice)
    country=random.choice(country_choice)
    activity_level=random.choice(activity_level_choice)
    BMI=round(BMI_calculator(weight_kg,height_m),2)
    status=categories(BMI)

    data.append([name,height, weight_kg, age, gender, country, activity_level, BMI, status])

with open("bmi_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "name",
        "height_cm",
        "weight_kg",
        "age",
        "gender",
        "country",
        "activity_level",
        "BMI",
        "status"
    ])
    writer.writerows(data)
