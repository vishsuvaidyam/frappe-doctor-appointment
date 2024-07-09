frappe.ready(function() {
	// console.log("jnjn",89)
	// bind events here
	frappe.web_form.on("pataient_age",(sdsd,frm)=>{
		let age = parseInt(frm);

		// Perform validation
		if (isNaN(age) || age < 10 || age > 50) {
			frappe.msgprint({
				title: __('Invalid Age'),
				// indicator: 'red',
				message: __('Please enter a valid age between 10 and 50.'),
			});
			return false; // Return false to prevent saving the form
		}
		return true; // Return true if validation passes
		 
	})
	
	frappe.web_form.on('date', (field, value) => {
		// console.log(field);
        if (field && field.$input) {
            field.$input.datepicker({
                minDate: new Date() 
            });
        }
    });

	frappe.web_form.on('email', (fields_dict) => {
		console.log("Validating email:", fields_dict.value);
		
		// Get the email value from the form
		let email = fields_dict.email;
		
		// Regular expression for validating an email address
		let email_regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
		
		// Check if the email matches the regex pattern
		if (!email_regex.test(email)) {
			// If the email is invalid, show a message
			frappe.msgprint(__('Invalid email format'));
			// Set validated to false to prevent form submission
			frappe.validated = true;
		}
	});
	
	
	
	
	
	
	
})

