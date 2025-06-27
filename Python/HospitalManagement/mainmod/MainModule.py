import sys
import os

# 👇 Add root folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.HospitalServiceImpl import HospitalServiceImpl
from entity.Appointment import Appointment
from exception.PatientNumberNotFoundException import PatientNumberNotFoundException

def displayMenu():
    print("\n------ HOSPITAL MANAGEMENT MENU ------")
    print("1. Get Appointment by ID")
    print("2. Get Appointments for a Patient")
    print("3. Get Appointments for a Doctor")
    print("4. Schedule a New Appointment")
    print("5. Update Appointment")
    print("6. Cancel Appointment")
    print("7. Exit")

def main():
    service = HospitalServiceImpl()

    while True:
        displayMenu()
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                aid = int(input("Enter Appointment ID: "))
                appt = service.getAppointmentById(aid)
                print(appt)

            elif choice == '2':
                pid = int(input("Enter Patient ID: "))
                # ✅ Fetch patient name
                name = service.getPatientNameById(pid)
                print(f"\n👤 Appointments for Patient: {name} (ID: {pid})")
                appts = service.getAppointmentsForPatient(pid)
                if not appts:
                    print("ℹ️ No appointments found for this patient.")
                else:
                    for a in appts:
                        print(a)

            elif choice == '3':
                did = int(input("Enter Doctor ID: "))
                # ✅ Fetch doctor name
                name = service.getDoctorNameById(did)
                print(f"\n👨‍⚕️ Appointments for Doctor: {name} (ID: {did})")
                appts = service.getAppointmentsForDoctor(did)
                if not appts:
                    print("ℹ️ No appointments found for this doctor.")
                else:
                    for a in appts:
                        print(a)

            elif choice == '4':
                aid = int(input("Enter Appointment ID: "))
                pid = int(input("Enter Patient ID: "))
                did = int(input("Enter Doctor ID: "))
                date = input("Enter Appointment Date (YYYY-MM-DD): ")
                desc = input("Enter Description: ")
                appointment = Appointment(aid, pid, did, date, desc)
                if service.scheduleAppointment(appointment):
                    print("✅ Appointment Scheduled Successfully.")

            elif choice == '5':
                aid = int(input("Enter Appointment ID to Update: "))
                pid = int(input("Enter Updated Patient ID: "))
                did = int(input("Enter Updated Doctor ID: "))
                date = input("Enter Updated Appointment Date (YYYY-MM-DD): ")
                desc = input("Enter Updated Description: ")
                appointment = Appointment(aid, pid, did, date, desc)
                if service.updateAppointment(appointment):
                    print("✅ Appointment Updated Successfully.")
                else:
                    print("❌ Update Failed.")

            elif choice == '6':
                aid = int(input("Enter Appointment ID to Cancel: "))
                if service.cancelAppointment(aid):
                    print("✅ Appointment Cancelled.")
                else:
                    print("❌ Appointment not found or already cancelled.")

            elif choice == '7':
                print("Exiting Application.")
                break

            else:
                print("❌ Invalid choice. Please try again.")

        except PatientNumberNotFoundException as e:
            print("❗", e)
        except Exception as e:
            print("❗ Unexpected Error:", e)

if __name__ == "__main__":
    main()
