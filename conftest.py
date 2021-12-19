"""
# @File    :    conftest.py
# @Time    :    17/12/2021 01:07
# @Author  :    Xinyao Qian
# @SN      :    19021373
# @Description: This file is pytest fixture to set up the data for test_user.py
                There are 5 fixtures in total
"""
import pytest
from user import User
import datetime


@pytest.fixture(scope='function')
def normal_user_without_birthday():
    user_no_bod = User(first_name='Xinyao', last_name='Qian',
                       email='qianxinyao@gmail.com', password='123345')
    yield user_no_bod


@pytest.fixture(scope='function')
def normal_user_with_birthday():
    user_with_bod = User(first_name='Moon', last_name='Sun',
                         email='MoonSun@gmail.com', password='1414314',
                         dob=datetime.datetime(2000, 6, 1))
    yield user_with_bod


@pytest.fixture(scope='function')
def user_with_wrong_email():
    user_with_wrong_email = User(first_name='Fish', last_name='Gomes',
                                 email='Hello_World', password='123141343',
                                 dob=datetime.datetime(2000, 10, 11))
    yield user_with_wrong_email


@pytest.fixture(scope='function')
def normal_user_with_abnormal_birthday():
    user_with_abnormal_dob = User(first_name='Sally', last_name='Day',
                                  email='SallyDay@gmail.com',
                                  password='1345135',
                                  dob=datetime.datetime(1000, 6, 1))
    yield user_with_abnormal_dob


@pytest.fixture(scope='function')
def user_name_with_number():
    user_name_number = User(first_name='2713819', last_name='123123',
                            email='111@gmail.com', password='13432sad5',
                            dob=datetime.datetime(2005, 6, 11))
    yield user_name_number
