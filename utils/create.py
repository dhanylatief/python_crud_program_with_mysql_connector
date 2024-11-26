import _mysql_connector
import tabulate
from utils import connecting_to_db
def new_patient_data(patient_data: dict):
    """Function for creating data
    """
    create_confirm = input("""\n1. Add new patient
2. Add a patient to queue
Select an option (1-2): """)
    if create_confirm.upper() == "1":
        try:
            patient_id = input("Enter patient ID (8 digits): ")
            name = input("Enter new patient name: ")
            waiting_time = int(input("Enter waiting time: "))
            exam_time = int(input("Enter exam time: "))
            subspecialty = input("Enter subspecialty: ")
            insurance = input("Enter insurance type: ")
            
            insert_patient_id = f"INSERT INTO patient(patientid, patient_name) VALUES ('{patient_id}', '{name}')"
            insert_patient_id_2 = f"INSERT INTO queue (patientid,registrationid,queuedate,queueat) VALUES ('{patient_id}','000','2018-09-01','00:00')"
            insert_detail = f'''INSERT INTO queuedetail (registrationid, subspecialty, waitingtime, examtime, caretime, insurance) VALUES
                                ('000','{subspecialty}','{waiting_time}','{exam_time}','{waiting_time+exam_time}','{insurance}')'''
            connecting_to_db.exec_query(connecting_to_db.conn, insert_patient_id)
            connecting_to_db.exec_query(connecting_to_db.conn, insert_patient_id_2)
            connecting_to_db.exec_query(connecting_to_db.conn, insert_detail)
            read_query = '''
                SELECT p.patientid, p.patient_name, qd.waitingtime, qd.examtime, qd.caretime, qd.subspecialty, qd.insurance 
                FROM patient p JOIN queue q ON p.patientid = q.patientid JOIN queuedetail qd ON q.registrationid = qd.registrationid;'''
            data, column_names = connecting_to_db.exec_query(connecting_to_db.conn, read_query)
            print(tabulate.tabulate(data, headers = column_names, tablefmt = "fancy_grid"))
            confirm_new_patient = input("Is the data correct (Y/N)? ")
            if confirm_new_patient.upper() == "Y":
                connecting_to_db.conn.commit()
                print("New patient added.")
                input("Press enter to return to main menu.")
            elif confirm_new_patient.upper() == "N":
                print("New patient not added.")
                input("Press enter to return to main menu.")
            else:
                print("Invalid entry")
        except Exception as e:
            print(f"Error Occured: {e}")
            input("Press enter to return to main menu.")
    elif create_confirm.upper() == "2":
        try:
            print("Feature under maintenance.")
            input("Press enter to return to main menu")
        except Exception as e:
            print(f"Error Occured: {e}")
            input("Press enter to return to main menu.")
    else:
        input("Invalid input. Press enter to return to main menu.")
    return 
