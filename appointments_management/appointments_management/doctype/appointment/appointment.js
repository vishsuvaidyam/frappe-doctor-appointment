// Copyright (c) 2024, vish and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Appointment', {
//     after_save: function(frm) {
//         if (frm.doc.contact_number) {
//             send_sms(frm.doc.contact_number, `Your appointment is confirmed for ${frm.doc.date}.`);
//         }
//     }
// });

// function send_sms(phone_number, message) {
//     frappe.call({
//         method: "appointments_management.appointments_management.send_sms",
//         args: {
//             phone_number: phone_number,
//             message: message
//         },
//         callback: function(response) {
//             if (!response.exc) {
//                 frappe.msgprint(__('SMS sent successfully'));
//             }
//         }
//     });
// }
