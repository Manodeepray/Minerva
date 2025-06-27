---
Task: Navigate between all major pages like dashboard, contacts, tickets, admin, etc.
Workflow:
Step 1: Start at the dashboard page by navigating to http://127.0.0.1:5000/dashboard.
Step 2: From the dashboard, navigate to the contacts page by clicking on the link that directs to http://127.0.0.1:5000/contacts.
Step 3: On the contacts page, fill out the search form with the following details: 
    - Form action: /contacts/search
    - Form method: GET
    - Form inputs: 
        - text: query (enter a search query)
    Then, press the button with type='submit' and text='Search'.
Step 4: From the contacts page, navigate to the tickets page by clicking on the link that directs to http://127.0.0.1:5000/tickets.
Step 5: From the tickets page, navigate to the admin page by clicking on the link that directs to http://127.0.0.1:5000/admin.
Step 6: On the admin settings page (http://127.0.0.1:5000/admin/settings), fill out the settings form with the following details: 
    - Form action: /admin/settings
    - Form method: POST
    - Form inputs: 
        - text: site_name (enter the site name)
        - email: support_email (enter the support email)
    Then, press the button with type='submit' and text='Save Settings'.
Step 7: From the admin page, navigate back to the contacts page by clicking on the link that directs to http://127.0.0.1:5000/contacts.
Step 8: On the contacts page, navigate to the add contact page by clicking on the link that directs to http://127.0.0.1:5000/contacts/add.
Step 9: On the add contact page, fill out the add contact form with the following details: 
    - Form action: /contacts/add
    - Form method: POST
    - Form inputs: 
        - text: name (enter the contact name)
        - email: email (enter the contact email)
        - textarea: notes (enter any notes about the contact)
    Then, press the button with type='submit' and text='Save Contact'.
Step 10: From the contacts page, navigate to the tickets page by clicking on the link that directs to http://127.0.0.1:5000/tickets.
Step 11: On the tickets page, navigate to the add ticket page by clicking on the link that directs to http://127.0.0.1:5000/tickets/add.
Step 12: On the add ticket page, fill out the add ticket form with the following details: 
    - Form action: /tickets/add
    - Form method: POST
    - Form inputs: 
        - select: contact_id (select a contact)
        - textarea: issue (enter the ticket issue)
    Then, press the button with type='submit' and text='Submit Ticket'.
Step 13: Finally, navigate back to the dashboard page by clicking on the link that directs to http://127.0.0.1:5000/dashboard to complete the task.