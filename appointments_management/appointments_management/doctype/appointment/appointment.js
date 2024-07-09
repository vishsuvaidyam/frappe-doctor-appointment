// // Copyright (c) 2024, vish and contributors
// // For license information, please see license.txt
frappe.ui.form.on('Appointment', {
   
    refresh: function(frm) {
        if (frm.fields_dict.date && frm.fields_dict.date.$input) {
            frm.fields_dict.date.$input.datepicker({
                minDate: new Date()  
            });
        }
    }
    
});


 
