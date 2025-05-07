from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
import time

# 获取app名和界面
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
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True,
	"noReset": True,
	"dontStopAppOnReset": True
})

cap1 = {
	"platformName": "Android",
	"appium:deviceName": "192.168.180.166:37999",
	"appium:platformVersion": "15",
	"appPackage": "com.android.settings",
	"appActivity": ".MainSettings",
	"appium:automationName": "UiAutomator2",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True,
	"noReset": True,
	"dontStopAppOnReset": True
}
driver = webdriver.Remote(url,options=options)
# driver = webdriver.Remote(url,options=UiAutomator2Options().load_capabilities(cap1))
driver.implicitly_wait(10)

# driver.get_screenshot_as_file('home.png')

