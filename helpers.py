import time

import pytest

from data import _to_print, _to_sleep


# Логирование - вывод в <stdout>
def _print_value(name, value):
    if _to_print:
        print(f'{name}="{value}"')


def _print_info(info_str):
    if _to_print:
        print(info_str)


def _sleep(amount):
    if _to_sleep:
        time.sleep(amount)


@pytest.mark.usefixtures('get_chrome_driver', 'get_firefox_driver')
def _get_browser(with_browser, get_chrome_driver, get_firefox_driver):
    if with_browser == 'Chrome':
        driver = get_chrome_driver
    else:
        driver = get_firefox_driver
    return driver


