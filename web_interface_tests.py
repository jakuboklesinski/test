## python3 functional_tests.py firefox eve.ii.pw.edu.pl 9007

# -*- coding=utf-8 -*-
"""functional testing for dnaasm web application"""

import sys
import os
import time
import unittest
import splinter
from splinter import Browser
from splinter.exceptions import DriverNotFoundError
##test 1234
## @brief test-cases
class TestFunctionalDnaasm(unittest.TestCase):

    ## Browser used for testing - default Google Chrome
    browser = ''
    admin_user = ''
    admin_user_password = ''

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        self.browser.reload()
        pass

    def tearDown(self):
        try:
            alert = self.browser.get_alert()
            alert.accept()
        except:
            pass

##drjghsrkljghrkljh

    def clickCssLink(self, ident, interval=0.1, maxTime=2):
        """Searches for an css and clicks it"""
        browser = self.browser
        counter = 0
        link = None
        while counter < maxTime:
            try:
                browser.find_by_css(ident).first.click()
                return
            except:
                time.sleep(interval)
                counter += interval
        link = browser.find_by_css(ident)
        self.assertGreaterEqual(len(link), 1, "Cannot find link with ident='{css}' in {brow}".format(css=ident, brow = 'browser'))
        link.first.click()

    def clickIdLink(self, ident, interval=0.1, maxTime=2):
        """Searches for an identifier and clicks it"""
        browser = self.browser
        counter = 0
        link = None
        while counter < maxTime:
            try:
                browser.find_by_id(ident).first.click()
                return

            except:
                time.sleep(interval)
                counter += interval
        link = browser.find_by_id(ident)
        self.assertGreaterEqual(len(link), 1, "Cannot find link with ident='{css}' in {brow}".format(css=ident, brow = 'browser'))
        link.first.click()

    def waitForElement(self, ident, interval=0.1, maxTime=2):
        """Waits for element"""
        browser = self.browser
        counter = 0
        while counter < maxTime:
            counter += interval
            time.sleep(interval)
            if browser.is_element_present_by_id(ident):
                return

    def test01AnyAnswer(self):
        """tests if the application is loaded"""
        self.assertTrue(len(self.browser.html) > 0)

    def test02ProperTitle(self):
        """tests if the web page title is correct"""
        title = self.browser.title
        if not isinstance(title, str):
            title = title.decode()
        self.assertEqual(title, 'DnaAssembler')

    def test03StartPageTranslations(self):
        """test 'start_page' page translations"""
        self.browser.reload()
        self.clickCssLink('#a_lang_en')
        self.assertEqual(len(self.browser.find_by_text(u'Welcome to DnaAssembler application')), 1)
        self.assertEqual(self.browser.find_by_id('loginAsGuestButton').first.text, u'Log in as guest')
        self.assertEqual(self.browser.find_by_id('loginAsGuestButton').first['title'], u"Click to log in as guest")
        self.assertEqual(self.browser.find_by_id('showLoginWindowButton').first.text, u'Log in')
        self.assertEqual(self.browser.find_by_id('showLoginWindowButton').first['title'], u"Click to log in")
        self.assertEqual(self.browser.find_by_id('showNewUserWindowButton').first.text, u'Create new user')
        self.assertEqual(self.browser.find_by_id('showNewUserWindowButton').first['title'], u"Click to create new user")
        self.assertEqual(self.browser.find_by_id('showHelpWindowButton').first.text, u'Help')
        self.assertEqual(self.browser.find_by_id('showHelpWindowButton').first['title'], u"Click to view help page")
        self.assertEqual(self.browser.find_by_id('a_lang_en').first['title'], u"Click to change language to english")
        self.assertEqual(self.browser.find_by_id('a_lang_pl').first['title'], u"Click to change language to polish")
        self.clickCssLink('#a_lang_pl')
        self.assertEqual(len(self.browser.find_by_text(u'Witaj w aplikacji DnaAssembler')), 1)
        self.assertEqual(self.browser.find_by_id('loginAsGuestButton').first.text, u'Zaloguj si?? jako go????')
        self.assertEqual(self.browser.find_by_id('loginAsGuestButton').first['title'], u"Kliknij, aby zalogowa?? si?? do aplikacji jako go????")
        self.assertEqual(self.browser.find_by_id('showLoginWindowButton').first.text, u'Zaloguj si??')
        self.assertEqual(self.browser.find_by_id('showLoginWindowButton').first['title'], u"Kliknij, aby zalogowa?? si?? do aplikacji")
        self.assertEqual(self.browser.find_by_id('showNewUserWindowButton').first.text, u'Dodaj u??ytkownika')
        self.assertEqual(self.browser.find_by_id('showNewUserWindowButton').first['title'], u"Kliknij, aby doda?? nowego u??ytkownika")
        self.assertEqual(self.browser.find_by_id('showHelpWindowButton').first.text, u'Pomoc')
        self.assertEqual(self.browser.find_by_id('showHelpWindowButton').first['title'], u"Kliknij, aby zobaczy?? pomoc dla aplikacji")
        self.assertEqual(self.browser.find_by_id('a_lang_en').first['title'], u"Kliknij, aby zmieni?? j??zyk na angielski")
        self.assertEqual(self.browser.find_by_id('a_lang_pl').first['title'], u"Kliknij, aby zmieni?? j??zyk na polski")

        def test04HelpPageENG(self):
        """test 'help' page_eng"""
        self.browser.reload()
        self.clickCssLink('#a_lang_en')
        self.clickCssButton('#showHelpWindowButton')
        self.assertEqual(len(self.browser.find_by_text(u'DnaAssembler - Help')), 1)
        self.assertEqual(self.browser.find_by_id('file_formats_href').first.text, u'Input and output file formats')
        self.assertEqual(self.browser.find_by_id('file_formats_href').first['title'], u"Click to view description of input file formats accepted by application and output file formats produced by application")
        self.assertEqual(self.browser.find_by_id('file_formats_href').first.text, u'Parameters and algorithms used in application')
        self.assertEqual(self.browser.find_by_id('file_formats_href').first['title'], u"Click to view description of parameters and algorithms used in application")
        self.assertEqual(len(self.browser.find_by_text(u'For more information send an email:')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'r.m.nowak@elka.pw.edu.pl')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Authors')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Robert Nowak - r.m.nowak@elka.pw.edu.pl')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Wiktor Ku??mirek')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Warsaw University of Technology,')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Faculty of Electronics and Information Technology,')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Warsaw 2015')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Application parameters')), 1)
        self.assertNotEqual(self.browser.find_by_id('server_time_val').first.text, u'0')
        self.assertEqual(len(self.browser.find_by_text(u'db version: PostgreSQL 9.4.18 on x86_64-unknown-linux-gnu')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'server version: 0.07.1635; Python: 3.5.3; Arch: ; Os: Linux #1 SMP Debian 4.9.110-1 (2018-07-05); Django: 2.0.2')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'client version: 0.06.1634')), 1)

        def test05HelpPagePL(self):
        """test 'help' page_pl"""
        self.browser.reload()
        self.clickCssLink('#a_lang_pl')
        self.clickCssButton('#showHelpWindowButton')
        self.assertEqual(len(self.browser.find_by_text(u'DnaAssembler - Pomoc')), 1)
        self.assertEqual(self.browser.find_by_id('file_formats_href').first.text, u'Formaty plik??w wej??ciowych i wyj??ciowych')
        self.assertEqual(self.browser.find_by_id('file_formats_href').first['title'], u"Kliknij, aby zobaczy?? opis format??w plik??w wej??ciowych akceptowanych przez aplikacj?? i opis format??w plik??w wyj??ciowych produkowanych przez aplikacj??")
        self.assertEqual(self.browser.find_by_id('file_formats_href').first.text, u'Parametry i algorytmy wykorzystane w aplikacji')
        self.assertEqual(self.browser.find_by_id('file_formats_href').first['title'], u"Kliknij, aby zobaczy?? opis parametr??w i algorytm??w wykorzystanych w aplikacji")
        self.assertEqual(len(self.browser.find_by_text(u'Uzyskaj wi??cej informacji wysy??aj??c wiadomo????:')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'r.m.nowak@elka.pw.edu.pl')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Autorzy')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Robert Nowak - r.m.nowak@elka.pw.edu.pl')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Wiktor Ku??mirek')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Politechnika Warszawska,')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Wydzia?? Elektroniki i Technik Informacyjnych,')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Warszawa 2015')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'Parametry aplikacji')), 1)
        self.assertNotEqual(self.browser.find_by_id('server_time_val').first.text, u'0')
        self.assertEqual(len(self.browser.find_by_text(u'wersja bazy danych: PostgreSQL 9.4.18 on x86_64-unknown-linux-gnu')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'wersja serwera: 0.07.1635; Python: 3.5.3; Arch: ; Os: Linux #1 SMP Debian 4.9.110-1 (2018-07-05); Django: 2.0.2')), 1)
        self.assertEqual(len(self.browser.find_by_text(u'wersja klienta: 0.06.1634')), 1)


if __name__ == "__main__":
    www_browser = sys.argv[1] if len(sys.argv) >= 2 else 'chrome'
    www_addr = sys.argv[2] if len(sys.argv) >= 3 else '127.0.0.1'
    www_port = sys.argv[3] if len(sys.argv) >= 4 else '9000'
    admin_user = sys.argv[4] if len(sys.argv) >= 5 else ''
    admin_user_password = sys.argv[5] if len(sys.argv) >= 6 else ''

    browser = None

    try:
        if www_browser == 'firefox':
            caps = {}
            caps['acceptInsecureCerts'] = True
            browser = Browser('firefox', capabilities=caps)
        else:
            browser = Browser(www_browser)
    except DriverNotFoundError:
        print("ERROR: WebDriver for browser '" + www_browser  + "' not found.")

    browser.driver.maximize_window()

    print('http://' + www_addr + ':' + www_port)

    browser.visit('http://' + www_addr + ':' + www_port)

    TestFunctionalDnaasm.browser = browser
    TestFunctionalDnaasm.admin_user = admin_user
    TestFunctionalDnaasm.admin_user_password = admin_user_password

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestFunctionalDnaasm))

    testToRun = 'all'

    if testToRun != 'all':
        anyTestWillBeRun = False

        for ts in suite:
            for t in ts:
                if testToRun not in t.id():
                    setattr(t, 'setUp', lambda: t.skipTest('Not running this time'))
                else:
                    anyTestWillBeRun = True
        if not anyTestWillBeRun:
            print('ERROR: Cannot run given test because it doesn\'t exist: ' + testToRun)
            sys.exit()

    try:
        from xmlrunner import XMLTestRunner
        if not os.path.exists('./reports'):
            os.makedirs('./reports')
        with open('./reports/functional_output.xml', 'wb') as output:
            XMLTestRunner(output=output, verbosity=3).run(suite)

    except ImportError:
        print("Failed to import xmlrunner library. Using TextTestRunner instead...\n\n")
        unittest.TextTestRunner(verbosity=3).run(suite)

    browser.quit()
