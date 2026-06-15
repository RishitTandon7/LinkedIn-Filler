import asyncio
from playwright.async_api import async_playwright
import os

USER_DATA_DIR = "./playwright_user_data"

async def get_browser_context(p):
    # Use a persistent context so the user only has to log in once
    context = await p.chromium.launch_persistent_context(
        user_data_dir=USER_DATA_DIR,
        headless=False, # Set to False so the user can see and log in if needed
        args=['--disable-blink-features=AutomationControlled']
    )
    return context

async def scrape_linkedin_profile(profile_url: str) -> dict:
    """
    Navigates to the given LinkedIn profile URL and extracts the basic information.
    If the user is not logged in, it will pause to let them log in.
    """
    async with async_playwright() as p:
        context = await get_browser_context(p)
        page = await context.new_page()
        
        await page.goto(profile_url)
        
        # Check if we are on the login page or feed
        if "login" in page.url or "checkpoint" in page.url:
            print("Please log in to LinkedIn in the opened browser window...")
            # Wait until the URL changes away from the login page
            await page.wait_for_url("**/in/**", timeout=0) # wait indefinitely for user to log in and go to profile

        # Wait for the main profile section to load
        try:
            await page.wait_for_selector(".pv-top-card", timeout=10000)
        except Exception:
            pass # Continue anyway and try to scrape what we can

        # Simple extraction logic (mocking the complex parsing for now)
        # In a real scenario, this would involve extensive BeautifulSoup or JS evaluation
        # to extract Experience, Education, Skills, etc.
        
        # Extract name
        try:
            name = await page.locator("h1.text-heading-xlarge").inner_text()
        except:
            name = "Unknown"
            
        # Extract About
        try:
            about = await page.locator("div#about ~ .pvs-list__outer-container").inner_text()
        except:
            about = ""

        await context.close()
        
        # Return a simplified dictionary matching what ai_brain expects
        return {
            "name": name,
            "about": about,
            "experience": [], # Would extract from #experience section
            "education": [],  # Would extract from #education section
            "skills": []      # Would extract from #skills section
        }

if __name__ == "__main__":
    # Test
    url = input("Enter LinkedIn Profile URL: ")
    data = asyncio.run(scrape_linkedin_profile(url))
    print(data)
