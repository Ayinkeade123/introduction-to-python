def filter_string_with_vowels(string):
    string_starting_with_vowel = []
    vowels = ("a","e", "i", "o", "u", "A", "E", "I", "O", "U")


    for x in tuple_of_names :
        if x and tuple_of_names [0] in vowels:
            string_starting_with_vowel.append(x)
    return tuple (string_starting_with_vowel)        


tuple_of_names =  ("zainab", "ayinke", "uche", "ayo")
new_tuple_of_names=filter_string_with_vowels(tuple_of_names)

print (new_tuple_of_names, filter_string_with_vowels)
print (tuple_of_names, filter_string_with_vowels)





