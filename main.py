from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def main():
    opts = Options()
    opts.headless = True

    driver = Chrome(options=opts, executable_path='chromedriver.exe')

    try:
        driver.get('http://webcode.me')
        driver.find_element(by=By.ID,value='login')
        # print(driver.title)/
        assert 'My html page' == driver.title
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
