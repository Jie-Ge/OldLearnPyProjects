# !/usr/bin/env python
# -*- coding:utf-8 -*-

from GraduationProject.Chaojiying import ChaojiyingClass
import random
import time
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

CHAOJIYING_NAME = '1275556926'  # 超级鹰账号
CHAOJIYING_PWD = '970706'  # 超级鹰密码
CHAOJIYING_ID = 894613  # 软件ID
CHAOJIYING_KIND = 9004  # 验证码类型 (超级鹰上可查到)


class VerificationCode(object):

    def __init__(self, url, chrome_options):
        self.url = url
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_window_position(1000, 10)
        self.chaojiying = ChaojiyingClass(CHAOJIYING_NAME, CHAOJIYING_PWD, CHAOJIYING_ID)

    def __del__(self):
        self.driver.close()

    def screen_shot(self):
        """
        网页截屏
        :return: bool值
        """
        # self.driver.maximize_window()
        time.sleep(2)
        # # 用于网页的向下滚动
        # js = 'var q=document.documentElement.scrollTop=300'
        # self.driver.execute_script(js)
        # time.sleep(1)
        self.driver.save_screenshot('html.png')
        return True

    def shear_location(self, div):
        '''
        计算验证码图片的坐标，注意这里不同电脑可能会修改start_x到end_y
        :param div: 验证码图片div
        :return: 返回图片坐标
        '''
        time.sleep(random.random() + 1)

        # 电脑默认缩放是125%
        start_x = int(div.location['x'] * 1.25)
        start_y = int(div.location['y'] * 1.25)
        end_x = int((div.location['x'] + div.size['width']) * 1.25)
        end_y = int((div.location['y'] + div.size['height']) * 1.25)
        result = (start_x, start_y, end_x, end_y)
        print(result)
        return result

    @staticmethod
    def shear_image(axis):
        im = Image.open('html.png')
        new_image = im.crop(axis)
        new_image.save('new_img.png')
        return new_image

    def upload_picture(self, img, div):
        """
        上传图片(Byte)，返回点击的坐标。这里对返回的坐标进行了处理，
        处理过程可以看成 shear_location 函数的坐标数据逆处理过程
        :param img: 上传的图片
        :param div: 验证码图片div
        :return: 点击坐标
        """
        image = img
        byte_array = BytesIO()
        image.save(byte_array, format('PNG'))
        # 提交图片
        result = self.chaojiying.post_pic(byte_array.getvalue(), CHAOJIYING_KIND)
        print(result)
        if '无可用题分' in result['err_str']:
            print('题分已经不足请充值')
            raise ValueError
        pic_str = result['pic_str']
        pic_list = [[i for i in x.split(',')] for x in pic_str.split('|')]

        # location获取的坐标是按显示100%时得到的坐标, 在shear_location函数中放大了25%
        # 所以，在移动定位时，需要等比缩小25%即可，后边添加的数是根据自己的电脑优化的
        for i in pic_list:
            i[0] = int((int(i[0]) + div.location['x']) * 0.85) - 10
            i[1] = int((int(i[1]) + div.location['y']) * 0.85) + 10
        print(pic_list)
        return pic_list

    def click_now(self, coordinates, axis, element):
        """
        这里如果验证失败会进行回调，实现验证码的自动验证。
        :param coordinates: 点击坐标
        :param axis: 剪切坐标
        :param element: 剪切位置的定位
        :return: 返回点击的成功信息
        """
        print('点击开始')
        print(coordinates)
        for location in coordinates:
            ActionChains(self.driver).move_to_element_with_offset(element, location[0], location[1]).click().perform()
            time.sleep(random.random() + 1.8)

        # submission = self.driver.find_element_by_xpath('//*[@id="btn"]')
        # submission.click()
        # time.sleep(1)

        # 点击验证码后，若成功，则跳转到正常页面，此时获取不到验证码图片，报错
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="imagediv"]/img')))
        except:
            return '点击成功'
        else:
            print('点击失败，正在重新识别新的验证码')
            time.sleep(1)
            self.main()

    def revalidation(self, axis, element):
        """
        网页跳转之后，执行验证的主程序
        :param axis: 剪切坐标
        :param element: 剪切位置的定位对象
        :return: 验证成果
        """
        self.screen_shot()
        if not self.screen_shot():
            return '截图失败'
        time.sleep(1)
        # 剪切图片
        new_image = self.shear_image(axis)

        # 上传图片并返回点击坐标
        click_coordinates = self.upload_picture(new_image, element)
        # 点击验证码
        # 点击坐标
        whole_html = self.driver.find_element_by_tag_name('html')
        print(self.click_now(click_coordinates, axis, whole_html))
        return '点击验证结束'

    def main(self):
        # 等待加载页面（慢）
        self.driver.get(self.url)

        # 以下两句，通过设置等待的方式来避免由于网络延迟或浏览器卡顿导致的偶然失败
        wait = WebDriverWait(self.driver, 10)

        # 获取有'验证码'图片的元素（直到返回值为True）
        element = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="imagediv"]/img')))
        axis = self.shear_location(element)
        self.revalidation(axis, element)


if __name__ == '__main__':
    url1 = 'http://www2.soopat.com'
    # selenium使用代理
    ip = '115.223.7.110:80'
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=%s' % ip)
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    vc = VerificationCode(url1, chrome_options)
    vc.main()