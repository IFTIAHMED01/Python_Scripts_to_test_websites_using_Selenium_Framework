#TestingWebsite

from selenium import webdriver
#from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # 2. Navigate to the W3Schools website
    driver.get("https://www.w3schools.com/")

    # 3. Retrieve the page title
    # The .title attribute returns the text found in the <title> tag of the HTML
    page_title = driver.title

    # 4. Print the title to your VS Code console
    print(f"The title of the page is: {page_title}")

finally:
    # 5. Always close the browser window after the task is complete
    driver.quit()