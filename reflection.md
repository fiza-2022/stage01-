## Part B - Human-Written Prototype Limitations
After running the initial human-written prototype, I have found the following five limitations:
1. **No Data Persistence:** The list of appointments are only stored in memory and they are lost when the Python terminates the script's execution.
2. **Hardcoded Data Entry:** The program does not authorize the receptionist to enter any details for a new appointment, instead it is hardcoded when the function book_appointment(‘Alice Smith’) is called.
3. **No Conflict Validation:** The book_appointment method only checks if the patient name is empty but does not confirm if the Expert is available at that time which means it can be double booked.
4. **No Time Format Validation:** The appointment_time accepts any string format. A user can type anything instead of using an actual date-time string, and the system will accept it without a problem.
5. **Missing Edit/Delete Functionality:** The prototype is only authorized to add and view the appointments. If any patient wants to cancel or requests rescheduling, there is no proper function available to delete or edit an entry.
