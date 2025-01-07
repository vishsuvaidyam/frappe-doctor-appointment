app_name = "appointments_management"
app_title = "appointments_management"
app_publisher = "vish"
app_description = " appointments web portal"
app_email = "vish.suvaidyam@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/appointments_management/css/appointments_management.css"
# app_include_js = "/assets/appointments_management/js/appointments_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/appointments_management/css/appointments_management.css"
# web_include_js = "/assets/appointments_management/js/appointments_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "appointments_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "appointments_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "appointments_management.utils.jinja_methods",
# 	"filters": "appointments_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "appointments_management.install.before_install"
# after_install = "appointments_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "appointments_management.uninstall.before_uninstall"
# after_uninstall = "appointments_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "appointments_management.utils.before_app_install"
# after_app_install = "appointments_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "appointments_management.utils.before_app_uninstall"
# after_app_uninstall = "appointments_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "appointments_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# "Appointment": {
#         "before_submit": "appointments_management.doctype.appointment.before_submit"
#     }
# }

# doc_events = {
#     "User": {
#         "on_update": "appointments_management.api.register_user"
#     }
# }
api_methods = [
    "appointments_management.controllers.api.register_user"
]



fixtures=[
    'Doctor',
    'Specialist',
    'Doctors_details',
    'User',
    'Role',
    'Role Profile',
    'Custom HTML Block',
    ]
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"appointments_management.tasks.all"
# 	],
# 	"daily": [
# 		"appointments_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"appointments_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"appointments_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"appointments_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "appointments_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "appointments_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "appointments_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["appointments_management.utils.before_request"]
# after_request = ["appointments_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["appointments_management.utils.before_job"]
# after_job = ["appointments_management.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"appointments_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


website_route_rules = [{'from_route': '/frontend/<path:app_path>', 'to_route': 'frontend'},]