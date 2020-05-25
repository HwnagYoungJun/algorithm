N, M = map(int, input().split())
if M > (N // 2):
    M = N - M
a = 1
b = 1
for i in range(1, M + 1):
    a *= (N -i + 1)
    b *= i
print(a //b)