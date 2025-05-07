from appium import webdriver
from appium.options.common import AppiumOptions
import time
from selenium.webdriver.common.by import By

# 获取app名和界面 adb shell dumpsys window | findstr mFocusedApp
def test_chrome_add_bookmark():
	url = "http://127.0.0.1:4723"
	options = AppiumOptions()
	options.load_capabilities({
		"platformName": "Android",
		"appium:deviceName": "HonorV8",
		"appium:platformVersion": "8",
		'appPackage': 'com.android.chrome',
		'appActivity': 'com.google.android.apps.chrome.Main',
		"appium:automationName": "UiAutomator2",
		"appium:ensureWebviewsHavePages": True,
		"appium:nativeWebScreenshot": True,
		"appium:newCommandTimeout": 10,
		"adbExecTimeout": 6000,
		"appium:connectHardwareKeyboard": True,
		"noReset": True
		# "dontStopAppOnReset": True
	})

	driver = webdriver.Remote(url,options=options)
	driver.implicitly_wait(6)
	driver.find_element(By.XPATH,'//android.widget.ImageButton[@content-desc="自定义及控制 Google Chrome"]').click()
	driver.find_element(By.XPATH,'//*[@text="书签"]').click()
	# driver.find_element(By.XPATH,'//*[@text="移动设备书签"]').click()
	time.sleep(3)
	driver.terminate_app("com.android.chrome")
