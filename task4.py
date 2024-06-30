#Task 1 : determine the BMI Catgory based on user input
height=float(input("Enter height in meters: "))
weight=int(input("Enter weight in kilogram: "))
BMI=weight/(height**2)
if BMI>=30:
    print("Obesity")
elif BMI>=29 or BMI>=25:
    print("Overweight")
elif BMI>=25 or BMI>=18.5:
    print("Normal")
else:
    print("Underweight")

#Task 2 : determine which country a city belongs to
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
city = input("Enter a city name: ").strip()
if city in Australia:
    country = "Australia"
elif city in UAE:
    country = "UAE"
elif city in India:
    country = "India"
else:
    country = None
if country:
    print(city,"is in",country)
else:
    print(city,"is not in the list")

#Task 3 : check if two cities belong to the same country 
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
city1 = input("Enter first city name: ").strip()
city2 = input("Enter second city name: ").strip()
if city1 in Australia and city2 in Australia:
    country = "Australia"
elif city1 in UAE and city2 in UAE:
    country = "UAE"
elif city1 in India and city2 in India:
    country = "India"
else:
    country = None
if country:
    print(city1,"and",city2,"belong to",country)
else:
    print(city1,"and",city2,"do not belong to any country")