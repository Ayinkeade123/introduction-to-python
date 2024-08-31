myTechList= ["python", "c++", "java", "mysql"] 
myTechList2= ["AWS"]
for x in myTechList:
    print(x[2])



 #appending HTML to myTechList
myTechList.append("HTML")

# print item on index 2
print(myTechList[-2]) 

#print the length of your list
print (len (myTechList))

#insert AWS , cybersecurity
myTechList.insert (5,"cybersecurity")

#extend myTechList to myTechList2
myTechList.extend (myTechList2)

#remove cybersecurity
myTechList.remove ("cybersecurity")

#pop AWS
myTechList.pop (5)

#del index 2
del myTechList [2]

print (myTechList)


