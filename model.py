from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Set



class Answer:
    aid1: str
    aid2: str

class DecisionLine:
    dec1: str
    dec2: str
    dec3: str
  

class Question:
    qid1: str
    qid2: str
    
   
    def eval_input(self, qid1, qid2, dec1, dec2, dec3, aid1, aid2):
        if qid1 == aid2:
            print(qid2)
            if qid2 == aid1:
               return(dec2)
            elif qid2 == aid2:
                return(dec3)
        elif qid1 == aid1:
            return(dec1)
    
 
    

    
        
       
   
        
        


        
    












      
