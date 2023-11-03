#Range() function overview

#start - inclusive 
#stop - exclusive 
#step - increment

#stop
for num in range(5):
    print(num)

#start/stop
for num in range(2, 10):
    print(num)

#start/stop/step
for num in range(2, 11, 2):
    print(num)

#range with a list
num_list = list(range(1, 6))
print(num_list)