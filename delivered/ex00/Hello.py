ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
temp = list(ft_tuple)
temp[1] = "Spain!" 
ft_tuple = tuple(temp)
ft_set.remove('tutu!')
ft_set.add("Barcelona!")
ft_dict.update({'Hello' : "42Barcelona!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
'''
#to reprint the set ONLY if it is properly sorted
listo = list(ft_set)
if (listo[0] == "Hello") :
	print(ft_set)
