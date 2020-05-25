T = int(input())
for test_case in range(1, T + 1):
    A, B = input().split()
    visit = [0] * len(A)
    count = 0
    temp_count = 0
    for i in range(len(A) - len(B) + 1):
        if visit[i] == 0:
            for j in range(len(B)):
                if A[i + j] != B[j]:
                    break
            else:
                for k in range(len(B)):
                    visit[i + k] = 1
                count += 1
                temp_count += 1
    count += len(A) - (temp_count * len(B))
    print("#{} {}".format(test_case, count))