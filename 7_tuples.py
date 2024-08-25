Nigeria = ("lagos", "ibadan", "ogun", "oyo", "ekiti")

print 


#to determine the tuple length
print (len(Nigeria))

#create tuple with only one item
Nigeria= ("ogun")
print (type(Nigeria))


#add to a tuple
Nigeria = ("lagos", "ibadan", "ogun", "oyo", "ekiti")
y = list(Nigeria)
y.append("abuja")
Nigeria = tuple (y)

#remove a tuple
Nigeria = ("lagos", "ibadan", "ogun", "oyo", "ekiti")
y = list(Nigeria)
y.remove("ibadan")
Nigeria = tuple (y)

#unpacking a tuple
Nigeria = ("lagos", "ibadan", "ogun", "oyo", "ekiti")
(white, blue, green, yellow, black) = Nigeria
print (white)
print (blue)
print (green)
print (yellow)
print (black)

#using asterisk *
Nigeria = ("lagos", "ibadan", "ogun", "oyo", "ekiti")
(white, *blue, green) = Nigeria
print (white)
print (blue)
print (green)

#loop in the tuple
Nigeria = ("lagos", "ibadan", "ogun", "oyo", "ekiti")
for x in Nigeria :
    print (x)

#join two tuples
Nigeria1 = ("a", "b", "c")
Nigeria2 = (1, 2, 3)
Nigeria3 = Nigeria1+Nigeria2
print (Nigeria3)

#multiply tuple
state = ("lagos", "ibadan", "ogun",)
Nigeria *3


print (Nigeria)
