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
        'A': Question('When will meetings be held?  During class?', commands.CampusActivityCommand(), prep_call=get_new_evaluate_data),
        'B': Question('When will meetings be held? After School?', commands.StudentActivityCommand(), prep_call=get_new_evaluate_data),
        'E': Question("Edit a question", commands.EditBookmarkCommand(), prep_call=get_new_evaluate_info),
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




