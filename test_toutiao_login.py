from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.common import AppiumOptions
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import  AppiumBy

# 获取app名和界面 adb shell dumpsys window | findstr mFocusedApp
def test_toutiao():
	url = "http://127.0.0.1:4723"
	options = AppiumOptions()
	options.load_capabilities({
		"platformName": "Android",
		"appium:deviceName": "HonorV8",
		"appium:platformVersion": "8",
		"appPackage": "io.manong.developerdaily",
		"appActivity": "io.toutiao.android.ui.activity.LaunchActivity",
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
	driver.implicitly_wait(6)
	driver.find_element(By.XPATH,'//*[@text="我的"]').click()
	driver.find_element(By.ID,'io.manong.developerdaily:id/login_btn').click()
	time.sleep(1)
	driver.find_element(By.ID,'io.manong.developerdaily:id/btn_email').click()
	# driver.find_element(By.XPATH,'//*[@text="注册"]').click()
	time.sleep(1)
	driver.find_element(By.ID,'io.manong.developerdaily:id/edt_email').send_keys('zhh123@126.com')
	time.sleep(3)
	driver.terminate_app("io.manong.developerdaily")
	# driver.find_element(By.ID,'io.manong.developerdaily:id/edt_password').send_keys('123123')
	# driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="io.manong.developerdaily:id/edt_email"]').send_keys('zhh123@126.com')
	# driver.find_element(By.XPATH,'//android.widget.EditText[@resource-id="io.manong.developerdaily:id/edt_password"]').send_keys('123123')

	# driver.find_element(By.XPATH,'//*[@text="登录"]').click()


