
from dataclasses import dataclass
from typing import Set 
import string



@dataclass
class DecisionLine:
    d_id : str
    dname: str
    #doutput: str

class AnswerLine:
    aid: str
    answers: str
    
    
    
    """def __init__(self) -> None:
        self.raw_text: str = None
        self.Questions = None
        pass"""
    
class Question:
    def __init__(self, qid:str, questions:str, aid:str):
        self.qid = qid
        self.questions = questions
        self.aid = aid
        #self.d_id = d_id
        self._evaluate = set() # type Set[DecisionLine]
    
    def evaluate(self, line: DecisionLine):
       if self.qid == "1" and self.aid == "1":
        return  True
        
       
   
        
        


        
    












      
