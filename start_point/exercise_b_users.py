users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# 2. Get Erik's hometown
# 3. Get the list of Erik's lottery numbers
# 4. Get the species of Avril's pet Monty
# 5. Get the smallest of Erik's lottery numbers
# 6. Return an list of Avril's lottery numbers that are even
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# 8. Change Erik's hometown to Edinburgh
# 9. Add a pet dog to Erik called "fluffy"
# 10. Add another person to the users dictionary



print(users["Jonathan"]["twitter"])                     #Q1

print(users["Erik"]["home_town"])                       #Q2

print(users["Erik"]["lottery_numbers"])                 #Q3

print(users["Avril"]["pets"][0]["species"])             #Q4

print(min(users["Erik"]["lottery_numbers"]))            #Q5

num_list = []                                           #Q6
for num in users["Avril"]["lottery_numbers"]:
    if num%2 == 0:
        num_list.append(num)
print(num_list)

users["Erik"]["lottery_numbers"].append(7)              #Q7

users["Erik"]["hometown"] = "Edinburgh"                 #Q8

new_pet = {"name" : "fluffy", "species" : "dog"}        #Q9
users["Erik"]["pets"].append(new_pet)                   
#print(users["Erik"]["pets"])

users = {                                               #Q10
    "Panos" :{
    "twitter" : "panots",
    "lottery_number" : [3, 23, 41, 26, 25, 39],
    "home_town" : "Megara",
    "pets" : {
      "name" : "takis",
      "species" : "turtle"
    }

    }
}

#users.append(new_person)
#print(users["Panos"])