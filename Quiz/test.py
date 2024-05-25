import mysql.connector
from mysql.connector import errorcode

# Define connection parameters
config = {
    'user': 'root',
    'password': '2721',
    'host': 'localhost',
    'raise_on_warnings': True
}

# Database name you want to check and possibly create
database_name = 'quiz'
conn = mysql.connector.connect(**config)
cursor = conn.cursor()
try:
    # Establish connection to the MySQL server
    
    cursor = conn.cursor()

    # Check if database exists
    cursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
    result = cursor.fetchone()

    if result:
        print(f"Database '{database_name}' already exists.")
    else:
        # Create the database
        cursor.execute(f"CREATE DATABASE {database_name}")
        print(f"Database '{database_name}' created successfully.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
finally:
    # Close cursor and connection
    cursor.close()
    conn.close()
