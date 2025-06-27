---
Task: 6. Save settings by filling out the form on the admin/settings page and submitting it via the 'Save Settings' button
Workflow:
Step 1: Navigate to the admin/settings page by going to http://127.0.0.1:5000/admin/settings.
Step 2: Fill out the form on the admin/settings page with the required inputs: 
    - site_name (text input)
    - support_email (email input)
Step 3: Locate the 'Save Settings' button on the admin/settings page using the following HTML characteristics: 
    - type: submit
    - text: Save Settings
Step 4: Press the 'Save Settings' button, which will submit the form to the action URL '/admin/settings' using the POST method.
Step 5: Verify that the form submission is successful, and the settings have been saved. The page may redirect to http://127.0.0.1:5000/admin/settings or another page, depending on the application's behavior.