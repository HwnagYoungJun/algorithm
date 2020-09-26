def solution(n, arr1, arr2):
	arr1_list = []
	arr2_list = []
	for i in range(n):
		res1 = soved_password(arr1[i], n)
		arr1_list.append(res1)
		res2 = soved_password(arr2[i], n)
		arr2_list.append(res2)
	
	pass_list = [[' ' for _ in range(n)] for _ in range(n)]
	for row in range(n):
		for col in range(n):
			if arr1_list[row][col] == '1' or arr2_list[row][col] == '1':
				pass_list[row][col] = '#'
	
	for i in range(n):
		pass_list[i] = ''.join(pass_list[i])

	return pass_list

def soved_password(num, n):
	num_2 = format(num, 'b')
	if len(num_2) < n:
		num_2 = '0' * (n - len(num_2)) + num_2
        
	return num_2