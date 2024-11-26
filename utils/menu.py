from . import connecting_to_db
import os
def crud_menu():
    os.system('cls')
    print(f'''\nWelcome to Ophthalmology Patient Database, {connecting_to_db.user_input}!
---------------------------
1. View Patient Database
2. Add a New Patient
3. Edit a Patient Data
4. Delete a Patient Data
5. Exit the Program
---------------------------
''')
    return 
    
# crud_menu() -> use this command to call the crud menu