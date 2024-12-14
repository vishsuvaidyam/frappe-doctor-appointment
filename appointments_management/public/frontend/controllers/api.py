 
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
    # user.save()
    user.set_password(password)
    return {"status": "success", "message": "User registered successfully"}


# @frappe.whitelist(allow_guest=True)
# def register_user(data):
#     if not data.get("email"):
#         return {'code':400,'msg':'Email is required'} 
#     try:
#         exits = frappe.db.exists('User',data.get('email'))
#         if exits:
#             return {'code':400,'msg':'User already exists'}
#         else:
#             new_user = frappe.new_doc("User")
#             new_user.email = data.get("email")

#             if data.get("full_name"):
#                 full_name = data.get("full_name").split(" ")
#                 new_user.first_name = full_name[0]
#                 new_user.last_name = full_name[1] if len(full_name) > 1 else ""

#             new_user.save(ignore_permissions=True)
#             # new_user.add_roles("System Manager")
#             return {'code':200,'msg':'Password reset instructions have been sent to your email','data':new_user} 
#     except Exception as e:
#         return {'code':500,'msg':'Internal Server Error','data':str(e)} 
