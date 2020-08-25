def findNextCellToFill(grid, i, j):
        for x in range(i,7):
                for y in range(j,7):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,7):
                for y in range(0,7):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1

def isValid(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(7)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(7)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 1 *(i//7), 1 *(j//7)
                        for x in range(secTopX, secTopX+7):
                                for y in range(secTopY, secTopY+7):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,8):
                if isValid(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False