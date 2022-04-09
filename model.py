#!/usr/bin/env python

import os
from collections import OrderedDict

from services.commands import *



class Question:
    def __init__(self, name, command, prep_call=None):
        self.name = name  
        self.command = command  
        self.prep_call = prep_call 

    def choose(self):  
        data = self.prep_call() if self.prep_call else None  
        message = self.command.execute(data) if data else self.command.execute()  
        print(message)

    def __str__(self):  
        return self.name


def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def print_questions(questions):
    for shortcut, question in questions.items():
        print(f'({shortcut}) {question}')
    print()


def question_choice_is_valid(choice, questions):
    return choice in questions or choice.upper() in questions  


def get_question_choice(questions):
    choice = input('Choose an option: ')  
    while not question_choice_is_valid(choice, questions):  
        print('Invalid choice')
        choice = input('Choose an option: ')
    return questions[choice.upper()] 


def get_user_input(label, required=True):  
    value = input(f'{label}: ') or None  
    while required and not value:  
        value = input(f'{label}: ') or None
    return value


def get_new_evaluate_data():  # <4>
    return {
        'teacher_name': get_user_input('Teacher_Name'),
        'club_name': get_user_input('Club_Name'),
    }

def get_new_evaluate_info():
    question_id = get_user_input("Enter a question ID to edit")
    field = get_user_input("Choose a value to edit (teacher_name, club_name)")
    new_value = get_user_input(f"Enter the new value for {field}")
    return {
        "id": question_id,
        "update": {field: new_value},
    }



def loop():  # <1>
    clear_screen()

    questions = OrderedDict({
        'A': Question('When will meetings be held?  During class?', CampusActivityCommand(), prep_call=get_new_evaluate_data),
        'B': Question('When will meetings be held? After School?', StudentActivityCommand(), prep_call=get_new_evaluate_data),
        'E': Question("Edit a question", EditEvaluateCommand(), prep_call=get_new_evaluate_info),
        'Q': Question('Quit', QuitCommand()),
    })
    print_questions(questions)

    chosen_question = get_question_choice(questions)
    clear_screen()
    chosen_question.choose()

    _ = input('Press ENTER to return to menu')  # <2>


if __name__ == '__main__':
    CreateEvaluateTableCommand().execute()

    while True:  
        loop()



