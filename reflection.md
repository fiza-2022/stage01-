## Part B - Human-Written Prototype Limitations
After running the initial human-written prototype, I have found the following five limitations:
1. **No Data Persistence:** The list of appointments are only stored in memory and they are lost when the Python terminates the script's execution.
2. **Hardcoded Data Entry:** The program does not authorize the receptionist to enter any details for a new appointment, instead it is hardcoded when the function book_appointment(‘Alice Smith’) is called.
3. **No Conflict Validation:** The book_appointment method only checks if the patient name is empty but does not confirm if the Expert is available at that time which means it can be double booked.
4. **No Time Format Validation:** The appointment_time accepts any string format. A user can type anything instead of using an actual date-time string, and the system will accept it without a problem.
5. **Missing Edit/Delete Functionality:** The prototype is only authorized to add and view the appointments. If any patient wants to cancel or requests rescheduling, there is no proper function available to delete or edit an entry.

## Part H - Final Reflection

1. **What did you build before using AI?**
Before using AI, I built a basic Python prototype for the SmartCare clinic that used lists and dictionaries to record patient names, practitioners, and appointment times. While it worked for basic data entry, it had significant limitations, such as lacking validation for double-bookings.

2. **What did AI help you understand?**
Using Microsoft Copilot as a tutor helped me better understand how to clearly explain dictionary structures and why conditional checks (like `if not appointments:`) are vital to prevent crashes when accessing empty lists. 

3. **Did AI make assumptions?**
When generating the alternative code, the AI successfully followed my constraints to avoid databases and GUIs. However, it assumed that all input data would be perfectly formatted and actually omitted the basic error handling (the blank name check) that existed in the original human code.

4. **How did you verify the AI output?**
I verified the output by executing several test scenarios in Python, including feeding it normal appointments, intentional double-bookings, blank strings, and `None` values to see exactly where the logic broke down. 

5. **What engineering work remained for you?**
Because the AI's version was overly simplistic, the core engineering work remained for me: I had to manually design and integrate a loop to check existing records and prevent practitioners from being double-booked.
