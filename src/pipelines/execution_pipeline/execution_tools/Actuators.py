from langchain.tools import tool
from bs4 import BeautifulSoup








@tool
async def navigate_to_link(state: dict, relative_url: str):
    """
    Navigate to a selected link (relative path like '/dashboard')
    Args:
        state (dict): Must contain a Puppeteer page object in `state["page"]`
        relative_url (str): e.g. '/dashboard'
    Returns:
        dict: Updated state with last action
    """
    page = state["page"]
    home_url = state["home_url"]

    # Construct absolute URL
    full_url = home_url.rstrip("/") + relative_url

    try:
        await page.goto(full_url, {'waitUntil': 'networkidle2'})
        state["curr_url"] = full_url
        state["last_action"] = f"✅ Navigated to {full_url}"
        print(f"✅ Navigated to {full_url}")
        return state
    except Exception as e:
        state["last_action"] = f"❌ Failed to navigate to {full_url}: {e}"
        return state









@tool
async def click_button_by_html(state: dict, html_string: str) -> dict:
    """
    Extract button text from HTML and click it on the current page.
    Args:
        state (dict): Must contain a Puppeteer page object in `state["page"]`
        html_string (str): e.g. '<button type="submit">Save Contact</button>'
    Returns:
        dict: Updated state with last action
    """
    page = state["page"]

    # Extract visible text from the button HTML
    try:
        soup = BeautifulSoup(html_string, 'html.parser')
        target_text = soup.get_text(strip=True)
    except Exception as e:
        state["last_action"] = f"❌ Failed to parse HTML: {e}"
        return state

    # Search all clickable elements
    try:
        buttons = await page.querySelectorAll('button, input[type="button"], input[type="submit"], [onclick]')
        
        for button in buttons:
            text = await page.evaluate('(el) => el.innerText || el.value || el.getAttribute("onclick") || ""', button)
            if text and target_text.lower() in text.strip().lower():
                await button.click()
                state["last_action"] = f"✅ Clicked button with text: {text.strip()}"
                return state
        
        state["last_action"] = f"❌ No button found with text: {target_text}"
        return state
    except Exception as e:
        state["last_action"] = f"❌ Error while clicking button: {e}"
        return state

# await click_button_by_html(state , buttons)



# form filling tool 

def parse_form_fields(html):
    soup = BeautifulSoup(html, "html.parser")
    inputs = soup.find_all(['input', 'textarea'])
    field_names = [tag.get("name") for tag in inputs if tag.get("name")]
    return field_names
    

# use this to the the field values for prompt



async def fill_form_fields(page, values: dict):
    """
    Fill out and submit a form using parsed field names and user-provided values.
    Args:
        page: Pyppeteer page object
        values: Dict of field names and their values
    """
    for field_name, field_value in values.items():

        # field_value = "<script>alert('XSS Attack!');</script>"


        selector = f'input[name="{field_name}"], textarea[name="{field_name}"], select[name="{field_name}"]'
        print(f"Filling: {selector} -> {field_value}")
        try:
            await page.waitForSelector(selector, timeout=2000)

            # Clear the input value using evaluate safely
            await page.evaluate(
                """(selector) => {
                    const el = document.querySelector(selector);
                    if (el) el.value = "";
                }""",
                selector
            )

            # Handle <select> separately if needed
            tag_name = await page.evaluate(
                """(selector) => {
                    const el = document.querySelector(selector);
                    return el ? el.tagName.toLowerCase() : null;
                }""",
                selector
            )

            if tag_name == "select":
                await page.select(selector, field_value)
            else:
                await page.type(selector, field_value)

        except Exception as e:
            print(f"⚠️ Failed to fill {field_name}: {e}")

    # Try to click the submit button
    try:
        submit_selectors = [
            'form button[type="submit"]',
            'form input[type="submit"]',
            'button[type="submit"]',
            'input[type="submit"]'
        ]
        for submit_selector in submit_selectors:
            try:
                await page.waitForSelector(submit_selector, timeout=1000)
                await page.click(submit_selector)
                await page.waitForNavigation(timeout=5000)
                return "✅ Form submitted."
            except:
                continue
        return "⚠️ No submit button found."
    except Exception as e:
        return f"⚠️ Failed to submit form: {e}"






@tool
async def form_filling_tool(state: dict, form_html: str, values: dict):
    """
    Fill out and submit a form using the parsed input names and user-provided values.
    
    Args:
        state: LangGraph agent state with a Puppeteer page
        form_html: HTML string of the <form>
        values: Dict of field names and their values (e.g., {"name": "John", "email": "john@example.com"})
    """
    fields = parse_form_fields(form_html)
    filtered_values = {k: v for k, v in values.items() if k in fields}
    
    result = await fill_form_fields(state["page"], filtered_values)
    state["last_action"] = result
    return state





