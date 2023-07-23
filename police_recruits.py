n = int(input())
m = list(map(int, input().split()))

crime = 0  
police = 0  

for i in m:
    if i == -1:
        if police > 0:
            police -= 1
        else:
            crime += 1
    else:
        police += i

print(crime)