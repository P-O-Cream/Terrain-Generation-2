import random,time

class TerrainGeneration(object):
    def __init__(self):
        self.map_width = 100
        self.sky_height = 30
        self.grass_block_height = 1
        self.soil_block_height = 3
        self.ground_height = 36
        self.map_height = 70
        self.grass_probability = 0
        self.common_tree_probability = 8
        self.yellow_tree_probability = 0
        self.purple_tree_probability = 0
        self.leave_probability = 4
        self.tree_height = [5,7]
        self.map = [[" " for i in range(self.map_width)] for j in range(self.sky_height)] + \
                   [["3" for i in range(self.map_width)] for j in range(self.grass_block_height)] + \
                   [["1" for i in range(self.map_width)] for j in range(self.soil_block_height)] + \
                   [["0" for i in range(self.map_width)] for j in range(self.ground_height)]
    
    # @copyright Copyright [C] Xiaoxuan 2023
    def fill(self,change_value,*coordinate):
        for i in coordinate:
            self.map[i[0]-1][i[1]-1] = change_value
            
    def fill2(self,height,x,y,change_value):
        for i in range(height):
            self.map[x][y] = change_value
            x -= 1
    
    def terrain_generation(self):
        for i in range(self.map_width):
            plant_tree = random.randint(0,self.common_tree_probability)
            if i > 1 and i < self.map_width - 3:
                if plant_tree == 0 and self.map[29][i-1] != "5" and self.map[29][i-2] != "5":
                    tree_height = random.randint(self.tree_height[0],self.tree_height[1])
                    self.fill2(tree_height,self.sky_height-1,i,"5")
                    tree_leave = random.randint(0,self.leave_probability)
                    if tree_leave == 0:
                        self.fill(
                            "2",
                            (29-tree_height+1,i+1),(29-tree_height,i+1),(29-tree_height+-1,i+1),
                            (29-tree_height+1,i),(29-tree_height+1,i+2),
                            (29-tree_height+1,i+3),(29-tree_height+1,i-1),
                            (29-tree_height,i+2),(29-tree_height,i)
                            )
                    if tree_leave == 1:
                        self.fill(
                            "2",
                            (29-tree_height+1,i+1),(29-tree_height,i+1),(29-tree_height-1,i+1),
                            (29-tree_height+1,i),(29-tree_height+1,i+2),
                            (29-tree_height+1,i+3),(29-tree_height+2,i+2),
                            (29-tree_height,i+2),(29-tree_height,i)
                            )
                    if tree_leave == 2:
                        self.fill(
                            "2",
                            (29-tree_height+1,i+1),(29-tree_height,i+1),(29-tree_height-1,i+1),
                            (29-tree_height+1,i),(29-tree_height+1,i+2),
                            (29-tree_height+1,i+3),(29-tree_height+2,i),
                            (29-tree_height,i+2),(29-tree_height,i)
                            )
                    if tree_leave == 3:
                        self.fill(
                            "2",
                            (29-tree_height+1,i+1),(29-tree_height,i+1),(29-tree_height-1,i+1),
                            (29-tree_height+1,i),(29-tree_height+1,i+2),
                            (29-tree_height+1,i+3),(29-tree_height+2,i),(29-tree_height+2,i+2),
                            (29-tree_height,i+2),(29-tree_height,i)
                            )
                    if tree_leave == 4:
                        self.fill(
                            "2",
                            (29-tree_height+1,i+1),(29-tree_height,i+1),(29-tree_height+-1,i+1),
                            (29-tree_height+1,i),(29-tree_height+1,i+2),
                            (29-tree_height+1,i+3),(29-tree_height+1,i-1),
                            (29-tree_height,i+2),(29-tree_height,i),
                            (29-tree_height,i+2),(29-tree_height-1,i+2)
                            )
        
    def print_generation(self):
        for i in range(self.map_height):
            for j in range(self.map_width):
                if self.map[i][j] == " ":print("\033[48;2;50;233;223m\033[30m  ",end="")
                if self.map[i][j] == "2":print("\033[48;2;64;192;32m  ",end="")
                if self.map[i][j] == "5":print("\033[48;2;128;128;16m▒▒",end="")
                if self.map[i][j] == "3":print("\033[48;5;52m\033[38;5;118m▀▀",end="")
                if self.map[i][j] == "1":print("\033[48;5;52m  ",end="")
                if self.map[i][j] == "0":print("\033[48;2;192;192;192m  ",end="")
            print();time.sleep(0.3)
        print("\033[m") 
        
_TerrainGeneration = TerrainGeneration()
_TerrainGeneration.terrain_generation()
_TerrainGeneration.print_generation()
