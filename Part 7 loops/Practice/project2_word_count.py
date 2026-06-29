countries = ['India', "United states", 'Australia', 'Ireland', 'Sri Lanka', 'Iceland', 'Cuba', 'Iran', 'Poland']

#count all the countries starting with "I"
#also print all the countries as a list
#can also use startswith function
counter = 0
output = []

for country in countries:
    if country[0] == "I":
        counter = counter + 1
        output.append(country)
        
print(counter)
print(output)