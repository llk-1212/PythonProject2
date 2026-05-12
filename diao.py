from selenium import webdriver
import time
from random import *
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    # 刷问卷的份数。
    for index in range(1, 10):
        print(index, "份正在执行操作......")

        # 给出所需的url和option参数
        url_survey = ("https://www.wjx.cn/vj/Pp7lrrz.aspx") # 根据需要填写url，也就是自己的网址
        option = webdriver.ChromeOptions()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=option,executable_path='C:\\Users\\liu\\Desktop\\chromedriver.exe')
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
        driver.get(url_survey)
        time.sleep(2)

        ##开始做题
        # 处理Q1
        # 生成随机数，决定点哪个按钮
        q1 = random()
        if 0 <= q1 <= 0.5:
            # 通过属性定位元素，第x题就是qx，第y个选项就是_y，例如Q1的"//a[@rel='q1_1']"中，'q1_1'表示第一题的第一个选项
            # q1_1是Q1的第1个按钮
            driver.find_element_by_xpath("//a[@rel='q1_1']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q1_2']").click()

        # 处理Q2
        # 生成随机数，决定点哪个按钮
        q2 = random()
        if 0 <= q2 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q2_1']").click()
        elif 0.1 < q2 <= 0.25:
            driver.find_element_by_xpath("//a[@rel='q2_2']").click()
        elif 0.25 < q2 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q2_3']").click()
        elif 0.5 < q2 <= 0.7:
            driver.find_element_by_xpath("//a[@rel='q2_4']").click()
        elif 0.7 < q2 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q2_5']").click()
        elif 0.8 < q2 <= 0.9:
            driver.find_element_by_xpath("//a[@rel='q2_6']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q2_7']").click()

        # 处理Q3
        # 生成随机数，决定点哪个按钮
        q3 = random()
        if 0 <= q3 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q3_1']").click()
        elif 0.1 < q3 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q3_2']").click()
        elif 0.3 < q3 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q3_3']").click()
        elif 0.5 < q3 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q3_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q3_5']").click()

        # 处理Q4
        # 生成随机数，决定点哪个按钮
        q4 = random()
        if 0 <= q4 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q4_1']").click()
        elif 0.1 < q4 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q4_2']").click()
        elif 0.3 < q4 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q4_3']").click()
        elif 0.5 < q4 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q4_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q4_5']").click()

        q5 = random()
        if 0 <= q5 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q5_1']").click()
        elif 0.1 < q5 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q5_2']").click()
        elif 0.3 < q5 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q5_3']").click()
        elif 0.5 < q5 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q5_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q5_5']").click()

        q6 = random()
        if 0 <= q6 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q6_1']").click()
        elif 0.1 < q6 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q6_2']").click()
        elif 0.3 < q6 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q6_3']").click()
        elif 0.5 < q6 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q6_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q6_5']").click()

        q7 = random()
        if 0 <= q7 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q7_1']").click()
        elif 0.1 < q7 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q7_2']").click()
        elif 0.3 < q7 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q7_3']").click()
        elif 0.5 < q7 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q7_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q7_5']").click()

        q8 = random()
        if 0 <= q8 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q8_1']").click()
        elif 0.1 < q8 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q8_2']").click()
        elif 0.3 < q8 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q8_3']").click()
        elif 0.5 < q8 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q8_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q8_5']").click()

        q9 = random()
        if 0 <= q9 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q9_1']").click()
        elif 0.1 < q9 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q9_2']").click()
        elif 0.3 < q9 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q9_3']").click()
        elif 0.5 < q9 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q9_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q9_5']").click()

        q10 = random()
        if 0 <= q10 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q10_1']").click()
        elif 0.1 < q10 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q10_2']").click()
        elif 0.3 < q10 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q10_3']").click()
        elif 0.5 < q10 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q10_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q10_5']").click()

        q11 = random()
        if 0 <= q11 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q11_1']").click()
        elif 0.1 < q11 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q11_2']").click()
        elif 0.3 < q11 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q11_3']").click()
        elif 0.5 < q11 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q11_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q11_5']").click()

        q12 = random()
        if 0 <= q12 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q12_1']").click()
        elif 0.2 < q12 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q12_2']").click()
        elif 0.3 < q12 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q12_3']").click()
        elif 0.5 < q12 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q12_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q12_5']").click()

        q13 = random()
        if 0 <= q13 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q13_1']").click()
        elif 0.1 < q13 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q13_2']").click()
        elif 0.3 < q13 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q13_3']").click()
        elif 0.5 < q13 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q13_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q13_5']").click()

        q14 = random()
        if 0 <= q14 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q14_1']").click()
        elif 0.1 < q14 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q14_2']").click()
        elif 0.3 < q14 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q14_3']").click()
        elif 0.5 < q14 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q14_4']").click()
        else:


            driver.find_element_by_xpath("//a[@rel='q14_5']").click()

        q15 = random()
        if 0 <= q15 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q15_1']").click()
        elif 0.1 < q15 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q15_2']").click()
        elif 0.3 < q15 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q15_3']").click()
        elif 0.5 < q15 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q15_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q15_5']").click()

        q16 = random()
        if 0 <= q16 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q16_1']").click()
        elif 0.1 < q16 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q16_2']").click()
        elif 0.3 < q16 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q16_3']").click()
        elif 0.5 < q16 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q16_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q16_5']").click()

        q17 = random()
        if 0 <= q17 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q17_1']").click()
        elif 0.1 < q17 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q17_2']").click()
        elif 0.3 < q17 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q17_3']").click()
        elif 0.5 < q17 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q17_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q17_5']").click()

        q18 = random()
        if 0 <= q18 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q18_1']").click()
        elif 0.1 < q18 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q18_2']").click()
        elif 0.3 < q18 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q18_3']").click()
        elif 0.5 < q18 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q18_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q18_5']").click()

        q19 = random()
        if 0 <= q19 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q19_1']").click()
        elif 0.1 < q19 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q19_2']").click()
        elif 0.3 < q19 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q19_3']").click()
        elif 0.5 < q19 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q19_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q19_5']").click()

        q20 = random()
        if 0 <= q20 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q20_1']").click()
        elif 0.1 < q20 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q20_2']").click()
        elif 0.3 < q20 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q20_3']").click()
        elif 0.5 < q20 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q20_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q20_5']").click()

        q21 = random()
        if 0 <= q21 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q21_1']").click()
        elif 0.1 < q21 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q21_2']").click()
        elif 0.3 < q21 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q21_3']").click()
        elif 0.5 < q21 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q21_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q21_5']").click()

        q22 = random()
        if 0 <= q22 <= 0.1:
            driver.find_element_by_xpath("//a[@rel='q22_1']").click()
        elif 0.1 < q22 <= 0.3:
            driver.find_element_by_xpath("//a[@rel='q22_2']").click()
        elif 0.3 < q22 <= 0.5:
            driver.find_element_by_xpath("//a[@rel='q22_3']").click()
        elif 0.5 < q22 <= 0.8:
            driver.find_element_by_xpath("//a[@rel='q22_4']").click()
        else:
            driver.find_element_by_xpath("//a[@rel='q22_5']").click()



        # 模拟点击提交按钮
        driver.find_element_by_xpath("//input[@value='提交']").click()
        time.sleep(0.5)

        # 模拟点击智能验证按钮
        # 先点确认
        driver.find_element_by_xpath("//button[text()='确认']").click()
        # 再点智能验证提示框，进行智能验证
        driver.find_element_by_xpath("//div[@id='captcha']").click()

        # 解决滑块拖动
        pyautogui.keyDown('Enter')
        time.sleep(2)
        cnt = 0
        while True:
            cposition = pyautogui.locateOnScreen('pics/ff5.png')
            if cposition: break
            time.sleep(0.5)
            cnt += 1
            if cnt > 6:
                try:
                    print("无需进行滑块验证")
                    invert_localtor = ("xpath", "//div[@id='ctl01_ContentPlaceHolder1_lbDefault']")
                    time.sleep(2)
                    finished = WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located(invert_localtor)
                    )
                    print('————————第%d页已完成————————' % index)
                    time.sleep(0.5)
                    driver.quit()
                    break
                except:
                    print("元素未等到")
                    print('————————第%d页失败！————————' % index)
                    break

        if cposition:
            print("正在进行滑块验证")
            cc = pyautogui.center(cposition)
            pyautogui.dragRel(256, 0, duration=0.8)
            pyautogui.moveTo(cc[0], cc[1])
            pyautogui.dragRel(320, 0, duration=3)  # duration 也不能太小

            try:
                print("滑块验证成功")
                time.sleep(2)
                finished = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located('//*[@id=”ctl01_ContentPlaceHolder1_lbDefault”]/div')
                )
                print('————————第%d页已完成————————' % index)
                time.sleep(0.5)
                driver.quit()
            except:
                print("滑块验证成功，但元素未等到")
                print('————————第%d页失败！————————' % index)

        # (By.CSS_SELECTOR, "#tbAward > tbody > tr:nth-child(2) > td:nth-child(2) > a")

