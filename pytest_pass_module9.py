'''
Eugene Bellau
11/20/2020
AgileUnoModule9
'''

import pytest

from my_module import greeting

from my_module import letter_text

def test_greeting_pass():
    assert "Hello Eugene" == greeting("Eugene"), "Test Failed"
    assert 100 != greeting("Eugene"), "Test Failed"

def test_letter_text():
    assert "Hello Sam, this letter is to inform you that you have won 10,000 dollars" == letter_text(name="Sam", amount="10,000", denomination="dollars"), "Test Failed"
    assert "nothing" != letter_text(name="Sam", amount="10,000", denomination="dollars"), "Test Failed"
    