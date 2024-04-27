s= open('pr.txt').readline()
k=0
for i in range (len(s)):
    if s[i].isdigit():
        k+=1
print (k)

a = 10.5
b = 2.5
m1 = a - b
m2 = a + b
m1,m2 = m2,m1
kv_raz = m2 ** 2
raz_kv = m1 * m2
r = raz_kv % kv_raz
print(r)

s = int(input())
s = s // 7
n = 1
k = 0
while s < 25:
    k += 1
    if (s + n) % 2 == 0:

        s = s + 11

        n = n + 5
print(n, k)

a = ['кот', 'котопёс', 'пёс']
k = 0
s = []
for i in range (len (a)):
    if 'кот' in a[i]:
        k += 1
        s.append (len(a[i]))
print (k, *s)
