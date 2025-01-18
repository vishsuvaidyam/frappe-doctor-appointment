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
	// Create the page with a single column layout
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

	// Add menu items
	page.add_menu_item('Send Email', () => open_email_dialog());
	page.add_menu_item('Send Email (Important)', () => open_email_dialog(), true);

	// Add action items
	page.add_action_item('Delete', () => delete_items());

	// Add an inner button
	page.add_inner_button('Update Posts', () => update_posts());

	// Add a dropdown field
	let field = page.add_field({
		label: 'Status',
		fieldtype: 'Select',
		fieldname: 'status',
		options: ['Open', 'Closed', 'Cancelled'],
		change() {
			console.log('Selected Status:', field.get_value());
		}
	});

	// Add custom HTML to the page
	$(page.body).append(`
        <div class="custom-page-content bg-red-200 w ">
            <h2 class="heading">Welcome to the Custom Page</h2>
            <p class="description">This is a dynamically added HTML section for additional content.</p>
            <div class="card">
                <h3>Card Title</h3>
                <p>Card content goes here. Add more details as needed.</p>
                <button class="btn btn-primary custom-button">Click Me</button>
            </div>
            <div class="row mt-3">
                <div class="col-md-6">
                    <h4>Left Section</h4>
                    <p>Content for the left column.</p>
                </div>
                <div class="col-md-6">
                    <h4>Right Section</h4>
                    <p>Content for the right column.</p>
                </div>
            </div>
        </div>
    `);

	// Example: Handle custom button click
	$('.custom-button').on('click', () => {
		frappe.msgprint('Custom button clicked!');
	});
};

// Example functions used in the actions
function create_new() {
	frappe.msgprint('Create New clicked!');
}

function refresh() {
	frappe.msgprint('Refresh clicked!');
}

function open_email_dialog() {
	frappe.msgprint('Open Email Dialog clicked!');
}

function delete_items() {
	frappe.msgprint('Delete clicked!');
}

function update_posts() {
	frappe.msgprint('Update Posts clicked!');
}
