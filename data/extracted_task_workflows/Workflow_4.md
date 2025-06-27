---
Task: Submit ticket via the form on the tickets/add page and the 'Submit Ticket' button
Workflow:
Step 1: Navigate to http://127.0.0.1:5000/dashboard
Step 2: Click on the link that navigates to http://127.0.0.1:5000/tickets
Step 3: Click on the link that navigates to http://127.0.0.1:5000/tickets/add
Step 4: Fill out the form with action '/tickets/add' and method 'POST' by providing the required inputs: 
    - select: contact_id
    - textarea: issue
Step 5: Press the button with type 'submit' and text 'Submit Ticket' to submit the form
Step 6: Verify that the ticket has been successfully submitted via the form on the tickets/add page