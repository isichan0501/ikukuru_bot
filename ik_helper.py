# -*- coding:utf-8 -*-
# ------------------------------------------------------------------
import sys
from random import choice, uniform
import time
import pathlib
import logging
import logging.config
from contextlib import contextmanager, suppress
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        ElementNotInteractableException,
                                        InvalidArgumentException,
                                        JavascriptException,
                                        NoAlertPresentException,
                                        NoSuchElementException,
                                        StaleElementReferenceException,
                                        TimeoutException)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import socket
import pysnooper
from importlib import reload
import os
# from pyvirtualdisplay import Display
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.proxy import Proxy, ProxyType
import logging

from BotHelper.util_driver import moji_hikaku, page_load, myClick, exe_click, mySendkey, slowClick, my_emojiSend, emoji_convert, add_ifin, send_gmail, mail_what, s3_img
from BotHelper import line_push, writeSheet, change_cell
from dotenv import load_dotenv
import re
import random
import atexit
import json
import datetime

lg = logging.getLogger(__name__)

# 環境変数を参照
load_dotenv()
SHEET_NAME = os.getenv('SHEET_NAME')


class Ikkr:

    def __init__(self, tem_ple):
        """

        Args:
            tem_ple (dict): 

        """
        self.tem_ple = tem_ple
        self.myid = self.tem_ple['ik'].split(':')[0]
        self.mypw = self.tem_ple['ik'].split(':')[1]
        self.cnm = tem_ple['cnm']

        self.action_data = {
            "cnm": tem_ple['cnm'],
            "id_pw": tem_ple['ik'],
            "hajime": 0,
            "asiato": 0,
            "meruado_otosi": 0,
            "gmail": 0
            }


    @pysnooper.snoop()
    @atexit.register
    def notify_bot_log(self):
        message = json.dumps(self.action_data)
        lg.debug(message)
        line_push(message)

        
    def __del__(self):
        self.notify_bot_log()
        
        

    @pysnooper.snoop()
    def login(self, driver):
        wait = WebDriverWait(driver, 10)
        lg.debug(self.tem_ple['cnm'])

        try:
            if '0' == self.myid[0]:
                page_load(
                    driver, "https://www.194964.com/registration/login/show_login_tel.html")
                time.sleep(2)
                if driver.current_url == "https://sp.194964.com/menu.html":
                    return True
            else:
                page_load(
                    driver, "https://www.194964.com/registration/login/show_login_mail.html")
                time.sleep(2)
                if driver.current_url == "https://sp.194964.com/menu.html":
                    return 1
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='form1']/div[1]/div/select")))
                Select(driver.find_element(By.NAME, "mailAddressDomain")
                       ).select_by_visible_text("その他のアドレス")

            mySendkey(
                driver, "xpath", "//*[@id='form1']/div[1]/input", self.myid)
            time.sleep(1)
            mySendkey(
                driver, "xpath", "//*[@id='form1']/div[2]/input", self.mypw)
            time.sleep(1)
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(3)
            if "ログイン失敗" == driver.find_element(By.ID, "title").text:
                imgName = "{0}.png".format(self.myid)
                driver.get_screenshot_as_file(imgName)
                time.sleep(2)
                sub = "{0}:{1} {2} イククル潰れたよ".format(self.myid, self.mypw, self.cnm)
                line_push(sub, imgName)
                ban_text = 'BAN-' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                change_cell(SHEET_NAME, self.tem_ple['ik'], ban_text)
                return False

            with suppress(socket.timeout, NoSuchElementException, TimeoutException, Exception):
                myClick(
                    driver, "xpath", "//*[@id=\"osusumeList\"]//img")
            time.sleep(3)
            return True

        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            raise

    def basyo_change(self, namae):

        if '青森' in namae:
            return 8
        if '岩手' in namae:
            return 9
        if '福島' in namae:
            return 10
        if '秋田' in namae:
            return 11
        if '宮城' in namae:
            return 12
        if '山形' in namae:
            return 13
        if '福井' in namae:
            return 15
        if '新潟' in namae:
            return 16
        if '石川' in namae:
            return 17
        if '富山' in namae:
            return 18
        if '東京' in namae:
            return 20
        if '神奈川' in namae:
            return 21
        if '埼玉' in namae:
            return 22
        if '茨城' in namae:
            return 23
        if '栃木' in namae:
            return 24
        if '群馬' in namae:
            return 25
        if '千葉' in namae:
            return 26
        if '岐阜' in namae:
            return 28
        if '長野' in namae:
            return 29
        if '山梨' in namae:
            return 30
        if '愛知' in namae:
            return 32
        if '静岡' in namae:
            return 33
        if '三重' in namae:
            return 34
        if '奈良' in namae:
            return 38
        if '滋賀' in namae:
            return 39
        if '京都' in namae:
            return 41
        if '広島' in namae:
            return 44
        if '島根' in namae:
            return 45
        if '鳥取' in namae:
            return 46
        if '山口' in namae:
            return 47
        if '愛媛' in namae:
            return 49
        if '高知' in namae:
            return 50
        if '香川' in namae:
            return 51
        if '徳島' in namae:
            return 52

        else:
            return 20

    @pysnooper.snoop()
    def toko_check(self, driver):
        """
        junList = ["今から遊ぼ", "すぐ会いたい", "大人の出会い", "友達・恋人・合コン", "アブノーマル"]
        全ジャンル投稿してたらリターンTrue.
        してなければ、してないジャンルで投稿
        """
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 15)
        lg.debug(self.tem_ple["cnm"])
        junList = ["今から遊ぼ", "すぐ会いたい", "大人の出会い", "友達・恋人・合コン", "アブノーマル"]
        selected_junls = []
        area_list = self.get_area_list()
        basyo = random.choice(area_list)
        random.seed()
        try:
            page_load(driver, "https://sp.194964.com/bbs/show_bbs_write_list.html")
            # 今投稿しているジャンルをチェック

            #まずはピュア募集
            exe_click(driver, "link_text", "ピュア募集")
            junl_elements = driver.find_elements(By.XPATH, "/html/body/article/div[1]/form[1]//div[@class=\'bgMiddle btn\']//p[@class=\'left btnBorderRound\']")
            if len(junl_elements) != 0:
                pure_junls = [jl.text for jl in junl_elements]
                selected_junls.extend(pure_junls)
                
            #大人の募集
            exe_click(driver, "link_text", "大人の募集")
            junl_elements = driver.find_elements(By.XPATH, "/html/body/article/div[1]/form[1]//div[@class=\'bgMiddle btn\']//p[@class=\'left btnBorderRound\']")
            if len(junl_elements) != 0:
                adult_junls = [jl.text for jl in junl_elements]
                selected_junls.extend(adult_junls)
                
            junlSet = set(junList) - set(selected_junls)
            # 全部投稿してたら終了
            if junlSet == set():
                return True
            page_load(
                driver, "https://sp.194964.com/other/area/show_pref_setting_list.html")
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/article/div[1]/span[2]")))
            # myadd = driver.find_element(By.XPATH,
            #                             "/html/body/article/div[1]/span[2]").text
            # if any(map(tem_ple["area"].__contains__, ("名古屋", "愛知", "岐阜", "三重", "長野", "静岡"))):
            #     basyo = random.choice(
            #         [myadd, myadd, myadd, myadd, myadd, myadd, myadd, myadd, "愛知", "愛知", "愛知", "愛知", "長野", "三重", "岐阜", "静岡"])
            # elif any(map(tem_ple["area"].__contains__, ("埼玉", "千葉", "茨城", "栃木", "群馬", "東京"))):
            #     basyo = random.choice(
            #         [myadd, myadd, myadd, myadd, myadd, myadd, myadd, myadd, "埼玉", "埼玉", "埼玉", "茨城", "栃木", "群馬", "千葉", "千葉"])
            # elif any(map(tem_ple["area"].__contains__, ("青森", "岩手", "宮城", "福島", "秋田", "山形"))):
            #     basyo = random.choice(
            #         [myadd, myadd, myadd, myadd, myadd, myadd, myadd, myadd, "宮城", "宮城", "宮城", "青森", "岩手", "福島", "秋田", "山形"])
            # elif any(map(tem_ple["area"].__contains__, ("大阪府", "滋賀県", "京都府", "兵庫県", "奈良県", "和歌山県"))):
            #     basyo = random.choice(
            #         [myadd, myadd, myadd, myadd, myadd, myadd, myadd, myadd, "大阪府", "滋賀県", "京都府", "兵庫県", "奈良県", "和歌山県"])

            # else:
            #     basyo = tem_ple["area"]
            junl = random.choice(list(junlSet))
            tokois = self.toko(driver, basyo, junl)
            if not tokois:
                tokois = self.toko(driver, basyo, junl)

            return False

        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            driver.refresh()
            return False

    # ピュア 今から遊ぼ,友達・恋人・合コン
    # アダルト すぐ会いたい、大人の出会い、アブノーマル

    @pysnooper.snoop()
    def toko(self, driver, basyo, junl):
        wait = WebDriverWait(driver, 10)
        tem_ple = self.tem_ple
        lg.debug(tem_ple["cnm"])
        basyo_num = self.basyo_change(basyo)
        random.seed()
        ik_list = []
        try:
            page_load(driver, "https://sp.194964.com/menu.html")
            time.sleep(2)
            # myClick(driver,"xpath","//*[@id=\"osusumeList\"]//img[@class=\"delButton\"]")
            time.sleep(1)
            slowClick(
                driver, "xpath", "//a[@href='/bbs/show_bbs.html']")
            time.sleep(2)
            driver.refresh()
            time.sleep(1)
            slowClick(driver, "link_text", "地域を移動")
            time.sleep(2)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/article/div/div[20]/a")))
            elm = driver.find_element(
                By.XPATH, "/html/body/article/div/div[{0}]/a".format(int(basyo_num)))
            driver.execute_script("arguments[0].click();", elm)
            time.sleep(2)
            page_load(driver, "https://sp.194964.com/menu.html")
            time.sleep(2)
            # # driver.switch_to.active_element()
            # element = driver.switch_to.active_element
            # element.find_element(By.XPATH, "//*[@id=\"PopupScreen\"]//button[@class=\"close\"]").click()
            # myClick(
            #     driver, "xpath", "//*[@id=\"PopupScreen\"]//button[@class=\"close\"]")
            driver.execute_script("scrollBy(0,800);")
            elm = driver.find_elements(By.LINK_TEXT, "書く")
            if junl == "今から遊ぼ" or junl == "友達・恋人・合コン":
                titles = emoji_convert(tem_ple["title_p"])
                texts = emoji_convert(tem_ple["text_p"])
                ik_list.append(titles)
                ik_list.append(texts)
                elm[0].click()
            else:
                titles = emoji_convert(tem_ple["title_a"])
                texts = emoji_convert(tem_ple["text_a"])
                ik_list.append(titles)
                ik_list.append(texts)
                elm[1].click()
            time.sleep(1)
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located)
            el = driver.find_element(
                By.XPATH, "//span[@class=\"subMenu100\" and contains(text(), \"{0}\")]".format(junl))
            el.click()
            time.sleep(2)
            select = Select(driver.find_element(By.XPATH,
                                                "//*[@id=\"formID\"]/div[1]/select"))
            select.select_by_index(random.randint(
                1, (len(select.options) - 1)))
            my_emojiSend(
                driver, "xpath", "//*[@id='formID']/div[3]/textarea[1]", ik_list[0])
            time.sleep(1)
            my_emojiSend(
                driver, "xpath", "//*[@id='formID']/div[3]/textarea[2]", ik_list[1])
            elm = driver.find_element(By.NAME, "write")
            driver.execute_script("arguments[0].click();", elm)
            time.sleep(3)
            return True
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            driver.refresh()
            return None

    @pysnooper.snoop()
    def retoko(self, driver, pure_adlut=None):
        # ピュアかｱﾀﾞﾙﾄどっちを再投稿するか
        junlnum = random.randint(1, 2)

        if (pure_adlut != None) and (pure_adlut == "pure"):
            junlnum = 1
        if (pure_adlut != None) and (pure_adlut == "adult"):
            junlnum = 2
        wait = WebDriverWait(driver, 10)
        tem_ple = self.tem_ple
        lg.debug(tem_ple["cnm"])
        junl_list = []
        try:
            driver.get("https://sp.194964.com/bbs/show_bbs_write_list.html")
            time.sleep(3)
            basyos = driver.find_elements(By.XPATH, "//span[@class=\"area\"]")
            basyo = basyos[-1].text
            basyo_num = self.basyo_change(basyo)
            driver.get("https://sp.194964.com/menu.html")
            time.sleep(2)
            slowClick(driver, "xpath", "//a[@href='/bbs/show_bbs.html']")
            time.sleep(2)
            slowClick(driver, "link_text", "地域を移動")
            time.sleep(2)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/article/div/div[20]/a")))
            elm = driver.find_element(
                By.XPATH, "/html/body/article/div/div[{0}]/a".format(int(basyo_num)))
            driver.execute_script("arguments[0].click();", elm)
            time.sleep(2)
            driver.get("https://sp.194964.com/bbs/show_bbs_write_list.html")
            time.sleep(4)
            toko_elem = "/html/body/div[4]/div[{0}]/a".format(junlnum)
            exe_click(driver, "xpath", toko_elem)
            time.sleep(2)

            last_toko = driver.find_elements(By.XPATH, "//div[@class=\"bgMiddle btn\"]//div[@class=\"contentsContribute\"]/a")
            driver.execute_script("arguments[0].click();", last_toko[-1])
            time.sleep(2)
            saitoko = driver.find_elements(By.XPATH, "/html/body/article//form/button[@type='submit' and contains(text(), '再投稿する')]")
            if len(saitoko) == 0:
                hensyu = driver.find_elements(By.XPATH, "/html/body/article//form/button[contains(text(), \"編集する\")]")
                if len(hensyu) != 0:
                    hensyu[0].submit()
                    time.sleep(2)
                    exe_click(
                        driver, "xpath", "//*[@id=\"formID\"]/div/button[contains(text(), \"募集する\")]")

                else:
                    #時間制限の確認
                    repost_limit_time = driver.find_element(By.XPATH, "/html/body/article//form[1]/button").text
                    lg.debug(repost_limit_time)
                    if 'から再投稿できます' in repost_limit_time:
                        return True
                    delete_elem = driver.find_elements(
                        By.XPATH, "/html/body/article//form/button[contains(text(), \"削除する\")]")
                    if len(delete_elem) != 0:
                        delete_elem[0].submit()
                        time.sleep(2)
                        delete_elem2 = driver.find_elements(By.XPATH,
                                                            "/html/body/article//form/button[contains(text(), \"削除する\")]")
                        if len(delete_elem2) != 0:
                            delete_elem2[0].submit()
                            time.sleep(2)
            else:
                exe_click(
                    driver, "xpath", "/html/body/article//form/button[@type='submit' and contains(text(), \"再投稿する\")]")
                time.sleep(3)
                select = Select(driver.find_element(By.XPATH,
                                                    "//*[@id=\"formID\"]/div[1]/select"))
                select.select_by_index(random.randint(
                    1, (len(select.options) - 1)))
                time.sleep(2)
                exe_click(
                    driver, "xpath", "//*[@id=\"formID\"]/div[4]/button")
            time.sleep(3)
            return True
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            driver.refresh()
            return None

    @pysnooper.snoop()
    def toko_all_delete(self, driver, del_min=4):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 15)
        lg.debug(tem_ple["cnm"])
        try:
            page_load(
                driver, "https://sp.194964.com/bbs/show_bbs_write_list.html")
            time.sleep(1)
            checks = driver.find_elements(
                By.XPATH, "//div[@class=\"bgMiddle btn\"]//input[@type=\"checkbox\"]")
            # 投稿数が5超えたら全削除
            if len(checks) < int(del_min):
                return None
            for che in checks:
                # che.click()
                driver.execute_script("arguments[0].click();", che)
            time.sleep(1)
            #exe_click(driver, "xpath", "//div[@class=\"bgMiddle\"]//button[contains(text(), \"チェックを削除\")]")
            exe_click(
                driver, "xpath", "//button[contains(text(), \"チェックを削除\")]")
            time.sleep(1)
            exe_click(
                driver, "xpath", "//button[contains(text(), \"削除する\")]")
            time.sleep(1)

        except (socket.timeout, NoSuchElementException, TimeoutException, ElementClickInterceptedException,
                ElementNotInteractableException, Exception) as e:
            lg.exception(e)

    @pysnooper.snoop()
    def user_prof_todb(self, driver, list_you):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 10)
        lg.debug(tem_ple["cnm"])
        ikdict = {'cnm': tem_ple["cnm"], 'kaiwa': list_you}

        try:
            wait.until(EC.presence_of_all_elements_located)
            user_name = driver.find_element(By.ID, "title").text
            ikdict["name"] = user_name
            profs = driver.find_element(By.XPATH, "/html/body/div[6]").text
            profs = profs.split()
            user_age = profs.pop(0)
            ikdict["age"] = user_age
            user_address = profs.pop(0) + profs.pop(0)
            ikdict["address"] = user_address
            user_info = profs
            ikdict["info"] = user_info
            nowdict = self.tb.get((self.Que.name == user_name) & (
                self.Que.age == user_age) & (self.Que.address == user_address))
            if not nowdict:
                self.tb.insert(ikdict)
            else:
                nowdict.update(ikdict)
                self.tb.upsert(nowdict, (self.Que.name == user_name) & (
                    self.Que.age == user_age) & (self.Que.address == user_address))

        except (TypeError, socket.timeout, NoSuchElementException, TimeoutException, Exception) as e:
            lg.exception(e)

    @pysnooper.snoop()
    def memo_mitya(self, driver):
        try:
            driver.execute_script("scrollBy(0,420);")
            exe_click(driver, "xpath", "//*[@id=\"icon-row\"]/a[6]")
            time.sleep(2)
            exe_click(
                driver, "xpath", "//*[@id=\"popup-option\"]/ul[1]/li[1]/a")
            time.sleep(1)
            exe_click(driver, "name", "copy")
            exe_click(
                driver, "xpath", "/html/body/article/div[1]/div[2]/form/div[2]/button")
            time.sleep(2)
            driver.execute_script("scrollBy(0,460);")

            slowClick(driver, "xpath", "//div[2]/div[2]/a/p/span")
            time.sleep(2)
            slowClick(driver, "xpath", "//button[@type='submit']")
            time.sleep(1)
            exe_click(
                driver, "xpath", "//*[@id=\"form1\"]/div[1]/div[2]/p[2]/a")

        except (socket.timeout, NoSuchElementException, TimeoutException, ElementClickInterceptedException,
                ElementNotInteractableException, Exception) as e:
            pass

    @pysnooper.snoop()
    def ik_msg(self, driver, nakami):
        wait = WebDriverWait(driver, 10)
        lg.debug(self.tem_ple['cnm'])
        try:
            # mySendkey(driver,"name","body",nakami)
            my_emojiSend(driver, "name", "body", nakami)
            time.sleep(1)
            exe_click(driver, "id", "sendButton")
            time.sleep(1)
            slowClick(driver, "id", "submitBtn")
            time.sleep(1)
            slowClick(
                driver, "xpath", "//div[@id='popupContent']/div[2]/button")
            time.sleep(2)
            wait.until(EC.presence_of_all_elements_located)
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)

    @pysnooper.snoop()
    def ik_tel(self, driver):
        lg.debug(self.tem_ple['cnm'])
        wait = WebDriverWait(driver, 10)
        try:
            exe_click(driver, "link_text", "電話に誘う")
            # mySendkey(driver,"name","telNumber",id_pw["IK_ID"])
            driver.find_element(By.XPATH,
                                "/html/body/article/div[1]/form/button").submit()

        except TypeError:
            pass

    @pysnooper.snoop()
    def ik_my_send(self, driver):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 10)
        lg.debug(tem_ple["cnm"])
        try:
            # メモがある＝Gメール送った人かどうか確認、送ってたらやめる
            wait.until(EC.presence_of_all_elements_located)
            #me_mo = driver.find_element(By.XPATH, "//p/a/span").text
            # if "メモの確認" in me_mo:
            #    return None
            last_send = driver.find_elements(
                By.XPATH, "//*[@id=\"mailboxList\"]//div")
            namae = driver.find_element(
                By.XPATH, "//*[@id=\"title\"]/ul/li[2]").text
            #namae = namae[1:]
            if len(last_send) == 0:
                asiato = tem_ple['asiato'].replace('namae', namae)
                self.ik_msg(driver, asiato)
                return None

            last_sendd = last_send[-1].get_attribute("class")
            if "OTHER" not in last_sendd.upper():
                return None
            my_send = driver.find_elements(
                By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_owner\"]")
            mylis = [myl.text.replace('★プロフィールから送信', '') for myl in my_send]
            my_receive = driver.find_elements(
                By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_other\"]")
            list_you = [yul.text.replace('★プロフィールから送信', '')
                        for yul in my_receive]

            mylis[-1]
            list_you.extend(mylis)
            mysend = mail_what(
                list_you, tem_ple, namae, asi_if=False, logname="ik")
            if not mysend:
                return None

            self.ik_msg(driver, mysend)
            ikok = moji_hikaku(mysend, tem_ple["after_mail"])
            if ikok:
                self.memo_mitya(driver)
                self.user_prof_todb(driver, tem_ple, list_you)
            return None
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None



    #未読メッセージのみ表示させれないのでメッセージが大量にあった場合にページ移動をうまくするためのヘルパー関数
    @pysnooper.snoop()
    def get_unread_message_count(self, driver):
        """
        Returns:
            int: 未読メッセージ数
        """
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 10)
        try:
            page_load(driver, "https://sp.194964.com/mail/inbox/show_mailbox.html")
            elm = driver.find_element(By.XPATH, "/html/body/nav/div[3]").text
            unread_messege_count = re.sub("\\D", "", elm)
            #なかったら0を返す
            if not unread_messege_count:
                unread_messege_count = 0
            lg.debug('unread message is {}'.format(unread_messege_count))
            return int(unread_messege_count)
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None


    def get_unread_message_count_test(self, driver):
    
        try:
            page_load(driver, "https://sp.194964.com/mail/inbox/show_mailbox.html")
            return 100
            
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None

    @pysnooper.snoop()
    def move_to_page_number(self, driver, page_number):
        """受信メッセージでページ数指定で移動する関数
        
        Args:
            int: 移動するページ
        Returns:
            int: 指定したページのURL
        """
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 10)
        lg.debug('move to page {}'.format(page_number))
        #最初のページで終わりなので
        if page_number == 0:
            return True
            
        try:
            #メッセージページか確認
            if 'mail/inbox/show_mailbox' not in driver.current_url:
                page_load(driver, "https://sp.194964.com/mail/inbox/show_mailbox.html")
            #ページ移動のボタン
            elem = driver.find_elements(By.LINK_TEXT, str(page_number))
            #なければ最終ページへ
            if len(elem) == 0:
                elem = driver.find_elements(By.XPATH, "/html/body/article//li[@class=\"listPaginator2 button\"]/a")
                driver.get(elem[-1].get_attribute('href'))
                self.move_to_page_number(driver, page_number)
            #移動するページのURL
            page_url = elem[0].get_attribute('href')
            page_load(driver, page_url)
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None



    @pysnooper.snoop()
    def ik_mail_new(self, driver):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 10)
        try:
            #未読メッセージ数を取得。0なら終了
            unread_messege_count = self.get_unread_message_count(driver)
            if not unread_messege_count:
                lg.debug('message is end.')
                return True
            
            #1ページに10通メッセージがあるのでunread_messege_count÷10(切り上げ)
            # page_number = -(-unread_messege_count // 10)
            page_number = (unread_messege_count // 10)
            #. +余分に何ページか移動するため.
            #移動ページできるページ数とelemの数が一致する
            elem = driver.find_elements(By.XPATH, "/html/body/article//li[@class=\"listPaginator2 button\"]/a")
            page_number += len(elem)
            #指定した数字(新規メッセージの最終）のページに移動
            self.move_to_page_number(driver, page_number)
            #現在のページURLを取得しておく
            now_url = driver.current_url
            while 0 < page_number:
                #新規メッセージ（NEWアイコンのあるのを選択)
                new_msg_elem = driver.find_elements(By.CLASS_NAME, "icon-new")
                #なければ前のページへ
                if len(new_msg_elem) == 0:
                    #0ページ（最初のページ）で且つnewアイコンもなければ終了
                    if page_number == 0:
                        lg.debug('message is end')
                        return True
                    page_number -= 1
                    self.move_to_page_number(driver, page_number)
                    now_url = driver.current_url
                    continue

                exe_click(driver, "ok", new_msg_elem[-1])
                self.reply_message(driver)
                page_load(driver, now_url)
            
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None

    @pysnooper.snoop()
    def send_email_until_success(self, mailado, kenmei, retry_count=3):
        tem_ple = self.tem_ple
        try:
            #送信に成功したTrueがかえってくる
            for i in range(retry_count):
                is_gmail = send_gmail(tem_ple['formurl'], tem_ple['namae'],tem_ple['money'], mailado, kenmei)
                if is_gmail:
                    lg.debug('gmail to {} is success!'.format(mailado))
                    break
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None
        
    @pysnooper.snoop()
    def reply_message(self, driver):
        """
        メッセージページに移動してから

        Args:
            driver (_type_): _description_

        Returns:
            _type_: _description_
        """
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 10)
        try:
            # メッセージ送信
            wait.until(EC.presence_of_all_elements_located)
            namae = driver.find_element(By.XPATH, "//*[@id=\"title\"]/ul/li[2]").text
            my_send = driver.find_elements(By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_owner\"]")
            meruado = tem_ple['meruado'].replace('namae', namae)
            # もし自分の送信がなければ
            if len(my_send) == 0:
                self.ik_msg(driver, meruado)
                #送信メッセージが増えてるか（増えてなければ連投帰省中）
                my_send_after = driver.find_elements(By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_owner\"]")
                if len(my_send) == len(my_send_after):
                    # lg.debug('連投規制、スリープ２分')
                    # time.sleep(60*2)
                    #スタンプを送って連投規制を回避
                    self.send_stamp(driver)
                    self.ik_msg(driver, meruado)
                
                #行動記録を追加
                self.action_data['meruado_otosi'] += 1
                return None


            send_check = [m.text for m in my_send if moji_hikaku(m.text, meruado)]
            if len(send_check) == 0:
                self.ik_msg(driver, meruado)

                #送信メッセージが増えてるか（増えてなければ連投帰省中）
                my_send_after = driver.find_elements(By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_owner\"]")
                if len(my_send) == len(my_send_after):
                    # lg.debug('連投規制、スリープ２分')
                    # time.sleep(60*2)
                    #スタンプを送って連投規制を回避
                    self.send_stamp(driver)
                    self.ik_msg(driver, meruado)
                #行動記録を追加
                self.action_data['meruado_otosi'] += 1
                return None
            
            last_message = my_send[-1].text.replace('★プロフィールから送信', '')
            if moji_hikaku(last_message, tem_ple["after_mail"]):
                lg.debug('this user after mail sended.')
                return None

            my_receive = driver.find_elements(
                By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_other\"]")
            list_you = [yul.text.replace('★プロフィールから送信', '')
                        for yul in my_receive]
            for r_txt in list_you:
                mailado = add_ifin(r_txt)
                if mailado:
                    kenmei = tem_ple['title_mail'].replace('namae', namae)
                    self.send_email_until_success(mailado, kenmei)
                    self.ik_msg(driver, tem_ple["after_mail"])
                    #送信メッセージが増えてるか（増えてなければ連投帰省中）
                    my_send_after = driver.find_elements(By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_owner\"]")
                    if len(my_send) == len(my_send_after):
                        # lg.debug('連投規制、スリープ２分')
                        # time.sleep(60*2)
                        #スタンプを送って連投規制を回避
                        self.send_stamp(driver)
                        self.ik_msg(driver, tem_ple["after_mail"])
                    #行動記録を追加 
                    self.action_data['gmail'] += 1
                    return None


            return None
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None

        
    @pysnooper.snoop()
    def ik_mail(self, driver):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 10)
        try:
            page_load(driver, "https://sp.194964.com/mail/inbox/show_mailbox.html")
            elm = driver.find_element(By.XPATH, "/html/body/nav/div[3]").text
            ex_mg = re.sub("\\D", "", elm)
            if not ex_mg:
                return True
            for i in range(2, 5, 1):
                if 4 < i:
                    exe_click(driver, "xpath",
                              "/html/body/article/div[1]/div[1]/a")
                    driver.execute_script("scrollBy(0,1200);")
                    wait.until(
                        EC.element_to_be_clickable((By.XPATH, "/html/body/article/div[2]/form[2]/div/button"))).submit()
                    wait.until(EC.presence_of_all_elements_located)
                    wait.until(EC.element_to_be_clickable(
                        (By.XPATH, "/html/body/article/div/form[1]/button"))).submit()
                    wait.until(EC.presence_of_all_elements_located)
                    return True
                driver.execute_script("scrollBy(0,200);")
                new_img = driver.find_elements(
                    By.XPATH, "//div[@class=\"bgMiddle btn \"]//span[@class=\"icon-new-box\"]")
                if not new_img:
                    tugi = driver.find_element(By.LINK_TEXT, "{}".format(i))
                    driver.execute_script("arguments[0].click();", tugi)
                    continue
                else:
                    driver.execute_script("arguments[0].click();", new_img[-1])
                    break

            # メッセージ送信
            wait.until(EC.presence_of_all_elements_located)
            namae = driver.find_element(By.XPATH, "//*[@id=\"title\"]/ul/li[2]").text
            my_send = driver.find_elements(By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_owner\"]")
            meruado = tem_ple['meruado'].replace('namae', namae)
            # もし自分の送信がなければ
            if len(my_send) == 0:
                self.ik_msg(driver, meruado)
                #送信メッセージが増えてるか（増えてなければ連投帰省中）
                my_send_after = driver.find_elements(By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_owner\"]")
                if len(my_send) == len(my_send_after):
                    # lg.debug('連投規制、スリープ２分')
                    # time.sleep(60*2)
                    #スタンプを送って連投規制を回避
                    self.send_stamp(driver)
                    self.ik_msg(driver, meruado)
                
                #行動記録を追加
                self.action_data['meruado_otosi'] += 1
                return None


            send_check = [m.text for m in my_send if moji_hikaku(m.text, meruado)]
            if len(send_check) == 0:
                self.ik_msg(driver, meruado)

                #送信メッセージが増えてるか（増えてなければ連投帰省中）
                my_send_after = driver.find_elements(By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_owner\"]")
                if len(my_send) == len(my_send_after):
                    # lg.debug('連投規制、スリープ２分')
                    # time.sleep(60*2)
                    #スタンプを送って連投規制を回避
                    self.send_stamp(driver)
                    self.ik_msg(driver, meruado)
                #行動記録を追加
                self.action_data['meruado_otosi'] += 1
                return None
            
            last_message = my_send[-1].text.replace('★プロフィールから送信', '')
            if moji_hikaku(last_message, tem_ple["after_mail"]):
                lg.debug('this user after mail sended.')
                return None

            my_receive = driver.find_elements(
                By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_other\"]")
            list_you = [yul.text.replace('★プロフィールから送信', '')
                        for yul in my_receive]
            for r_txt in list_you:
                mailado = add_ifin(r_txt)
                if mailado:
                    kenmei = tem_ple['title_mail'].replace('namae', namae)
                    send_gmail(tem_ple['formurl'], tem_ple['namae'],tem_ple['money'], mailado, kenmei)
                    self.ik_msg(driver, tem_ple["after_mail"])
                    #送信メッセージが増えてるか（増えてなければ連投帰省中）
                    my_send_after = driver.find_elements(By.XPATH, "//*[@id=\"mailboxList\"]//div[@class=\"bubble_owner\"]")
                    if len(my_send) == len(my_send_after):
                        # lg.debug('連投規制、スリープ２分')
                        # time.sleep(60*2)
                        #スタンプを送って連投規制を回避
                        self.send_stamp(driver)
                        self.ik_msg(driver, tem_ple["after_mail"])
                    #行動記録を追加 
                    self.action_data['gmail'] += 1
                    return None


            return None
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None


    def send_stamp(self, driver):
        """
        メッセージ送受信ページで使う
        """
        wait = WebDriverWait(driver, 10)
        lg.debug('stamp')
        try:
            #スタンプボタンを押す
            exe_click(driver, "xpath", "//*[@id=\"icon-row\"]/a[3]")

            #スタンプ履歴、猫スタンプ、ハムスタースタンプと選択肢があって最後のスタンプを選択
            exe_click(driver, "xpath", "//*[@id=\"popupStampBox\"]/div[3]/ul/li[4]/a")
            #スタンプのリストから選択,１ページ目に８個ある
            random_stamp_number = random.randint(1,8)
            #ランダムで選択
            elem = "//*[@id=\"popupStampBox\"]/div[2]/div/a[{}]".format(random_stamp_number)
            exe_click(driver, "xpath", elem)
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)

# 0,足跡があるかないか
# 1,足跡なし　＝　足跡送信
# 2,足跡あり　＝　メルアド落としあるか確認
# 2-1,足跡有でメルアド落としなし　＝＝　メルアド落とし
# 2-2,足跡有でメルアド落とし有　＝＝　メルアドあるか確認
# 2-2-1,足跡有でメルアド落とし有でメルアドなし　＝＝　何もしない
# 2-2-2,足跡有でメルアド落とし有でメルアド有　＝＝　見ちゃいや確認(メモ)
# 2-2-2-1,足跡有でメルアド落とし有でメルアド有で見ちゃいや（メモ）なし　＝＝　gmail送信で見ちゃいや（メモ）
# 2-2-2-2,足跡有でメルアド落とし有でメルアド有で見ちゃいや（メモ）有　＝＝　何もしない

    @pysnooper.snoop()
    def search_user(self, driver, ppn):
        tem_ple = self.tem_ple

        wait = WebDriverWait(driver, 10)
        try:
            page_load(driver, "https://sp.194964.com/profile/profilesearch/show_profile_search.html")
            exe_click(driver, "id", "input_search_outer")
            exe_click(driver, "xpath", "(//a[contains(text(),\"プロフィールを見る\")])[{0}]".format(ppn))
            time.sleep(2)
            # 履歴確認
            history_btn = driver.find_element(
                By.XPATH, "*//div[@class=\"user-profile-btn-history\"]").get_attribute('style')
            if "none" not in history_btn:
                lg.debug('this user exist history. return')
                return None
            namae = driver.find_element(By.ID, "titleNickname").text
            hajime = tem_ple["hajime"].replace('namae', namae)

            #send message
            exe_click(driver, "id", "messageBtn")
            time.sleep(2)
            my_emojiSend(driver, "id", "send-message", hajime)
            time.sleep(1)
            exe_click(driver, "xpath","//*[@id=\"submitMessageButton\"]/button")
            time.sleep(1)
            self.action_data['hajime'] += 1
            # exe_click(driver,"link_text","あしあとを残す")
            # exe_click(driver,"xpath","//div[@id='popupContent']/div/button")
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)


    @pysnooper.snoop()
    def asiato_kaesi(self, driver, ppn):
        """
        ppnは足跡ページのユーザーリストの何番目のユーザーを選択するか
        10から2の間で
        """
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 10)
        res_word = ""
        try:
            page_load(driver, "https://sp.194964.com/sns/snsashiato/show.html")
            wait.until(EC.presence_of_all_elements_located)
            #userの個別ページへ
            user_link = driver.find_element(By.XPATH, "//*[@id=\"tab1\"]/div[{}]/a".format(ppn))
            exe_click(driver, "ok", user_link)
            time.sleep(2)
            # 履歴確認
            history_btn = driver.find_element(
                By.XPATH, "*//div[@class=\"user-profile-btn-history\"]").get_attribute('style')
            if "none" not in history_btn:
                lg.debug('this user exist history. return')
                return None
            namae = driver.find_element(By.ID, "titleNickname").text
            asiato = tem_ple["asiato"].replace('namae', namae)

            #send message
            exe_click(driver, "id", "messageBtn")
            time.sleep(2)
            my_emojiSend(driver, "id", "send-message", asiato)
            time.sleep(1)
            exe_click(driver, "xpath","//*[@id=\"submitMessageButton\"]/button")
            time.sleep(1)
            self.action_data['asiato'] += 1
            # exe_click(driver,"link_text","あしあとを残す")
            # exe_click(driver,"xpath","//div[@id='popupContent']/div/button")
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)



    @pysnooper.snoop()
    def asiato_newface(self, driver, ppn):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 10)
        res_word = ""
        try:
            page_load(driver, "https://sp.194964.com/sns/snsashiato/show.html")
            wait.until(EC.presence_of_all_elements_located)
            new_faces = driver.find_elements(
                By.XPATH, "//*[@id=\"tab1\"]//div[@class=\"type-list-name\"]/img")
            try:
                new_face = new_faces[ppn]
            except IndexError:
                return True
            exe_click(driver, "ok", new_faces[ppn])
            time.sleep(2)
            # 履歴確認
            history_btn = driver.find_element(
                By.XPATH, "*//div[@class=\"user-profile-btn-history\"]").get_attribute('style')
            if "none" not in history_btn:
                print('this user exist history. return')
                return None
            namae = driver.find_element(By.ID, "titleNickname").text
            asiato = tem_ple["asiato"].replace('namae', namae)

            msgbtn = driver.find_elements(By.ID, "messageBtn")
            if len(msgbtn) == 0:
                return None
            exe_click(driver, "id", "messageBtn")
            time.sleep(2)
            # 相手が年齢確認してないと定型文以外送れないので定型文を選択
            exe_click(driver, "id", "message-d-1")
            # my_emojiSend(driver, "id", "send-message", asiato)
            time.sleep(1)
            exe_click(driver, "xpath","//*[@id=\"submitMessageButton\"]/button")
            time.sleep(1)
            # 0,足跡があるかないか
            return None
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None

    @pysnooper.snoop()
    def yaungik_asi(self, driver, ppn):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 10)
        try:
            page_load(driver, "https://sp.194964.com/menu.html")
            slowClick(driver, "xpath", "//a[2]/img")
            wait.until(EC.presence_of_all_elements_located)
            yaunglist = []
            agelist = driver.find_elements(
                By.XPATH, "//*[@id=\"tab1\"]//div[@class=\"type-list-age\"]")
            for a in range(len(agelist)):
                ages = re.sub("\\D", "", agelist[a].text)
                if int(ages) < 35:
                    yaunglist.append(agelist[a])
            try:
                a = yaunglist[ppn]
            except IndexError:
                return True
            driver.execute_script("arguments[0].click();", yaunglist[ppn])
            time.sleep(2)
            namae = driver.find_element(By.ID, "titleNickname").text
            asiato = tem_ple["asiato"].replace('namae', namae)

            msgbtn = driver.find_elements(By.ID, "messageBtn")
            if len(msgbtn) == 0:
                return None
            exe_click(driver, "id", "messageBtn")
            time.sleep(2)
            mySendkey(driver, "id", "send-message", asiato)
            time.sleep(1)
            exe_click(
                driver, "xpath", "//*[@id=\"submitMessageButton\"]/button")
            time.sleep(1)
            return None
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None

    @pysnooper.snoop()
    def delete_mitya(self, driver):
        wait = WebDriverWait(driver, 10)
        try:
            driver.get(
                "https://sp.194964.com/sns/snsmylist/show_notsees_list.html")
            time.sleep(5)
            miruna = driver.find_element(By.ID, "title").text
            miruna = miruna.split('/')
            miruna_num = re.sub("\\D", "", miruna[0])
            if int(miruna_num) < 30:
                return
            else:
                exe_click(driver, "link_text", "次を表示")
                exe_click(driver, "link_text", "次を表示")
                for ch in range(1, 10, 1):
                    exe_click(
                        driver, "xpath", "//form[@id='form1']/div[{0}]/div[2]/p/label/span".format(ch))

                exe_click(driver, "xpath", "//button[@type='submit']")
                time.sleep(3)
                exe_click(driver, "xpath", "//button[@type='submit']")

        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)

    @pysnooper.snoop()
    def asipeta(self, driver, ppn):

        wait = WebDriverWait(driver, 10)
        try:
            page_load(driver, "https://sp.194964.com/profile/profilesearch/show_profile_search.html")
            exe_click(driver, "id", "input_search_outer")
            exe_click(driver, "xpath", "(//a[contains(text(),\"プロフィールを見る\")])[{0}]".format(ppn))
            time.sleep(random.randint(8, 16))
            # exe_click(driver,"link_text","あしあとを残す")
            # exe_click(driver,"xpath","//div[@id='popupContent']/div/button")
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)

    # S3から画像をもってきてプロフに

    @pysnooper.snoop()
    def ik_profimg(self, driver):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 15)
        lg.debug(tem_ple["cnm"])
        try:
            page_load(driver, "https://sp.194964.com/mypage.html")
            noimg = driver.find_element(By.XPATH, "//*[@id=\"prof\"]//div[@class=\"profile-thumb\"]/img").get_attribute(
                "src")
            if "no-img" not in str(noimg):
                return True
            else:
                page_load(
                    driver, "https://sp.194964.com/sns/snssetting/show_image_register.html")
                eximg = driver.find_elements(
                    By.XPATH, "//*[@id='profileWarningBefore']/div")
                ex_num = re.sub("\\D", "", eximg[0].text)
                if ex_num != "3":
                    return None
                myimg = s3_img()
                # imgpath = "./{0}".format(myimg)
                # imgok = os.path.abspath(imgpath)
                driver.find_element(By.ID, "fileupload").send_keys(myimg)
                time.sleep(5)
                wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//*[@id='profile_preview_message']/div/button"))).submit()
                time.sleep(3)

            return False
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return False

    @pysnooper.snoop()
    def prof_text(self, driver):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 15)
        lg.debug(tem_ple["cnm"])
        random.seed()
        proftext = tem_ple["prof"].strip()
        try:
            page_load(
                driver, "https://sp.194964.com/sns/snssetting/show_edit_profile_intro.html")
            time.sleep(1)
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/article/form/div/div[1]/textarea")))
            word_a = driver.find_element(
                By.XPATH, "/html/body/article/form/div/div[1]/textarea").text
            word_b = proftext
            profok = moji_hikaku(word_a, word_b)
            if profok == True:
                return True
            wait.until(
                EC.presence_of_element_located((By.XPATH, "/html/body/article/form/div/div[1]/textarea"))).clear()
            my_emojiSend(
                driver, "xpath", "/html/body/article/form/div/div[1]/textarea", proftext)
            time.sleep(1)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/article/form/div/div[3]/button"))).submit()
            time.sleep(2)

            return True
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None

    @pysnooper.snoop()
    def ik_prof1(self, driver):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 15)
        lg.debug(tem_ple["cnm"])
        random.seed()
        if (tem_ple["height"] == '') or isinstance(tem_ple["height"], float):
            tem_ple["height"] = "155～159"
        if (tem_ple["style"] == '') or isinstance(tem_ple["style"], float):
            tem_ple["style"] = "普通"
        if (tem_ple["marriage"] == '') or isinstance(tem_ple["marriage"], float):
            tem_ple["marriage"] = "未婚"

        age_str = str(int(tem_ple["age"])).strip()
        myage = age_str + "歳"
        print(myage)
        try:
            page_load(
                driver, "https://sp.194964.com/config/settingprof/show_profile_setting.html")
            time.sleep(2)
            wait.until(EC.element_to_be_clickable((By.NAME, "name")))
            myname = driver.find_element(
                By.NAME, "name").get_attribute("Value")


            if tem_ple["myname"] != myname:
                mySendkey(driver, "name", "name", tem_ple["myname"])
            #age --
            # select = Select(driver.find_element(By.NAME, "age"))
            # age_now = select.all_selected_options[0].text
            # if myage == age_now:
            #     print('age ok')
            # else:
            #     select.select_by_visible_text(myage)

            # if (tem_ple["myname"] == myname) and (myage == age_now):
            #     print('prof name and age ok. return True')
            #     return True
            with suppress(NoSuchElementException):
                Select(driver.find_element(By.NAME, "height")
                       ).select_by_visible_text(tem_ple["height"])
            with suppress(NoSuchElementException):
                Select(driver.find_element(By.NAME, "style")
                       ).select_by_visible_text(tem_ple["style"])
            with suppress(NoSuchElementException):
                bloodtype = random.choice(range(4))
                select = Select(driver.find_element(By.NAME, "blood"))
                select.select_by_index(bloodtype)
            with suppress(NoSuchElementException):
                select = Select(driver.find_element(By.NAME, "looks"))
                max_select = len(select.options) - 1
                sind = random.randint(1, max_select)
                select.select_by_index(sind)
            with suppress(NoSuchElementException):
                Select(driver.find_element(By.NAME, "married")
                       ).select_by_visible_text(tem_ple["marriage"])

            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/article/div/form//button[contains(text(), \"更新する\")]"))).submit()
            time.sleep(4)

            return True
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)

    @pysnooper.snoop()
    def ik_prof2(self, driver):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 15)
        lg.debug(tem_ple["cnm"])
        myjob = str(tem_ple["ik_job"])
        random.seed()
        try:
            page_load(
                driver, "https://sp.194964.com/sns/snssetting/show_edit_profile.html")
            # with suppress(NoSuchElementException):
            #     select = Select(driver.find_element(By.NAME, "birthCity"))
            #     max_select = len(select.options) - 1
            #     sind = random.randint(1, max_select)
            #     select.select_by_index(sind)
            select = Select(driver.find_element(By.NAME, "occupation"))
            job_now = select.all_selected_options[0].text
            
            if myjob == job_now:
                print('job ok.return True')
                return True
            else:
                select.select_by_visible_text(myjob)
            with suppress(NoSuchElementException):
                Select(driver.find_element(By.NAME,
                                           "income")).select_by_index(0)
            with suppress(NoSuchElementException):
                select = Select(driver.find_element(By.NAME, "constellation"))
                max_select = len(select.options) - 1
                sind = random.randint(1, max_select)
                select.select_by_index(sind)
            with suppress(NoSuchElementException):
                Select(driver.find_element(By.NAME, "cigarette")
                       ).select_by_visible_text("吸わない")
            with suppress(NoSuchElementException):
                Select(driver.find_element(By.NAME,
                                           "alcohol")).select_by_index(0)
            with suppress(NoSuchElementException):
                Select(driver.find_element(By.NAME, "child")
                       ).select_by_visible_text("いない")
            with suppress(NoSuchElementException):
                Select(driver.find_element(By.NAME, "eyes")
                       ).select_by_visible_text("二重")
            with suppress(NoSuchElementException):
                Select(driver.find_element(By.NAME,
                                           "freeTime")).select_by_index(-1)
            with suppress(NoSuchElementException):
                Select(driver.find_element(By.NAME,
                                           "ageFrom")).select_by_index(1)
            with suppress(NoSuchElementException):
                Select(driver.find_element(By.NAME, "ageTo")).select_by_index(10)
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/article/form/div//button[contains(text(), \"更新する\")]"))).submit()
            time.sleep(2)

        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)

    @pysnooper.snoop()
    def ik_basyo(self, driver):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 15)
        lg.debug(tem_ple["cnm"])
        random.seed()
        try:
            page_load(driver, "https://sp.194964.com/other/area/show_pref_setting_list.html")
            time.sleep(2)
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, "/html/body/article/div[1]/span[2]")))
            basyo = tem_ple["area"].strip()
            bnm = int(self.basyo_change(basyo)) - 1
            elem = "/html/body/article/div[2]/div[{0}]/a".format(bnm)
            exe_click(driver, "xpath", elem)
            time.sleep(3)
            lens = driver.find_elements(By.XPATH,
                                        "/html/body/article/div[2]/div")
            max_len = len(lens) - 1
            myRum = random.choice(range(1, max_len))
            elem = "/html/body/article/div[2]/div[{0}]/a".format(myRum)
            exe_click(driver, "xpath", elem)
            time.sleep(3)

            return True
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)

    @pysnooper.snoop()
    def ik_prof_basyo(self, driver):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 15)
        lg.debug(tem_ple["cnm"])
        random.seed()
        area_list = self.get_area_list()
        basyo = random.choice(area_list)
        # myadd = tem_ple["area"]
        # if any(map(tem_ple["area"].__contains__, ("名古屋", "愛知", "岐阜", "三重", "長野", "静岡", "愛知県", "岐阜県", "三重県", "長野県", "静岡県"))):
        #     basyo = random.choice(
        #         [myadd, myadd, myadd, myadd, myadd, myadd, myadd, myadd, "愛知", "愛知", "愛知", "愛知", "長野", "三重", "岐阜",
        #          "静岡"])
        # elif any(map(tem_ple["area"].__contains__, ("神奈川", "埼玉", "千葉", "茨城", "栃木", "群馬", "東京", "埼玉県", "千葉県", "茨城県", "栃木県", "群馬県", "東京都", "神奈川県"))):
        #     basyo = random.choice(
        #         [myadd, myadd, myadd, myadd, myadd, myadd, myadd, myadd, "神奈川", "神奈川", "埼玉", "埼玉", "埼玉", "茨城", "栃木", "群馬", "千葉",
        #          "千葉"])

        # elif any(map(tem_ple["area"].__contains__, ("青森", "岩手", "宮城", "福島", "秋田", "山形"))):
        #     basyo = random.choice(
        #         [myadd, myadd, myadd, myadd, myadd, myadd, myadd, myadd, "宮城", "宮城", "宮城", "青森", "岩手", "福島", "秋田",
        #          "山形"])
        # elif any(map(tem_ple["area"].__contains__, ("大阪府", "滋賀県", "京都府", "兵庫県", "奈良県", "和歌山県"))):
        #     basyo = random.choice(
        #         [myadd, myadd, myadd, myadd, myadd, myadd, myadd, myadd, "大阪府", "滋賀県", "京都府", "兵庫県", "奈良県", "和歌山県"])

        # else:
        #     basyo = tem_ple["area"]

        try:
            #プロフ検索で探す相手の場所を設定
            driver.get("https://sp.194964.com/profile/profilesearch/show_profile_search.html")
            time.sleep(4)
            exe_click(driver, "id", "city_button")
            time.sleep(4)
            #もし既に検索地域が設定されていたら削除
            pref_elem = driver.find_elements(
                By.XPATH, "/html/body/article//input[@name='prefAndCity[]']")
            if len(pref_elem) != 0:
                exe_click(driver, "xpath", "/html/body/article//input[@name='prefAndCity[]']")
                time.sleep(1)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='prefAndCity']/div[2]/button"))).submit()
                time.sleep(2)
                exe_click(driver, "id", "city_button")
                time.sleep(2)
            bnm = int(self.basyo_change(basyo)) + 3
            elem = "/html/body/article/div[1]/div[{0}]/a".format(bnm)
            exe_click(driver, "xpath", elem)
            time.sleep(3)
            driver.find_element(By.ID, "checkbox1").click()
            driver.execute_script("scrollBy(0,1200);")
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='form1']/div[2]/button"))).submit()
            wait.until(EC.presence_of_all_elements_located)
            # time.sleep(3)
            #Select(driver.find_element(By.NAME, "ageTo")).select_by_index(3)
            time.sleep(2)
            exe_click(driver, "id", "input_search_outer")
            return True
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)


    @pysnooper.snoop()
    def get_area_list(self):
        tem_ple = self.tem_ple
        lg.debug(tem_ple["cnm"])
        myadd = tem_ple["area"]
        if any(map(tem_ple["area"].__contains__, ("名古屋", "愛知", "岐阜", "三重", "長野", "静岡", "愛知県", "岐阜県", "三重県", "長野県", "静岡県"))):
            area_list = ['愛知', '静岡', '岐阜', '三重', '長野']
        elif any(map(tem_ple["area"].__contains__, ("神奈川", "埼玉", "千葉", "茨城", "栃木", "群馬", "東京", "埼玉県", "千葉県", "茨城県", "栃木県", "群馬県", "東京都", "神奈川県"))):
            area_list = ['神奈川', '埼玉', '千葉', '東京', '群馬', '茨城', '栃木']

        elif any(map(tem_ple["area"].__contains__, ("青森", "岩手", "宮城", "福島", "秋田", "山形"))):
            area_list = ['青森', '岩手', '宮城', '福島', '秋田', '山形']
        elif any(map(tem_ple["area"].__contains__, ("大阪府", "滋賀県", "京都府", "兵庫県", "奈良県", "和歌山県"))):
            area_list = ['大阪', '滋賀', '京都', '兵庫', '奈良', '和歌山']

        elif any(map(tem_ple["area"].__contains__, ("石川県", "富山県", "福井県", "新潟県", "山梨県"))):
            area_list = ["石川県", "富山県", "福井県", "新潟県", "山梨県"]
        elif tem_ple["area"] == "福島県":
            ["福島県", "山形県", "栃木県", "新潟県", "茨城県"]
        else:
            area_list = [myadd]

        return area_list
        
    @pysnooper.snoop()
    def ik_change_search_prof_area(self, driver):
        """
        地域を複数選択するように変更。
        東海地方なら　愛知、岐阜、三重、静岡、長野
        """
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 15)
        lg.debug(tem_ple["cnm"])
        random.seed()
        area_list = self.get_area_list()
        #basyo = random.choice(area_list)
        # myadd = tem_ple["area"]
        # if any(map(tem_ple["area"].__contains__, ("名古屋", "愛知", "岐阜", "三重", "長野", "静岡", "愛知県", "岐阜県", "三重県", "長野県", "静岡県"))):
        #     area_list = ['愛知', '静岡', '岐阜', '三重', '長野']
        # elif any(map(tem_ple["area"].__contains__, ("神奈川", "埼玉", "千葉", "茨城", "栃木", "群馬", "東京", "埼玉県", "千葉県", "茨城県", "栃木県", "群馬県", "東京都", "神奈川県"))):
        #     area_list = ['神奈川', '埼玉', '千葉', '三重', '東京', '群馬', '茨城', '栃木']

        # elif any(map(tem_ple["area"].__contains__, ("青森", "岩手", "宮城", "福島", "秋田", "山形"))):
        #     area_list = ['青森', '岩手', '宮城', '福島', '秋田', '山形']
        # elif any(map(tem_ple["area"].__contains__, ("大阪府", "滋賀県", "京都府", "兵庫県", "奈良県", "和歌山県"))):
        #     area_list = ['大阪', '滋賀', '京都', '兵庫', '奈良', '和歌山']

        # else:
        #     area_list = [myadd]
        try:
            #プロフ検索で探す相手の場所を設定
            driver.get("https://sp.194964.com/profile/profilesearch/show_profile_search.html")
            time.sleep(4)
            exe_click(driver, "id", "city_button")
            time.sleep(4)
            #すでに設定されていたら終了
            area_text_element = driver.find_elements(By.ID, "prefAndCity")
            if len(area_text_element) != 0:
                area_text = area_text_element[0].text
                area_check = [basyo for basyo in area_list if basyo in area_text]
                #area_listの中で選択されてないのだけに絞る
                area_list = list(set(area_list) - set(area_check))
                if len(area_list) == 0:
                    print('area ok.return True')
                    return True
                
                
            #もし既に検索地域が設定されていたら削除
            pref_elem = driver.find_elements(By.XPATH, "/html/body/article//input[@name='prefAndCity[]']")
            if len(pref_elem) == 1:
                exe_click(driver, "xpath", "/html/body/article//input[@name='prefAndCity[]']")
                time.sleep(1)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='prefAndCity']/div[2]/button"))).submit()
                time.sleep(2)
                exe_click(driver, "id", "city_button")
                time.sleep(2)

            #area_listの地域全部追加
            for basyo in area_list:
                city_btn = driver.find_elements(By.ID, "city_button")
                if len(city_btn) != 0:
                    exe_click(driver, "id", "city_button")
                
                change_city_btn = driver.find_elements(By.ID, "btnChange")
                if len(change_city_btn) != 0:
                    exe_click(driver, "id", "btnChange")
                
                bnm = int(self.basyo_change(basyo)) + 3
                elem = "/html/body/article/div[1]/div[{0}]/a".format(bnm)
                exe_click(driver, "xpath", elem)
                time.sleep(3)
                is_check = driver.find_element(By.ID, "checkbox1").get_attribute('checked')
                if not is_check:
                    driver.find_element(By.ID, "checkbox1").click()
                driver.execute_script("scrollBy(0,1200);")
                wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='form1']/div[2]/button"))).submit()
                wait.until(EC.presence_of_all_elements_located)
                time.sleep(2)
            # time.sleep(3)
            #Select(driver.find_element(By.NAME, "ageTo")).select_by_index(3)

            search_profile_element = driver.find_elements(By.LINK_TEXT, "プロフィール検索")
            if len(search_profile_element) != 0:
                exe_click(driver, "LINK_TEXT", "プロフィール検索")
            time.sleep(2)
            exe_click(driver, "id", "input_search_outer")
            return True
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)



    @pysnooper.snoop()
    def ik_aitai(self, driver):
        tem_ple = self.tem_ple
        wait = WebDriverWait(driver, 10)
        lg.debug(tem_ple["cnm"])
        try:
            page_load(driver, "https://sp.194964.com/mypage.html")
            time.sleep(5)
            exe_click(driver, "id", "btn-meetday")
            time.sleep(2)
            wait.until(EC.presence_of_all_elements_located)
            time.sleep(2)
            aitai = driver.find_elements(
                By.XPATH, "//*[@id=\"calendar\"]//span[@class=\"fc-day-number selectDate\"]")
            elem = driver.find_elements(By.XPATH,
                                        "//*[@id=\"calendar\"]//td[contains(@class, \"fc-future\")]/span")
            for ele in elem:
                ele.click()
            # slowClick(driver,"ok",elem[0])
            time.sleep(1)
            slowClick(driver, "id", "saveBtn")
            time.sleep(5)
            # element = driver.switch_to.active_element
            # element.find_element(By.ID, "successCalendar").click()

            #slowClick(driver, "id", "successCalendar")
            time.sleep(3)
            return None
        except (socket.timeout, NoSuchElementException, TimeoutException,
                ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
            lg.exception(e)
            return None

    @pysnooper.snoop()
    def toko_mitya_check(self, driver):
        self.toko_all_delete(driver)
        tockis = self.toko_check(driver)
        if not tockis:
            retois = self.retoko(driver)
            if not retois:
                retois = self.retoko(driver)
        self.delete_mitya(driver)
