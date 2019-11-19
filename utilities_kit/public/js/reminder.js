/**
 * Created by jvfiel on 9/27/17.
 */
$(function() {

	frappe.call({
		method: "utilities_kit.utilities_kit.notif.get_reminders",
		args: {
			"owner": frappe.session.user
		},
		callback: function (r) {
			if(r.message)
			{
				frappe.msgprint(r.message);
			}
		}
	});
});