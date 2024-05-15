import pyautogui
import os

def clickWebGridTarget():
    cwd = os.getcwd()
    target_image = cwd + '/images/blue-button.png'
    test_logo = cwd + '/images/logo.png'

    target = pyautogui.locateCenterOnScreen(target_image, confidence=0.9)
    pyautogui.click(target[0], target[1])

def saveScreenshot():
    im = pyautogui.screenshot('test_screenshot.png')

def helloWorld():
    print('hello world')

if __name__ == '__main__':
    saveScreenshot()