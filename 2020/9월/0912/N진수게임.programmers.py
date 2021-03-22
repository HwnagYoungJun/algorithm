def solution(n, t, m, p):
	temp_list = [i for i in range(t * m)]

	for i in range(len(temp_list)):
		temp_list[i] = conv(temp_list[i], n)

	temp_string = "".join(temp_list)
	res = ''
	turn = p - 1
	for i in range(t):
		res += temp_string[turn]
		turn += m
  
	return res


def conv(number, base):
	T = '0123456789ABCDEF'
	i, j = divmod(number, base)
	if i == 0:
		return T[j]
	else:
		return conv(i, base) + T[j]

n = 16
t = 16
m = 2
p = 1
print(solution(n, t, m, p))