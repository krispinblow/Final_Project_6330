The repository is named Final and each branch are the individual assignments.

github https://github.com/krispinblow/Final_Project_6330.git

My domain model is based on a decision tree with responses stored in a database.

Assignment 6
    Step 1: the domain model
    Step 2: the repository pattern
    Step 3: the service layer


I have reworked my domain model. It is a decision tree. 

I have a question class that has a predetermined set of questions and answers. The answer chosen will be evaluated. The evaluation can be directed to ask another question or give a decision. There is a decision class with four outcomes.

I worked to get the model.py working. There are nested functions that I will extract. Next is the database. I will be using Sqlite.

I scraped my orginal model.py and reworked it. I don't need to code the details only define each class and their functions. I test the functions/methods. I have a class for Decisions and Questions. The questions will be evaluated based on the respective answer.