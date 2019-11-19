# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "utilities_kit"
app_title = "Utilities Kit"
app_publisher = "John Vincent Fiel"
app_description = "Utilities Kit"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "johnvincentfiel@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/utilities_kit/css/utilities_kit.css"
# app_include_js = "/assets/utilities_kit/js/utilities_kit.js"
app_include_js = "/assets/js/utilities_kit.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/utilities_kit/css/utilities_kit.css"
# web_include_js = "/assets/utilities_kit/js/utilities_kit.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "utilities_kit.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "utilities_kit.install.before_install"
# after_install = "utilities_kit.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "utilities_kit.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    # "*": {
    # 	"on_update": "method",
    # 	"on_cancel": "method",
    # 	"on_trash": "method"
    # }
    "Communication":
        {
            "after_insert": "utilities_kit.utilities_kit.notif.get_comments"
        }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"utilities_kit.tasks.all"
# 	],
# 	"daily": [
# 		"utilities_kit.tasks.daily"
# 	],
# 	"hourly": [
# 		"utilities_kit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"utilities_kit.tasks.weekly"
# 	]
# 	"monthly": [
# 		"utilities_kit.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "utilities_kit.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "utilities_kit.event.get_events"
# }
