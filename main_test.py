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
from tinydb import TinyDB, Query, where

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


def mail_try(ik, driver):
    #メール返信、足跡返し、新規メール
    ik.my_info = ik.get_my_info(driver)
    #----メール返信,未読なくなるまで
    ik.ik_mail_new(driver)
        

    #足跡返し(ppnは2~21で指定)
    for ppn in range(7, 2, -1):
        ik.asiato_chatgpt(driver, ppn)

    #ユーザー検索から新規メール送信
    for ppn in range(10, 1, -1):
        ik.search_user_chatgpt(driver, ppn)

    #ユーザー検索から新規メール送信
    for ppn in range(10, 1, -1):
        ik.search_user_chatgpt(driver, ppn)

        
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
                mail_try(ik, driver)


            # if (loop_num % 2) == 0:
            #     #pure or adultを引数に
            #     ik.retoko(driver, pure_adlut="pure")
            # else:
            #     ik.retoko(driver, pure_adlut="adult")

            if not is_toko:
                
                is_toko = ik.toko_check(driver)    


def save_temple(content):
    with open('temple.txt', 'a', encoding='utf-8') as f:
        f.write(content)


def modify_temple_with_chatgpt(tem_ple):
    change_keys = ["prof", "prof_a", "title_p", "text_p", "title_a", "text_a"]
    content = "--------------{}--------------\n".format(tem_ple['cnm'])
    save_temple(content)
    for ky in change_keys:
        content = "\n--------------{}--------------\n".format(ky)
        #言い換えようプロンプト
        # prompt = """以下の文章を意味合いを保ちつつ、なるべく口調や言い回し等が多彩になるよう言い換えてください。3つ挙げてほしいので、まずは1つ目の文章を作成してください。\n\n"""
        prompt = ""
        if 'title' in ky:
            prompt += "文字数をなるべく変えないようにして、"
        prompt += "以下の文章を、意味合いを保ちつつ、顔文字や絵文字などの使い方も参考にしながら、できるだけ重複を避けて、３通りに言い換えてください。\n\n"
        prompt += tem_ple[ky]
        cb = ChatbotUtil()
        res = cb.ask_chat(prompt)
        content += res
        save_temple(content)
        
        

        # content += res + '\n----------------------------------\n'
        # #---------２個目---------
        # prompt2 = "２つ目の文章を作成してください。"
        # res = cb.ask_chat(prompt2)
        # content += res + '\n----------------------------------\n'
        # #---------3個目---------
        # prompt3 = "3つ目の文章を作成してください。"
        # res = cb.ask_chat(prompt3)
        # content += res + '\n----------------------------------\n'
        # save_temple(content)



if __name__ == "__main__":
    df = get_sheet_with_pd(sheetname=SHEET_NAME)
    #イククルのIDのあるアカウントだけ
    df.dropna(subset=['cnm'], inplace=True)
    tem_ple = df[df['cnm'] == sys.argv[1]].to_dict(orient='records')[0]
    
    
    # modify_temple_with_chatgpt(tem_ple)
    # import pdb;pdb.set_trace()
    
    ik_index = df.loc[~df['ik'].isnull()].index
    
    # len(sys.argv)
    # import pdb;pdb.set_trace()
    
    for loop_num, n in enumerate(ik_index):
        #テンプレ取得
        tem_ple = df.iloc[n,:]
        if len(sys.argv) == 2 and tem_ple['cnm'] != sys.argv[1]:
            continue

        
        # is_main = super_main(tem_ple, main_loop=100)
        # import pdb;pdb.set_trace()
        # reload(ik_helper);ik = ik_helper.Ikkr(tem_ple)
        #---driver---
        driver = compose_driver(proxy_info=False, userdata_dir=None, use_profile=None, use_ua=None)
        ik = ik_helper.Ikkr(tem_ple)
        is_login = ik.login(driver)
        import pdb;pdb.set_trace()
        if not is_login:
            import pdb;pdb.set_trace()

        #画像設定されていたらTrue、その場合のみ投稿やメッセージ返信に進む
        # is_img = ik.ik_profimg(driver)
        # if not is_img:
        #     import pdb;pdb.set_trace()
        # ik.ik_prof1(driver)
        # ik.ik_prof2(driver)
        # ik.prof_text(driver)
        # ik.ik_basyo(driver)
        # #これは地域１つだけランダムで設定
        # # ik.ik_prof_basyo(driver)
        # #地方すべて選択
        # ik.ik_change_search_prof_area(driver)
        # is_toko = ik.toko_check(driver)


        ik.my_info = ik.get_my_info(driver)
        #ik-mail-new------------------
        is_chatgpt = True
        #未読メッセージ数を取得。0なら終了
        unread_messege_count = ik.get_unread_message_count(driver)
        if not unread_messege_count:
            lg.debug('message is end.')
            print('return True');import pdb;pdb.set_trace()
        #1ページに10通メッセージがあるのでunread_messege_count÷10(切り上げ)
        # page_number = -(-unread_messege_count // 10)
        page_number = (unread_messege_count // 10)
        #. +余分に何ページか移動するため.
        #移動ページできるページ数とelemの数が一致する
        elem = driver.find_elements(By.XPATH, "//*[@id=\"pc_iframe\"]/article//li[@class=\"listPaginator2 button\"]")
        page_number += len(elem)
        #指定した数字(新規メッセージの最終）のページに移動
        ik.move_to_page_number(driver, page_number)
        #現在のページURLを取得しておく
        now_url = driver.current_url
        while 0 < page_number:
            print('page_number: {}'.format(page_number))
            #新規メッセージ（NEWアイコンのあるのを選択)
            new_msg_elem = driver.find_elements(By.CLASS_NAME, "icon-new")
            #なければ前のページへ
            if len(new_msg_elem) == 0:
                #0ページ（最初のページ）で且つnewアイコンもなければ終了
                if page_number == 0:
                    lg.debug('message is end')
                    print('return True');import pdb;pdb.set_trace()
                page_number -= 1
                ik.move_to_page_number(driver, page_number)
                now_url = driver.current_url
                # import pdb;pdb.set_trace()
                continue

            exe_click(driver, "ok", new_msg_elem[-1])
            # import pdb;pdb.set_trace()
            if not is_chatgpt:
                #テンプレ返信
                ik.reply_message(driver)
            else:
                #chatgptバージョン
                ik.reply_chatgpt(driver, user_info=None)
            page_load(driver, now_url)
        #ik-mail-new------------------
        import pdb;pdb.set_trace()
        ik.ik_mail_new(driver)
        

        # import pdb;pdb.set_trace()
        # ik.retoko(driver, pure_adlut="adult")

        
        #足跡返し
        for ppn in range(5, 2, -1):
            ik.asiato_chatgpt(driver, ppn)

        #ユーザー検索から新規メール送信
        for ppn in range(10, 1, -1):
            ik.search_user_chatgpt(driver, ppn)
        
        import pdb;pdb.set_trace()