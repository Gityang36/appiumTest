from appium import webdriver
from appium.options.common import AppiumOptions
import time
from selenium.webdriver.common.by import By

# 获取app名和界面 adb shell dumpsys window | findstr mFocusedApp
url = "http://127.0.0.1:4723"
options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:deviceName": "HonorV8",
	"appium:platformVersion": "8",
	'appPackage': 'tv.danmaku.bili',
	'appActivity': '.MainActivityV2',
	"appium:automationName": "UiAutomator2",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 600,
    "adbExecTimeout": 6000,
	"appium:connectHardwareKeyboard": True,
	"noReset": True,
	"dontStopAppOnReset": True
})

driver = webdriver.Remote(url,options=options)
driver.implicitly_wait(10)
time.sleep(5)
driver.terminate_app("tv.danmaku.bili")
# driver.find_element(By.XPATH,'//*[@text="动画"]').click()
# driver.find_element(By.XPATH,'//*[@text="国创"]').click()
