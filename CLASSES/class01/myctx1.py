
class MyDecor:
    def __enter__(self):
        print("Entered a wonderful technicolor world. Build it up")
    
    def __exit__(self,*args):
        ## *args hold the exception arg if needed
        print("...exiting this wonderful world. Tear it down.")
        