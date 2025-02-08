import frappe
# import stripe
from frappe import _
from frappe.utils.password import update_password
from frappe.utils.password import check_password
from frappe.core.doctype.communication.email import make
from frappe.utils import get_url
import json



@frappe.whitelist(allow_guest=True)
def register_user(email, password, first_name):
    if frappe.db.exists("User", email):
        return {"code": 400, "message": "User already exists"}

    try:
        user = frappe.get_doc(
            {
                "doctype": "User",
                "email": email,
                "first_name": first_name,
                "enabled": 1,
                "send_welcome_email": 0,
                "user_type": "Website User",
            }
        )
        user.insert(ignore_permissions=True)
        update_password(user.name, password)

        # send_registration_email(email, password, first_name)

        return {"code": 200, "message": "User registered successfully"}
    except Exception as e:
        frappe.log_error(message=str(e), title="User Registration Error")
        return {
            "code": 500,
            "message": "An error occurred during registration. Please try again later.",
        }


@frappe.whitelist(allow_guest=True)
def login_user(email, password):
    try:
        user = frappe.db.get_value(
            "User", {"email": email}, ["name", "enabled", "user_image", "full_name"], as_dict=True
        )
        if not user:
            return {"code": 404, "message": "User not found"}
        if not user.enabled:
            return {"code": 403, "message": "User account is disabled"}

        # Validate password
        try:
            check_password(user.name, password)
        except frappe.AuthenticationError:
            return {"code": 401, "message": "Invalid password"}

        # Optionally: Create a session if required
        frappe.local.login_manager.user = user.name
        frappe.local.login_manager.post_login()

        session_user = frappe.get_doc("User", frappe.session.user)
        return {
            "code": 200,
            "message": "Login successful",
            "user": {
                "name": session_user.full_name or session_user.name,
                "user_image": session_user.user_image,
            },
        }
    except Exception as e:
        frappe.log_error(message=str(e), title="User Login Error")
        return {
            "code": 500,
            "message": "An error occurred during login. Please try again later.",
        }
    
@frappe.whitelist(allow_guest=True)
def set_new_password(email, new_password):
    try:
        # Fetch the user by email
        user = frappe.db.get_value("User", {"email": email}, ["name", "email"], as_dict=True)
        if not user:
            return {"code": 404, "message": "User not found"}

        # Update the password using Frappe's function
        frappe.utils.password.update_password(user["name"], new_password)

        return {"code": 200, "message": "Password updated successfully"}
    except frappe.AuthenticationError as e:
        frappe.log_error(message=str(e), title="Password Reset Error")
        return {"code": 400, "message": "Unable to update password. Please try again later."}
    except Exception as e:
        frappe.log_error(message=str(e), title="Password Reset Error")
        return {"code": 500, "message": f"An error occurred: {str(e)}"}
    

@frappe.whitelist(allow_guest=True)
def profile():
    try:
        # Fetch the session user
        session_user = frappe.get_doc("User", frappe.session.user)

        return {
            "code": 200,
            "user": {
                "name": session_user.full_name or session_user.name,
                "user_image": session_user.user_image,
                "email": session_user.email,
            },
        }
    except Exception as e:
        frappe.log_error(message=str(e), title="Fetch Profile Error")
        return {
            "code": 500,
            "message": "An error occurred while fetching the profile data.",
        }


@frappe.whitelist(allow_guest=True)
def logout():
    frappe.local.login_manager.logout()
    frappe.db.commit()


@frappe.whitelist(allow_guest=True)
def doctors_data():
    doctors = frappe.get_all(
        "Doctor", 
        fields=["*"]   
    )
    
    for doctor in doctors:
        doctor_doc = frappe.get_doc("Doctor", doctor.name)
        doctor["shifts"] = doctor_doc.get("shift", [])
    
    return doctors

@frappe.whitelist(allow_guest=True)
def Languages_data():
    lan = frappe.get_all(
        "Languages", 
        fields=["*"]   
    )
    return lan

@frappe.whitelist(allow_guest=True)
def city_data():
    """Fetch City data including MultiSelect 'doctors' field from child table."""
    try:
        cities = frappe.get_all("City", fields=["name", "town_name"])

        # city_list = []
        # for city in cities:
        #     city_doc = frappe.get_doc("City", city["name"])
        #     doctor_names = [frappe.get_value("Doctor c", doctor, "doctor") for doctor in city_doc.doctors]

        #     city_list.append({
        #         "city_name": city["town_name"],
        #         "doctors": doctor_names
        #     })

        return cities

    except Exception as e:
        frappe.log_error(f"Error fetching city data: {str(e)}")
        return {"error": str(e)}



@frappe.whitelist(allow_guest=True)
def get_doctors_by_city(town_name):
    """Fetch doctors linked to a specific City via the MultiSelect field."""
    try:
        city = frappe.get_all(
            "City",
            filters={"town_name": town_name},  
            fields=[ "*"] 
        )
        city = city[0]
        city_doc = frappe.get_doc("City", city["name"])
        doctor_names = []
        if city_doc.doctors:
            for doctor in city_doc.doctors:
                doctor_name = frappe.get_value("Doctor c", doctor, "*", as_dict=True)
                if doctor_name:
                    doctor_names.append(doctor_name)

        return {
            "town_name": town_name,
            "doctors": doctor_names
        }

    except Exception as e:
        frappe.log_error(f"Error fetching doctors for {town_name}: {str(e)}")
        return {"error": str(e)}


@frappe.whitelist(allow_guest=True)
def spaclist():
    spaclist = frappe.get_all("Specialist", fields=["*"])
    return spaclist




@frappe.whitelist(allow_guest=True)
def doctors_filter(specialist=None):
    filters = {}
    if specialist:
        filters["specialist"] = specialist

    doctors = frappe.get_all(
        "Doctor",
        fields=["full_name", "specialist", "status", "doctor_image", "city"],
        filters=filters,
    )
    return doctors


@frappe.whitelist(allow_guest=True)
def doctor_details(full_name, specialist):
    """
    Fetches the details of a doctor and their shifts based on the given full name and specialist.
    """
    if not full_name or not specialist:
        return {"message": "Full name or specialist not provided"}

    # Retrieve doctor details
    doctor = frappe.db.get_value("Doctor", {"full_name": full_name, "specialist": specialist}, "*", as_dict=True)

    if not doctor:
        return {"message": "Doctor not found"}

    # Retrieve doctor's shifts
    shifts = frappe.get_all(
        "Doctor Shift",
        filters={"parent": doctor["name"]},
        fields=["*"]
    )

    # Return a structured response
    return {"message": {"doctor": doctor, "shifts": shifts}}

@frappe.whitelist(allow_guest=True)
def details(full_name):
    if not full_name:
        return {"message": "Full name not provided"}
    
    # Get the doctor record by full_name
    doctor = frappe.get_all(
        "Doctor",
        filters={"full_name": full_name},
        fields="*"
    )
    
    if not doctor:
        return {"message": "Doctor not found"}
    
    # Since frappe.get_all returns a list, fetch the first record
    return {"message": doctor[0] if len(doctor) > 0 else {}}



@frappe.whitelist(allow_guest=True)
def related_doctors(specialist=None):
    if not specialist:
        frappe.throw("Specialist is required")
    try:
        doctors = frappe.db.get_all(
            "Doctor",
            filters={"specialist": specialist},
            fields=[
                "name",
                "doctor_image",
                "qulifications",
                "specialist",
                "experience",
                "doctor_fee",
            ],
            limit=5,  # Optional: limit the number of results
        )
        return {"message": doctors}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Related Doctors Fetch Error")
        return {"error": str(e)}


@frappe.whitelist(allow_guest=True)
def appointment_data():
    try:
        # Log incoming data
        frappe.logger().info(f"Received Data: {frappe.form_dict}")
        # Extract and validate fields
        doctor_name = frappe.form_dict.get("doctor_name")
        patient = frappe.form_dict.get("patient")
        specialist = frappe.form_dict.get("specialist")
        experience = frappe.form_dict.get("experience")
        doctor_image = frappe.form_dict.get("doctor_image")
        address = frappe.form_dict.get("address")
        doctor_fees = frappe.form_dict.get("doctor_fees")
        pataient_age=frappe.form_dict.get("pataient_age")
        pataient_gender=frappe.form_dict.get("gender")
        pataient_email=frappe.form_dict.get("email")
        datatimes=frappe.form_dict.get("datetime")

        if not all([doctor_name, patient, specialist, experience, doctor_image, address,doctor_fees,pataient_age,pataient_gender,pataient_email,datatimes]):
            frappe.throw("All fields are mandatory.")

        # Log validated data
        frappe.logger().info(f"Validated Data: doctor_name={doctor_name}, patient={patient}, ...")

        # Create and insert document
        appointment = frappe.get_doc({
            "doctype": "Appointment",
            "doctor_name": doctor_name,
            "patient": patient,
            "specialist": specialist,
            "experience": experience,
            "doctor_image": doctor_image,
            "address": address,
            "doctor_fees":doctor_fees,
            "pataient_age":pataient_age,
            "gender":pataient_gender,
            "email":pataient_email,
            "datetime":datatimes 
        })
        appointment.insert(ignore_permissions=True)
        frappe.db.commit()

        return {"status": "success", "message": "Appointment created successfully."}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Appointment Creation Failed")
        return {"status": "error", "message": str(e)}

@frappe.whitelist(allow_guest=True)
def my_appointment():
    appointment = frappe.get_all(
        "Appointment",
        fields="*"
    )
    return appointment




@frappe.whitelist(allow_guest=True)
def delete_appointment(name):
    try:
        if not name:
            frappe.throw("Appointment Name is required.")
        
        # Fetch the appointment by name
        appointment = frappe.get_doc("Appointment", {"name": name})  
        
        # Ensure appointment exists
        if not appointment:
            frappe.throw("Appointment not found.")
        
        appointment.delete()
        frappe.db.commit()

        return {"status": "success", "message": "Appointment deleted successfully."}
    
    except frappe.DoesNotExistError:
        frappe.log_error(f"Appointment not found: {name}", "Delete Appointment")
        return {"status": "error", "message": "Appointment not found."}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Delete Appointment Error")
        return {"status": "error", "message": str(e)}

# accept to send email message
@frappe.whitelist()
def send_appointment_email(recipient_email, patient, doctor_name, datetime):
    try:
        subject = f"Appointment Status Update for {patient}"
        message = f"Dear {patient},\n\nYour appointment with Dr. {doctor_name} on {datetime} has been updated. Please check your status in the system.\n\nBest regards,\nYour Healthcare Team"
        frappe.sendmail(
            recipients=recipient_email,
            subject=subject,
            message=message,
        )
        return "success"
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), f"Send Email Error: {str(e)}")
        return "failed"

@frappe.whitelist()
def approve_appointment(appointment_name, status):
    try:
        appointment_doc = frappe.get_doc('Appointment', appointment_name)
        appointment_doc.workflow_state = status   
        appointment_doc.save()
        return "success"
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), f"Approve Appointment Error: {str(e)}")
        return "failed"

@frappe.whitelist()
def reject_appointment(appointment_name, status):
    try:
        appointment_doc = frappe.get_doc('Appointment', appointment_name)
        appointment_doc.workflow_state = status  # Update workflow state to 'Rejected'
        appointment_doc.save()
        return "success"
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), f"Reject Appointment Error: {str(e)}")
        return "failed"
    
@frappe.whitelist()
def review_action(appointment_name, status):
    doc = frappe.get_doc('Appointment', appointment_name)  # Fetching the Appointment record
    workflow_field = doc.meta.get_field("workflow_state")
    
    # Get the options (valid workflow states) as a list
    available_states = workflow_field.options.split('\n') if workflow_field.options else []

    # Check if the status exists in the workflow_state field options
    if status not in available_states:
        frappe.throw(_("Invalid Workflow State: {0}".format(status)))

    # Set the workflow state to the requested status
    doc.workflow_state = status
    
    try:
        doc.save()
        return {'message': 'success'}
    except frappe.exceptions.LinkValidationError as e:
        frappe.msgprint(f"Link validation error: Could not save {doc.workflow_state}. Please check the field or values.")
        return {'message': 'failure'}
    except Exception as e:
        # Catch other exceptions and provide a useful message
        frappe.msgprint(f"An error occurred: {str(e)}")
        return {'message': 'failure'}


@frappe.whitelist(allow_guest=True)
def set_status_canceled(appointment_id):
    # Update the status field to 'Canceled' based on the appointment_id
    appointment = frappe.get_doc('Appointment', appointment_id)
    appointment.status = 'Canceled'
    appointment.save()

    return _("Status updated to Canceled")

# Set your Stripe secret key
# stripe.api_key = "sk_test_51QeDoT079z0KEg54PD4xXTJ9Mmo9t42PZSoEOa0tgIxOR0m7m8j7fKLTXQ52XmFmyi9KIj47x6Mt1PRaIyQ8Ap5r00iV9GWqJv"

# @frappe.whitelist(allow_guest=True)
# def create_payment_session(appointment_id):
#     try:
#         # Get appointment data from the database (this assumes you have a DocType for appointments)
#         appointment = frappe.get_doc("Appointment", appointment_id)
        
#         # Create a Stripe Checkout session
#         session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[{
#                 'price_data': {
#                     'currency': 'usd',
#                     'product_data': {
#                         'name': f"Appointment with Dr. {appointment.doctor_name}",
#                     },
#                     'unit_amount': int(appointment.price * 100),  # Convert to cents
#                 },
#                 'quantity': 1,
#             }],
#             mode='payment',
#             success_url=frappe.utils.get_url('/success?session_id={CHECKOUT_SESSION_ID}'),
#             cancel_url=frappe.utils.get_url('/cancel'),
#         )

#         # Return the session ID to the frontend
#         return {
#             'sessionId': session.id
#         }

#     except stripe.error.StripeError as e:
#         frappe.log_error(message=str(e), title="Stripe Payment Error")
#         raise frappe.ValidationError(_("Error creating payment session"))

@frappe.whitelist(allow_guest=True)
def send_email(recipients):
    frappe.log_error("Send email function executed", "Scheduler Test")
    try:
        subject = "Appointment Scheduler test"
        message_content = frappe.render_template("appointments_management/templates/pages/email.html")
        frappe.sendmail(
            recipients=[recipients],
            subject=subject,
            message=message_content,
        )

        return "success"

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Reject Email Error")
        frappe.throw("Unable to send rejection email. Please check the logs.")



@frappe.whitelist()
def send_email_if_approved(doc, method=None):
   
    if doc.workflow_state == "Approved":
        recipient_email = doc.get("email")  
        if recipient_email:
            subject = f"Appointment Approved: {doc.name}"
            message = f"""
            Hello,

            Your appointment has been approved.

            Details:
            - Appointment ID: {doc.name}
            - Date: {doc.get('datetime')}  
            """
            # message_content = frappe.render_template("appointments_management/templates/pages/email.html")
            # Send the email
            frappe.sendmail(
                recipients=[recipient_email],
                subject=subject,
                message=message
            )
        else:
            frappe.log_error(
                title="Email Not Sent",
                message=f"No email address found for Appointment {doc.name}"
            )
 
@frappe.whitelist()
def send_email_if_rejected(doc, method=None):
    if doc.workflow_state == "Rejected":
        recipient_email = doc.get("email")  
        if recipient_email:
            subject = f"Appointment Rejected: {doc.name}"
            message = f"""
            Hello,

            Your appointment has been Rejected.

            Details:
            - Appointment patient name: {doc.name}
            - Date: {doc.get('datetime')}  
            """
            # message_content = frappe.render_template("appointments_management/templates/pages/email.html")
            # Send the email
            frappe.sendmail(
                recipients=[recipient_email],
                subject=subject,
                message=message
            )
        else:
            frappe.log_error(
                title="Email Not Sent",
                message=f"No email address found for Appointment {doc.name}"
            )
 