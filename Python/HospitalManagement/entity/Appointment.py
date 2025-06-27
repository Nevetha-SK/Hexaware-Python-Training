class Appointment:
    def __init__(self, appointmentId=None, patientId=None, doctorId=None, appointmentDate=None, description=None):
        self.__appointmentId = appointmentId
        self.__patientId = patientId
        self.__doctorId = doctorId
        self.__appointmentDate = appointmentDate
        self.__description = description

    # Getters
    def getAppointmentId(self): return self.__appointmentId
    def getPatientId(self): return self.__patientId
    def getDoctorId(self): return self.__doctorId
    def getAppointmentDate(self): return self.__appointmentDate
    def getDescription(self): return self.__description

    # Setters
    def setAppointmentId(self, val): self.__appointmentId = val
    def setPatientId(self, val): self.__patientId = val
    def setDoctorId(self, val): self.__doctorId = val
    def setAppointmentDate(self, val): self.__appointmentDate = val
    def setDescription(self, val): self.__description = val

    # toString
    def __str__(self):
        return (f"Appointment [ID: {self.__appointmentId}, Patient ID: {self.__patientId}, "
                f"Doctor ID: {self.__doctorId}, Date: {self.__appointmentDate}, "
                f"Description: {self.__description}]")
