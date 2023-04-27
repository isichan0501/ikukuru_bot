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
import undetected_chromedriver as uc
from selenium.webdriver.common.proxy import Proxy, ProxyType
import logging

from BotHelper.util_driver import page_load, myClick, exe_click, mySendkey
from BotHelper import line_push, writeSheet, change_cell
from dotenv import load_dotenv


lg = logging.getLogger(__name__)

# 環境変数を参照
load_dotenv()
SHEET_NAME = os.getenv('SHEET_NAME')

@pysnooper.snoop()
def login(driver, login_id, login_pw):
    wait = WebDriverWait(driver, 10)
    lg.debug(login_id)
    try:
        page_load(driver, 'https://www.194964.com/')
        page_load(driver, "https://www.194964.com/registration/login/show_login_tel.html")
        # myClick(driver, "css", "#mainvisual > div.main_loginbox > div > a > img")
        time.sleep(5)
        # driver.switch_to.frame(driver.find_element(By.TAG_NAME,("iframe")))
        # myClick(driver, "xpath", "//*input[name=\"tel\"]")
        mySendkey(driver, "xpath", "//*[@id='form1']/div[1]/input", login_id)
        # myClick(driver, "xpath", "//*input[name=\"password\"]")      
        mySendkey(driver, "xpath", "//*[@id='form1']/div[2]/input", login_pw)
        exe_click(driver, "xpath", "//button[@type='submit']")
        # exe_click(driver, "xpath", "//*button[contains(text(), \"ログイン\")]")
        time.sleep(3)
        # driver.switch_to.default_content()

    except (socket.timeout, NoSuchElementException, TimeoutException,
            ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
        lg.debug(e)



@pysnooper.snoop()
def is_login(driver, login_id, login_pw):
    try:
        # ban_elems = driver.find_elements(By.ID, "//*[@id=\"loginform\"]/h3")
        
        ban_elems = driver.find_elements(By.ID, "title")
        if len(ban_elems) != 0 and ban_elems[0].text == "ログイン失敗":
            imgName = "{0}.png".format(login_id)
            driver.get_screenshot_as_file(imgName)
            id_pw = f"{login_id}:{login_pw}"
            time.sleep(2)
            message = "{0}ik潰れたよ".format(id_pw)
            line_push(message, img_path=imgName)
            change_cell(SHEET_NAME, id_pw, "")
            return False

        #おすすめユーザーのポップアップを消す
        myClick(driver, "xpath", "//*[@id=\"osusumeList\"]//img")
        return True
    except (socket.timeout, NoSuchElementException, TimeoutException,
            ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
        lg.debug(e)