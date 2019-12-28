from PThread import PThread
class Lab02:

    def __init__(self):
        self.lists = [9,3,4,8]

    def noOfProcess(self):
        n= len(self.lists)
        return int(n*(n-1)/2)
    
    def install(self):
        Threads=[]
        for i in range(len(self.lists)):
            st=self.lists[i]
            for j in range(i+1,len(self.lists)):
                thread=PThread(st,self.lists[j])
                thread.start()
                if thread.getData()==False:
                    Threads.append(i)
                else:
                    Threads.append(j)
                    
        smallest=None
        for i in range(len(self.lists)):
            if i not in Threads:
                smallest=self.lists[i]
            
        print("Smallest Number is:"+str(smallest))

Lab02().install()