# Copyright (c) 2024, vish and contributors
# For license information, please see license.txt

# import frappe
import frappe
 

from frappe.model.document import Document

class Appointment(Document):
    def after_insert(self):
        queue_number = self.add_to_appointment_queue()
        print(f"Your queue number========================: {queue_number}")

    def add_to_appointment_queue(self):
        try:
            # Fetch or create the Appointment Queue document
            q = frappe.get_doc({
                "doctype": "Appointment Queue",
                "date": self.date,
                "clinic": self.clinic
            })

            # Append the new appointment to the queue
            q.append("queue", {"appointment": self.name, "status": ""})
            q.save(ignore_permissions=True)
            

            # Return the length of the queue
            return len(q.queue)
        except frappe.DoesNotExistError:
            frappe.throw("Appointment Queue document does not exist.")
        except Exception as e:
            frappe.throw(f"An error occurred: {str(e)}")