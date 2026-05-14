from posnext.utils import get_build_version

app_name = "posnext"
app_title = "POS Next"
app_publisher = "BrainWise"
app_description = "POS built on ERPNext that brings together real-time billing, stock management, multi-user access, offline mode, and direct ERP integration. Run your store or restaurant with confidence and control, while staying 100% open source."
app_email = "support@brainwise.me"
app_license = "agpl-3.0"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "posnext",
# 		"logo": "/assets/posnext/logo.png",
# 		"title": "POS Next",
# 		"route": "/posnext",
# 		"has_permission": "posnext.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# Get unique build version for cache busting
_asset_version = get_build_version()

# include js, css files in header of desk.html
# app_include_css = f"/assets/posnext/css/posnext.css?v={_asset_version}"
# app_include_js = f"/assets/posnext/js/posnext.js?v={_asset_version}"

# include js, css files in header of web template
# web_include_css = "/assets/posnext/css/posnext.css"
# web_include_js = "/assets/posnext/js/posnext.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "posnext/public/scss/website"

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
# app_include_icons = "posnext/public/icons.svg"

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
# 	"methods": "posnext.utils.jinja_methods",
# 	"filters": "posnext.utils.jinja_filters"
# }

# Fixtures
# --------
fixtures = [
	{
		"dt": "Custom Field",
		"filters": [
			[
				"name",
				"in",
				[
					"Sales Invoice-posa_pos_opening_shift",
					"Sales Invoice-posa_is_printed",
					"Item-custom_company",
					"POS Profile-posa_cash_mode_of_payment",
					"POS Profile-posa_allow_delete",
					"POS Profile-posa_block_sale_beyond_available_qty"
				]
			]
		]
	},
	{
		"dt": "Print Format",
		"filters": [
			[
				"name",
				"in",
				[
					"POS Next Receipt"
				]
			]
		]
	}
]

# Installation
# ------------

# before_install = "posnext.install.before_install"
after_install = "posnext.install.after_install"
after_migrate = "posnext.install.after_migrate"

# Uninstallation
# ------------

before_uninstall = "posnext.uninstall.before_uninstall"
# after_uninstall = "posnext.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "posnext.utils.before_app_install"
# after_app_install = "posnext.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "posnext.utils.before_app_uninstall"
# after_app_uninstall = "posnext.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "posnext.notifications.get_notification_config"

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

# Standard Queries
# ----------------
# Custom query for company-aware item filtering
standard_queries = {
	"Item": "posnext.validations.item_query"
}

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item": {
		"validate": "posnext.validations.validate_item"
	},
	"Sales Invoice": {
		"validate": "posnext.api.sales_invoice_hooks.validate",
		"before_cancel": "posnext.api.sales_invoice_hooks.before_cancel",
		"on_submit": "posnext.realtime_events.emit_stock_update_event",
		"on_cancel": "posnext.realtime_events.emit_stock_update_event",
		"after_insert": "posnext.realtime_events.emit_invoice_created_event"
	},
	"POS Profile": {
		"on_update": "posnext.realtime_events.emit_pos_profile_updated_event"
	}
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	"hourly": [
		"posnext.tasks.branding_monitor.monitor_branding_integrity",
	],
	"daily": [
		"posnext.tasks.cleanup_expired_promotions.cleanup_expired_promotions",
		"posnext.tasks.branding_monitor.validate_all_active_sessions",
	],
	"monthly": [
		"posnext.tasks.branding_monitor.reset_tampering_counter",
	],
}

# Testing
# -------

# before_tests = "posnext.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "posnext.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "posnext.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["posnext.utils.before_request"]
# after_request = ["posnext.utils.after_request"]

# Job Events
# ----------
# before_job = ["posnext.utils.before_job"]
# after_job = ["posnext.utils.after_job"]

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
# 	"posnext.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


website_route_rules = [{'from_route': '/pos/<path:app_path>', 'to_route': 'pos'},]