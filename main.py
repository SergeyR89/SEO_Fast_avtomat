import pickle
from time import sleep

from moduls import look_video


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options


login = 'musor-12@mail.ru'
password = '6c29793a14'

url = 'https://seo-fast.ru'


def resole_capcha(driver, action):
        print('Capcha!!!')
        driver.get_screenshot_as_file('Capcha.png')
        pots = input('Number/s pots? ')
        list_posts = pots.split(',')
        capcha_blok = driver.find_element(By.ID, 'capcha')
        capcha_items = capcha_blok.find_elements(By.TAG_NAME, 'label')
        for index in range(0, 6):
            if str(index) in list_posts:
                action.click(capcha_items[index]).perform()
        checkout = capcha_blok.find_element(By.CLASS_NAME, 'sf_button')
        action.click(checkout).perform()



def avtoris_cookies(driver, action, By, name_cookies):
    driver.get(url='https://seo-fast.ru/login')
    login = 'musor-12@mail.ru'
    password = '6c29793a14'
    sleep(1)

    log_in = driver.find_element(By.ID, 'logusername')
    password_in = driver.find_element(By.ID, 'logpassword')
    action.click(log_in).send_keys(login).perform()
    sleep(1)
    action.click(password_in).send_keys(password).perform()

    sleep(60)
    pickle.dump(driver.get_cookies(), open(name_cookies + '_cookeis', 'wb'))
    sleep(2)
    driver.quit()


def add_cookies(driver, name_cookies):
    for item in pickle.load(open(name_cookies + '_cookeis', 'rb')):
        driver.add_cookie(item)
    sleep(5)

    driver.refresh()


def SEO_bot(urls):
    agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0'
    optins = Options()
    optins.headless = True
    optins.set_preference('dom.webdriver.enabled', False)
    optins.set_preference('media.volume_scale', '0.0')
    optins.set_preference('dom.ipc.processCount', 3)
    optins.set_preference('toolkit.cosmeticAnimations.enabled', False)
    optins.set_preference('general.useragent.override', agent)
    optins.set_preference('browser.sessionstore.max_tabs_undo', 2)
    optins.set_preference('browser.sessionhistory.max_entries', 10)
    optins.set_preference('browser.sessionhistory.max_total_viewers', 3)
    optins.set_preference('geo.enabled', False)
    optins.set_preference('network.prefetch-next', False)
    optins.set_preference('media.cache_size', 128000)

    serves = Service(executable_path='Draiver/geckodriver.exe')
    driver = webdriver.Firefox(service=serves, options=optins)
    action = ActionChains(driver)
    driver.get(url=urls)
    driver.set_window_size(1276, 1024)

    name_cookies = 'SEO-Fast'

    # avtoris_cookies(driver, action, By, name_cookies)
    #  добавление кукис
    add_cookies(driver, name_cookies)

    sleep(1)

    look_video.look_video(driver, action, By)


def while_look_video():
    for index in range(5):
        SEO_bot(url)
        print('Refresh Brouser')
        sleep(15)


def main():
    while_look_video()


if __name__ == '__main__':
    main()
