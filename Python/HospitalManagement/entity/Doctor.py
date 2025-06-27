class Doctor:
    def __init__(self, doctorId=None, firstName=None, lastName=None, specialization=None, contactNumber=None):
        self.__doctorId = doctorId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__specialization = specialization
        self.__contactNumber = contactNumber

    # Getters
    def getDoctorId(self): return self.__doctorId
    def getFirstName(self): return self.__firstName
    def getLastName(self): return self.__lastName
    def getSpecialization(self): return self.__specialization
    def getContactNumber(self): return self.__contactNumber

    # Setters
    def setDoctorId(self, val): self.__doctorId = val
    def setFirstName(self, val): self.__firstName = val
    def setLastName(self, val): self.__lastName = val
    def setSpecialization(self, val): self.__specialization = val
    def setContactNumber(self, val): self.__contactNumber = val

    # toString
    def __str__(self):
        return (f"Doctor [ID: {self.__doctorId}, Name: {self.__firstName} {self.__lastName}, "
                f"Specialization: {self.__specialization}, Contact: {self.__contactNumber}]")
