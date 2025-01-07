import frappe
# import stripe
from frappe import _
from frappe.utils.password import update_password
from frappe.utils.password import check_password
from frappe.core.doctype.communication.email import make
from frappe.utils import get_url


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
        # Fetch user details
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

        return {
            "code": 200,
            "message": "Login successful",
            "user": {
                "name": user.name,
                "user_image": user.user_image,
                "full_name": user.full_name,
            },
        }
    except Exception as e:
        frappe.log_error(message=str(e), title="User Login Error")
        return {
            "code": 500,
            "message": "An error occurred during login. Please try again later.",
        }


# def send_registration_email(email, password, first_name):
#     """Send a registration email with user credentials."""
#     subject = "Welcome to Our Platform"
#     message = f"""
#     Hi {first_name},

#     Welcome to our platform! Your account has been successfully created.

#     Here are your login details:
#     - Email: {email}
#     - Password: {password}

#     Please log in and change your password for security reasons.

#     Regards,
#     The Team
#     """
#     try:
#         frappe.sendmail(
#             recipients=email,
#             subject=subject,
#             message=message,
#         )
#     except Exception as e:
#         frappe.log_error(message=str(e), title="Email Sending Error")


@frappe.whitelist(allow_guest=True)
def doctors_data():
    doctors = frappe.get_all(
        "Doctor", fields=["full_name", "specialist", "status", "doctor_image"]
    )
    # print(doctors, "==========================================")
    return doctors


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
        fields=["full_name", "specialist", "status", "doctor_image"],
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
def delete_appointment():
    try:
        appointment_id = frappe.form_dict.get("appointment_name")  
        if not appointment_id:
            frappe.throw("Appointment ID is required.")
        appointment = frappe.get_doc("Appointment", appointment_id)
        appointment.delete()
        frappe.db.commit()
        
        return {"status": "success", "message": "Appointment deleted successfully."}
    except frappe.DoesNotExistError:
        frappe.log_error(f"Appointment not found: {appointment_id}", "Delete Appointment")
        return {"status": "error", "message": "Appointment not found."}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Delete Appointment Error")
        return {"status": "error", "message": str(e)}


# accept to send email message
@frappe.whitelist()
def send_accept_email(recipient_email, patient, doctor_name, datetime):
    """
    Send an email for appointment confirmation.

    Args:
        recipient_email (str): Recipient's email address.
        patient (str): Patient's name.
        doctor_name (str): Doctor's name.
        datetime (str): Appointment date and time.

    Returns:
        str: "success" if the email is sent, else raises an exception.
    """
    try:
        subject = "Appointment Confirmation"
        message_content = f"""
            <p>Dear {patient},</p>
            <p>Your appointment with {doctor_name} is confirmed.</p>
            <p><strong>Date and Time:</strong> {datetime}</p>
            <p>Thank you for choosing our services.</p>
            <p>Regards,</p>
            <p>Appointments Management Team</p>
        """

        # Sending the email
        frappe.sendmail(
            recipients=[recipient_email],
            subject=subject,
            message=message_content,
        )

        return "success"

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Send Email Error")
        frappe.throw("Unable to send email. Please check the logs.")
    """
    Send an email notification when a message is sent.

    Args:
        message (str): The content of the message to be sent.
        recipient_email (str): The recipient's email address.
    """
    try:
        subject = "New Message Notification"
        message_content = f"""
            <p>Hello,</p>
            <p>You have received a new message:</p>
            <blockquote>{message}</blockquote>
            <p><a href="{get_url()}">View it on the system</a></p>
        """

        # Sending email
        frappe.sendmail(
            recipients=[recipient_email],
            subject=subject,
            message=message_content,
        )

        return {"status": "success", "message": "Email sent successfully!"}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Send Message Email Error")
        return {"status": "error", "message": str(e)}
    
    # reject to send email message

@frappe.whitelist()
def send_reject_email(recipient_email, doctor_name, datetime):
    """
    Send a rejection email to the doctor.

    Args:
        recipient_email (str): Recipient's email address (doctor).
        doctor_name (str): Doctor's name.
        datetime (str): Appointment date and time.

    Returns:
        str: "success" if the email is sent, else raises an exception.
    """
    try:
        subject = "Appointment Rejection Notification"
        message_content = f"""
            <p>Dear. {doctor_name},</p>
            <p>We regret to inform you that the appointment scheduled on <strong>{datetime}</strong> has been rejected by the patient.</p>
            <p>If you have any questions, please contact our support team.</p>
            <p>Thank you for your understanding.</p>
            <p>Regards,</p>
            <p>Appointments Management Team</p>
        """

        # Sending the email
        frappe.sendmail(
            recipients=[recipient_email],
            subject=subject,
            message=message_content,
        )

        return "success"

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Reject Email Error")
        frappe.throw("Unable to send rejection email. Please check the logs.")


@frappe.whitelist()
def accept_appointment(appointment_name, status):
    appointment = frappe.get_doc("Appointment", appointment_name)
    appointment.status = status
    appointment.save()
    return _("success")

@frappe.whitelist()
def reject_appointment(appointment_name, status):
    # Fetch the appointment record by name
    appointment = frappe.get_doc("Appointment", appointment_name)
    
    # Update the status to "Rejected"
    appointment.status = status
    
    # Save the updated appointment
    appointment.save()
    
    # Optionally, send rejection email (or handle any other logic)
    return "success"


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

