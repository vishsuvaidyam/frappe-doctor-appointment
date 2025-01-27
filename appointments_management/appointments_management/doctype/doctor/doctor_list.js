frappe.listview_settings['Doctor'] = {
    get_indicator: function (doc) {
        if (doc.status === "Available") {
            return ["<span class=''>Available</span>", "green", "status,=,Available"];
        } else if (doc.status === "Not Available") {
            return [ "<span  '>Not Available</span>", "orange", "status,=,Not Available"];
        }
    }
};
 