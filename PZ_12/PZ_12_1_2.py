string = "HeLlo WoRlD"
converted_string = ''.join(map(lambda char:char.lower(
    if char.insupper()
    else char, string))
print(converted_string))