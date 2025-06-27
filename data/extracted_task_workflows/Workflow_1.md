---
Task: 2. Search for a contact using the form on the contacts page
Workflow:
Step 1: Navigate to http://127.0.0.1:5000/contacts from any of the connected pages (http://127.0.0.1:5000/dashboard, http://127.0.0.1:5000/tickets, http://127.0.0.1:5000/admin).
Step 2: Locate the form on the contacts page with action '/contacts/search' and method 'GET', which contains a single input field 'query' of type 'text'.
Step 3: Fill in the 'query' input field with the desired search term.
Step 4: Locate the 'Search' button on the contacts page, identified by its type 'submit' and text 'Search'.
Step 5: Press the 'Search' button to submit the form, which will send a GET request to http://127.0.0.1:5000/contacts/search with the query parameter.
Step 6: The search results will be displayed on the resulting page, allowing for further interaction or navigation as needed.