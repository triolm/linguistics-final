
import random

class NGram:
    def __init__(self, str):
        self.str = str;
        self.children = {};
    
    def __str__(self):
        return self.str
    
    def __repr__(self):
        return self.str

    def add(self, child):
        if(self.children.get(child)):
            self.children.get(child)["weight"] += 1;
            return;
        self.children[child] = {"child":child, "weight":1}

    def get(self, str):
        return dict.get(str)
    
    def getFirst(self):
        for i in self.children:
            return i;
        
    def getRand(self):
        total = 0;
        for i in self.children:
            total += self.children[i].get("weight")
        
        rand = random.randint(0, total)
        randSum = 0
        for i in self.children:
            randSum += self.children[i].get("weight")
            if(randSum >= rand):
                return i;

        return self.getFirst()