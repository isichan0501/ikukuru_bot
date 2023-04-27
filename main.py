<<<<<<< HEAD
# -*- coding:utf-8 -*-
from ctypes import util
import pandas as pd
import time
from BotHelper import JsonSearch, get_sheet_with_pd, set_sheet_with_pd, line_push, writeSheet
from BotHelper.util_driver import compose_driver, twitter_login, ouath_twitter_not_login, http_check, wifi_reboot, check_ip, s3_img
from BotHelper.util_driver import moji_hikaku, page_load, myClick, exe_click, mySendkey, slowClick, my_emojiSend, emoji_convert, add_ifin, send_gmail, mail_what, s3_img
import pysnooper
from importlib import reload
import os
import sys
from contextlib import contextmanager

from dotenv import load_dotenv
import logging

import ik_helper_pc as ik_helper
# import ik_helper
from ChatBotHelper.util_chat import ChatbotUtil
#-----------debug-----
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



from BotHelper.util_driver import page_load, myClick, exe_click, mySendkey,send_gmail
#-----debug---------



logging.config.fileConfig('logconf.ini')
lg = logging.getLogger(__name__)



# 環境変数を参照
load_dotenv()
API_URL = os.getenv('API_URL')
CHROME_PROFILE_DIR = os.getenv('CHROME_PROFILE_DIR')
SHEET_NAME = os.getenv('SHEET_NAME')



@contextmanager
def driver_set(prox=False, profdir=None, prof_name=None, ua_name=None):

    driver = compose_driver(proxy_info=prox, userdata_dir=profdir, use_profile=prof_name, use_ua=ua_name)
    try:
        yield driver
    finally:
        driver.quit()

        


def main(tem_ple):

    with driver_set(prox=False, profdir=None, prof_name=None, ua_name=tem_ple['ua']) as driver:

        #まずはwifi再起動
        wifi_reboot(driver)
        is_reboot = http_check(driver)

        
        ik = ik_helper.Ikkr(tem_ple)
        is_login = ik.login(driver)
        if not is_login:
            return False

        #画像設定されていたらTrue、その場合のみ投稿やメッセージ返信に進む
        is_img = ik.ik_profimg(driver)
        if not is_img:
            return False
        ik.ik_prof1(driver)
        ik.ik_prof2(driver)
        ik.prof_text(driver)
        ik.ik_basyo(driver)
        ik.ik_prof_basyo(driver)
        ik.toko_check(driver)
        
        #----メール返信
        for i in range(30):
            is_mail = ik.ik_mail(driver)
            if is_mail:
                break
            
        for loop_num in range(30):
            for ppn in range(9, 1, -1):
                ik.asipeta(driver, ppn)
            
        #----メール返信
        for i in range(30):
            is_mail = ik.ik_mail(driver)
            if is_mail:
                break


def chatgpt_try(ik, driver):
    #メール返信、足跡返し、新規メール
    ik.my_info = ik.get_my_info(driver)
    #----メール返信,未読なくなるまで
    ik.ik_mail_new(driver, is_chatgpt=True)
        

    #足跡返し(ppnは2~21で指定)
    for ppn in range(7, 2, -1):
        ik.asiato_chatgpt(driver, ppn)

    #ユーザー検索から新規メール送信
    for ppn in range(10, 1, -1):
        ik.search_user_chatgpt(driver, ppn)

    #ユーザー検索から新規メール送信
    for ppn in range(10, 1, -1):
        ik.search_user_chatgpt(driver, ppn)


def mail_try(ik, driver):
    #BANチェック
    
    #メール返信、足跡返し、新規メール
    ik.my_info = ik.get_my_info(driver)
    #----メール返信,未読なくなるまで
    ik.ik_mail_new(driver, is_chatgpt=False)
        

    #足跡返し(ppnは2~21で指定)
    for ppn in range(7, 2, -1):
        ik.asiato_kaesi(driver, ppn)

    #ユーザー検索から新規メール送信
    for ppn in range(10, 1, -1):
        ik.search_user(driver, ppn)

    #ユーザー検索から新規メール送信
    for ppn in range(10, 1, -1):
        ik.search_user(driver, ppn)


def initial_setting(ik, driver):
    """
    画像やプロフ設定、投稿など最初にやること
    """
    #画像設定されていたらTrue、その場合のみ投稿やメッセージ返信に進む
    is_img = ik.ik_profimg(driver)
    if not is_img:
        return False
    ik.ik_prof1(driver)
    ik.ik_prof2(driver)
    ik.prof_text(driver)
    ik.ik_basyo(driver)
    #これは地域１つだけランダムで設定
    # ik.ik_prof_basyo(driver)
    #地方すべて選択
    ik.ik_change_search_prof_area(driver)
    is_toko = ik.toko_check(driver)

    
def super_main(tem_ple, main_loop=3):
    """
    新規メールを連投、再投稿を頻繁に
    """

    #全ジャンル投稿してるかの判定用
    is_toko = False
    with driver_set(prox=False, profdir=None, prof_name=None, ua_name=None) as driver:

        # #まずはwifi再起動
        # wifi_reboot(driver)
        # is_reboot = http_check(driver)

        
        ik = ik_helper.Ikkr(tem_ple)
        is_login = ik.login(driver)
        if not is_login:
            return False

        #画像設定されていたらTrue、その場合のみ投稿やメッセージ返信に進む
        is_img = ik.ik_profimg(driver)
        if not is_img:
            return False
        ik.ik_prof1(driver)
        ik.ik_prof2(driver)
        ik.prof_text(driver)
        ik.ik_basyo(driver)
        #これは地域１つだけランダムで設定
        # ik.ik_prof_basyo(driver)
        #地方すべて選択
        ik.ik_change_search_prof_area(driver)
        is_toko = ik.toko_check(driver)

        for loop_num in range(main_loop):

            for j in range(3):
                #bancheck
                is_ban = ik.is_account_ban(driver)
                if not is_ban:
                    return False
                mail_try(ik, driver)
                # chatgpt_try(ik, driver)


            # if (loop_num % 2) == 0:
            #     #pure or adultを引数に
            #     ik.retoko(driver, pure_adlut="pure")
            # else:
            #     ik.retoko(driver, pure_adlut="adult")

            if not is_toko:
                
                is_toko = ik.toko_check(driver)    



if __name__ == "__main__":
    df = get_sheet_with_pd(sheetname=SHEET_NAME)
    #イククルのIDのあるアカウントだけ
    df.dropna(subset=['cnm'], inplace=True)
    ik_index = df.loc[~df['ik'].isnull()].index
    
    # len(sys.argv)
    # import pdb;pdb.set_trace()
    
    for loop_num, n in enumerate(ik_index):
        #テンプレ取得
        tem_ple = df.iloc[n,:]
        if len(sys.argv) == 2 and tem_ple['cnm'] != sys.argv[1]:
            continue
        
=======
# -*- coding:utf-8 -*-
from ctypes import util
import pandas as pd
import time
from BotHelper import JsonSearch, get_sheet_with_pd, set_sheet_with_pd, line_push, writeSheet
from BotHelper.util_driver import compose_driver, twitter_login, ouath_twitter_not_login, http_check, wifi_reboot, check_ip, s3_img
from BotHelper.util_driver import moji_hikaku, page_load, myClick, exe_click, mySendkey, slowClick, my_emojiSend, emoji_convert, add_ifin, send_gmail, mail_what, s3_img
import pysnooper
from importlib import reload
import os
import sys
from contextlib import contextmanager

from dotenv import load_dotenv
import logging

import util_login
import ik_helper

#-----------debug-----
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



from BotHelper.util_driver import page_load, myClick, exe_click, mySendkey,send_gmail
#-----debug---------



logging.config.fileConfig('logconf.ini')
lg = logging.getLogger(__name__)



# 環境変数を参照
load_dotenv()
API_URL = os.getenv('API_URL')
CHROME_PROFILE_DIR = os.getenv('CHROME_PROFILE_DIR')
SHEET_NAME = os.getenv('SHEET_NAME')



@contextmanager
def driver_set(prox=False, profdir=None, prof_name=None, ua_name=None):

    driver = compose_driver(proxy_info=prox, userdata_dir=profdir, use_profile=prof_name, use_ua=ua_name)
    try:
        yield driver
    finally:
        driver.quit()

        


def main(tem_ple):

    with driver_set(prox=False, profdir=None, prof_name=None, ua_name=tem_ple['ua']) as driver:

        #まずはwifi再起動
        wifi_reboot(driver)
        is_reboot = http_check(driver)

        
        ik = ik_helper.Ikkr(tem_ple)
        is_login = ik.login(driver)
        if not is_login:
            return False

        #画像設定されていたらTrue、その場合のみ投稿やメッセージ返信に進む
        is_img = ik.ik_profimg(driver)
        if not is_img:
            return False
        ik.ik_prof1(driver)
        ik.ik_prof2(driver)
        ik.prof_text(driver)
        ik.ik_basyo(driver)
        ik.ik_prof_basyo(driver)
        ik.toko_check(driver)
        
        #----メール返信
        for i in range(30):
            is_mail = ik.ik_mail(driver)
            if is_mail:
                break
            
        for loop_num in range(30):
            for ppn in range(9, 1, -1):
                ik.asipeta(driver, ppn)
            
        #----メール返信
        for i in range(30):
            is_mail = ik.ik_mail(driver)
            if is_mail:
                break


def mail_try(ik, driver):
    #メール返信、足跡返し、新規メール
    
    #----メール返信,未読なくなるまで
    ik.ik_mail_new(driver)
        

    #足跡返し(ppnは2~21で指定)
    for ppn in range(7, 2, -1):
        ik.asiato_kaesi(driver, ppn)

    #ユーザー検索から新規メール送信
    for ppn in range(10, 1, -1):
        ik.search_user(driver, ppn)

    #ユーザー検索から新規メール送信
    for ppn in range(10, 1, -1):
        ik.search_user(driver, ppn)

def initial_setting(ik, driver):
    """
    画像やプロフ設定、投稿など最初にやること
    """
    #画像設定されていたらTrue、その場合のみ投稿やメッセージ返信に進む
    is_img = ik.ik_profimg(driver)
    if not is_img:
        return False
    ik.ik_prof1(driver)
    ik.ik_prof2(driver)
    ik.prof_text(driver)
    ik.ik_basyo(driver)
    #これは地域１つだけランダムで設定
    # ik.ik_prof_basyo(driver)
    #地方すべて選択
    ik.ik_change_search_prof_area(driver)
    is_toko = ik.toko_check(driver)

    
def super_main(tem_ple, main_loop=3):
    """
    新規メールを連投、再投稿を頻繁に
    """

    #全ジャンル投稿してるかの判定用
    is_toko = False
    with driver_set(prox=False, profdir=None, prof_name=None, ua_name=tem_ple['ua']) as driver:

        # #まずはwifi再起動
        # wifi_reboot(driver)
        # is_reboot = http_check(driver)

        
        ik = ik_helper.Ikkr(tem_ple)
        is_login = ik.login(driver)
        if not is_login:
            return False

        #画像設定されていたらTrue、その場合のみ投稿やメッセージ返信に進む
        is_img = ik.ik_profimg(driver)
        if not is_img:
            return False
        ik.ik_prof1(driver)
        ik.ik_prof2(driver)
        ik.prof_text(driver)
        ik.ik_basyo(driver)
        #これは地域１つだけランダムで設定
        # ik.ik_prof_basyo(driver)
        #地方すべて選択
        ik.ik_change_search_prof_area(driver)
        is_toko = ik.toko_check(driver)

        for loop_num in range(main_loop):

            for j in range(3):
                mail_try(ik, driver)


            # if (loop_num % 2) == 0:
            #     #pure or adultを引数に
            #     ik.retoko(driver, pure_adlut="pure")
            # else:
            #     ik.retoko(driver, pure_adlut="adult")

            if not is_toko:
                
                is_toko = ik.toko_check(driver)    



if __name__ == "__main__":
    df = get_sheet_with_pd(sheetname=SHEET_NAME)
    #イククルのIDのあるアカウントだけ
    df.dropna(subset=['cnm'], inplace=True)
    ik_index = df.loc[~df['ik'].isnull()].index
    
    # len(sys.argv)
    # import pdb;pdb.set_trace()
    
    for loop_num, n in enumerate(ik_index):
        #テンプレ取得
        tem_ple = df.iloc[n,:]
        if len(sys.argv) == 2 and tem_ple['cnm'] != sys.argv[1]:
            continue
        
>>>>>>> 13bd2515aafca55e29d80ff79dadd967b5c1ad14
        is_main = super_main(tem_ple, main_loop=100)