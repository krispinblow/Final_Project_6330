#!/usr/bin/env python

import os
from collections import OrderedDict

import commands


def print_evaluations(evaluations):
    for evaluate in evaluations:
        print('\t'.join(
            str(field) if field else ''
            for field in evaluate
        ))


class Question:
    def __init__(self, name, command, prep_call=None):
        self.name = name  # <1>
        self.command = command  # <2>
        self.prep_call = prep_call  # <3>

    def _handle_message(self, message):
        if isinstance(message, list):
            print_evaluations(message)
        else:
            print(message)

    def choose(self):  # <4>
        data = self.prep_call() if self.prep_call else None  # <5>
        message = self.command.execute(data) if data else self.command.execute()  # <6>
        self._handle_message(message)

    def __str__(self):  # <7>
        return self.name


def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def print_questions(questions):
    for shortcut, question in questions.items():
        print(f'({shortcut}) {question}')
    print()


def question_choice_is_valid(choice, questions):
    return choice in questions or choice.upper() in questions  # <1>


def get_question_choice(questions):
    choice = input('Choose an option: ')  # <2>
    while not question_choice_is_valid(choice, questions):  # <3>
        print('Invalid choice')
        choice = input('Choose an option: ')
    return questions[choice.upper()]  # <4>


def get_user_input(label, required=True):  # <1>
    value = input(f'{label}: ') or None  # <2>
    while required and not value:  # <3>
        value = input(f'{label}: ') or None
    return value


def get_new_evaluate_data():  # <4>
    return {
        'name': get_user_input('Name'),
    }

'''
def get_bookmark_id_for_deletion():  # <6>
    return get_user_input('Enter a bookmark ID to delete')'''


def loop():  # <1>
    clear_screen()

    questions = OrderedDict({
        'A': Question('When will meetings be held?  During class?', commands.CampusActivityCommand(), prep_call=get_new_evaluate_data),
        'B': Question('When will meetings be held? After School?', commands.StudentActivityCommand(), prep_call=get_new_evaluate_data),
        'Q': Question('Quit', commands.QuitCommand()),
    })
    print_questions(questions)

    chosen_question = get_question_choice(questions)
    clear_screen()
    chosen_question.choose()

    _ = input('Press ENTER to return to menu')  # <2>


if __name__ == '__main__':
    commands.CreateEvaluateTableCommand().execute()

    while True:  # <3>
        loop()


def for_listings_only():
    questions = {
        'A': Question('When will meetings be held?  During class?', commands.AddEvaluateCommand()),
        'B': Question('When will meetings be held? After School?', commands.ListEvaluatesCommand()),
        'Q': Question('Quit', commands.QuitCommand()),
    }
    print_questions(questions)


'''
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
  

class evaluate:
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
            break '''
    

    
        
       
   
        
        


        
    












      
