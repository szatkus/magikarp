from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from threading import Thread

from application import application
import main

Thread(target=lambda: application.run(port=5001), daemon=True).start()

def test_sample():
    driver = webdriver.Firefox()
    driver.get("http://localhost:5001")
    elem = driver.find_element_by_id('sample')
    assert elem.text == 'loading'
    sleep(3)
    assert elem.text == 'done'
    driver.close()
