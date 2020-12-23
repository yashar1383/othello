import threading
from os import system
from time import sleep
def go(col,row,color,x,y):
    #print('test go_D_R : ',table[row][col],row,col)
    try : 
        if table[row][col] == 'N' or col < 0 or row < 0 or col > 7 or row > 7:
            #print(False)
            return 0
        
    except :
        return 0
    if table[row][col] == color :
            #print(True)
            return 1
    y = go(col+x,row+y,color,x,y)
    table[row][col] = color if y else table[row][col]
    #if y == 1:
    #    yy = threading.Thread(target=start, args=(row,col,color))
    #    yy.start()
    #    yy.join()
    return y
def table_show():
    List = {'N':'\u25E6','1':'@','0':'\u25CB'}
    print(end=' ')
    for i in range(ord('A'),ord('H')+1):
        print(chr(i),end=' ')
    print()
    for i,k in zip(table,range(1,9)) :
        print(k,end='')
        for j in i :
            print(List[j],end=' ')
        print()
    sleep(0.5)
def start(row,col,color):
 
    table[row][col] = color
    #print(row,col)
    x = threading.Thread(target=go, args=(col+1,row+1,color,1,1))
    x.start()
    #go(col+1,row+1,color,1,1)
    x1 = threading.Thread(target=go, args=(col-1,row+1,color,-1,1))
    x1.start()
    #go(col-1,row+1,color,-1,1)
    x2 = threading.Thread(target=go, args=(col+1,row-1,color,1,-1))
    x2.start()
    #go(col+1,row-1,color,1,-1)
    x3 = threading.Thread(target=go, args=(col-1,row-1,color,-1,-1))
    x3.start()
    #go(col-1,row-1,color,-1,-1)
    x4 = threading.Thread(target=go, args=(col,row+1,color,0,1))
    x4.start()
    #go(col,row+1,color,0,1)
    x5 = threading.Thread(target=go, args=(col-1,row,color,-1,0))
    x5.start()
    #go(col-1,row,color,-1,0)
    x6 = threading.Thread(target=go, args=(col,row-1,color,0,-1))
    x6.start()
    #go(col,row-1,color,0,-1)
    x7 = threading.Thread(target=go, args=(col+1,row,color,1,0))
    x7.start()
    #go(col+1,row,color,1,0)
ops = lambda x : str((int(x)+1)%2)
table = [['N'].copy()*8 for i in range(8)]
table[3][3] , table[4][4] = "0" , "0"
table[3][4] , table[4][3] = "1" , "1"
color = '1'
#int(input())
#location = input().split()
table_show()
for _ in range(int(input())):
    i = input()
    system('cls')
    #print(f"----> {i}")
    col = ord(i[0])-65
    row = int(i[1])-1
    start(row,col,color)
    table_show()
    # END :
    color = ops(color)
table_show()
#from time import sleep
#sleep(1)
o = [j for i in table for j in i]
print(o.count('1'),o.count('0'))
#print(*table,sep='\n')
