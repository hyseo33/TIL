import sys
sys.stdin = open('연습_input.txt')

data = [input()]

print(data)

arr = [ 0,0,0,0,0,0,0,1,1,1, 1,0,0,0,0,0,0,1,1,0, 0,0,0,0,0,1,1,1,1,0,
        0,1,1,0,0,0,0,1,1,0, 0,0,0,1,1,1,1,0,0,1, 1,1,1,0,0,1,1,1,1,1, 1,0,0,1,1,0,0,1,1,1]

for i in range(10):
    n = 0
    for j in range(i*7, i*7+7, 1):
        n = n * 2 + arr[j]
    print(n, end=' ')
print()