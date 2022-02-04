N = int(input())
cnt = 0
c_name = 666

while True:
    if '666' in str(c_name):
        cnt+=1
    if cnt == N:
        print(c_name)
        break
    c_name+=1
