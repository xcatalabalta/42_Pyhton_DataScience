def all_thing_is_obj(object: any) -> int:
	known = [type([]).__name__ , type(()).__name__ , type({}).__name__ , type(set()).__name__]
	obj = type(object)
	name = type(object).__name__
	if name in known:
		print (f"{name.capitalize()} : {obj}")
	elif (object.__class__.__name__ == 'str'):
		print (f"{object} is in the kitchen : {obj}")
	else:
		print ("Type not found")
	return 42


'''
# main starts here

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
#print (known)
all_thing_is_obj(ft_list)

all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj(ft_list[1])
all_thing_is_obj(69)
print(all_thing_is_obj(690))

print (type(ft_list).__name__.capitalize())
print (type(ft_tuple).__name__.capitalize())
print (type(ft_set).__name__.capitalize())
print (type(ft_dict).__name__.capitalize())
print (type("Hello").__name__.capitalize())
print (type(1532).__name__.capitalize())
'''
