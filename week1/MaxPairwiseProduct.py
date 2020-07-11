long n = long(input())
long a = [long (x) for x in input().split()]
assert(len(a) == n)

long result = 0

for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > result:
            result = a[i]*a[j]

print(result)