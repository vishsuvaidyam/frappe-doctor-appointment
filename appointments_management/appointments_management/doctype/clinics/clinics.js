// Copyright (c) 2024, vish and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Clinics", {
    
// 	refresh(frm) {
//         frm.fields_dict['shifts'].set_input(frm.doc.shifts);
//     },
//     shifts: function(frm) {
//         let time = frm.doc.shifts;
//         if (time) {
//             let [hours, minutes] = time.split(':').map(Number);
//             if (hours > 12) {
//                 hours = hours - 12;
//                 frm.set_value('shifts', `${hours}:${minutes < 10 ? '0' : ''}${minutes} PM`);
//             } else {
//                 frm.set_value('shifts', `${hours}:${minutes < 10 ? '0' : ''}${minutes} AM`);
//             }
//         }

// 	},
// });
