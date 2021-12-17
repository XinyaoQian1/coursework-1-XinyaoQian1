"""
# @File    :    test_user.py
# @Time    :    17/12/2021 01:07
# @Author  :    Xinyao Qian
# @SN      :    19021373
# @Description: This file is associated with test called user.py
                There are 9 tests in total.
"""
from datetime import datetime

import pytest


def test_full_name_is_created_when_user_created(normal_user_without_birthday):
    """
    GIVEN a user is created
    And first_name is Xinyao,  last_name is Qian
    WHEN first_name and last_name are passed to create_full_name function
    THEN the result should return Xinyao Qian
    """
    full_name = normal_user_without_birthday.create_full_name()
    assert full_name == 'Xinyao Qian'


def test_age_not_calculated_when_user_has_no_dob(normal_user_without_birthday):
    """
    GIVEN a user is created
    And Date of birth is null
    WHEN calculate_age function is called
    THEN a warning message should appear
    """
    age = normal_user_without_birthday.calculate_age()
    assert age == 'Age not calculated, date of birth unknown'


def test_age_is_calculated_when_user_has_dob(normal_user_with_birthday):
    """
    GIVEN a user is created
    And Date of birth is 2000, 6, 1
    When calculate_age function is called
    THEN age should return 21
    """

    age = normal_user_with_birthday.calculate_age()
    assert age == 21


def test_age_is_warned_when_user_has_abnormal_dob(
        normal_user_with_abnormal_birthday):
    """
    GIVEN a user is created
    And Date of birth is 1000, 6, 1
    When calculate_age function is called
    THEN an exception should raise
    """
    with pytest.raises(Exception) as exp:
        normal_user_with_abnormal_birthday.calculate_age()


def test_age_is_invalid_when_user_has_dob_in_future(
        normal_user_with_abnormal_birthday):
    """
    GIVEN a user is created
    And Date of birth is 2025, 6, 1
    When calculate_age function is called
    THEN an exception should raise
    """
    with pytest.raises(Exception) as exp:
        normal_user_with_abnormal_birthday.dob = datetime.datetime(2025, 6, 1)
        normal_user_with_abnormal_birthday.calculate_age()


def test_password_match_is_true_when_correct_password(
        normal_user_with_birthday):
    """
      GIVEN a user is created
      And password is '1414314'
      When is_correct_password function is called
      And entered password is '1414314'
      THEN result should return True
    """
    match = normal_user_with_birthday.is_correct_password('1414314')
    assert match is True


def test_password_match_is_False_when_wrong_password_entered(
        normal_user_with_birthday):
    """
      GIVEN a user is created
      And password is '1414314'
      When is_correct_password function is called
      And entered password is '1234325'
      THEN result should return False
    """
    match = normal_user_with_birthday.is_correct_password('1234325')
    assert match is False


def test_email_is_not_right_when_user_is_created(normal_user_with_birthday):
    """
      GIVEN user email is '73891273'
      When a new user is created
      THEN an exception should raise indicating a wrong format
    """
    with pytest.raises(Exception) as exp:
        normal_user_with_birthday.email = '73891273'


def test_name_is_invalid_when_containing_number(user_name_with_number):
    """
    GIVEN a user first_name is '123' and last_name is '123123'
    WHEN the user is created
     THEN an exception should raise indicating a wrong format of name
    """
    with pytest.raises(Exception) as exp:
        user_name_with_number.first_name = '123'
