# collection = single "variable" used to store multiple values
# list = [] ordered and changeable. Duplicates OK
#set = {} unordered and immutable, but Add/Remove OK, No duplicates 
# list = () ordered and unchangeable, Duplicates okay, Faster
#fruits = ["apple", "orange", "banana" ,"coconut","kiwi","strawberry","dragonfruit"] 
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

#print(fruits.index("coconut")) 

#print(fruits)

cars =["bmw","maserati","audi","mercedes","ferraru"]
#print(f"these are list of{cars}")
#print(f"the first care is {cars[0]}")

#changing the value of the list
#cars[0] = "toyota"
#print(f"the first car is {cars[0]}")

#print(f"the last car is {cars[-1]}")
#cars[-1] = "lamborghini"
#print(f"the last car is {cars[-1]}")

#adding a new value to the text
#cars.append("buggatti")
#print(cars)
#cars.remove("maserati")
#print (cars)

#looping through the list
# otherwide called iterating through the list
for car in cars:
   # print(len(car))
   # print(car)
    #carRequest = input("add a new car please : ")
    #cars.append(carRequest)
    #print(cars)
    #print(len(cars))
    #print(cars.upper())
    #print(cars)
    #if len(cars) > 10:
       # break

# challenge
# create a list of friends
# make sure the initial list is none 
   friends = []
# add a new friend to the list, add at least 5 friends
friends.append("lorenzo")
friends.append("diego")
friends.append("alex")
friends.append("angel")
friends.append("jim")
#remove a friend
friends.remove("diego")
print(friends)
# insert a friend at a specific index maybe 2
friends[2]="dwade" 
for friend in friends:
        
   print(friends)
   friendAdd= input("add a new friend : ")
   friends.append(friendAdd)
   print(friends)
   print(len(friends))
   print(friends)
   if len(friends) > 10:
      break
# print the list of friends
#loop through the list and print the friends name
# see if a particular friend is in the list (boolean value)
print("alex" in friends)
 # if the list is greater then 10 break the loop