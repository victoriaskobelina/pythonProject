#Составить генератор (yield), который переведет символы строки из верхнего регистра в нижний.
def lower_case(string): #нижний регистр
    for char in string:
        if char.isupper():
            yield char.lower()
        else:
            yield char
line = "HeLLo WoRLd"
lower_case_l = lower_case(line)
converted_line = ''.join(lower_case_l)
print(converted_line)