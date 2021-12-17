"""
# @File    :    test_user.py
# @Time    :    17/12/2021 01:07
# @Author  :    Xinyao Qian
# @SN      :    19021373
# @Description: This file is associated with test called user.py
"""
from datetime import datetime

import pytest


def test_full_name_is_created_when_user_created(normal_user_without_birthday):
    '''
    GIVEN a user
    WHEN first_name is Xinyao last_name is Qian
    THEN the create_full_name should return Xinyao Qian
    '''
    full_name = normal_user_without_birthday.create_full_name()
    assert full_name == 'Xinyao Qian'


def test_age_not_calculated_when_user_has_no_bod(normal_user_without_birthday):
    '''
    GIVEN a user
    WHEN first_name is Xinyao last_name is Qian
    THEN the create_full_name should return Xinyao Qian
    '''
    age = normal_user_without_birthday.calculate_age()
    assert age == 'Age not calculated, date of birth unknown'


def test_age_is_calculated_when_user_has_bod(normal_user_with_birthday):
    '''
    GIVEN a user
    WHEN first_name is Xinyao last_name is Qian
    THEN the create_full_name should return Xinyao Qian
    '''
    age = normal_user_with_birthday.calculate_age()
    assert age == 21


def test_password_match_is_True_when_correct_password_entered(
        normal_user_with_birthday):
    '''
    GIVEN a user
    WHEN first_name is Xinyao last_name is Qian
    THEN the create_full_name should return Xinyao Qian
    '''
    match = normal_user_with_birthday.is_correct_password('1414314')
    assert match is True


def test_password_match_is_False_when_wrong_password_entered(
        normal_user_with_birthday):
    '''
    GIVEN a user
    WHEN first_name is Xinyao last_name is Qian
    THEN the create_full_name should return Xinyao Qian
    '''
    match = normal_user_with_birthday.is_correct_password('1234325')
    assert match is False


def test_email_is_not_right_when_user_is_created(normal_user_with_birthday):
    '''
     GIVEN a user
     WHEN first_name is Xinyao last_name is Qian
     THEN the create_full_name should return Xinyao Qian
     '''
    with pytest.raises(Exception) as exp:
        normal_user_with_birthday.email = '73891273'


def test_age_is_warned_when_user_has_bod(normal_user_with_abnormal_birthday):
    '''
    GIVEN a user
    WHEN first_name is Xinyao last_name is Qian
    THEN the create_full_name should return Xinyao Qian
    '''
    with pytest.raises(Exception) as exp:
        age = normal_user_with_abnormal_birthday.calculate_age()

def test_name_is_invalid_when_containing_number(user_name_with_number):
    '''
    GIVEN a user
    WHEN first_name is Xinyao last_name is Qian
    THEN the create_full_name should return Xinyao Qian
    '''
    with pytest.raises(Exception) as exp:
        user_name_with_number.first_name = 123

def test_age_is_warned_when_user_has_bod(normal_user_with_abnormal_birthday):
    '''
    GIVEN a user
    WHEN first_name is Xinyao last_name is Qian
    THEN the create_full_name should return Xinyao Qian
    '''
    with pytest.raises(Exception) as exp:
        normal_user_with_abnormal_birthday.dob = datetime.datetime(2025, 6, 1)
        age = normal_user_with_abnormal_birthday.calculate_age()