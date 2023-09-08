db = open('7_3_passwd.txt', mode='r')
lines = db.read().splitlines()
db.close

passwd = {}

for str in lines:
    info = str.split(":")
    passwd[info[0]] = info[1]


id = input("아이디 입력: ")
pw = input("패스워드 입력: ")

if pw == passwd.get(id):
    print("안녕하세요")
else:
    print("너 누구니?")


