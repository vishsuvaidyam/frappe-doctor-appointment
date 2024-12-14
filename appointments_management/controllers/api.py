import frappe

@frappe.whitelist(allow_guest=True)
def register_user(email, password, first_name):
    if frappe.db.exists("User", email):
        return {"status": "error", "message": "User already exists"}
    # return "hhh"
    user = frappe.get_doc({
        "doctype": "User",
        "email": email,
        "first_name":  first_name,
        "enabled": 1,
        "send_welcome_email": 0,
        "user_type": "Website User"
    })
    user.insert(ignore_permissions=True)
    user.save()
    user.set_password(password)
    return {"status": "success", "message": "User registered successfully"}

@frappe.whitelist(allow_guest=True)
def doctors_data():
    doctors = frappe.get_all("Doctor",fields=["full_name","specialist","status","doctor_image"])
    # print(doctors, "==========================================")   
    return doctors

@frappe.whitelist(allow_guest=True)
def spaclist():
    spaclist=frappe.get_all("Specialist",fields=["*"])
    return spaclist
 
@frappe.whitelist(allow_guest=True)
def doctors_filter(specialist=None):
    filters = {}
    if specialist:
        filters["specialist"] = specialist
    
    doctors = frappe.get_all(
        "Doctor",
        fields=["full_name", "specialist", "status", "doctor_image"],
        filters=filters
    )
    
    return doctors
