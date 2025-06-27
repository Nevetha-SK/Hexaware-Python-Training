from dao.IHospitalService import IHospitalService
from entity.Appointment import Appointment
from util.DBConnUtil import getConnection
from exception.PatientNumberNotFoundException import PatientNumberNotFoundException

class HospitalServiceImpl(IHospitalService):

    def getAppointmentById(self, appointmentId):
        conn = getConnection()
        if conn is None:
            raise Exception("Database connection error.")
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Appointment WHERE appointmentId = ?", (appointmentId,))
            row = cursor.fetchone()
            if row:
                return Appointment(*row)
            else:
                raise Exception("Appointment not found.")
        finally:
            conn.close()

    def getAppointmentsForPatient(self, patientId):
        conn = getConnection()
        if conn is None:
            raise Exception("Database connection error.")
        try:
            cursor = conn.cursor()

            # ✅ Validate patient exists
            cursor.execute("SELECT * FROM Patient WHERE patientId = ?", (patientId,))
            patient = cursor.fetchone()
            if not patient:
                raise PatientNumberNotFoundException("Patient number not found in the database.")

            cursor.execute("SELECT * FROM Appointment WHERE patientId = ?", (patientId,))
            rows = cursor.fetchall()
            return [Appointment(*row) for row in rows]
        finally:
            conn.close()

    def getAppointmentsForDoctor(self, doctorId):
        conn = getConnection()
        if conn is None:
            raise Exception("Database connection error.")
        try:
            cursor = conn.cursor()

            # ✅ Validate doctor exists
            cursor.execute("SELECT * FROM Doctor WHERE doctorId = ?", (doctorId,))
            doctor = cursor.fetchone()
            if not doctor:
                raise Exception("Doctor ID not found in the database.")

            cursor.execute("SELECT * FROM Appointment WHERE doctorId = ?", (doctorId,))
            rows = cursor.fetchall()
            return [Appointment(*row) for row in rows]
        finally:
            conn.close()

    def scheduleAppointment(self, appointment):
        conn = getConnection()
        if conn is None:
            raise Exception("Database connection error.")
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Appointment (appointmentId, patientId, doctorId, appointmentDate, description) VALUES (?, ?, ?, ?, ?)",
                (appointment.getAppointmentId(), appointment.getPatientId(), appointment.getDoctorId(),
                 appointment.getAppointmentDate(), appointment.getDescription())
            )
            conn.commit()
            return True
        finally:
            conn.close()

    def updateAppointment(self, appointment):
        conn = getConnection()
        if conn is None:
            raise Exception("Database connection error.")
        try:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Appointment SET patientId=?, doctorId=?, appointmentDate=?, description=? WHERE appointmentId=?",
                (appointment.getPatientId(), appointment.getDoctorId(), appointment.getAppointmentDate(),
                 appointment.getDescription(), appointment.getAppointmentId())
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    def cancelAppointment(self, appointmentId):
        conn = getConnection()
        if conn is None:
            raise Exception("Database connection error.")
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Appointment WHERE appointmentId = ?", (appointmentId,))
            conn.commit()
            return cursor.rowcount > 0
        finally:
            conn.close()

    # ✅ Added: Get patient full name
    def getPatientNameById(self, patientId):
        conn = getConnection()
        if conn is None:
            raise Exception("Database connection error.")
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT firstName, lastName FROM Patient WHERE patientId = ?", (patientId,))
            row = cursor.fetchone()
            if row:
                return f"{row[0]} {row[1]}"
            else:
                raise PatientNumberNotFoundException("Patient not found.")
        finally:
            conn.close()

    # ✅ Added: Get doctor full name
    def getDoctorNameById(self, doctorId):
        conn = getConnection()
        if conn is None:
            raise Exception("Database connection error.")
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT firstName, lastName FROM Doctor WHERE doctorId = ?", (doctorId,))
            row = cursor.fetchone()
            if row:
                return f"{row[0]} {row[1]}"
            else:
                raise Exception("Doctor not found.")
        finally:
            conn.close()
