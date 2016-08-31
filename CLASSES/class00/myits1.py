
"""Let's make an iterator"""
class Reverse(object):
    """Iterator class for looping over a sequence backwards"""
    def __init__(self,data):
        self.data = data
        self.index = len(data)
        
    def __iter__(self):
        #this is a required of an iterating class
        return self
    
    def __next__(self):
        #we got to the front of the array
        if self.index == 0:
            raise StopIteration
            
        self.index = self.index - 1
        return self.data[self.index]
    