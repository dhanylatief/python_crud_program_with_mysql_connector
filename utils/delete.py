import _mysql_connector
import tabulate
from utils import connecting_to_db
def remove_patient(patient_data: dict):
    """Function for deleting data
    """
    read_query = f"""SELECT p.patientid, p.patient_name, qd.waitingtime, qd.examtime, qd.caretime, qd.subspecialty, qd.insurance 
    FROM patient p JOIN queue q ON p.patientid = q.patientid JOIN queuedetail qd ON q.registrationid = qd.registrationid;"""
    data, column_names = connecting_to_db.exec_query(connecting_to_db.conn, read_query)
    print(tabulate.tabulate(data, headers = column_names, tablefmt = "fancy_grid"))
    id_del = input("Enter patient ID of the patient you want to delete (type C to cancel): ")
    if id_del.upper() == "C":
        print("Returning to main menu.")
    elif id_del.upper() == "ALL":
        del_all_confirm = input("Are you sure you want to delete all data? (Y/N): ")
        if del_all_confirm.upper() == "Y":
            del_all_query = f"""DELETE FROM patient"""
            connecting_to_db.exec_query(connecting_to_db.conn, del_all_query)
            print("Database purged.")
            input("Press enter to return to main menu.")
        elif del_all_confirm.upper() == "N":
            print("Returning to main menu.")
    else:
        try:
            del_query1 = f"""DELETE FROM patient WHERE patientid = '{id_del}'"""
            connecting_to_db.exec_query(connecting_to_db.conn, del_query1)
            read_query = f"""SELECT p.patientid, p.patient_name, qd.waitingtime, qd.examtime, qd.caretime, qd.subspecialty, qd.insurance 
                            FROM patient p JOIN queue q ON p.patientid = q.patientid JOIN queuedetail qd ON q.registrationid = qd.registrationid;"""
            data, column_names = connecting_to_db.exec_query(connecting_to_db.conn, read_query)
            print(tabulate.tabulate(data, headers = column_names, tablefmt = "fancy_grid"))
            confirm_del_patient = input("Are you sure (Y/N)? ")
            if confirm_del_patient.upper() == "Y":
                connecting_to_db.conn.commit()
                print("Patient data deleted.")
                input("Press enter to return to main menu.")
            elif confirm_del_patient.upper() == "N":
                print("Patient data not deleted.")
                input("Press enter to return to main menu.")
            else:
                print("Invalid entry")
        except Exception:
                print("Input not recognized")
    return