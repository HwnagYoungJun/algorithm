sw = True
print('')
for x in range(10):
    print(x)
    if x == 4:
        sw = False
        break
print(x)
if sw == True:
    print('!')