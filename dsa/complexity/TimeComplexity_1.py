'''
Time Complexity
No of steps in program -> represent time for that execution

'''

# Complexity -> Length  of n
n = 10
for val in range(1, n + 1):
    print(val, end=" ")

list = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]

for val in list:
    print(val, end=" ")

from _datetime import datetime


# Complexity will be CONSTANT as not dependent on input
def main(list):
    initial = datetime.now()
    for val in [1, 2, 3, 4, 5]:
        print(val, end='')
    end = datetime.now()
    print((end - initial).microseconds)


for list in [
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3, 4, 5, 6, 7]
]:
    main(list)
    print()

# For Infinite Loop   -> The complexity is undetermined
# i = 10
# while(i > 0):
#     print(i)




