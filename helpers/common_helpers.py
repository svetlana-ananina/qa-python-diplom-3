import allure
import pytest
import time
import random
import string


from data import _to_print, _to_sleep, _to_sleep_ff


# Логирование - вывод в <stdout>
def _print_value(name, value):
    if _to_print:
        print(f'{name}="{value}"')


def _print_info(info_str):
    if _to_print:
        print(info_str)


def _sleep(amount=10):
    if _to_sleep:
        time.sleep(amount)


def _sleep_ff(amount=10):
    if _to_sleep_ff:
        time.sleep(amount)

