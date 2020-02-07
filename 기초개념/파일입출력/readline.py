f = open("인공지능캠프.txt", 'r')
while True:
    line = f.readline() #파일 한 줄 읽기.
    if not line: break
    print(line)
f.close()