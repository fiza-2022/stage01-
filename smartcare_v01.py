# TASK 1: Basic Input/Output
# Create and run a simple Python file with basic input,output statements
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")
# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")
# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

# TASK 1 ENHANCED
# Use lists, dictionaries and functions to enhance the Python file
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

## PART F:TESTING SCENERIOS


** 1. Normal appointment
book_appointment("Kaneez Fiza", "Dr. John Doe", "2026-09-10 10:00 AM")
print("Normal appointment booked successfully.")

# 2. Two appointments for the same practitioner/time
book_appointment("Alex Jones", "Dr. Jane Roe", "2026-09-11 02:00 PM")
book_appointment("Alice Myers", "Dr. Jane Roe", "2026-09-11 02:00 PM")
print("Double booking executed.")

# 3. Strange input such as patient_name=None or appointment_time=None
book_appointment(None, "Dr. Adams", None)
except Exception as e:
print(f"Strange input caught: {e}")

# 4. Blank patient name
print("Attempting blank patient name...")
# book_appointment("", "Dr. Smith", "2026-09-12 10:00 AM") 
# IMPORTANT: If you uncomment the line above, the program will crash with a ValueError!

display_appointments()
print("Welcome to SmartCare: The Clinical Appointment Booking System.")
book_appointment('Alice Myers', 'Dr. John Doe', '2026-09-11 02:00 PM')
book_appointment('Alex Jones', 'Dr. Jane Roe', '2026-09-11 03:30 PM')
display_appointments()

Part G - Improve One Thing
