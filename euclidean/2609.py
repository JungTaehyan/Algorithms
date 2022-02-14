A, B = map(int, input().split())


# 최대공약수
if B>A:
    A, B = B, A
def gcd(A, B):
    while B > 0:
        A, B = B, A % B
    return A

# 최소공배수
def lcm(A, B):
    return int(A * B / gcd(A, B))

print(gcd(A, B))
print(lcm(A, B))