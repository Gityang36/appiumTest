from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import  AppiumBy

# 获取app名和界面 adb shell dumpsys window | findstr mFocusedApp
def test_wifi_scan():
	url = "http://127.0.0.1:4723"
	options = AppiumOptions()
	options.load_capabilities({
		"platformName": "Android",
		"appium:deviceName": "HonorV8",
		"appium:platformVersion": "8",
		"appPackage": "com.android.settings",
		"appActivity": ".Settings$WifiSettingsActivity",
		"appium:automationName": "UiAutomator2",
		"appium:ensureWebviewsHavePages": True,
		"appium:nativeWebScreenshot": True,
		"forceAppLaunch": True,
		"appium:newCommandTimeout": 100,
		"adbExecTimeout": 30000,
		"appium:connectHardwareKeyboard": True,
		"noReset": True,
		"dontStopAppOnReset": True
	})

	driver = webdriver.Remote(url,options=options)
	driver.implicitly_wait(6)
	time.sleep(3)
	driver.find_element(By.XPATH,'//*[@text="扫描"]').click()
	# time.sleep(5)
	hotpot = driver.find_element(By.XPATH,'//android.widget.TextView[@resource-id="android:id/title" and @text="ADTCTS-5G"]').text
	# print(hotpot)
	if driver.find_element(By.ID,'android:id/title').text == 'ADTCTS-5G':
		print('找到热点')
	driver.terminate_app("com.android.settings")