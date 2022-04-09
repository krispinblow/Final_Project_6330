import sys
from datetime import datetime

from database import DatabaseManager

db = DatabaseManager('evaluates.db')  # <1>


class CreateEvaluateTableCommand:
    def execute(self):  # <2>
        db.create_table('evaluates', {  # <3>
            'id': 'integer primary key autoincrement',
            'teacher_name': 'text not null',
            'club_name': 'text not null',
            'date_added': 'text not null',
        })


class CampusActivityCommand:
    def execute(self, data):
        data['date_added'] = datetime.utcnow().isoformat()  # <1>
        db.add('evaluates', data)  # <2>
        return 'You chose during classtime. This is a campus activity!'  # <3>
                     

class StudentActivityCommand:
     def execute(self, data):
        data['date_added'] = datetime.utcnow().isoformat()  # <1>
        db.add('evaluates', data)  # <2>
        return 'You chose after school. This is a student activity!'  # <3>
    
class QuitCommand:
    def execute(self):
        sys.exit()  # <1>  