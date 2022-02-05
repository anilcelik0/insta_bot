from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from index import Ui_Form
from portal import Ui_MainWindow
from takip import Ui_Form1
from takipci import Ui_Form2
from unfollow import Ui_Form3


class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.GirisYap.clicked.connect(self.save)
        self.ui.GirisYap.clicked.connect(self.portal)
        
        
    def save(self):
        self.username = self.ui.leUsername.text()
        self.password = self.ui.lePassword.text()

        
    def portal(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui1 = Ui_MainWindow()
        self.ui1.setupUi(self.window1)
        self.window1.show()
    
        
        self.ui1.lbusername.setText(self.username)
        self.ui1.lbusername.setAlignment(QtCore.Qt.AlignCenter)
        myApp.insselenium(self)
        

        self.ui1.lbLenTakipci.setText(str(len(self.listTakipci)))
        self.ui1.lbLenTakipci.setAlignment(QtCore.Qt.AlignCenter)
        self.ui1.lbLenTakip.setText(str(len(self.listTakip)))
        self.ui1.lbLenTakip.setAlignment(QtCore.Qt.AlignCenter)
        self.ui1.btnRefresch.clicked.connect(self.insselenium)
        self.ui1.lbLenTakip.setFont(QtGui.QFont('align',12))
        self.ui1.lbLenTakipci.setFont(QtGui.QFont('align',12))
        self.ui1.lbusername.setFont(QtGui.QFont('align',12))
        
        
        self.ui1.btnTakip.clicked.connect(self.takip)
        self.ui1.btnTakipci.clicked.connect(self.takipci)
        self.ui1.btnunfollow.clicked.connect(self.unfollow)
        

    def insselenium(self):
        myApp.insLists(self)
        myApp.insGiris(self)
        myApp.takipList(self)
        myApp.takipcilist(self)
        myApp.saveTakipci(self)
        myApp.saveTakip(self)
        myApp.notFollow(self)
        QtWidgets.QMessageBox.question(self, 'instakip', "Yükleme tamam", QtWidgets.QMessageBox.Ok)
        

    def insLists(self):
        self.listTakipciLink = []
        self.listTakipLink = []
        self.listTakip = []
        self.listTakipci = []
        self.listNotFollow = []

    def insGiris(self):
        coptions = Options()
        coptions.add_argument('--headless')
        self.br  = webdriver.Chrome()
        url = "https://www.instagram.com/"
        self.br.get(url)
        giris1 = WebDriverWait(self.br,10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
        )
        giris1.send_keys(self.username)
        self.br.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        self.br.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()

    def bekle(self):
        WebDriverWait(self.br, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/ul/div/li'))
        )

    def takipList(self):
        WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span'))
        )
        self.br.get(f'https://www.instagram.com/{self.username}')

        takip = WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'))
        )
        takip.click()
        time.sleep(1)
        dialog = self.br.find_element_by_css_selector('div[role=dialog] ul')
        followerCount = len(dialog.find_elements_by_css_selector('li'))
        action = webdriver.ActionChains(self.br)
        dialog.click()
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(2)
        while True:
            dialog.click()
            dialog.click()
            i=0
            while i<50:
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                i+=1
            time.sleep(3)
            newCount = len(dialog.find_elements_by_css_selector('li'))

            if followerCount != newCount:
                followerCount = newCount
                time.sleep(1)
            else:
                break


        followers = dialog.find_elements_by_css_selector('li')
        time.sleep(1)
        for user in followers:
            link = user.find_element_by_css_selector('a').get_attribute('href')
            self.listTakipLink.append(link)

    def takipcilist(self):
        self.br.get(f'https://www.instagram.com/{self.username}')
        takipci = WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'))
        )
        takipci.click()
        time.sleep(1)
        dialog = self.br.find_element_by_css_selector('div[role=dialog] ul')
        followerCount = len(dialog.find_elements_by_css_selector('li'))
        action = webdriver.ActionChains(self.br)
        dialog.click()
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(2)
        while True:
            dialog.click()
            dialog.click()
            i=0
            while i<50:
                action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                i+=1
            time.sleep(3)
            newCount = len(dialog.find_elements_by_css_selector('li'))
            
            if followerCount != newCount:
                followerCount = newCount
                time.sleep(1)
            else:
                break


        followers = dialog.find_elements_by_css_selector('li')
        time.sleep(1)

        for user in followers:
            link = user.find_element_by_css_selector('a').get_attribute('href')
            self.listTakipciLink.append(link)


    def saveTakipci(self):    
        for user in self.listTakipciLink:
            result = user.split("/")
            self.listTakipci.append(result[3])

    
    def saveTakip(self):
        for user in self.listTakipLink:
            result = user.split("/")
            self.listTakip.append(result[3])

    def notFollow(self):
        for takip in self.listTakip:
            if takip in self.listTakipci:
                pass
            else:
                self.listNotFollow.append(takip)



    def takip(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Form1()
        self.i = 0
        self.ui.setupUi(self.window2)
        self.window2.show()
        self.window1.show()
        self.listTakipYedek = self.listTakip
        self.listAsil = len(self.listTakipYedek)  
        self.a = self.listAsil % 10
        self.b = 11 - self.a
        for sayi in range(1,self.b):
            self.listTakipYedek.append('* '*sayi)



        myApp.yazdirTakip(self)
        self.ui.btnBack.clicked.connect(self.eksiTakip)
        self.ui.btnNext.clicked.connect(self.artiTakip)       

    
    def artiTakip(self):
        if self.i>self.listAsil-self.a-10:
            pass
        else:
            self.i+=10
            myApp.yazdirTakip(self)


    def eksiTakip(self):  
        if self.i>=10:
            self.i-=10
            myApp.yazdirTakip(self)
        else:
            pass

    def yazdirTakip(self):
        if self.i <= self.listAsil+self.b-1:
            self.ui.lbusername.setText(self.listTakipYedek[self.i])
            self.ui.btnunfollow.clicked.connect(self.block1) 

            self.ui.lbusername_2.setText(self.listTakipYedek[self.i+1])
            self.ui.btnunfollow_2.clicked.connect(self.block2)

            self.ui.lbusername_3.setText(self.listTakipYedek[self.i+2])
            self.ui.btnunfollow_3.clicked.connect(self.block3)

            self.ui.lbusername_4.setText(self.listTakipYedek[self.i+3])
            self.ui.btnunfollow_4.clicked.connect(self.block4)

            self.ui.lbusername_5.setText(self.listTakipYedek[self.i+4])
            self.ui.btnunfollow_5.clicked.connect(self.block5)

            self.ui.lbusername_6.setText(self.listTakipYedek[self.i+5])
            self.ui.btnunfollow_6.clicked.connect(self.block6)

            self.ui.lbusername_7.setText(self.listTakipYedek[self.i+6])
            self.ui.btnunfollow_7.clicked.connect(self.block7)

            self.ui.lbusername_8.setText(self.listTakipYedek[self.i+7])
            self.ui.btnunfollow_8.clicked.connect(self.block8)
            
            self.ui.lbusername_9.setText(self.listTakipYedek[self.i+8])
            self.ui.btnunfollow_9.clicked.connect(self.block9)

            self.ui.lbusername_10.setText(self.listTakipYedek[self.i+9])
            self.ui.btnunfollow_10.clicked.connect(self.block10)
                



    def block1(self):
        self.ui.btnunfollow.setText('...')
        self.br.get(f'https://www.instagram.com/{self.ui.lbusername.text()}')
        WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).click()
        WebDriverWait(self.br,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]'))).click()
        self.ui.btnunfollow.setText('Başarılı')

    def block2(self):
        self.ui.btnunfollow_2.setText('...')
        self.br.get(f'https://www.instagram.com/{self.ui.lbusername_2.text()}')
        WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).click()
        WebDriverWait(self.br,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]'))).click()
        self.ui.btnunfollow_2.setText('Başarılı')

    def block3(self):
        self.ui.btnunfollow_3.setText('...')
        self.br.get(f'https://www.instagram.com/{self.ui.lbusername_3.text()}')
        WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).click()
        WebDriverWait(self.br,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]'))).click()
        self.ui.btnunfollow_3.setText('Başarılı')
    
    def block4(self):
        self.ui.btnunfollow_4.setText('...')
        self.br.get(f'https://www.instagram.com/{self.ui.lbusername_4.text()}')
        WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).click()
        WebDriverWait(self.br,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]'))).click()
        self.ui.btnunfollow_4.setText('Başarılı')

    def block5(self):
        self.ui.btnunfollow_5.setText('...')
        self.br.get(f'https://www.instagram.com/{self.ui.lbusername_5.text()}')
        WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).click()
        WebDriverWait(self.br,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]'))).click()
        self.ui.btnunfollow_5.setText('Başarılı')

    def block6(self):
        self.ui.btnunfollow_6.setText('...')
        self.br.get(f'https://www.instagram.com/{self.ui.lbusername_6.text()}')
        WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).click()
        WebDriverWait(self.br,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]'))).click()
        self.ui.btnunfollow_6.setText('Başarılı')

    def block7(self):
        self.ui.btnunfollow_7.setText('...')
        self.br.get(f'https://www.instagram.com/{self.ui.lbusername_7.text()}')
        WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).click()
        WebDriverWait(self.br,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]'))).click()
        self.ui.btnunfollow_7.setText('Başarılı')

    def block8(self):
        self.ui.btnunfollow_8.setText('...')
        self.br.get(f'https://www.instagram.com/{self.ui.lbusername_8.text()}')
        WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).click()
        WebDriverWait(self.br,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]'))).click()
        self.ui.btnunfollow_8.setText('Başarılı')
        

    def block9(self):
        self.ui.btnunfollow_9.setText('...')
        self.br.get(f'https://www.instagram.com/{self.ui.lbusername_9.text()}')
        WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).click()
        WebDriverWait(self.br,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]'))).click()
        self.ui.btnunfollow_9.setText('Başarılı')

    def block10(self):
        self.ui.btnunfollow_10.setText('...')
        self.br.get(f'https://www.instagram.com/{self.ui.lbusername_10.text()}')
        WebDriverWait(self.br, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button'))).click()
        WebDriverWait(self.br,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[1]'))).click()
        self.ui.btnunfollow_10.setText('Başarılı')


    
    def takipci(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_Form2()
        self.i =0
        self.ui.setupUi(self.window3)
        self.window3.show()
        self.window1.show()
        self.listTakipciYedek = self.listTakipci
        self.listAsil = len(self.listTakipci)  
        self.a = self.listAsil % 10
        self.b = 11 - self.a
        for sayi in range(1,self.b):
            self.listTakipciYedek.append('* '*sayi)

        myApp.yazdirTakipci(self)
        self.ui.btnBack.clicked.connect(self.eksiTakipci)
        self.ui.btnNext.clicked.connect(self.artiTakipci) 
     




    def eksiTakipci(self):
        if self.i>=10:
            self.i-=10
            myApp.yazdirTakipci(self)
        else:
            pass

    def artiTakipci(self):
        if self.i>self.listAsil-self.a-10:
            pass
        else:
            self.i+=10
            myApp.yazdirTakipci(self)


    def yazdirTakipci(self):
        if self.i <= self.listAsil+self.b-1:
            self.ui.lbusername.setText(self.listTakipciYedek[self.i])

            self.ui.lbusername_2.setText(self.listTakipciYedek[self.i+1])

            self.ui.lbusername_3.setText(self.listTakipciYedek[self.i+2])

            self.ui.lbusername_4.setText(self.listTakipciYedek[self.i+3])

            self.ui.lbusername_5.setText(self.listTakipciYedek[self.i+4])

            self.ui.lbusername_6.setText(self.listTakipciYedek[self.i+5])

            self.ui.lbusername_7.setText(self.listTakipciYedek[self.i+6])

            self.ui.lbusername_8.setText(self.listTakipciYedek[self.i+7])
            
            self.ui.lbusername_9.setText(self.listTakipciYedek[self.i+8])

            self.ui.lbusername_10.setText(self.listTakipciYedek[self.i+9])



    def unfollow(self):
        self.window4 = QtWidgets.QMainWindow()
        self.ui = Ui_Form3()
        self.i=0
        self.ui.setupUi(self.window4)
        self.window4.show()
        self.window1.show()
        self.listNotFollowYedek = self.listNotFollow
        self.listAsil = len(self.listNotFollow)  
        self.a = self.listAsil % 10
        self.b = 11 - self.a
        for sayi in range(1,self.b):
            self.listNotFollowYedek.append('* '*sayi)



        myApp.yazdirUnfollow(self)
        self.ui.btnBack.clicked.connect(self.eksiUnfollow)
        self.ui.btnNext.clicked.connect(self.artiUnfollow)  



    def eksiUnfollow(self):
        if self.i>=10:
            self.i-=10
            myApp.yazdirUnfollow(self)
        else:
            pass

    def artiUnfollow(self):
        if self.i>self.listAsil-self.a-10:
            pass
        else:
            self.i+=10
            myApp.yazdirUnfollow(self)

    
    def yazdirUnfollow(self):
        if self.i <= self.listAsil+self.b-1:
            self.ui.lbusername.setText(self.listNotFollowYedek[self.i])
            self.ui.btnunfollow.clicked.connect(self.block1) 

            self.ui.lbusername_2.setText(self.listNotFollowYedek[self.i+1])
            self.ui.btnunfollow_2.clicked.connect(self.block2)

            self.ui.lbusername_3.setText(self.listNotFollowYedek[self.i+2])
            self.ui.btnunfollow_3.clicked.connect(self.block3)

            self.ui.lbusername_4.setText(self.listNotFollowYedek[self.i+3])
            self.ui.btnunfollow_4.clicked.connect(self.block4)

            self.ui.lbusername_5.setText(self.listNotFollowYedek[self.i+4])
            self.ui.btnunfollow_5.clicked.connect(self.block5)

            self.ui.lbusername_6.setText(self.listNotFollowYedek[self.i+5])
            self.ui.btnunfollow_6.clicked.connect(self.block6)

            self.ui.lbusername_7.setText(self.listNotFollowYedek[self.i+6])
            self.ui.btnunfollow_7.clicked.connect(self.block7)

            self.ui.lbusername_8.setText(self.listNotFollowYedek[self.i+7])
            self.ui.btnunfollow_8.clicked.connect(self.block8)
            
            self.ui.lbusername_9.setText(self.listNotFollowYedek[self.i+8])
            self.ui.btnunfollow_9.clicked.connect(self.block9)

            self.ui.lbusername_10.setText(self.listNotFollowYedek[self.i+9])
            self.ui.btnunfollow_10.clicked.connect(self.block10)

        
    


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())
    


    

app()




