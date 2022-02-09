from data import*
from question_model import*
from quiz_brain import*

qbnak=[]
for i in range(len(question_data)):
    m=Que(question_data[i]["text"],question_data[i]["answer"])
    qbnak.append(m)
    m.lss=qbnak

k=QBank(qbnak)
while k.eq():
    k.nextq()


print(f"wowho you have completed the quiz \n your final score is {k.score}/{k.qno}  ")





    