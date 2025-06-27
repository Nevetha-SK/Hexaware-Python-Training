from abc import ABC, abstractmethod
from entity.Appointment import Appointment

class IHospitalService(ABC):

    @abstractmethod
    def getAppointmentById(self, appointmentId) -> Appointment:
        pass

    @abstractmethod
    def getAppointmentsForPatient(self, patientId) -> list:
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self, doctorId) -> list:
        pass

    @abstractmethod
    def scheduleAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def updateAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def cancelAppointment(self, appointmentId) -> bool:
        pass

    @abstractmethod
    def getPatientNameById(self, patientId): 
        pass

    @abstractmethod
    def getDoctorNameById(self, doctorId): 
        pass
