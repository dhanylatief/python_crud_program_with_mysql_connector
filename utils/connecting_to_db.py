import mysql.connector, pandas as pd
def log_in(file_path, user_input, password_input):
    df = pd.read_csv(file_path)
    return (df.isin([user_input]).any().any() and df.isin([password_input]).any().any())

def connection_to_db(db:str, username:str, password:str):
    """Connect to MySQL Database
    """
    try:
        if log_in(file_path, user_input, password_input):
            conn = mysql.connector.connect(host="localhost",
                                           user="root", #MySQL user
                                           password="19Mei1995", #MySQL password
                                           database=db)
            print("\nConnected to database")
            return conn
        else:
            print("\nInvalid input")
            exit()
    except Exception as e:
        print(f"Error connecting to database: {e}")


def exec_query(conn:object, query:str):
    """Executing query

    Args:
        conn (object): MySQL Connector
        query (str): Query

    Returns:
        _type_: _description_
    """
    # Creating access to database
    mycursor = conn.cursor()

    # Execute query
    mycursor.execute(query)

    # Fetch data
    return mycursor.fetchall(), mycursor.column_names

user_data = pd.read_excel(r'H:\Purwadhika Les2an\Programming Bootcamp\Modul 2 Data Anal\DATA ANALYSIS - DAY 18\00. Dataset\Sample - Superstore.xls')

print("Log in")
file_path = r"H:\Purwadhika Les2an\Programming Bootcamp\Capstone Project with SQL\python_crud_program_hospital_patients\utils\User_List.csv"
user_input = input("Username: ")
password_input = input("Password: ")
    
conn = connection_to_db("ophthalmology_patients",user_input,password_input)