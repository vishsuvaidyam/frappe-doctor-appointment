frappe.pages['appoitnment-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Page',
		single_column: true
	});
	
}