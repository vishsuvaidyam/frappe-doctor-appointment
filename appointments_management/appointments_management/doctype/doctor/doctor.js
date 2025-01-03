// Copyright (c) 2024, vish and contributors
// For license information, please see license.txt

frappe.ui.form.on("Doctor", {
    refresh(frm) {
        frm.fields_dict.booking_slots.$input.datepicker({ 
            minDate: new Date(),
            maxDate: new Date('2024-12-20')
        });
	},
      first_name: function(frm) {
        update_full_name(frm);
    },
    last_name: function(frm) {
        update_full_name(frm);
    },
	refresh(frm) {
        

	},
});
// first name and last name =fullname
function update_full_name(frm) {
    if (frm.doc.first_name && frm.doc.last_name) {
        frm.set_value('full_name', frm.doc.first_name + " " + frm.doc.last_name);
    } else {
        frm.set_value('full_name', frm.doc.first_name || frm.doc.last_name || '');
    }
}