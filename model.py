from connection import *

class Model(Connection):
    def __init__(self):
        super().__init__()

    # Method demonstrating Inheritance
    def select(self):
        try:
            # Establish a connection and create a cursor
            cur = self.conn().cursor()

            # Execute a SELECT query
            cur.execute("SELECT * FROM producto")

            # Return the fetched data
            return cur.fetchall()
        except sqlite3.Error as err:
            # Exception handling in case of an error
            print(f"Problem encountered while retrieving products: {err}")
        finally:
            # Close the connection in the finally block to ensure it is closed even if an exception occurs
            self.con.close()

    # Method demonstrating Inheritance and Encapsulation
    def add(self, *args):
        try:
            # Establish a connection and create a cursor
            con = self.conn()
            cur = con.cursor()

            # Execute an INSERT query with parameters
            cur.execute("INSERT INTO producto(product_name, product_quantity, product_price) VALUES(?,?,?)", args)

            # Commit the changes to the database
            con.commit()

            # Return a success message
            return "Product Insertion was Successful"
        except sqlite3.Error as err:
            # Exception handling in case of an error
            print(f"Error while inserting data: {err}")
        finally:
            # Close the connection in the finally block to ensure it is closed even if an exception occurs
            self.con.close()

    # Method demonstrating Inheritance and Encapsulation
    def update(self, *args):
        try:
            # Establish a connection and create a cursor
            con = self.conn()
            cur = con.cursor()

            # Execute an UPDATE query with parameters
            cur.execute("UPDATE producto SET product_name = ?, product_quantity = ?, product_price = ? WHERE product_code = ?", args)

            # Commit the changes to the database
            con.commit()

            # Return a success message
            return "Product update was successful"
        except sqlite3.Error as err:
            # Exception handling in case of an error
            print(f"A problem encountered while updating: {err}")
        finally:
            # Close the connection in the finally block to ensure it is closed even if an exception occurs
            self.con.close()

    # Method demonstrating Inheritance and Encapsulation
    def delete(self, *args):
        try:
            # Establish a connection and create a cursor
            con = self.conn()
            cur = con.cursor()

            # Execute a DELETE query with parameters
            cur.execute("DELETE FROM producto WHERE product_code = ?", args)

            # Commit the changes to the database
            con.commit()

            # Return a success message
            return "Product delete was successful"
        except sqlite3.Error as err:
            # Exception handling in case of an error
            print(f"Problem encountered while deleting the product: {err}")
        finally:
            # Close the connection in the finally block to ensure it is closed even if an exception occurs
            self.con.close()


# usage to create a new database with a table
if __name__ == "__main__":
    # Create an instance of the Connection class
    db_connection = Connection()

    # Specify the table name and columns for the new database
    table_name = "producto"
    columns = ["product_code INTEGER PRIMARY KEY",
               "product_name TEXT",
               "product_quantity INTEGER",
               "product_price REAL"]

    try:
        # Call the create_database method to create a new table
        result = db_connection.create_database(table_name, columns)
        print(result)
    except sqlite3.Error as err:
        print(f"Error during database creation: {err}")
