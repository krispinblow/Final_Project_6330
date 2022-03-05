

OPTIONS1 = ['during class time', 'before/after school or during non-instructional time']
OPTIONS2 = ['Elementary', 'Secondary']

class TeacherchoiceSimulation:
    def __init__(self):
        self.teacher_choice = None
    
    def get_teacher_choice_1(self):
        choice_number = int(input('When will the meetings be held?\nEnter the number of your choice: '))
        self.teacher_choice = OPTIONS1[choice_number]
    
    def print_options(self):
        print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(OPTIONS1)))
        
    
    def print_choices(self):
        print(f'You chose {self.teacher_choice}.')
    
    def print_result(self):
        if self.teacher_choice == 'during class time':
            print(f'This is a campus activity.')
        elif self.teacher_choice == 'before/after school or during non-instructional time':
            print(f'This may be a student activity. Please continue...')
    
    def get_teacher_choice_2(self):
        choice_number = int(input('Elementary or Secondary Level?\nEnter the number of your choice: '))
        self.teacher_choice = OPTIONS2[choice_number - 1]
    
    def print_options_2(self):
        print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(OPTIONS2)))
    
    def simulate(self):
        self.print_options()
        self.get_teacher_choice_1()
        self.print_choices()
        self.print_result()
        self.get_teacher_choice_2()
        self.print_options_2()

TCS = TeacherchoiceSimulation()
TCS.simulate()