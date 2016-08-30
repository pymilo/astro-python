
class MyDecor1:
    
    def __init__(self,expression="None"):
        self.expression = expression
    def __enter__(self):
        print("Entered a wonderful technicolor world. Build it up") 
        return eval(self.expression)
    def __exit__(self,*args):
        print("...exiting this wonderful world. Tear it down.")