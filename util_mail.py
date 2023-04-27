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
import re
from BotHelper.util_driver import page_load, myClick, exe_click, mySendkey
from BotHelper import line_push, writeSheet, change_cell
from dotenv import load_dotenv


lg = logging.getLogger(__name__)

# 環境変数を参照
load_dotenv()
SHEET_NAME = os.getenv('SHEET_NAME')




@pysnooper.snoop()
def check_unread_message(driver):
    """

    Returns:
        boolean: 未読メッセージがあればTrue
    """
    try:
        page_load(driver, "https://sp.194964.com/mail/inbox/show_mailbox.html")
        
        elm = driver.find_element(By.XPATH, "/html/body/nav/div[3]").text
        ex_mg = re.sub("\\D", "", elm)
        if not ex_mg:
            return True

        return False
    except (socket.timeout, NoSuchElementException, TimeoutException,
            ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
        lg.debug(e)
        return False


@pysnooper.snoop()
def send_mail(driver):
    try:
        page_load(driver, "https://sp.194964.com/mail/inbox/show_mailbox.html")
        

    except (socket.timeout, NoSuchElementException, TimeoutException,
            ElementClickInterceptedException, ElementNotInteractableException, Exception) as e:
        lg.debug(e)

