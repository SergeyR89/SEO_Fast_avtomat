from time import sleep
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ECi


def look_video(driver, action, By):
    wait = WebDriverWait(driver, 600)
    steps = 11
    link_id = 2
    scroll = 800
    error_id = visit_complite = 0
    count_sleep = randint(40, 80)
    try:
        menu_links = driver.find_element(By.ID, 'menu_icon')
        links_item = menu_links.find_elements(By.ID, 'ajax_load')

        action.click(links_item[7]).perform()

        nav_youtube = wait.until(ECi.visibility_of_element_located((By.CLASS_NAME, 'm_stc')))
        looke_video = nav_youtube.find_elements(By.ID, 'ajax_load')[0]
        action.click(looke_video).perform()

        blok_links_youtube = wait.until(ECi.visibility_of_element_located((By.CLASS_NAME, 'list_rek_table')))

        list_tr = blok_links_youtube.find_elements(By.TAG_NAME, 'tr')
        driver.execute_script(f'window.scrollTo(0, {scroll})')
        print('Start')
        for count_link in range(1, 5000, 4):
            link_id += 4
            steps -= 1
            driver.switch_to.window(driver.window_handles[0])

            sleep(.2)
            if not visit_complite % 50:
                print(visit_complite)
            if link_id // 4 == 3500:
                print('Finish')
                break

            if error_id == 100:
                break

            if not steps:
                steps = 10
                scroll += 550
                driver.execute_script(f'window.scrollTo(0, {scroll})')
                driver.get_screenshot_as_file('test positions.png')

#   Sleep
            if visit_complite == count_sleep:
                print('sleep', count_sleep)
                count_sleep *= 2
                sleep(10)
            try:
                youtube_link = list_tr[count_link].find_elements(By.TAG_NAME, 'td')
                total_visit = youtube_link[2].find_element(By.TAG_NAME, 'span').text
                if int(total_visit[1:-1]) < 43:
                    continue
                link_click = youtube_link[1].find_elements(By.CLASS_NAME, 'surf_ckick')
                action.click(link_click[1]).perform()
                sleep(1.5)
                driver.switch_to.window(driver.window_handles[1])
            except:
                error_id += 1
                print('Error ID_link ', error_id)
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

                driver.close()
                visit_complite += 1
            except:
                print('Problem in play ')
                driver.close()


# play video end
    except EOFError as er:
        print(er)
    finally:
        driver.quit()
