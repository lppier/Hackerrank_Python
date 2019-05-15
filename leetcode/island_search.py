
# Depth first search soln
class Solution:
    isle_count = 0 
    
    def numIslands(self, grid) -> int:
        
        r_dim = len(grid)
        if r_dim != 0:
            c_dim = len(grid[0])
            
        # Set searched items to 0
        def dfs(g, r, c):
            
            if r+1 < r_dim and g[r+1][c]=='1': # down
                g[r+1][c] = '0'
                dfs(g, r+1, c)
                
            if r-1 >= 0 and g[r-1][c]=='1': # up
                g[r-1][c] = '0'
                dfs(g, r-1, c)
            
            if c+1 < c_dim and g[r][c+1]=='1': # right
                g[r][c+1] = '0'
                dfs(g, r, c+1)
                
            if c-1 >= 0 and g[r][c-1]=='1': # left
                g[r][c-1] = '0'
                dfs(g, r, c-1)
                
            
        def island_search(g): # grid, row, col
            for row in range(r_dim):
                for col in range(c_dim):
                    if grid[row][col]=='1':
                        self.isle_count+= 1 # add an island whenever encounter a root
                        dfs(grid, row, col)
        
        island_search(grid)
        return self.isle_count

# Breadth first search soln
class Solution:
    isle_count = 0 
    
    def numIslands(self, grid) -> int:
        
        r_dim = len(grid)
        if r_dim != 0:
            c_dim = len(grid[0])
            
        def bfs(g, r, c):
            queue = []
            g[r][c] = '0' # visited
            queue.append((r, c)) # store vertices
            
            while queue:
                curr_r, curr_c = queue.pop(0)
                
                # add all the neighbours, only add if it is 1
                if curr_r-1 >= 0 and g[curr_r-1][curr_c]=='1':
                    g[curr_r-1][curr_c] = '0' # visited
                    queue.append((curr_r-1, curr_c))

                if curr_r+1 < r_dim and g[curr_r+1][curr_c]=='1':
                    g[curr_r+1][curr_c] = '0' # visited
                    queue.append((curr_r+1, curr_c))

                if curr_c-1 >= 0 and g[curr_r][curr_c-1]=='1':
                    g[curr_r][curr_c-1] = '0' # visited
                    queue.append((curr_r, curr_c-1))

                if curr_c+1 < c_dim and g[curr_r][curr_c+1]=='1':
                    g[curr_r][curr_c+1] = '0' # visited
                    queue.append((curr_r, curr_c+1))

        def island_search(g): # grid, row, col
            for row in range(r_dim):
                for col in range(c_dim):
                    if grid[row][col]=='1':
                        self.isle_count+= 1 # add an island whenever encounter a root
                        bfs(grid, row, col)
        
        island_search(grid)
        return self.isle_count
                