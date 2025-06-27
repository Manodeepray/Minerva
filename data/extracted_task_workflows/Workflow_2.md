---
Task: 3. Submit a search query on the contacts page by pressing the 'Search' button
Workflow:
Step 1: Navigate to http://127.0.0.1:5000/dashboard.
Step 2: Click on the link that redirects to http://127.0.0.1:5000/contacts.
Step 3: On the http://127.0.0.1:5000/contacts page, locate the form with action '/contacts/search' and method 'GET', and fill in the 'text:query' input with the desired search query.
Step 4: Locate the button with type 'submit' and text 'Search', and press it to submit the form.
Step 5: The browser will then navigate to http://127.0.0.1:5000/contacts/search with the search query as a GET parameter, displaying the search results.