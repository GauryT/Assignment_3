import sqlite3

class Connection:
    def __init__(self):
        pass

    def conn(self):
        try:
            # Encapsulation: Database connection is encapsulated within the class
            self.con = sqlite3.connect('database/database.db')

            # Abstraction: The details of the database connection are abstracted from the user
            return self.con
        except sqlite3.Error as err:
            # Exception handling in case of a connection error
            print("Connection Failed")

    # Method for creating a new database with specified columns and table name
    def create_database(self, table_name, columns):
        try:
            # Establish a connection
            con = self.conn()
            cur = con.cursor()

            # Construct SQL query to create a new table
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
            cur.execute(query)

            # Commit the changes to the database
            con.commit()

            # Return a success message
            return f"Table '{table_name}' created successfully"
        except sqlite3.Error as err:
            # Exception handling in case of an error
            print(f"Error while creating table: {err}")
        finally:
            # Close the connection in the finally block to ensure it is closed even if an exception occurs
            self.con.close()



