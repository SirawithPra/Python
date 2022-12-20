#1
def reverse_words_order_and_swap_cases(sentence):
    sentence=input()
    x,y=sentence.swapcase().split(' ')
    return y+' '+x

#2
def numCells(grid):
    r=0
    xx=len(grid)
    yy=len(grid[0])
    for x in range(xx):
        for y in range(yy):
            rs=0
            neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),
            (x+1,y-1),(x-1,y+1),(x-1,y-1)]
            for i, j in enumerate(neighbors):
                if j[0] < 0 or j[1] < 0 or j[0] > xx-1 or j[1] >yy-1 :
                    rs+=1
                elif grid[x][y] >grid[j[0]][j[1]] :
                    rs+=1
            print(rs)
            if rs==8:
                r+=1
    return r
grid=[[1,2,7],[4,5,6],[8,8,9]]

k=numCells(grid)

