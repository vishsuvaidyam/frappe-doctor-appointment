# Copyright (c) 2024, vish and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document

class Appointment(Document):

    @frappe.whitelist()
    def send_approval_message(self):
        # Get the Appointment document
        appointment = frappe.get_doc('Appointment', self.name)
        
        # Check if the appointment is approved
        if appointment.status == "Approved":
            # Email content
            subject = f"Appointment {self.name} Approved"
            message = f"Dear {appointment.patient},\n\nYour appointment with ID {self.name} has been approved."
            
            # Send the email
            recipients = [appointment.email]
            frappe.sendmail(
                recipients=recipients,
                subject=subject,
                message=message
            )
            frappe.msgprint(f"Approval message sent to {appointment.patient}.")
