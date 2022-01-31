class User:
    def __init__(self,name,age,birth,born):
        self.name = name
        self.age = age
        self.birth = birth
        self.born = born
    def change_name(self,name):
        self.name = name
        
  
N,K = map(int,input().split())
User_list = [0]*N
for i in range(N):
    name,age,birth,born = input().split()
    User_list[i] = User(name,age,birth,born)
    
for i in range(K):
    index,new_name = input().split()
    User_list[int(index)-1].change_name(new_name)
    
for user in User_list:
    print(user.name,user.age,user.birth,user.born)
    