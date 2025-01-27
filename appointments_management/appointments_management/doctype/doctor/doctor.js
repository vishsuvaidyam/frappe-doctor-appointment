// Copyright (c) 2024, vish and contributors
// For license information, please see license.txt

frappe.ui.form.on("Doctor", {
    test: function (frm) {
        update_status(frm);
    },

    refresh: function (frm) {
        // Ensure booking_slots has a datepicker with the correct configuration
        if (frm.fields_dict.booking_slots) {
            $(frm.fields_dict.booking_slots.input).datepicker({
                minDate: new Date(),
                maxDate: new Date('2024-12-20'),
            });
        }

        // Add custom buttons
        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Membership', {
                doctor: frm.doc.name,
            });
        });

        frm.add_custom_button('Create Transaction', () => {
            frappe.new_doc('Transaction', {
                doctor: frm.doc.name,
            });
        });

        update_status(frm);
    },

    first_name: function (frm) {
        update_full_name(frm);
    },

    last_name: function (frm) {
        update_full_name(frm);
    },
});

// Helper function to update full_name
function update_full_name(frm) {
    const firstName = frm.doc.first_name || '';
    const lastName = frm.doc.last_name || '';
    frm.set_value('full_name', [firstName, lastName].filter(Boolean).join(' '));
}

// Helper function to update status and indicator
function update_status(frm) {
    if (frm.doc.test) {
        frm.set_value('status', 'Available');
        frm.set_indicator('Available', 'green');
    } else {
        frm.set_value('status', 'Not Available');
        frm.set_indicator('Not Available', 'red');
    }
}
