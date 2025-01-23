// frappe.pages['test'].on_page_load = function (wrapper) {
// 	// var page = frappe.ui.make_app_page({
// 	// 	parent: wrapper,
// 	// 	title: 'Test',
// 	// 	single_column: true
// 	// });
// 	// page.set_title_sub('Subtitle')
// 	let page = frappe.ui.make_app_page({
// 		title: 'My Page',
// 		parent: wrapper,
// 		single_column: true
// 	})
// 	page.set_title('Page')
// 	page.set_title_sub('Subtitle')
// 	page.set_indicator('Pending', 'orange')
// 	let $btns = page.set_primary_action('New', () => create_new(), 'octicon octicon-plus');
// 	let $btn = page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync');
// 	page.add_menu_item('Send Email', () => open_email_dialog());
// 	page.add_menu_item('Send Email', () => open_email_dialog(), true);
// 	page.add_action_item('Delete', () => delete_items());
// 	// page.clear_actions_menu();
// 	// add a normal inner button
// 	page.add_inner_button('Update Posts', () => update_posts())
// 	let field = page.add_field({
// 		label: 'Status',
// 		fieldtype: 'Select',
// 		fieldname: 'status',
// 		options: [
// 		'Open',
// 		'Closed',
// 		'Cancelled'
// 		],
// 		change() {
// 		console.log(field.get_value());
// 		}
// 	   });
// // change type of ungrouped button
// page.change_inner_button_type('Update Posts', null, 'primary');

// // change type of a button in a group
// page.change_inner_button_type('Delete Posts', 'Actions', 'danger');


// }

frappe.pages['test'].on_page_load = function (wrapper) {
    // Create the page with a single-column layout
    let page = frappe.ui.make_app_page({
        title: 'My Page',
        parent: wrapper,
        single_column: true
    });

    // Set the title, subtitle, and indicator
    page.set_title('Page');
    page.set_title_sub('Subtitle');
    page.set_indicator('Pending', 'orange');

    // Add primary and secondary action buttons
    page.set_primary_action('New', () => create_new(), 'octicon octicon-plus');
    page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync');

    // Add menu item for Send Email
    page.add_menu_item('Send Email', () => open_email_dialog());

    // Add custom HTML with inline styling
    // $(page.body).append(`
    //     <div style="padding: 20px; font-family: Arial, sans-serif;">
    //         <h2 style="color: #333; font-weight: bold;">Welcome to the Custom Page</h2>
    //         <p style="color: #555;">This is a dynamically added HTML section for additional content.</p>
    //         <div style="border: 1px solid #ddd; padding: 15px; border-radius: 5px; margin-top: 10px;">
    //             <h3 style="color: #007bff;">Card Title</h3>
    //             <p style="color: #666;">Card content goes here. Add more details as needed.</p>
    //             <button style="background-color: #007bff; color: #fff; border: none; padding: 10px 15px; border-radius: 5px; cursor: pointer;">
    //                 Click Me
    //             </button>
    //         </div>
    //         <div style="display: flex; margin-top: 20px;">
    //             <div style="flex: 1; padding-right: 10px;">
    //                 <h4 style="color: #333;">Left Section</h4>
    //                 <p style="color: #555;">Content for the left column.</p>
    //             </div>
    //             <div style="flex: 1; padding-left: 10px;">
    //                 <h4 style="color: #333;">Right Section</h4>
    //                 <p style="color: #555;">Content for the right column.</p>
    //             </div>
    //         </div>
    //     </div>
    // `);

    // Example: Handle custom button click
    // $('button').on('click', () => {
    //     frappe.msgprint('Custom button clicked!');
    // });
};

// Example functions used in the actions
function create_new() {
    frappe.msgprint('Create New clicked!');
}

function refresh() {
    frappe.msgprint('Refresh clicked!');
}

function open_email_dialog() {
    frappe.call({
        method: "appointments_management.controllers.api.send_email",
        args: {
            recipients: "vish.suvaidyam@gmail.com",
            subject: "Test Email from Custom Page",
            content: "This is a test email sent from the custom page in Frappe.",
            send_email: true
        },
        callback: function (response) {
            console.log("Response:", response);
            if (response.message) {
                frappe.msgprint({
                    title: 'Partial Success',
                    message: `The email send has been successfully `,
                    indicator: 'green'
                });
            } else {
                frappe.msgprint({
                    title: 'Email Error',
                    message: 'Unexpected response from the server.',
                    indicator: 'red'
                });
            }
        },
        error: function (error) {
            console.error("Error:", error);
            frappe.msgprint({
                title: 'Email Error',
                message: 'An error occurred while attempting to send the email. Please check the console for details.',
                indicator: 'red'
            });
        }
    });
}




