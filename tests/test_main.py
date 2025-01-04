from streamlit.testing.v1 import AppTest

def test_general_exception():
    at = AppTest.from_file('scripts/main.py').run()
    assert not at.exception

def test_just_sponsor_name():
    ...
