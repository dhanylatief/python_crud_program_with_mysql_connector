# ===================================
# [Ophthalmology Patient Database]
# ===================================
# Developed by. [Muhammad Dhany Latief]
# JCDS - [JCDS 0412]
import mysql.connector
import tabulate
import os
from utils import menu, create, read, update, delete
from utils import connecting_to_db
# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    menu.crud_menu()
    input_user = input("Insert option number (1-5): ")
    if input_user == "1":
        os.system('cls')
        read.show_patientdb(database)
    elif input_user == "2":
        os.system('cls')
        create.new_patient_data(database)
    elif input_user == "3":
        os.system('cls')
        update.edit_patient(database)
    elif input_user == "4":
        os.system('cls')
        delete.remove_patient(database)
    elif input_user == "5":
        os.system('cls')
        print("Exiting...")
        exit()
    else:
        print("Invalid Input.")


if __name__ == "__main__":
    database = "ophthalmology_patients"
    while True:   
        main()
    else:
        print("Invalid input.")
        exit()