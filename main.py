from time import sleep
import pickle



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECi

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


def looks_yotube(driver, action, By):
    wait = WebDriverWait(driver, 600)
    steps = 11
    link_id = 2
    scroll = 800
    count_bad = 0
    try:
        # driver.get_screenshot_as_file('avtorizovan.png')
        menu_links = driver.find_element(By.ID, 'menu_icon')
        links_item = menu_links.find_elements(By.ID, 'ajax_load')
        # for link in links_item:
        #     print(link.rect)
        # action.move_by_offset(139, 423).click().perform()
        action.click(links_item[7]).perform()

        if not wait.until_not(ECi.visibility_of_element_located((By.ID, 'window_popup_y'))):
            popup = driver.find_element(By.ID, 'window_popup_y')
            text_ok = popup.find_element(By.CLASS_NAME, 'sf_button')
            sleep(.5)
            action.click(text_ok).perform()
            sleep(.5)

        nav_youtube = wait.until(ECi.visibility_of_element_located((By.CLASS_NAME, 'm_stc')))
        looke_video = nav_youtube.find_elements(By.ID, 'ajax_load')[0]
        action.click(looke_video).perform()
# start while

        # link_id += 4
        # steps -= 1
        # driver.switch_to.window(driver.window_handles[0])
        #
        # if not wait.until_not(ECi.visibility_of_element_located((By.ID, 'capcha'))):
        #     driver.maximize_window()
        #     driver.execute_script(f'window.scrollTo(0, {scroll})')
        #
        # sleep(.2)
        # print(link_id // 4)
        # # driver.execute_script(f'window.scrollTo(0, {scroll + 100})')
        # if link_id // 4 == 3500:
        #     print('Finish')
        #     break
        # if not steps:
        #     steps = 10
        #     scroll += 550
        #     driver.execute_script(f'window.scrollTo(0, {scroll})')
        #     driver.get_screenshot_as_file('test positions.png')


        blok_links_youtube = wait.until(ECi.visibility_of_element_located((By.CLASS_NAME, 'list_rek_table')))
        print('Start')
        list_tr = blok_links_youtube.find_elements(By.TAG_NAME, 'tr')
        driver.execute_script(f'window.scrollTo(0, {scroll})')

        # blok_links_youtube = wait.until(ECi.visibility_of_element_located((By.CLASS_NAME, 'list_rek_table')))
        # youtube_link = blok_links_youtube.find_element(By.XPATH, f'tbody / tr[{link_id}] / td[2] / div / a')
        # action.click(youtube_link).perform()

        for count_link in range(1, 5000, 4):
            link_id += 4
            steps -= 1
            driver.switch_to.window(driver.window_handles[0])

            if not wait.until_not(ECi.visibility_of_element_located((By.ID, 'capcha'))):
                resole_capcha(driver, action)
            #     print('Capcha!!!')
            #     driver.execute_script(f'window.scrollTo(0, {scroll})')
            #     pots = input('Number/s pots? ')
            #     list_posts = pots.split(',')
            #     capcha_blok = driver.find_element(By.ID, 'capcha')
            #     capcha_items = capcha_blok.find_elements(By.TAG_NAME, 'label')
            #     for index in range(0, 6):
            #         if str(index) in list_posts:
            #             action.click(capcha_items[index]).perform()
            #     checkout = capcha_blok.find_element(By.CLASS_NAME, 'sf_button')
            #     action.click(checkout).perform()

            sleep(.2)
            print(link_id // 4)

            if link_id // 4 == 3500:
                print('Finish')
                break
            if not steps:
                steps = 10
                scroll += 550
                driver.execute_script(f'window.scrollTo(0, {scroll})')
                driver.get_screenshot_as_file('test positions.png')

            try:
                youtube_link = list_tr[count_link].find_elements(By.CLASS_NAME, 'surf_ckick')
                action.click(youtube_link[1]).perform()
                sleep(1.5)
                driver.switch_to.window(driver.window_handles[1])
            except:
                count_bad += 1
                print('Error ID_link ', count_bad)
                continue

# play video start
            sleep(2.5)
            try:
                frame = driver.find_element(By.XPATH, ' html / body / table / tbody / tr[2] / td / iframe')
                driver.switch_to.frame(frame)
                play_btn = driver.find_element(By.CLASS_NAME, 'ytp-large-play-button')

                action.click(play_btn).perform()
                driver.switch_to.default_content()

                capcha_blok = driver.find_element(By.ID, 'capcha-tr-block')
                wait.until(ECi.visibility_of(capcha_blok))

                sleep(1)
                driver.close()
            except:
                count_bad += 1
                print('Problem in play ', count_bad)
                driver.close()

# play video end
    except EOFError as er:
        print(er)
    finally:
        driver.quit()


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
    optins.set_preference('browser.sessionhistory.max_total_viewers', 4)
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

    looks_yotube(driver, action, By)


def main():
    SEO_bot(url)


if __name__ == '__main__':
    main()
