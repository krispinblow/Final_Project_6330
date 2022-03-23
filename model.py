




class Decision:
    decisionID1: str
    decisionID2: str
    decisionID3: str
    decisionID4: str
    qID1: str
    qID2: str
    qID3: str
    qID4: str
    qID5: str
    qID6: str
    qID7: str
    qID8: str
    qID9: str
    answer1: str
    answer2: str

class Questions:
    def __init__(self, qID1:str, qID2:str, answer1:str, answer2: str):
        self.qID1 = qID1
        self.qID2 = qID2       
        self.answer1 = answer1
        self.answer2 = answer2
        
        
        
    def evaluation(self):
        while True:
            if self.qID1 == self.answer1:
                print(Decision.decisionID1)
                break
            elif self.qID1 == self.answer2:
                print("Continue")
            if self.qID2 == self.answer1:
                print("Continue to question 3")
            elif self.qID2 == self.answer2:
                print("Continue to question 4")
                break
        
    
# def evaluate_questions():
#     while True:
#         qID1 == answer1
#         print(Decision.decisionID1)
        
    












      
                  
            