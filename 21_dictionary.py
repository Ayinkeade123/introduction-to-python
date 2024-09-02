countries_and_capital = {

    "Nigeria": "Abuja",
    "England": "London",
    "Ghana": "Accra"
}
#method 1
print(countries_and_capital ["England"])

#method 2
second_country = list (countries_and_capital.keys())[1]
capital_of_second_country = countries_and_capital [second_country]
print(f"The capital of {second_country} is {capital_of_second_country}") 
