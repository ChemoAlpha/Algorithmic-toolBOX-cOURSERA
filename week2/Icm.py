import sys

def lcm_naive(a, b):
	prod = a*b
	return (prod//gcd_naive(a,b))

def gcd_naive(a, b):
	if a==0:
		return b
	elif  b == 0:
		return a
	else:
		return	gcd_naive(b%a,a)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
