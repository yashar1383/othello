import threading
def go(col,row,color,x,y):
    #print('test go_D_R : ',table[row][col],row,col)
    try : 
        if table[row][col] == 'N' or col < 0 or row < 0 or col > 7 or row > 7:
            #print(False)
            return 0
    except: return 0
    if table[row][col] == color :
        #print(True)
        return 1
    y = go(col+x,row+y,color,x,y)
    table[row][col] = color if y else table[row][col]
    return y
ops = lambda x : str((int(x)+1)%2)
table = [['N'].copy()*8 for i in range(8)]
table[3][3] , table[4][4] = "0" , "0"
table[3][4] , table[4][3] = "1" , "1"
color = '1'
int(input())
location = input().split()
for i in location:
    #print(f"----> {i}")
    col = ord(i[0])-65
    row = int(i[1])-1
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
    x.join() ; x1.join() ; x2.join() ; x3.join() ; x4.join() ; x5.join() ; x6.join() ; x7.join()
    #go(col+1,row,color,1,0)
    # END :
    color = ops(color)
d = [j for i in table for j in i].count('1')
print(d,len(location)+4 - d)
