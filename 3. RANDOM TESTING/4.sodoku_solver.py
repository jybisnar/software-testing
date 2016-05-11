# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
hard = [[1,0,0,0,0,7,0,9,0],
         [0,3,0,0,2,0,0,0,8],
         [0,0,9,6,0,0,5,0,0],
         [0,0,5,3,0,0,9,0,0],
         [0,1,0,0,8,0,0,0,2],
         [6,0,0,0,0,4,0,0,0],
         [3,0,0,0,0,0,0,1,0],
         [0,4,0,0,0,0,0,0,7],
         [0,0,7,0,0,0,3,0,0]]


def initmat(l, c, val):
    return [[val for j in range(c)] for i in range(l)]

def quad(i,j):
    if i >= 0 and i < 3: # 0 or 1 or 2
        if j >= 0 and j < 3:
            return 0
        if j >= 3 and j < 6:
            return 1
        if j >= 6 and j < 9:
            return 2
    if i >= 3 and i < 6: #3 or 4 or 5
        if j >= 0 and j < 3:
            return 3
        if j >= 3 and j < 6:
            return 4
        if j >= 6 and j < 9:
            return 5
    if i >= 6 and i < 9: #6 or 7 or 8
        if j >= 0 and j < 3:
            return 6
        if j >= 3 and j < 6:
            return 7
        if j >= 6 and j < 9:
            return 8

def isSudokuNum(n):
    return isinstance(n, int) and n >=0 and n < 10

def checkFormat(grid):
    if not (len(grid) == 9):
        return False
    for el in grid:
        if len(el) != 9:
            return False
    return True

global ql
global qc
global qq
global empty_pos

def checkValidity(n, l, c):
    if n == 0:
        return True
    i = n-1
    return not (ql[i][l] or qc[i][c] or qq[i][quad(l, c)])


def markElement(el, i, j):
    if el <= 0:
        return;
    ql[el-1][i] = True #mark element
    qc[el-1][j] = True
    qq[el-1][quad(i,j)] = True

def unmarkElement(el, i, j):
    if el <= 0:
        return;
    ql[el-1][i] = False
    qc[el-1][j] = False
    qq[el-1][quad(i,j)] = False

#obtains info about the grid and check validity
def scan(grid):
    if(not checkFormat(grid)):
        return None
    global ql, qc, qq, empty_pos
    ql = initmat(9,9, False) #ql[i][j] element i+1 happens in line j
    qc = initmat(9,9, False) #qc[i][j] element i+1 happens in column j
    qq = initmat(9,9, False) #qq[i][j] element i+1 in quad j
    empty_pos = list()
    for i in range(9):
        for j in range(9):
            if not isSudokuNum(grid[i][j]):
                return None
            el= grid[i][j]
            if el == 0:
                empty_pos.append((i,j))
            else:
                if not checkValidity(el,  i, j):
                    return False
                markElement(el, i, j)
    return True

def printMat(grid):
    for i in grid:
        print i

def solve_sudoku (grid):
    scret = scan(grid)
    if scret != True:
        return scret
    sz = len(empty_pos)
    k = 0
    lastVisited = initmat(9,9, 0) #last element tested for the position i, j
    inter = 0
    #printMat(ql)
    while k < sz:
        inter += 1
        u = empty_pos[k][0]
        y = empty_pos[k][1]
        fac = False#is factible?
        unmarkElement(lastVisited[u][y], u, y)
        grid[u][y] = 0
        for el in range(lastVisited[u][y]+1,10):    
            if checkValidity(el, u, y):
                grid[u][y] = el
                lastVisited[u][y] = el
                markElement(el, u, y)
                fac = True
                k += 1
                break#breaks the for loop
        if not fac:
            if k == 0:
                return False # no possible solutions anymore
            else:
                k -= 1
                unmarkElement(grid[u][y], u, y)
                lastVisited[u][y] = 0
                grid[u][y] = 0
    return grid

#print solve_sudoku(ill_formed) # --> None
#print solve_sudoku(valid)      # --> True
#print solve_sudoku(invalid)    # --> False
#print solve_sudoku(easy)       # --> True
#print solve_sudoku(hard)       # --> True

