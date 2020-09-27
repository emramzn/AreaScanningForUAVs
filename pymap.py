from bokeh.io import export_png
from bokeh.models import GMapOptions
from bokeh.plotting import gmap
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from matplotlib import colors
from PIL import Image


import heapq

class Cell(object):
    def __init__(self, x, y, reachable):
        """Initialize new cell.
        @param reachable is cell reachable? not a wall?
        @param x cell x coordinate
        @param y cell y coordinate
        @param g cost to move from the starting cell to this cell.
        @param h estimation of the cost to move from this cell
                 to the ending cell.
        @param f f = g + h
        """
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __lt__(self, other):
        return self.f < other.f
        
class AStar(object):
    def __init__(self):
        # open list
        self.opened = []
        heapq.heapify(self.opened)
        # visited cells list
        self.closed = set()
        # grid cells
        self.cells = []
        self.grid_height = None
        self.grid_width = None

    def init_grid(self, width, height, walls, start, end):
       
        self.grid_height = height
        self.grid_width = width
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if (x, y) in walls:
                    reachable = False
                else:
                    reachable = True
                self.cells.append(Cell(x, y, reachable))
        self.start = self.get_cell(*start)
        self.end = self.get_cell(*end)

    def get_heuristic(self, cell):
        
        return 10 * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))

    def get_cell(self, x, y):
        
        return self.cells[x * self.grid_height + y]

    def get_adjacent_cells(self, cell):
      
        cells = []
        if cell.x < self.grid_width-1:
            cells.append(self.get_cell(cell.x+1, cell.y))
        if cell.y > 0:
            cells.append(self.get_cell(cell.x, cell.y-1))
        if cell.x > 0:
            cells.append(self.get_cell(cell.x-1, cell.y))
        if cell.y < self.grid_height-1:
            cells.append(self.get_cell(cell.x, cell.y+1))
        return cells

    def get_path(self):
        cell = self.end
        path = [(cell.x, cell.y)]
        while cell.parent is not self.start:
            cell = cell.parent
            path.append((cell.x, cell.y))

        path.append((self.start.x, self.start.y))
        path.reverse()
        return path

    def update_cell(self, adj, cell):
      
        adj.g = cell.g + 10
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def solve(self):
       
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):
           
            f, cell = heapq.heappop(self.opened)
            self.closed.add(cell)
            if cell is self.end:
                return self.get_path()
            adj_cells = self.get_adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        if adj_cell.g > cell.g + 10:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))
                        
                        

a=AStar()
walls = ((0, 5), (1, 0), (1, 1), (1, 5), (2, 3),(3, 1), (3, 2), (3, 5), (4, 1), (4, 4), (5, 1),(20,6),(20,18),(14,5),(14,6),(14,7),(14,8)
,(14,9),(15,1),(15,8),(27,15),(26,16),(27,16),(28,16),(29,16),(30,16),(26,17),(27,17),(28,17),(29,17),(30,17),(26,18),(27,18),(28,18),(29,18),(30,18),(26,19),(27,19),(28,19),(29,19))
a.init_grid(47, 47, walls, (0, 0), (0,46))


path = a.solve()
objects=[AStar() for i in range(15)]

for i in range(13):   
    if i %2 ==0:
        objects[i].init_grid(47,47,walls, (i,0),(i+1,46))
        path +=objects[i].solve()
        
    else:
        objects[i].init_grid(47,47,walls, (i,46),(i+1,0))
        path +=objects[i].solve()  
        
print("Terrain Scan Data ", path ,"--- ",len(path))

from PIL import ImageOps
def DrawGrid(self,lat,lng):    
  
    lat,lng=lat,lng
    
    map_options = GMapOptions(lat=lat, lng=lng, map_type="hybrid", zoom=16)
    p = gmap("&key=AIzaSyAzNpn-Q7DbAQe_pXGuhHOaRGuiEhiRmR4", map_options, title="Austin")
    p.height, p.width=1000,1000
    export_png(p,filename='mapsPY.png')
     

    # Open image file
    image = Image.open('mapsPY.png')
    my_dpi=50.
    
    border = (45, 25, 30, 22) # left, up, right, bottom
    image=ImageOps.crop(image, border)
    # Set up figure
    fig=plt.figure(figsize=((float(image.size[0])/my_dpi),(float(image.size[1])/my_dpi)),dpi=my_dpi)
    ax=fig.add_subplot(111)
    
    # Remove whitespace from around the image
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    
    # Set the gridding interval: here we use the major tick interval
    myInterval=20.
    loc = plticker.MultipleLocator(base=myInterval)
    ax.xaxis.set_major_locator(loc)
    ax.yaxis.set_major_locator(loc)
    
    my_cmap = colors.ListedColormap(['r', 'g', 'b'])
    my_cmap.set_bad(color='w', alpha=0)
    
    ax.grid(which='major', color='#CCCCCC', linestyle='-')
    ax.imshow(image, interpolation='none', cmap=my_cmap,  zorder=0 )
 
  
#     Add the image
#     Find number of gridsquares in x and y direction
    nx=abs(int(float(ax.get_xlim()[1]-ax.get_xlim()[0])/float(myInterval)))
    ny=abs(int(float(ax.get_ylim()[1]-ax.get_ylim()[0])/float(myInterval)))
    
    # Add some labels to the gridsquares
    for j in range(ny):
        y=myInterval/2+j*myInterval
        for i in range(nx):
            x=myInterval/2.+float(i)*myInterval
            ax.text(x,y,'{},{}'.format(j,i),color='red',ha='center',va='center', fontsize=2)


    # Add line to gridsquares
    for k in range(len(walls)):
        ax.text(myInterval/2+myInterval*walls[k][0],myInterval/2+myInterval*walls[k][1],'{}'.format('||||'),color='red',ha='center',va='center', fontsize=14, fontstyle='italic')
      
        
    for k in range(0,len(path)):
#        if(myInterval/2+myInterval*path[0][0] > myInterval/2+myInterval*path[k-1][0]):
         ax.text(myInterval/2+myInterval*path[0][0],myInterval/2+myInterval*path[0][1],'{}'.format('|||'),color='yellow',ha='center',va='center', fontsize=25, fontstyle='italic')
        
        
    for k in range(0,len(path)):
   
        if (k>0 and (myInterval/2+myInterval*path[k][0] > myInterval/2+myInterval*path[k-1][0])):
            ax.text(myInterval/2+myInterval*path[k][0],myInterval/2+myInterval*path[k][1],'{}'.format('->'),color='blue',ha='center',va='center', fontsize=20, fontstyle='italic')
        elif (k>0 and (myInterval/2+myInterval*path[k][0] < myInterval/2+myInterval*path[k-1][0])):
             ax.text(myInterval/2+myInterval*path[k][0],myInterval/2+myInterval*path[k][1],'{}'.format('<-'),color='blue',ha='center',va='center', fontsize=20, fontstyle='italic')  
           
        else:
            ax.text(myInterval/2+myInterval*path[k][0],myInterval/2+myInterval*path[k][1],'{}'.format('|'),color='blue',ha='center',va='center', fontsize=27, fontstyle='italic')
    
        
        
          

    fig.savefig('myImageGrid.png',dpi=my_dpi)
    
















