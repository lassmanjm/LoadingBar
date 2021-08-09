from datetime import datetime
class LoadingBar:
    """
    Loading bar object. 

    Usage:
        Initialize with number of iterations. Execute self.load() every iteration. Execute self.end()
        after the final iteration.
    """

    def __init__(self,n,barLength=40,give_ETA=True):
        self.i=0
        self.n=int(n)
        self.barLength=int(barLength)
        self.barPix=100/self.barLength
        self.startTime=datetime.now().replace(microsecond=0)
        self.give_ETA=give_ETA
    def setIter(self,i):
        self.i=i
    def reset(self):
        self.i=0
    def load(self):
        if self.i==0:
            print('\n')
        perc=self.i/self.n*100
        numPlus=int(perc//self.barPix)
        if self.give_ETA==True:
            if self.i==0:
                ETA='N/A'
            else:
                ETA=str((self.time-self.startTime)*(self.n-self.i)/self.i).split('.')[0]
        if self.give_ETA==True:
            print('\r%i/%i ['%(self.i,self.n)+'+'*numPlus+'-'*(self.barLength-numPlus)+'] %.2f%% ETA: %s '%(perc,ETA),end='')
        else:
            print('\r%i/%i ['%(self.i,self.n)+'+'*numPlus+'-'*(self.barLength-numPlus)+'] %.2f%% '%(perc),end='')
        self.i+=1
        if self.give_ETA==True:
            self.time=datetime.now()
    def end(self):
        self.load()
        print('\n')
        self.reset()