f = open("인공지능캠프.txt", 'w')
for i in range(1, 6):
    data = "%d명 참여 중입니다.\n" % i
    f.write(data)
f.close()