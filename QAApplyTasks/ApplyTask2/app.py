import mysql.connector
from mysql.connector import Error

######################################################### CONNECTION FUNCTION #######################################################

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("You have successfully connected to the Car Warehouse")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("localhost", "root", "password", "projectCars")

######################################################### CREATE FUNCTION #########################################################

def createEntry(connection):
    cursor = connection.cursor()
    try:
        # Prompt user for car details
        crManufacturer = input("Enter the manufacturer: ").capitalize()
        crModel = input("Enter the model: ").capitalize()
        crYear = input("Enter the year: ")
        crEngine = input("Enter the engine type (e.g., V6, I4): ").upper()
        crEngine_size = input("Enter the engine size (in liters, e.g., 2.0L): ")
        crDrivetrain = input("Enter the drivetrain (e.g., FWD, AWD, RWD): ").upper()
        crFuel_type = input("Enter the fuel type (e.g., Petrol, Diesel): ").capitalize()
        crName = input("Enter your name: ").capitalize()

        # SQL query to insert data
        query = """
        INSERT INTO Cars (Manufacturer, Model, Year, Engine, Engine_Size, Drivetrain, Fuel_Type, Name)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """

        # Execute the query
        cursor.execute(query, (crManufacturer, crModel, crYear, crEngine, crEngine_size, crDrivetrain, crFuel_type, crName))
        connection.commit()
        print("Car data inserted successfully")

    except Error as e:
        print(f"The error '{e}' occurred")
        connection.rollback()  # rollback on error

    finally:
        cursor.close()

######################################################### READ FUNCTION ######################################################### 

def readEntry(connection, name):
    cursor = connection.cursor()
    query = "SELECT * FROM Cars WHERE name = %s;"
    try:
        cursor.execute(query, (name,))
        results = cursor.fetchall()
        if results:
            print(f"Here are {name}'s cars: ")
            for row in results:
                print(row)
        else:
            print(f"No cars found for {name}")
    except Error as e:
        print(f"The error '{e}' occurred")

######################################################### UPDATE FUNCTION ######################################################### 

def updateEntry(connection):
    cursor = connection.cursor()
    try:
        # User specifies the car to update
        name = input("Enter your name: ").capitalize()
        manufacturer = input("Enter the manufacturer of the car to update: ").capitalize()
        model = input("Enter the model of the car to update: ").capitalize()

        # Options for user to update
        print("What would you like to update?")
        print("1. Year")
        print("2. Engine")
        print("3. Engine Size")
        print("4. Drivetrain")
        print("5. Fuel Type")
        print("Enter all numbers you want to update separated by comma (e.g., 1,3,5): ")
        choices = input().split(',')

        fields = ["Year", "Engine", "Engine_Size", "Drivetrain", "Fuel_Type"]
        updates = []
        params = []

        # Collect updates based on user choices
        for choice in choices:
            i = int(choice.strip()) - 1  # Adjust index for zero-based Python indexing
            field = fields[i]
            new_value = input(f"Enter new {field}: ")
            if field == "Engine" or field == "Drivetrain":
                new_value = new_value.upper()  # Assuming these should be uppercase
            updates.append(f"{field} = %s")
            params.append(new_value)

        params.extend([manufacturer, model, name])  # Add identifiers for the WHERE clause

        # SQL query to update data
        update_query = f"UPDATE Cars SET {', '.join(updates)} WHERE Manufacturer = %s AND Model = %s AND Name = %s;"
        
        # Execute the query
        cursor.execute(update_query, params)
        connection.commit()

        if cursor.rowcount > 0:
            print("Car data updated successfully")
        else:
            print("No car found with the specified manufacturer and model or no data changed.")

    except Error as e:
        print(f"The error '{e}' occurred")
        connection.rollback()  # Rollback on error

    finally:
        cursor.close()

######################################################### DELETE FUNCTION ######################################################### 

def deleteEntry(connection):
    try:
        # Get user input
        name = input("Enter your name: ").strip()
        manufacturer = input("Enter the car's manufacturer: ").strip().capitalize()
        model = input("Enter the car's model: ").strip().capitalize()

        # Check if the entry exists and display it
        cursor = connection.cursor()
        search_query = """
        SELECT * FROM Cars
        WHERE Name = %s AND Manufacturer = %s AND Model = %s;
        """
        cursor.execute(search_query, (name, manufacturer, model))
        result = cursor.fetchone()
        
        if result:
            # Display the result
            print("Found Entry:")
            print(f"Name: {result[7]} \nManufacturer: {result[0]} \nModel: {result[1]} \nYear: {result[2]} \nEngine: {result[3]}\nEngine Size: {result[4]}\nDrivetrain: {result[5]}\nFuel Type: {result[6]}")
            
            # Confirm deletion
            confirm = input(f"Are you sure you want to delete {name}'s {manufacturer} {model}? Please note once an entry is deleted, it cannot be reverted. (yes/no): ").lower()
            if confirm == 'yes':
                delete_query = """
                DELETE FROM Cars
                WHERE Name = %s AND Manufacturer = %s AND Model = %s;
                """
                cursor.execute(delete_query, (name, manufacturer, model))
                connection.commit()
                if cursor.rowcount > 0:
                    print("The car entry has been deleted.")
                else:
                    print("Error: The car could not be deleted.")
            else:
                print("Deletion cancelled.")
        else:
            print("No entry found matching the criteria.")

    except Error as e:
        print(f"Error occurred: {e}")
        connection.rollback()  # Rollback in case of any error during the delete operation
    finally:
        if 'cursor' in locals():
            cursor.close()

######################################################### APP FUNCTION ######################################################### 
while True:
    print("Welcome to the Car Warehouse! What would you like to do? \n1) Register a new car \n2) Search for an existing car \n3) Update an existing car \n4) Delete an existing car \n5) I want to leave" )
    answer = input("Please enter either 1, 2, 3, 4 or 5: ")

    if answer == "1":
        print("You're registering a new car.")
        createEntry(connection)
        print("Thanks for using our service, we hope to see you soon!")
        break
    elif answer == "2":
        print("You're searching for an existing car.")
        name = input("Enter your name: ")
        name = name.capitalize()
        readEntry(connection, name)
        print("Thanks for using our service, we hope to see you soon!")
        break
    elif answer == "3":
        print("You're updating an existing car.")
        updateEntry(connection)
        print("Thanks for using our service, we hope to see you soon!")
        break
    elif answer == "4":
        print("You're deleting an existing car from our database.")
        deleteEntry(connection)
        print("Thanks for using our service, we hope to see you soon!")
        break
    elif answer == "5":
        print("Thanks for using our service, we hope to see you soon!")
        break
    else:
        print("Sorry, I didn't understand. Let's try again")






