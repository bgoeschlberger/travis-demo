import pytest
import GreetingGenerator from GreetingGenerator

def test_get_greeting():
    gg = GreetingGenerator()
    assert gg.get_greeting() == "hello world!"
