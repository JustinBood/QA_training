import pyodbc

connectionString = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'

#newtable = """
#CREATE TABLE Cars(
#    Manufacturer NVARCHAR(30) PRIMARY KEY,
#    Model NVARCHAR(30),
#    Year INT,
#    [Engine size] NVARCHAR(30),
#    Engine NVARCHAR(30)
#    );
#    """



try:
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()

    insert_sql = """
    INSERT INTO Cars  (Manufacturer, Model, Year, [Engine Size], Engine)
    VALUES (?, ?, ?, ?, ?);"""
    data = ('Audi', 'RS6', 2023, '4.0L', 'V8')

#    read  = "SELECT * FROM Cars;"
    cur.execute(insert_sql, data)

# row = cur.fetchall()
#  for r in row:
#       print(r)

    conn.commit()
    conn.close()
    print("data inserted")
except pyodbc.Error as ex:
    print("SQL Error:", ex)
except Exception as w:
    print("General Error:", w)
finally:
    try:
        cur.close()
        conn.close()
    except:
        pass