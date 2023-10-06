import pyodbc

connectionString = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=MIS;DATABASE=qastore;Trusted_Connection=yes'

newtable = """
CREATE TABLE Cars(
    Manufacturer NVARCHAR(30) PRIMARY KEY,
    Model NVARCHAR(30),
    Year INT,
    Engine size NVARCHAR(30),
    Engine NVARCHAR(30)
    );
    """

conn = pyodbc.connect(connectionString)
cur = conn.cursor()
cur.execute(newtable)

conn.commit()
conn.close()
