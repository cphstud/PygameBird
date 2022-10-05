class Gamekeeper:
    # level
    # counter
    # liv

    def __init__(self,numoflives):
        self.level=1
        self.counter=1
        self.liv=numoflives
        self.factor=1

    def modifscore(self):
        self.counter = self.counter + self.factor

    def modiflevel(self):
        self.level = self.level + self.factor

    def modifliv(self):
        self.liv = self.liv - self.factor

    def gameover(self):
        retval=False
        if self.liv == 0:
            retval=True
        return(retval)
