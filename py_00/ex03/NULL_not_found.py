def NULL_not_found(object: any) -> int:
    if object is None:
        name = "Nothing"
    elif object is False:
        name = "Fake"
    elif object == 0:
        name = "Zero"
    elif object == '':
        name = "Empty"
    elif object != object:
        name = "Cheese"
    else:
        print("Type not Found")
        return 1
    print(f"{name}: {object} {type(object)}")
    return 0


"""
#original function
    if object is None:
        print(f"Nothing: {object} <class 'NoneType'>")
        return 0
    elif object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    elif object == 0:
        print(f"Zero: {object} <class 'int'>")
        return 0
    elif object == '':
        print(f"Empty: {object} <class 'str'>")
        return 0
    elif object != object:
        print(f"Cheese: {object} <class 'float'>")
        return 0
    else:
        print("Type not Found")
    return 1 """

# Un/comment below to run as main or not
"""
if __name__ == '__main__':
    Nothing = None
    Garlic = float("NaN")
    Zerito = 0
    zeroFloat = 0.0
    Empty = ""
    Fake = False
    num = 69
    NULL_not_found(Nothing)
    NULL_not_found(Garlic)
    NULL_not_found(Zerito)
    NULL_not_found(Empty)
    NULL_not_found(Fake)
    NULL_not_found(zeroFloat)
    print(NULL_not_found("Brian"))
    print(NULL_not_found(Fake))
    print(NULL_not_found(num))
 """
