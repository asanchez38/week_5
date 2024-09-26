# collection = single "variable" used to store multiple values
# list = [] ordered and changeable. Duplicates OK
#set = {} unordered and immutable, but Add/Remove OK, No duplicates 
# list = () ordered and unchangeable, Duplicates okay, Faster
fruits = ["apple", "orange", "banana" ,"coconut","kiwi","strawberry","dragonfruit"] 
#print(dir(fruits))  prints all methods that come with it
#print(help(fruits)) 
#print(len(fruits)) tells the length
#print("pineapple" in fruits) tells if something is in their or not true/false boolean value

#print(fruits[::2])
#print(fruits[::-1])

#for fruit in fruits
#print(fruit)

#fruits[0]= "pineapple"  reasign values using this 
#print(fruits)

#fruits.append("pineapple") #this adds pineapple into the list
#print(fruits)
#fruits.remove("apple")  #This takes away apple from the list
#print(fruits)
#fruits.sort() #this sorts it by alphabetical order
#fruits.reverse () #This reverses the whole list
#fruits.clear() #This clears the whole list

print(fruits.index("coconut")) 

print(fruits)

cars =["bmw","maserati","audi","mercedes","ferraru"]
print(f"these are list of{cars}")
print(f"the first care is {cars[0]}")

#changing the value of the list
cars[0] = "toyota"
print(f"the first car is {cars[0]}")

print(f"the last car is {cars[-1]}")
cars[-1] = "lamborghini"
print(f"the last car is {cars[-1]}")

#adding a new value to the text
cars.append("buggatti")
print(cars)
cars.remove("maserati")
print (cars)

#looping through the list
# otherwide called iterating through the list
for car in cars:
   # print(len(car))
   # print(car)
    carRequest = input("add a new car please : ")
    cars.append(carRequest)
    print(cars)
    print(len(cars))
    print(cars.upper())
    print(cars)
    if len(cars) > 10:
        break