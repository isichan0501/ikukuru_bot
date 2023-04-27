from BotHelper.util_driver import wifi_reboot, http_check,compose_driver
from contextlib import contextmanager

@contextmanager
def driver_set(prox=False, profdir=None, prof_name=None, ua_name=None):

    driver = compose_driver(proxy_info=prox, userdata_dir=profdir, use_profile=prof_name, use_ua=ua_name)
    try:
        yield driver
    finally:
        driver.quit()


def change_ip_set2():
    try:
        driver = compose_driver(proxy_info=None, userdata_dir=None, use_profile=None, use_ua=None)
        old_ip = http_check(driver)
        wifi_reboot(driver)
        new_ip = http_check(driver)
    finally:
        driver.quit()

def change_ip_set():
    with driver_set(prox=False, profdir=None, prof_name=None, ua_name=None) as driver:
        old_ip = http_check(driver)
        wifi_reboot(driver)
        new_ip = http_check(driver)
        
if __name__ == "__main__":
    change_ip_set()