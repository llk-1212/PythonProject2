from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains, chrome
import time
class fe():
    driver = webdriver.Chrome()
    # 打开首页
    url = 'https://love.alipay.com/donate/itemDetail.htm?name=2014010616214122130'
    driver.get(url)
    name = driver.find_element_by_class_name('fn-left.donate-detail-title').text
    pri = driver.find_element_by_class_name('ft-amount-16.ft-orange.ft-bold').text
    yi = driver.find_element_by_class_name('ft-green').text
    ji = driver.find_element_by_class_name('donate-list-info-puborg-text').text
    p = driver.find_elements_by_class_name('donate-list-info.donate-info-content-item')
    i = 1
    for ip in p:
        if len(ip.find_elements_by_xpath('.//*')) == 0 and i == 1:
            bai = ip.text
            i = 3
        if len(ip.find_elements_by_xpath('.//*')) == 0 and i == 3:
            shi = ip.text
            print(shi)
    print("项目名称： %s,已筹:  %s  元,%s, 捐款人次:  %s 次,%s,%s" % (name, pri, bai, yi, shi, ji))
    xiang = driver.find_element_by_id('J-intro')
    xiangm = xiang.find_elements_by_xpath('.//*')
    for xiangd in xiangm:
        if xiangd.tag_name == 'div':
            ur = xiangd.find_element_by_css_selector('img').get_attribute('src')
            print(ur)
        else:
            print(xiangd.text)
    driver.find_element_by_id('J-Desc1').click()
    a = driver.find_element_by_class_name('ui-page').find_elements_by_xpath('.//*')
    for ad in a:
        if ad.tag_name == 'span':
            feed = driver.find_element_by_id('J-feed-list').find_elements_by_css_selector('li')
            for fel in feed:
                te = fel.find_element_by_xpath('.//h4').text
                tex = fel.find_element_by_class_name('donate-detail-application-text-small').text
                print(te)
                print(tex)
                ur = fel.find_element_by_class_name('donate-detail-application-img-small')
                if len(ur.find_elements_by_xpath('.//*')) != 0:
                    urs = ur.find_elements_by_xpath('.//*')
                    for ursl in urs:
                        url = ursl.find_element_by_css_selector('img').get_attribute('src')
                        print(url)



if __name__ == '__main__':
    fe()