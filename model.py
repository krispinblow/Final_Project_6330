from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Set


choices = {
    'A': 'answer1',
    'B': 'answer2',
}

#print(f'{choice} is for {choices[choice]}')



class DecisionLine:
    dec1 = "Campus Activity"
    dec2 = "Student Activity"
    dec3 = "Not an Activity Fund"
  

class Question:
    qid1: str
    qid2: str
    
   
    '''def eval_input(self, qid1, qid2, dec1, dec2, dec3, aid1, aid2):
        if qid1 == aid2:
            print(qid2)
            if qid2 == aid1:
               return(dec2)
            elif qid2 == aid2:
                return(dec3)
        elif qid1 == aid1:
            return(dec1)'''
    
while True:
    qid1 = input(f'When are meetings held? {choices}:')
    if qid1 == "A":
        print(DecisionLine.dec1)
        break
    elif qid1 == "B":
        qid2 = input(f'Elementary or Secondary? {choices}')
        if qid2 == "A":
            print(DecisionLine.dec2)
            break
        elif qid2 == "B":
            print(DecisionLine.dec3)
            break 
    

    
        
       
   
        
        


        
    












      
