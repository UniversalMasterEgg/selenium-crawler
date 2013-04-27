from selenium import webdriver

def handle_link(link):
    driver = webdriver.Chrome('/tmp/bin/chromedriver')
    driver.implicitly_wait(30)
    driver.get(link)

    driver.find_element_by_xpath("//div[@class='header']/div[@class='continue']/a").click()

    results = {
        'url': driver.current_url,
        'source': driver.page_source
    }
    driver.quit()

    return results
