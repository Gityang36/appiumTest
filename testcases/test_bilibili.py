from appium import webdriver
from appium.options.common import AppiumOptions
import time
from selenium.webdriver.common.by import By

# 获取app名和界面 adb shell dumpsys window | findstr mFocusedApp  或者adb shell dumpsys activity recents | find "intent={"
# 如果已经获得apk，在Dos执行： D:\appium\androidsdk\build-tools\29.0.3\aapt.exe dump badging D:\apk\bili.apk | find "package: name="
# 输出信息中，就有应用的package名称
# package: name='tv.danmaku.bili'versionCode='5531000'versionName='5.53.1' platform
# 在命令行窗口执行
# ols\29.0.3\aapt.exe dump badging d:\tools\apk\bili.apkfind
# "launchable-activity"
# 输出信息中，就有应用的启动Activity
# launchable-activity: name='tv.danmaku.bili.ui.splash.SplashActivity' label='icon:
def test_launch_bilibili():
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
		"adbExecTimeout": 10000,
		"appium:connectHardwareKeyboard": True,
		"noReset": True,
		"dontStopAppOnReset": True
	})

	driver = webdriver.Remote(url,options=options)
	driver.implicitly_wait(12)
	driver.find_element(By.XPATH,'//*[@text="动画"]').click()
	time.sleep(2)
	driver.terminate_app("tv.danmaku.bili")


	# driver.find_element(By.XPATH,'//*[@text="国创"]').click()
