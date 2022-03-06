

"""OPTIONS1 = ['during class time', 'before/after school or during non-instructional time']
#OPTIONS2 = ['Elementary', 'Secondary']

class TeacherchoiceSimulation:
    def __init__(self):
        self.teacher_choice = None
    
    def get_teacher_choice_1(self):
        choice_number = int(input('When will the meetings be held?\nEnter the number of your choice: '))
        self.teacher_choice = OPTIONS1[choice_numer]
    
    def print_options(self):
        print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(OPTIONS1)))
        
    
    def print_choices(self):
        print(f'You chose {self.teacher_choice}.')
    
    def print_result(self):
        if self.teacher_choice == 'during class time':
            print(f'This is a campus activity.')
        elif self.teacher_choice == 'before/after school or during non-instructional time':
            print(f'This may be a student activity. Please continue...')
    
    '''def get_teacher_choice_2(self):
        choice_number = int(input('Elementary or Secondary Level?\nEnter the number of your choice: '))
        self.teacher_choice_2 = OPTIONS2[choice_number]
    
    def print_options_2(self):
        print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(OPTIONS2)))'''
    
    def simulate(self):
        self.print_options()
        self.get_teacher_choice_1()
        self.print_choices()
        self.print_result()
        #self.get_teacher_choice_2()
        #self.print_options_2()

TCS = TeacherchoiceSimulation()
TCS.simulate()
 """
#from tabulate import tabulate
 
class Decision:
   
    decision1 = "This is a campus activty fund."
    decision2 = "This is a student activity fund."
    decision3 = "This is not activity funds."
    decision4 = "This is a student led group."
    '''decisions = [[1,"CA","This is a campus activity fund"],
            [2, "SA", "This is a student activity fund"],
            [3, "Not AF", "This is not an actifity fund"],
            [4, "Student Led", "This is a student led group"]]
    
    col_names = ["decisionID", "decisionName", "dOutput"] 
 
    print(tabulate(decisions, headers=col_names, tablefmt="grid", showindex="no"))'''
    
#OPTIONS1 = ['during class time', 'before/after school or during non-instructional time'] 
#OPTIONS2 = ['Elementary', 'Secondary']
 
class Questions:
    while True:
        qid1 = input("When will the meetings be held? \n 1) during class time \n 2) before/after school or non-instructional time \n: ")
        if qid1 == "1":
            print(Decision.decision1)
            break
        elif qid1 == "2":
            print("This may be a student activity. Please continue...") 
            
        
        qid2 = input("Elementary or Secondary Level? \n 1) Elementary \n 2) Secondary \n: ")
        if qid2 == "1":
            qid3 = input("STUCO? \n 1) Yes \n 2) No \n:")
            if qid3 == "1":
                print(Decision.decision2)
                break
            elif qid3 == "2":
               print(Decision.decision1)
               break
        elif qid2 == "2":
             print("This may be a student activity. Please continue...")
        
        qid4 = input("Who runs the meetings/makes decisions? \n 1) Sponsor/Teacher \n 2) Students/Members \n: ")
        if qid4 == "1":
             print(Decision.decision1)
             break
        elif qid4 == "2":
            print("This may be a student activity. Please continue...")
        
        qid5 = input("Documented minutes of each meeting? \n 1) Yes \n 2) No \n: ")
        if qid5 == "1":
            qid6 = input("Vote for Officers? \n 1) Yes \n 2) No \n: ")
            if qid6 == "1":
                qid7 = input("Monetary transactions? \n 1) Yes \n 2) No \n: ")
                if qid7 == "1":
                    qid8 = input("Open to the student body? \n 1) Yes \n 2) No \n: ")
                    if qid8 == "1":
                        qid9 = input("Curriculum based? \n 1) Yes \n 2) No \n: ")
                        if qid9 == "1":
                            print(Decision.decision2)
                            break
                        elif qid9 == "2":
                            print(Decision.decision4)
                            break
                    elif qid8 == "2":
                        print(Decision.decision1)
                        break
                elif qid7 == "2":
                    print(Decision.decision3)
                    break
            elif qid6 == "2":
                print(Decision.decision1)
                break
        elif qid5 == "2":
            print(Decision.decision1)
            break
           