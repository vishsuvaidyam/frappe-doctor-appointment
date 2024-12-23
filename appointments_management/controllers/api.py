import frappe
# from frappe.utils.password import update_password


@frappe.whitelist(allow_guest=True)
def register_user(email, first_name):
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
        # update_password(user.name, password)

        return {"code": 200, "message": "User registered successfully"}
    except Exception as e:
        frappe.log_error(message=str(e), title="User Registration Error")
        return {
            "code": 500,
            "message": "An error occurred during registration. Please try again later.",
        }


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


# @frappe.whitelist(allow_guest=True)
# def doctor_details():
#     details=frappe.get_all("Doctors_details",fields=["name","description","doctor_fee","booking_slots","experience","image_doctor","spacelist","qulification"])
#     # print(details,"====================================================================")
#     return details


@frappe.whitelist(allow_guest=True)
def doctor_details(full_name):
    if not full_name:
        return {"message": "No full name provided"}

    doctor = frappe.db.get_value("Doctor", {"full_name": full_name}, "*", as_dict=True)
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
