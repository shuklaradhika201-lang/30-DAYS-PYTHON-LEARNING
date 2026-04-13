#dictionary are declared with {}
#items under dictionary can be accessed specifically name of variable[name of item]
#we can change the value of items in eictionary by variablename[name of item]="value"
#when we apply for loop in dicitonary we get the item names
person={"name" : "radhika", "age":"20" , "college":"LNCTE", "course":"BTECH" , "branch":"DS"}
print(person)

print(person["name"])  #ascessing the item

person["name"]="Radhika" #changing the value of item
print(person)

for personn in person:
    print(personn)  #this give every item in dictionary

for key,value in person.items():   #this gives every key with its value
    print(key,value)

#we can check conditions in dictionary
if "name" in person:
    print("the name of the person is given in dictionary")

#we can check the number of items in dictionary by using length
print(len(person))

#we can add keys in the dictionary
person["section"]="B"
print(person)

#we can pop the value from the dictionary bu we have to provide the value of item which we have to remove
person.pop("section")
print(person) 

#this pop outs the last item in the dictionary
print(person.popitem())  

#as the last item is poped it will be removed from the dictionary
print(person)

#we can use del keyword to delete items from dictionary
del person["course"]
print(person)

#we can make multiple dicitonary inside the dictionary
teashop={
    "chai" : {"masala" : "spicy","ginger" : "zesty"},
    "tea" : {"green" : "mild","black" : "strong"}
}
print(teashop)

print(teashop["chai"])

print(teashop["chai"]["ginger"])

#we can print conditons with the help of dictionary
squareno={x:x**2 for x in range(5)}
print(squareno)  #we can also clear the squareno by using squareno.clear() output will be {}

#when we have values and keys present seprately and we need to construct dicitonary by combining them

keys=["cadbuary" , "kitkat" , "nestle"]
default_values="delicious"
new_dict=dict.fromkeys(keys,default_values)
print(new_dict)