import mysql.connector
import tabulate
from utils import connecting_to_db 
def edit_patient(patient_data: dict):
    """Function for updating data
    """
    try:
        read_query = f"""SELECT p.patientid, p.patient_name, qd.waitingtime, qd.examtime, qd.caretime, qd.subspecialty, qd.insurance 
        FROM patient p JOIN queue q ON p.patientid = q.patientid JOIN queuedetail qd ON q.registrationid = qd.registrationid;"""
        data, column_names = connecting_to_db.exec_query(connecting_to_db.conn, read_query)
        print(tabulate.tabulate(data, headers = column_names, tablefmt = "fancy_grid"))
        id_edited = input("Enter patient ID of the patient you want to edit (type C to cancel): ")
        if id_edited.upper() == "C":
            print("Returning to main menu.")
        else:
            new_name = input("Enter new patient name: ")
            new_waiting_time = int(input("Enter waiting time: "))
            new_exam_time = int(input("Enter exam time: "))
            new_subspecialty = input("Enter subspecialty: ")
            new_insurance = input("Enter insurance type: ")
            edit_query_name = f"UPDATE patient SET patient_name = '{new_name}' WHERE patientid = {id_edited}"
            connecting_to_db.exec_query(connecting_to_db.conn, edit_query_name)
            edit_query_detail = f'''UPDATE 
                                    queuedetail qd JOIN queue q ON q.registrationid = qd.registrationid 
                                    JOIN patient p ON p.patientid = q.patientid 
                                    SET 
                                    subspecialty = '{new_subspecialty}', 
                                    waitingtime = '{new_waiting_time}', 
                                    examtime = '{new_exam_time}', 
                                    caretime = '{new_waiting_time + new_exam_time}', 
                                    insurance = '{new_insurance}' 
                                    WHERE p.patientid = {id_edited};'''
            connecting_to_db.exec_query(connecting_to_db.conn, edit_query_detail)
            read_query = f"""SELECT p.patientid, p.patient_name, qd.waitingtime, qd.examtime, qd.caretime, qd.subspecialty, qd.insurance 
            FROM patient p JOIN queue q ON p.patientid = q.patientid JOIN queuedetail qd ON q.registrationid = qd.registrationid WHERE p.patientid = {id_edited};"""
            edited_data, column_names = connecting_to_db.exec_query(connecting_to_db.conn, read_query)
            print(tabulate.tabulate(edited_data, headers = column_names, tablefmt = "fancy_grid"))
            confirm_edit_patient = input("Is the data correct (Y/N)? ")
            if confirm_edit_patient.upper() == "Y":
                connecting_to_db.conn.commit()
                print("Patient data edited.")
                input("Press enter to return to main menu.")
            elif confirm_edit_patient.upper() == "N":
                print("Patient data not edited.")
                input("Press enter to return to main menu.")
            else:
                print("Invalid entry")
    except Exception:
            print("Input not recognized")
    return