import mysql.connector

class Database:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="qwerty123",
            database="final_year_db"
        )

    def close(self):
        self.cnx.close()

    # def addViolation(self, number_plate):
    #     print('Adding violation to database')
    #     print(number_plate)
    #     cursor = self.cnx.cursor()
    #     q1 = 'SELECT violations FROM Violations WHERE number_plate = %s'
    #     cursor.execute(q1, (number_plate,))
    #     result = cursor.fetchall()
    #     if len(result) == 0:
    #         q2 = 'INSERT INTO Violations (number_plate, violations) VALUES (%s, 1)'
    #         cursor.execute(q2, (number_plate,))
    #     else:
    #         q3 = 'UPDATE Violations SET violations = violations + 1 WHERE number_plate = %s'
    #         cursor.execute(q3, (number_plate,))
    #     self.cnx.commit()
    #     cursor.close()
        
    def addViolation(self, number_plate, proof):
        print("Adding Violation to database")
        print(number_plate)
        cursor = self.cnx.cursor()
        query = 'INSERT INTO Violations (number_plate, timestamp, proof) VALUES (%s, NOW(), %s)'
        cursor.execute(query, (number_plate, proof))
        self.cnx.commit()
        cursor.close()
    
    def getViolations(self, number_plate):
        cursor = self.cnx.cursor()
        query = 'SELECT * FROM Violations WHERE number_plate = %s'
        cursor.execute(query, (number_plate,))
        result = cursor.fetchall()
        cursor.close()
        return result
    