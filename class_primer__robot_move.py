# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
class Robot:
    large = {1:2, 2:2, 3:5, 4:10}
    dirs = {'N':[-1,0],'S':[1,0],'E':[0,1],'W':[0,-1]}
    
    def __init__(self,y,x,lv):
        self.y = y
        self.x = x
        self.lv = lv
        self.lg = self.large[self.lv]
    
    def move(self,direction):
        value = self.dirs[direction]
        self.y += value[0]*self.lg
        self.x += value[1]*self.lg
        
    def level_up(self):
        self.lv = min(self.lv+1,4)
        self.lg = self.large[self.lv]
    
    def get_point(self):
        return [self.y,self.x]
    
    def print(self):
        print(self.x,self.y,self.lv)
        
        
        
h,w,n,k = [int(x) for x in input().split()]
boxes = [[None]for _ in range(10)]
robots = [None]*n

for i in range(10):
    x,y = [int(x)for x in input().split()]
    boxes[i] = [y,x]
    
for i in range(n):
    x,y,lv = [int(x)for x in input().split()]
    robots[i] = Robot(y,x,lv)
    
for _ in range(k):
    values = input().split()
    index = int(values[0])-1
    direction = values[1]
    
    robots[index].move(direction)
    point = robots[index].get_point()
    
    if point in boxes:
        robots[index].level_up()
        
for robot in robots:
    robot.print()
        
        
        
#answer
class Robot:
    large = {1: 1, 2: 2, 3: 5, 4: 10}
    dirs = {"N": [-1, 0], "S": [1, 0], "E": [0, 1], "W": [0, -1]}

    def __init__(self, y, x, lv):
        self.y = y
        self.x = x
        self.lv = lv

        self.lg = self.large[self.lv]

    def move(self, direction):
        value = self.dirs[direction]

        self.y += value[0] * self.lg
        self.x += value[1] * self.lg

    def level_up(self):
        self.lv = min(self.lv+1, 4)
        self.lg = self.large[self.lv]

    def get_point(self):
        return [self.y, self.x]

    def print(self):
        print(self.x, self.y, self.lv)


h, w, n, k = [int(x) for x in input().split()]

boxes = [[None] for _ in range(10)]
robots = [None] * n

for i in range(10):
    x, y = [int(x) for x in input().split()]
    boxes[i] = [y, x]

for i in range(n):
    x, y, lv = [int(x) for x in input().split()]
    robots[i] = Robot(y, x, lv)

for _ in range(k):
    values = input().split()

    index = int(values[0]) - 1
    direction = values[1]

    robots[index].move(direction)

    point = robots[index].get_point()
    if point in boxes:
        robots[index].level_up()

for robot in robots:
    robot.print()
        
        
        
        