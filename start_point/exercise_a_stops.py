stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
#2. Add "Glasgow Queen St" to the start of the list
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
#4. Print out the index position of "Linlithgow"
#5. Remove "Livingston" from the list using its name
#6. Delete "Cumbernauld" from the list by index
#7. Print the number of stops there are in the list
#8. Sort the list alphabetically
#9. Reverse the positions of the stops in the list
#10 Print out all the stops using a for loop


stops.append("Edinburgh Waverly")       #Q1
stops.insert(0,"Glasgow Qeen St")       #Q2
stops.insert(4,"Polmot")                #Q3
print(stops.index("Linlithgow"))        #Q4
stops.remove("Livingston")              #Q5
del(stops[stops.index("Cumbernauld")])  #Q6
print(len(stops))                       #Q7
stops.sort()                            #Q8
stops.reverse()                         #Q9
for stop in stops:                      #Q10    

    print(stop , end=" ")
# print(stops)