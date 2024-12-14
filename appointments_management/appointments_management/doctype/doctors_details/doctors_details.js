// Copyright (c) 2024, vish and contributors
// For license information, please see license.txt

frappe.ui.form.on("Doctors_details", {
	refresh(frm) {
        frm.fields_dict.booking_slots.$input.datepicker({ 
            minDate: new Date(),
            maxDate: new Date('2024-12-20')
        });
	},
});
