// Copyright (c) 2024, vish and contributors
// For license information, please see license.txt

frappe.ui.form.on("Doctor", {
    test: function(frm) {
        update_status_and_style(frm);
        if (frm.doc.test) {   
            frm.set_value('status', 'Available');
        } else {
            frm.set_value('status', 'Not Available');
        }
    },
    refresh(frm) {

        frm.fields_dict.booking_slots.$input.datepicker({
            minDate: new Date(),
            maxDate: new Date('2024-12-20')
        });

        frm.add_custom_button('Create Membership');
        frm.add_custom_button("test")
    },
    first_name: function (frm) {
        update_full_name(frm);
    },
    last_name: function (frm) {
        update_full_name(frm);
    },
    refresh: function(frm) {
        update_status_and_style(frm);
        if (frm.doc.test) {
            frm.set_value('status', 'Available');
            frm.set_indicator('Available', 'green');
        } else {
            frm.set_value('status', 'Not Available');
        }
        
        function update_status_and_style(frm) {
            if (frm.doc.check_field_name) {
                frm.set_value('status', 'Available');
                frm.fields_dict.status.$wrapper.css('background-color', 'lightgreen');
            } else {
                frm.set_value('status', 'Not Available');
                frm.fields_dict.status.$wrapper.css('background-color', 'lightcoral');
            }
        }
    },

    
    // refresh(frm) {
    //     frm.add_custom_button('Create Membership', () => {
    //         frappe.new_doc('Doctor', {
    //             library_member: frm.doc.name
    //         })
    //     })
    //     frm.add_custom_button('Create Transaction', () => {
    //         frappe.new_doc('Specialist', {
    //             library_member: frm.doc.name
    //         })
    //     })
    // },
});
// first name and last name =fullname
function update_full_name(frm) {
    if (frm.doc.first_name && frm.doc.last_name) {
        frm.set_value('full_name', frm.doc.first_name + " " + frm.doc.last_name);
    } else {
        frm.set_value('full_name', frm.doc.first_name || frm.doc.last_name || '');
    }
}