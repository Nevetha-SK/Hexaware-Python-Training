class Patient:
    def __init__(self, patientId=None, firstName=None, lastName=None, dateOfBirth=None, gender=None, contactNumber=None, address=None):
        self.__patientId = patientId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__contactNumber = contactNumber
        self.__address = address

    # Getters
    def getPatientId(self): return self.__patientId
    def getFirstName(self): return self.__firstName
    def getLastName(self): return self.__lastName
    def getDateOfBirth(self): return self.__dateOfBirth
    def getGender(self): return self.__gender
    def getContactNumber(self): return self.__contactNumber
    def getAddress(self): return self.__address

    # Setters
    def setPatientId(self, val): self.__patientId = val
    def setFirstName(self, val): self.__firstName = val
    def setLastName(self, val): self.__lastName = val
    def setDateOfBirth(self, val): self.__dateOfBirth = val
    def setGender(self, val): self.__gender = val
    def setContactNumber(self, val): self.__contactNumber = val
    def setAddress(self, val): self.__address = val

    # toString equivalent
    def __str__(self):
        return (f"Patient [ID: {self.__patientId}, Name: {self.__firstName} {self.__lastName}, "
                f"DOB: {self.__dateOfBirth}, Gender: {self.__gender}, "
                f"Contact: {self.__contactNumber}, Address: {self.__address}]")
