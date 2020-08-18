N = int(input())
br, h = map(int, input().split(' '))
l=list(map(int, input().split()))
sp=pow(10,9)+7
Sum = sum(l)
maxVol = 0
temp = 0
stack = list()
for i in range(N):
    while(stack and l[i] <= l[stack[-1]]):
        a = stack.pop(-1)
        if (not stack):
            temp = l[a]*i
        else:
            temp = l[a]*(i-stack[-1]-1)
        maxVol = max(maxVol%sp, temp)
    stack.append(i)
while stack:
    a = stack.pop(-1)
    if (not stack):
        temp = l[a]*N
    else:
        temp = l[a]*(N-stack[-1]-1)
    maxVol = max(maxVol%sp, temp)

print(((Sum%sp - maxVol%sp)%sp*br%sp*h%sp)%sp)
        
