f = open("인공지능캠프.txt", 'a')
for i in range(6, 11):
    data = "%d명 참여 중입니다.\n" %i
    f.write(data)
f.close()
