import time
from core import wrapSeleniumEvent
from locust import events
from locust.exception import StopLocust
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import random
class NetworkHandler(webdriver.Chrome):
    def __init__(self, executable_path="chromedriver", port=0,
                 options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None,
                 chrome_options=None):
        if chrome_options  is None:      
            self.chrome_option=webdriver.ChromeOptions()
        else:
            self.chrome_option=chrome_options
        x=random.randint(0,100000000000)
        self.chrome_option.add_argument("-user-data-dir=C:/root/Downloads/abc_"+str(x))
        self.chrome_option.add_argument("start-maximized")
        self.driver=webdriver.Chrome(executable_path=executable_path, port=port,
                 options=options, service_args=service_args,
                 desired_capabilities=desired_capabilities, service_log_path=service_log_path,
                 chrome_options=self.chrome_option)
        

    def getNetworkData(self):
        script="""
                var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;
                """
        time.sleep(1)
        self.networkData=self.driver.execute_script(script)

    def sendToLocust(self):
        for data in self.networkData:
            if "initiatorType" in data.keys() and data["initiatorType"]=="xmlhttprequest":
                events.request_success.fire(
                    request_type="API REQ",
                    name=data['name'].split("?")[0],
                    response_time=data['duration'],
                    response_length=0
                )
