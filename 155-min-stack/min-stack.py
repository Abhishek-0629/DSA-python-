class MinStack:

    def __init__(self):
        self.item=[]
        
        

    def push(self, value: int) -> None:
        if len(self.item)==0:
            self.item.append([value,value])
        else:
            mini=min([self.item[-1][1],value])
            self.item.append([value,mini])




    def pop(self) -> None:
        if self.item:
            self.item.pop()
        

    def top(self) -> int:
        return self.item[-1][0]
        

    def getMin(self) -> int:
        if len(self.item)==0:
            return 0
        return self.item[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()