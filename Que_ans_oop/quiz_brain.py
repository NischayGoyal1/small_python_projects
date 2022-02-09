class QBank:
    def __init__(self,list) :
        self.bank=list
        self.qno=0
        self.score=0

    def eq(self):
        return self.qno<len(self.bank)
    def nextq(self):
        question=self.bank[self.qno]
        self.qno+=1
        usera=input((f"{question.q} ? (TRUE/FALSE)"))
        self.check_ans(usera,question.a)

    def check_ans(self,usera,aans):
        if usera==aans:
            self.score+=1
            print(f"Coreect ans \n your current score is {self.score}/{self.qno}")
        else:
            print(f"Wrong ans \n your current score is {self.score}/{self.qno}")
            



        