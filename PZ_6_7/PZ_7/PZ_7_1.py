#Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S вставить строку S0.
def insert_string(C, S, S0):
    return S.replace(C, S0 + C)
C = 'a'
S = 'banana'
S0 = 'x'
result = insert_string(C, S, S0)
print(result)