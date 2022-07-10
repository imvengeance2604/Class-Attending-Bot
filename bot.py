import webbrowser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import datetime
driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
mail = "adityakamarthi.is20@rvce.edu.in"
pasw = "welcome123*"
tday = datetime.date.today()
day = tday.weekday()
i = 1

if(day == 0):
    ma = 0
    me = 0
    ch = 0
    el = 0
    cp = 0
    mat = datetime.time(9, 0, 0)
    met = datetime.time(13, 23, 0)
    cht = datetime.time(12, 30, 0)
    elt = datetime.time(11, 20, 0)
    cpt = datetime.time(10, 10, 0)
    c = 0



    while (c<5):
        t = datetime.datetime.now().time()
        if(t > mat and ma == 0):

            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Engineering Mathematics - II - 18MA21')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=23783','new window')")
            allTabsm = driver.window_handles
            tab = allTabsm[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsm1 = driver.window_handles
            tab1 = allTabsm1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            ma = ma+1
            c = c+1
        if(t>cpt and cp==0):

            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')




            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Programming in C - 18CS13/23')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24529','new window')")
            allTabsc = driver.window_handles
            tab = allTabsc[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsc1 = driver.window_handles
            tab1 = allTabsc1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            cp = cp+1
            c = c+1
        if(t>elt and el==0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')




            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Elements of Electronics Engineering - 18EC14/24')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24402','new window')")
            allTabse = driver.window_handles
            tab = allTabse[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabse1 = driver.window_handles
            tab1 = allTabse1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            el = el+1
            c = c+1
        if(t > cht and ch == 0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')




            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Engineering Chemistry -18CH12/22')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-left")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24522','new window')")
            allTabsch = driver.window_handles
            tab = allTabsch[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsch1 = driver.window_handles
            tab1 = allTabsch1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            ch = ch+1
            c = c+1

if(day == 1):
    ma = 0
    me = 0
    ch = 0
    el = 0
    cp = 0
    mat = datetime.time(11, 20, 0)
    met = datetime.time(10, 10, 0)
    cht = datetime.time(9, 0, 0)
    elt = datetime.time(12, 30, 0)
    cpt = datetime.time(10, 10, 0)
    c = 0



    while (c<5):
        t = datetime.datetime.now().time()
        if(t > mat and ma == 0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Engineering Mathematics - II - 18MA21')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=23783','new window')")
            allTabsm = driver.window_handles
            tab = allTabsm[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsm1 = driver.window_handles
            tab1 = allTabsm1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            ma = ma+1
            c = c+1
        if(t>met and me==0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')




            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Programming in C - 18CS13/23')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24529','new window')")
            allTabsme = driver.window_handles
            tab = allTabsme[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsme1 = driver.window_handles
            tab1 = allTabsme1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            me = me+1
            c = c+1
        if(t>elt and el==0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')




            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            cpro = driver.find_element_by_link_text('Elements of Electronics Engineering - 18EC14/24')
            cpro.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24402','new window')")
            allTabse = driver.window_handles
            tab = allTabse[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabse1 = driver.window_handles
            tab1 = allTabse1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            el = el+1
            c = c+1
        if(t > cht and ch == 0):

            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')




            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            cpro = driver.find_element_by_link_text('Engineering Chemistry -18CH12/22')
            cpro.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-left")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24522','new window')")
            allTabsch = driver.window_handles
            tab = allTabsch[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsch1 = driver.window_handles
            tab1 = allTabsch1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            ch = ch+1
            c = c+1
if (day == 2):
    ma = 0
    me = 0
    ch = 0
    el = 0
    cp = 0
    mat = datetime.time(11, 20, 0)
    met = datetime.time(9, 0, 0)
    cht = datetime.time(12, 30, 0)
    elt = datetime.time(10, 10, 0)
    cpt = datetime.time(11, 20, 0)
    c = 0



    while (c < 5):
        t = datetime.datetime.now().time()
        if (t > cpt and cp == 0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Programming in C - 18CS13/23')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24529','new window')")
            allTabsc = driver.window_handles
            tab = allTabsc[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsc1 = driver.window_handles
            tab1 = allTabsc1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            cp = cp + 1
            c = c + 1
        if (t > met and me == 0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Programming in C - 18CS13/23')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24529','new window')")
            allTabsme = driver.window_handles
            tab = allTabsme[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsme1 = driver.window_handles
            tab1 = allTabsme1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            me = me + 1
            c = c + 1
        if (t > elt and el == 0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            cpro = driver.find_element_by_link_text('Elements of Electronics Engineering - 18EC14/24')
            cpro.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24402','new window')")
            allTabse = driver.window_handles
            tab = allTabse[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabse1 = driver.window_handles
            tab1 = allTabse1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            el = el + 1
            c = c + 1
        if (t > cht and ch == 0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            cpro = driver.find_element_by_link_text('Engineering Chemistry -18CH12/22')
            cpro.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-left")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24522','new window')")
            allTabsch = driver.window_handles
            tab = allTabsch[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsch1 = driver.window_handles
            tab1 = allTabsch1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            ch = ch + 1
            c = c + 1
if(day == 3):
    ma = 0
    me = 0
    ch = 0
    el = 0
    cp = 0
    mat = datetime.time(11, 20, 0)
    met = datetime.time(13, 23, 0)
    cht = datetime.time(12, 30, 0)
    elt = datetime.time(9, 0, 0)
    cpt = datetime.time(10, 10, 0)
    c = 0



    while (c<4):
        t = datetime.datetime.now().time()
        if(t > mat and ma == 0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')
            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Engineering Mathematics - II - 18MA21')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=23783','new window')")
            allTabsm = driver.window_handles
            tab = allTabsm[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsm1 = driver.window_handles
            tab1 = allTabsm1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            ma = ma+1
            c = c+1
        if(t>cpt and cp==0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')




            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Programming in C - 18CS13/23')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24529','new window')")
            allTabsc = driver.window_handles
            tab = allTabsc[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsc1 = driver.window_handles
            tab1 = allTabsc1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            cp = cp+1
            c = c+1
        if(t>elt and el==0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')




            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Elements of Electronics Engineering - 18EC14/24')
            math.click()
            i = 1

            driver.implicitly_wait(12)
            driver.execute_script("window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24402','new window')")
            allTabse = driver.window_handles
            tab = allTabse[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabse1 = driver.window_handles
            tab1 = allTabse1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            el = el+1
            c = c+1
if (day == 4):
    ma = 0
    me = 0
    ch = 0
    el = 0
    cp = 0
    mat = datetime.time(9, 0, 0)
    met = datetime.time(11, 20, 0)
    cht = datetime.time(10, 10, 0)
    elt = datetime.time(12, 30, 0)
    cpt = datetime.time(10, 10, 0)
    c = 0

    while (c < 5):
        t = datetime.datetime.now().time()
        if (t > mat and ma == 0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Engineering Mathematics - II - 18MA21')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script(
                "window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=23783','new window')")
            allTabsm = driver.window_handles
            tab = allTabsm[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsm1 = driver.window_handles
            tab1 = allTabsm1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            ma = ma + 1
            c = c + 1
        if (t > met and me == 0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            math = driver.find_element_by_link_text('Programming in C - 18CS13/23')
            math.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script(
                "window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24529','new window')")
            allTabsme = driver.window_handles
            tab = allTabsme[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsme1 = driver.window_handles
            tab1 = allTabsme1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            me = me + 1
            c = c + 1
        if (t > elt and el == 0):
            driver.quit()
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            cpro = driver.find_element_by_link_text('Elements of Electronics Engineering - 18EC14/24')
            cpro.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-right")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script(
                "window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24402','new window')")
            allTabse = driver.window_handles
            tab = allTabse[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabse1 = driver.window_handles
            tab1 = allTabse1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            el = el + 1
            c = c + 1
        if (t > cht and ch == 0):
            driver = webdriver.Chrome(executable_path='C:/path/to/chromedriver.exe')

            driver.get('https://quiklrn.com/login.php')
            entry = driver.find_element_by_id('email')

            paasww = driver.find_element_by_id('password')
            entry.send_keys(mail)
            paasww.send_keys(pasw)
            login = driver.find_element_by_class_name("btn.btn-primary.btn-block")
            login.click()
            cpro = driver.find_element_by_link_text('Engineering Chemistry -18CH12/22')
            cpro.click()
            i = 1
            arrow = driver.find_element_by_class_name("icon-arrow-left")
            arrow.click()
            driver.implicitly_wait(12)
            driver.execute_script(
                "window.open('https://lms.quiklrn.com/mod/bigbluebuttonbn/view.php?id=24522','new window')")
            allTabsch = driver.window_handles
            tab = allTabsch[1]
            driver.switch_to.window(tab)
            join = driver.find_element_by_class_name("btn.btn-primary")
            join.click()
            allTabsch1 = driver.window_handles
            tab1 = allTabsch1[2]
            driver.switch_to.window(tab1)
            listenonly = driver.find_element_by_class_name("icon--2q1XXw.icon-bbb-listen")
            listenonly.click()
            ch = ch + 1
            c = c + 1
