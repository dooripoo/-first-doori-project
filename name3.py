from asyncore import write

f = open("C:/Users/LCW/Desktop/python work space/매수종목1.txt", mode="wt", encoding="utf-8")
f.write("005930\n")
f.write("005930\n")
f.close()

print("write의 type : ", type(write))