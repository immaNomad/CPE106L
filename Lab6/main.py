import os
import pyodbc

def create_chinook_database():
    # Read the SQL script from the file
    with open('database.sql', 'r') as file:
        sql_code = file.read()

    # Get the connection details from environment variables
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_DATABASE')
    driver = os.getenv('DB_DRIVER')

    # Create the database connection
    conn_string = (
        f'DRIVER={driver};'
        f'SERVER={server};'
        f'DATABASE={database};'
        'Trusted_Connection=yes;'
    )
    conn = pyodbc.connect(conn_string)
    cursor = conn.cursor()

    try:
        # Execute the SQL script
        cursor.execute(sql_code)
        conn.commit()
        print("Chinook database created successfully.")
    except pyodbc.Error as e:
        print(f'Error creating the Chinook database: {e}')
    finally:
        # Close the database connection
        cursor.close()
        conn.close()

if __name__ == '__main__':
    create_chinook_database()
