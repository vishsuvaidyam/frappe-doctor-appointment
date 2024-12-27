import frappe
from frappe.utils.password import update_password
from frappe.utils.password import check_password
from frappe.core.doctype.communication.email import make


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
            "User", {"email": email}, ["name", "enabled"], as_dict=True
        )
        if not user:
            return {"code": 404, "message": "User not found"}
        if not user.enabled:
            return {"code": 403, "message": "User account is disabled"}

        try:
            check_password(user.name, password)
        except frappe.AuthenticationError:
            return {"code": 401, "message": "Invalid password"}

        # Optionally: Create a session if required
        frappe.local.login_manager.user = user.name
        frappe.local.login_manager.post_login()

        return {"code": 200, "message": "Login successful", "user": user.name}
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
    # print(f"Received full_name: {full_name}, specialist: {specialist}")

    if not full_name or not specialist:
        return {"message": "Full name or specialist not provided"}

    doctor = frappe.db.get_value("Doctor", {"full_name": full_name, "specialist": specialist}, "*", as_dict=True)
    if not doctor:
        return {"message": "Doctor not found"}
    
    return {"message": doctor}


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
