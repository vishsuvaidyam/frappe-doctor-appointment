
frappe.listview_settings['Appointment'] = {
    get_indicator: function (doc) {
        if (doc.status === "Rejected") {
            return ["<span class='custom-status-open'>Rejected</span>", "green", "status,=,Rejected"];
        } else if (doc.status === "Approved") {
            return [ "<span class=.custom-status-in-progress '>Approved</span>", "orange", "status,=,Approved"];
        }
    }
};
 