import threading

class PThread(threading.Thread):
    
    def __init__(self,val1,val2):
        threading.Thread.__init__(self)
        self.val1=val1
        self.data=""
        self.val2=val2
    
    def getData(self):
        return self.data

    def run(self):
        if int(self.val1)>int(self.val2):
            self.data=False
        else:
            self.data=True
