import math
#__author__ = 'ChengDH'
def get_number_of_params(a):
    number=0
    for i in range(len(a)):
        if a[i]=='A':
            number+=10*math.pow(16,len(a)-i-1)
        elif a[i]=='B':
            number+=11*math.pow(16,len(a)-i-1)
        elif a[i] == 'C':
            number += 12 * math.pow(16, len(a) - i - 1)
        elif a[i]=='D':
            number+=13*math.pow(16,len(a)-i-1)
        elif a[i]=='E':
            number+=14*math.pow(16,len(a)-i-1)
        elif a[i]=='F':
            number+=15*math.pow(16,len(a)-i-1)
        else:
            number += int(a[i]) * math.pow(16, len(a) - i - 1)
    #print("该报文参数的数量为：{}".format(number))

def get_long_of_params(a,b):
    number=0
    for i in range(len(a)):
        if a[i]=='A':
            number+=10*math.pow(16,len(a)-i-1)
        elif a[i]=='B':
            number+=11*math.pow(16,len(a)-i-1)
        elif a[i] == 'C':
            number += 12 * math.pow(16, len(a) - i - 1)
        elif a[i]=='D':
            number+=13*math.pow(16,len(a)-i-1)
        elif a[i]=='E':
            number+=14*math.pow(16,len(a)-i-1)
        elif a[i]=='F':
            number+=15*math.pow(16,len(a)-i-1)
        else:
            number += int(a[i]) * math.pow(16, len(a) - i - 1)
    b=number
    if number>=4:

        number=(number-4)*8
    #print("该报文参数的长度为：{}".format(number)+"bit")

def turn0x(b):
    str1=''
    str2=''
    for i in range(len(b)):
        str1+=b[i]
    for i in range(len(str1)):
        if str1[i]=='0':
            str2+='0000'
        elif str1[i]=='1':
            str2+='0001'
        elif str1[i]=='2':
            str2+='0010'
        elif str1[i]=='3':
            str2+='0011'
        elif str1[i]=='4':
            str2+='0100'
        elif str1[i]=='5':
            str2+='0101'
        elif str1[i]=='6':
            str2+='0110'
        elif str1[i]=='7':
            str2+='0111'
        elif str1[i]=='8':
            str2+='1000'
        elif str1[i]=='9':
            str2+='1001'
        elif str1[i]=='A':
            str2+='1010'
        elif str1[i]=='B':
            str2+='1011'
        elif str1[i]=='C':
            str2+='1100'
        elif str1[i]=='D':
            str2+='1101'
        elif str1[i]=='E':
            str2+='1110'
        elif str1[i]=='F':
            str2+='1111'
    return str2

def ttoint(str):
    num1=0
    for i in range(len(str)):
        if str[i]=='0':
            num1+=0*math.pow(2,len(str)-i-1)
        else:
            num1 += 1 * math.pow(2, len(str) - i - 1)
    return num1

def mintomax(string):
    chunks = [string[i:i + 8] for i in range(0, len(string), 8)]
    # 逆序所有小块
    reversed_chunks = chunks[::-1]
    # 合并小块为最终字符串
    merged_string = ''.join(reversed_chunks)
    return merged_string

def jiexif(number,res,off,Size,data):
    if Size<=8:
        str1 = data[number:number + Size]
        num2 = res * ttoint(str1) + off
    else:
        str1 = data[number:number + Size]
        if Size%8==0:
            str1=mintomax(str1)
        else:
            for j in range(Size%8):
                str1='0'+str1
            str1=mintomax(str1)
        num2 = res * ttoint(str1) + off
    return num2


def getint0x(a):
    number = 0
    for i in range(len(a)):
        if a[i] == 'A':
            number += 10 * math.pow(16, len(a) - i - 1)
        elif a[i] == 'B':
            number += 11 * math.pow(16, len(a) - i - 1)
        elif a[i] == 'C':
            number += 12 * math.pow(16, len(a) - i - 1)
        elif a[i] == 'D':
            number += 13 * math.pow(16, len(a) - i - 1)
        elif a[i] == 'E':
            number += 14 * math.pow(16, len(a) - i - 1)
        elif a[i] == 'F':
            number += 15 * math.pow(16, len(a) - i - 1)
        else:
            number += int(a[i]) * math.pow(16, len(a) - i - 1)
    return number
