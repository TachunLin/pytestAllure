
## Python Mobile Automation Testing Framework 

---

A python mobile automation testing framework based on ```Appium```, ```Pytest``` and ```Allure``` 

---

### Framework Dependencies

* Appium 1.7 above
* Python 3.5.2
* Pytest 1.7.10
* Allure Framework 1.x 

---

### Features

1. Automated trigger and close server 
2. Command line trigger with on-demand argument
3. Display execution log and save in file 
4. Generate clear HTML test report

    ![image](https://user-images.githubusercontent.com/29251855/39994762-c9d73d10-57ac-11e8-895f-83a3d25cc82d.png)

5. Attached failure screenshot and log on test report

    ![image](https://user-images.githubusercontent.com/29251855/39995019-ac9fffa6-57ad-11e8-9f5a-0d0ec3cbe089.png)

6. Reusable page object and common library 
7. Support parallel testing (Android)

    ![image](https://user-images.githubusercontent.com/29251855/39995064-d14fc70a-57ad-11e8-816a-08754c57c559.png)

---

### Prerequisite and Required Package 

* Prepare Android Studio, Appium test environment

    Mac: http://blog.autoruby.com/2018/03/android-appium.html

    Windows: http://blog.autoruby.com/2018/03/android-appium-windows.html 

* ttab (launch open terminal from script)

    > npm install -g ttab

* Install ```Pytest```

    > pip3 install pytest 

* Install ```pytest-allure-adaptor```

    > pip3 install pytest-allure-adaptor

* Install ```formulas```

    > brew tap qatools/formulas

* Instal Allure Command Tool

    > brew install ```allure-commandline```

* Instal PyYaml

    > pip3 install PyYaml 

* Instal requests

    > pip3 install requests

---

### Trigger Testing


1. Launch emulator or connect real device 

2. Run command in terminal 

    > pytest -v -s --device [```deviceName```] [```test file```] --tb=short --alluredir report

    ex. pytest -v -s --device AVD6.0 API_Demos.py --tb=short --alluredir report

    This will connect to Android 6.0 emulator then trigger test script, generate test result in repport folder 

3. Generate Allure test report 

    > allure generate report/ -o report/html 

    This will generate test report in your project report/html folder 

---

### Open test report 

1. If you are using Pycharm, you can right click html/index.html to open it in browser

2. You can also change to report folder in terminal and run command 

    > allure report open --report-dir ./html

---

### Contact me at

Blog: http://blog.autoruby.com/  
Email: davidtclin58@gmail.com  
Linkedin: https://www.linkedin.com/in/davidtclin/



