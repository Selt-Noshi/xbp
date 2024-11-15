from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def chat_gpt_query(input_text):
    driver.get('https://chat.openai.com/')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea")))  # 等待文本框加载

    input_field = driver.find_element(By.CSS_SELECTOR, "textarea")
    
    # 等待文本框可交互
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(input_field))
    
    input_field.click()
    
    query = f"日本語に書き直してください：「{input_text}」"
    input_field.send_keys(query)
    input_field.send_keys(Keys.RETURN)
    
    time.sleep(5)  # 等待ChatGPT响应
    
    result = driver.find_element(By.CSS_SELECTOR, '.result-selector').text
    print(f"Result 1: {result}")
    
    return result
