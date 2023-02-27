# Destroying the array : the maximum possible sum of elements on the segment containing no destroyed elements, after first i operations are performed.
class DSU:
    def __init__(self,n):
        self.parent = [-1 for i in range(n)]
        self.rank = [-1]*n 
        self.setSize = [0]*n 
        self.setCount = n
        self.setSum = [0]*n 
    
    def makeSet(self,i,x):
        self.parent[i] = i 
        self.rank[i] = 0
 
        self.setSize[i] = 1 
        self.setSum[i] = x 
 
        self.setCount += 1
    
    def findSet(self,i):
        if self.parent[i] == i:
            return i 
        
        self.parent[i] = self.findSet(self.parent[i])
 
        return self.parent[i]
 
    def sameSet(self,i,j):
        return self.findSet(i) == self.findSet(j)
    
    def union(self,i,j):
        if not self.sameSet(i,j):
            parent_i = self.findSet(i)
            parent_j = self.findSet(j)
 
            parent_i,parent_j = (parent_j,parent_i) if self.rank[parent_i] > self.rank[parent_j] else (parent_i,parent_j)
            
            self.parent[parent_i] = parent_j
 
            if self.rank[parent_i] == self.rank[parent_j]:
                self.rank[parent_j] += 1
            
            self.setSize[parent_j] += self.setSize[parent_i]
            self.setSum[parent_j] += self.setSum[parent_i]
            
 
            self.setCount -= 1
 
    def sizeOfSet(self,i):
        return self.setSize[self.findSet(i)]
 
    def getSetCount(self):
        return self.setCount
    
    def sumOfSet(self,i):
        return self.setSum[self.findSet(i)]
 
n = int(input())
arr_values = list(map(int,input().split()))
destroying_order = [int(i)-1 for i in input().split()]
# print(destroying_order)
 
constructing_order = destroying_order[::-1]
array_state = [0]*n # (if the value of some index is 1->not destroyed ,0 ->destroyed)
 
max_subset_sum = [0]
curr_sum = 0
dsu = DSU(n)
for index in constructing_order:
    dsu.makeSet(index,arr_values[index])
    array_state[index] = 1
    if index > 0 and array_state[index-1]:
        dsu.union(index-1,index)
    if index < n-1 and array_state[index+1]:
        dsu.union(index,index+1)
    
    curr_sum = max(dsu.sumOfSet(index),curr_sum)
    max_subset_sum.append(curr_sum)
 
max_subset_sum.reverse()
max_subset_sum.pop(0)
for ele in max_subset_sum:
    print(ele)
 

# Now , we have to find the minimum possible sum of elements on the segment containing no destroyed elements, after first i operations are performed.
# We can do this by using the same DSU data structure.
# We will just have to change the union function a bit.
# We will have to find the minimum element in the set and then add it to the sum of the set.
# We will have to do this in the union function.
# We will have to change the makeSet function a bit.
# We will have to add a new array to the DSU class.
# This array will store the minimum element in the set.

class DSU:
    def __init__(self,n):
        self.parent = [-1 for i in range(n)]
        self.rank = [-1]*n 
        self.setSize = [0]*n 
        self.setCount = n
        self.setSum = [0]*n 
        self.setMin = [0]*n
    
    def makeSet(self,i,x):
        self.parent[i] = i 
        self.rank[i] = 0
 
        self.setSize[i] = 1 
        self.setSum[i] = x 
        self.setMin[i] = x
 
        self.setCount += 1
    
    def findSet(self,i):
        if self.parent[i] == i:
            return i 
        
        self.parent[i] = self.findSet(self.parent[i])
 
        return self.parent[i]
 
    def sameSet(self,i,j):
        return self.findSet(i) == self.findSet(j)
    
    def union(self,i,j):
        if not self.sameSet(i,j):
            parent_i = self.findSet(i)
            parent_j = self.findSet(j)
 
            parent_i,parent_j = (parent_j,parent_i) if self.rank[parent_i] > self.rank[parent_j] else (parent_i,parent_j)
            
            self.parent[parent_i] = parent_j
 
            if self.rank[parent_i] == self.rank[parent_j]:
                self.rank[parent_j] += 1
            
            self.setSize[parent_j] += self.setSize[parent_i]
            self.setSum[parent_j] += self.setSum[parent_i]
            self.setMin[parent_j] = min(self.setMin[parent_i],self.setMin[parent_j])
            
 
            self.setCount -= 1
 
    def sizeOfSet(self,i):
        return self.setSize[self.findSet(i)]
 
    def getSetCount(self):
        return self.setCount
    
    def sumOfSet(self,i):
        return self.setSum[self.findSet(i)]
    
    def minOfSet(self,i):
        return self.setMin[self.findSet(i)]

# Now , we will have to change the max_subset_sum array to min_subset_sum array.
# We will have to change the curr_sum variable to curr_min variable.

min_subset_sum = [0]
curr_min = 0
dsu = DSU(n)
for index in constructing_order:
    dsu.makeSet(index,arr_values[index])
    array_state[index] = 1
    if index > 0 and array_state[index-1]:
        dsu.union(index-1,index)
    if index < n-1 and array_state[index+1]:
        dsu.union(index,index+1)
    
    curr_min = min(dsu.minOfSet(index),curr_min)
    min_subset_sum.append(curr_min)

# Now , we will have to print the answer.

min_subset_sum.reverse()
min_subset_sum.pop(0)
for ele in min_subset_sum:
    print(ele)


