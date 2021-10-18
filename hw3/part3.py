import random

def createGraph(n,p):
    # initiate matrix with 0s
    matrix = [[0 for x in range(n)] for y in range(n)]

    # inserting 1s into the graph
    # where the probability
    # calls for it
    for x in range(0,n):
        for y in range(0,n):
            if(x < y):
                q = random.random()
                if(q < p):
                    matrix[x][y] = 1

    return matrix

def connect_test(G, t):

    n = len(G[0])

    # if t==0, every graph will pass the test,
    # therefore return 1

    if(t==0): 
        return 1
    else:
        empty = True                #
        for x in range(0,n):        # Otherwise, check for an empty
            for y in range(0,n):    # graph because it will fail
                if(G[x][y] == 1):   # in every case, used primarily
                    empty = False   # to increase the speed of the
        if(empty):                  # program
            return 0                #


    # I created a copy of G for the purpose
    # that in my method of traversing
    # by DFS this is essential

    temp = copy(G)


    # The following code will traverse through
    # the matrix and start a DFS from every
    # spot containing a 1

    for x in range(0,n):
        for y in range(0,n):
            if(G[x][y] == 1):
                G[x][y] = 8                 # 8 is the value
                G[y][x] = 8                 # used for
                ans = DFS(G,x,y,x,0,[])     # visited nodes
                G = copy(temp)
                if(ans >= t):       # if the value of the largest
                    return 1        # connection is >= t then
    return 0                        # return 1, return 0 otherwise



# I know this code could've been done more efficiently
# But I don't want to mess it up and there is only
# 1 hour before submission time
def DFS(G, x, y, tarNode, counter, connect_list):

    # the following code will check through
    # a horizontal path in a DFS

    n = len(G[0])
    for z in range(0,n):
        if(G[y][z] != 8 and G[y][z] != 0):      # I picked a value of 8 to represent
            G[y][z] = 8                         #  visited nodes
            G[z][y] = 8
            if(z == tarNode or y == tarNode):
                connect_list.append(counter+2)              # append connection size
            else:                                           # to list of connection
                DFS(G,y,z,tarNode,counter+1,connect_list)   # sizes, recurse if 
                                                            # connection not found


    # the following code does the same thing
    # but for vertical paths in the matrix
    # this is where I could've combined
    # them but I'm afraid I'll mess
    # something up

    z=0
    for z in range(0,n):
        if(G[z][y] != 8 and G[z][y] != 0 and G[y][z] != 8):
            G[z][y] = 8
            G[y][z] = 8
            if(z == tarNode or y == tarNode):
                connect_list.append(counter+2)
            else:
                DFS(G,y,z,tarNode,counter+1,connect_list)


    # if there is only one a one edged
    # connection return 2, because 2
    # nodes participate in this connection

    if(len(connect_list) == 0):
        return 2

    # Otherwise, sort the list from smallest
    # to largest and grab the final value
    # which is the largest connection length

    connect_list.sort()
    return connect_list[-1]

def test(n, p):
    total_pass = 0

    for x in range(0,500):
        G = createGraph(n, p)
        total_pass = total_pass + connect_test(G, 30)

    print(total_pass/500*100)




def copy(G):
    n = len(G[0])

    copy = [[0 for x in range(n)] for y in range(n)]

    for x in range(0,n):                #
        for y in range(0,n):            #   creating a copy
            if(G[x][y] == 1):           #   of a matrix
                copy[x][y] = 1          #
    return copy


def printGraph(G):  #used for testing
    for row in G:
        print(row)



#         test cases          #

n = 40
c = 0.0
while(c <= 3.0):
    c = c + 0.2
    p = c/float(n)
    test(n, p)

# testG = [0,1,1,1],[0,0,1,1],[0,0,0,1],[0,0,0,0]

# G = createGraph(4,0.5)
# printGraph(G)
# if(connect_test(G,4) == 1):
#     print("True")
# else:
#     print("False")
# print("\n")
# printGraph(G)

# printGraph(testG)
# connect_test(testG,4)
# print("\n")
# printGraph(testG)