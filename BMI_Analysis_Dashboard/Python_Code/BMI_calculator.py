"""
FORMULA FOR BMI = (weight in kg) / [(height in meter)^2]
BMI standards:
    < 18.5 = UNDERWEIGHT
    18.5 - 24.9 = NORMAL 
    24.9 - 29.9 = OVERWEIGHT
    > 30 = OBESE

"""
def height_cm(H):
    height=H/100
    return height

def height_ft(feet,inches):
    total_inches=(feet*12)+inches
    total_cm=total_inches*2.54
    total_m=total_cm/100
    return total_m

def BMI_calculator(weight_kg,height_m):
    return weight_kg/height_m**2

def categories(BMI_value):
    if(BMI_value<18.5):
        return "underweight"
    elif(18.5<=BMI_value<=24.9):
        return "normal"
    elif(24.9<BMI_value<=30):
        return "overweight"
    else:
        return "obese! get some help bro"

unit=input("enter the unit for height(cm / ft / m):").lower()
if unit=="cm":
    height=float(input("enter the height:"))
    height_m=height_cm(height)
elif unit=="ft":
    feet=int(input("enter the feet:"))
    inches=int(input("enter the inches:"))
    height_m=height_ft(feet,inches)
elif unit=="m":
    inp=float(input("enter the height:"))
    height_m=inp
else:
    print("NOT A VALID UNIT, TRY AGAIN!")

weight=float(input("weight in kg:"))

BMI=BMI_calculator(weight,height_m)
status=categories(BMI)

print(f"\nBMI: {BMI:.2f}")
print("status:",status)

if (status=="underweight"):
    weight_needed=18.5*(height_m**2)
    Gains=weight_needed-weight
    print(f"weight need to be gained:{Gains:.2f}kg")
elif(status=="normal"):
    print("good job!")
else:
    weight_needed=24.9*(height_m**2)
    loss=weight-weight_needed
    print(f"weight need to be loss:{loss:.2f}kg")
print("\n")
print("""BMI standards:
    < 18.5 = UNDERWEIGHT
    18.5 - 24.9 = NORMAL 
    24.9 - 29.9 = OVERWEIGHT
    > 30 = OBESE""")
