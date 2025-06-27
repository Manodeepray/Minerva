---
Task: 8. Interact with the website by submitting forms for adding contacts or tickets, or saving admin settings
Workflow:
Step 1: Navigate to http://127.0.0.1:5000/contacts/add to add a new contact.
Step 2: Fill out the form with action '/contacts/add' and method 'POST' by providing inputs for 'text:name', 'email:email', and 'textarea:notes'.
Step 3: Press the Button with type 'submit' and text 'Save Contact' to submit the contact addition form.
Step 4: Navigate to http://127.0.0.1:5000/tickets/add to add a new ticket.
Step 5: Fill out the form with action '/tickets/add' and method 'POST' by providing inputs for 'select:contact_id' and 'textarea:issue'.
Step 6: Press the Button with type 'submit' and text 'Submit Ticket' to submit the ticket addition form.
Step 7: Navigate to http://127.0.0.1:5000/admin/settings to save admin settings.
Step 8: Fill out the form with action '/admin/settings' and method 'POST' by providing inputs for 'text:site_name' and 'email:support_email'.
Step 9: Press the Button with type 'submit' and text 'Save Settings' to submit the admin settings form.
Step 10: Optionally, navigate to http://127.0.0.1:5000/contacts and press the Button with type 'submit' and text 'Search' after filling out the form with action '/contacts/search' and method 'GET' by providing input for 'text:query' to search for contacts.