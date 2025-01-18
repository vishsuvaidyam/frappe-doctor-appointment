frappe.listview_settings['Doctor'] = {
    get_indicator: function (doc) {
        if (doc.status === "Available") {
            return ["<span class='custom-status-open'>Available</span>", "", "status,=,Available"];
        } else if (doc.status === "Not Available") {
            return [ "<span class=.custom-status-in-progress '>Not Available</span>", "orange", "status,=,Not Available"];
        }
    }
};
