---
Task: 7. Navigate to specific sub-pages like contacts/add or tickets/add from their respective main pages
Workflow:
Step 1: Navigate to the contacts main page by going to the URL http://127.0.0.1:5000/contacts from the dashboard page http://127.0.0.1:5000/dashboard.
Step 2: On the contacts main page, locate the link to the contacts/add sub-page, which is http://127.0.0.1:5000/contacts/add, and navigate to it.
Step 3: Verify that the current URL is http://127.0.0.1:5000/contacts/add, which is the contacts/add sub-page.
Step 4: Navigate to the tickets main page by going to the URL http://127.0.0.1:5000/tickets from the dashboard page http://127.0.0.1:5000/dashboard.
Step 5: On the tickets main page, locate the link to the tickets/add sub-page, which is http://127.0.0.1:5000/tickets/add, and navigate to it.
Step 6: Verify that the current URL is http://127.0.0.1:5000/tickets/add, which is the tickets/add sub-page.
Step 7: Totest the navigation, fill out the form on the contacts/add page with sample data: 
    - Fill the 'name' input with a sample name.
    - Fill the 'email' input with a sample email.
    - Fill the 'notes' textarea with sample notes.
    - Press the 'Save Contact' button (type='submit', text='Save Contact') to submit the form.
Step 8: To test the navigation, fill out the form on the tickets/add page with sample data: 
    - Select a sample contact from the 'contact_id' select input.
    - Fill the 'issue' textarea with a sample issue description.
    - Press the 'Submit Ticket' button (type='submit', text='Submit Ticket') to submit the form.
Step 9: Verify that after submitting the forms on both the contacts/add and tickets/add pages, the navigation to these sub-pages was successful, and the sample data was submitted.