import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

cservice = webdriver.ChromeService('C:/Users/sanke/Desktop/TESTING/chromedriver-win64/chromedriver.exe')
CONFIGS = {"Driver": webdriver.Chrome(service=cservice),
           "URL": "https://www.spotify.com",
           "username": "spotifyseleniumspotify@gmail.com",
           "password": "abcd123xyz",
           "search_key": "drake"}


class SpotifyTest:

    def __init__(self):

        self.driver = CONFIGS["Driver"]
        self.URL = CONFIGS["URL"]
        self.user = CONFIGS["username"]
        self.password = CONFIGS["password"]
        self.search_key = CONFIGS["search_key"]
        self.Is_loggedin = False
        self.Is_search_result = False

    def getPage(self):

        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.cookiecloser = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#onetrust-close-btn-container > button'))).click()
        self.cur_url = self.driver.current_url()
        self.cur_url = True

        return self.cur_url

    def signIn(self):

        self.nav_account_list = self.driver.find_element("xpath",'//span[text()="Log in"]').click()
        self.user_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#login-username'))).send_keys(self.user)

        self.user_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#login-password'))).send_keys(self.password)
        self.submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#login-button > span.ButtonInner-sc-14ud5tc-0.liTfRZ.encore-bright-accent-set'))).click()
        self.Is_loggedin = True
        ActionChains(self.driver).key_down(Keys.ESCAPE)
        return self.Is_loggedin
    

    def searchArtist(self):
        self.search_locate = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#Desktop_LeftSidebar_Id > nav > div:nth-child(1) > ul > li:nth-child(2) > a'))).click()
        self.search_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.jEMA2gVoLgPQqAFrPhFw > header > div.hV9v6y_uYwdAsoiOHpzk.contentSpacing > div.rovbQsmAS_mwvpKHaVhQ > div > div > form > input'))).send_keys(self.search_key)
        self.find_artist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#searchPage > div > div > section.vKsgiy0W3aHYmZUlwHoQ.QyANtc_r7ff_tqrf5Bvc.Shelf > div.iKwGKEfAfW7Rkx2_Ba4E.Z4InHgCs2uhk0MU93y_a.deJGxfMNXUc8uApEGgoQ.nrVisibleCards-2.fJTotRs7ANTq1nrBwlqA > div > div > div > div.cofBW8sjoBtMAmzDgqKt > a'))).click()

        res = True
        return res

    def playSong(self):
        self.playsong = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.jEMA2gVoLgPQqAFrPhFw > div.main-view-container > div.main-view-container__scroll-node > div:nth-child(2) > div.main-view-container__scroll-node-child > main > section > div > div.EmeHQXR87mUskYK6xEde > div.contentSpacing > div:nth-child(1) > div > div.fnphAtjtCDYY99lYBfLK.PHHrto0Qhh4dJcnnPhwu > div > div > div:nth-child(2) > div:nth-child(3) > div > div.fS0C4IgbHviZxIVGC736 > div'))).click()
        time.sleep(5)
        self.pausesong = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.JG5J9NWJkaUO9fiKECMA > footer > div.udArIAqnfUQPQew2VAns > div.sVv2OQORCQ4kf6iKfUTF > div > div.XrZ1iHVHAPMya3jkB2sa > button'))).click()
        self.Is_page = True
        return self.Is_page
    
    def createPlaylist(self):
        self.clickonplus = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#Desktop_LeftSidebar_Id > nav > div.lHJd4oSttKLxkxuoZ0Lr.wM72343CksOCaL3bZvKK > div.hgJel0bLlS_1Uf0EIfSA > div.WxM1eb7qnneSkMiT4dvw > div:nth-child(2) > div > section:nth-child(1) > div.wv308QWnPnkI8n0GdqYO > button'))).click()
        
        res = True
        return res

    def addSong(self):
        self.find_song = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.jEMA2gVoLgPQqAFrPhFw > div.main-view-container > div.main-view-container__scroll-node > div:nth-child(2) > div.main-view-container__scroll-node-child > main > div.GlueDropTarget.GlueDropTarget--tracks.GlueDropTarget--local-tracks.GlueDropTarget--episodes.GlueDropTarget--albums > section > div.rezqw3Q4OEPB1m4rmwfw > div.contentSpacing > section > div > div > input'))).send_keys('Jimmy Cooks')
        self.add_song = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.jEMA2gVoLgPQqAFrPhFw > div.main-view-container > div.main-view-container__scroll-node > div:nth-child(2) > div.main-view-container__scroll-node-child > main > div.GlueDropTarget.GlueDropTarget--tracks.GlueDropTarget--local-tracks.GlueDropTarget--episodes.GlueDropTarget--albums > section > div.rezqw3Q4OEPB1m4rmwfw > div.contentSpacing > div > div:nth-child(1) > div > div:nth-child(2) > div:nth-child(1) > div > div.PAqIqZXvse_3h6sDVxU0 > button'))).click()
        time.sleep(5)

        self.added_song =  True

    def playLoopPlaylist(self):
        self.playPlaylist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.jEMA2gVoLgPQqAFrPhFw > div.main-view-container > div.main-view-container__scroll-node > div:nth-child(2) > div.main-view-container__scroll-node-child > main > div.GlueDropTarget.GlueDropTarget--tracks.GlueDropTarget--local-tracks.GlueDropTarget--episodes.GlueDropTarget--albums > section > div.rezqw3Q4OEPB1m4rmwfw > div:nth-child(2) > div:nth-child(2) > div > div > div.ix_8kg3iUb9VS5SmTnBY > button'))).click()
        time.sleep(2)
        self.LoopPlaylist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.JG5J9NWJkaUO9fiKECMA > footer > div > div.sVv2OQORCQ4kf6iKfUTF > div > div.XrZ1iHVHAPMya3jkB2sa > div.Qt226Z4rBQs53aedRQBQ > button:nth-child(2)'))).click()
        res = True
        return res
    
    def checkProfile(self):
        self.click_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.jEMA2gVoLgPQqAFrPhFw > header > div.hV9v6y_uYwdAsoiOHpzk.contentSpacing > div.rwdnt1SmeRC_lhLVfIzg > button.Button-sc-1dqy6lx-0.kTFJuL.encore-text-body-medium-bold.encore-over-media-set.SFgYidQmrqrFEVh65Zrg'))).click()
        self.open_profile = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#context-menu > div > ul > li:nth-child(2) > a > span'))).click()
        time.sleep(5)
        self.IsProfile = True

    def followProfile(self):
        self.search_locate = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#Desktop_LeftSidebar_Id > nav > div:nth-child(1) > ul > li:nth-child(2) > a'))).click()
        self.search_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.jEMA2gVoLgPQqAFrPhFw > header > div.hV9v6y_uYwdAsoiOHpzk.contentSpacing > div.rovbQsmAS_mwvpKHaVhQ > div > div > form > input'))).send_keys('srihari_v_r')
        self.find_artist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#searchPage > div > div > section.vKsgiy0W3aHYmZUlwHoQ.QyANtc_r7ff_tqrf5Bvc.Shelf > div.iKwGKEfAfW7Rkx2_Ba4E.Z4InHgCs2uhk0MU93y_a.deJGxfMNXUc8uApEGgoQ.nrVisibleCards-2.fJTotRs7ANTq1nrBwlqA > div > div > div > div.cofBW8sjoBtMAmzDgqKt > a'))).click()
        self.followArtist = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.jEMA2gVoLgPQqAFrPhFw > div.main-view-container > div.main-view-container__scroll-node > div:nth-child(2) > div.main-view-container__scroll-node-child > main > section > div > div:nth-child(3) > div:nth-child(2) > div > div > button.Button-sc-y0gtbx-0.fbysdG.encore-text-body-small-bold'))).click()
        time.sleep(3)
        self.is_followed = True

    def logout(self):
        self.click_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#main > div > div.ZQftYELq0aOsg6tPbVbV > div.jEMA2gVoLgPQqAFrPhFw > header > div.hV9v6y_uYwdAsoiOHpzk.contentSpacing > div.rwdnt1SmeRC_lhLVfIzg > button.Button-sc-1dqy6lx-0.kTFJuL.encore-text-body-medium-bold.encore-over-media-set.SFgYidQmrqrFEVh65Zrg'))).click()
        time.sleep(5)
        self.log_out = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#context-menu > div > ul > li:nth-child(5) > button'))).click()
        time.sleep(5)
        return True

class TestSpotifyTest:

    def test_getPage(self):

        spotify_class_instance = SpotifyTest()
        url = spotify_class_instance.getPage()
        assert url == True 

    def test_signIn(self):

        spotify_class_instance = SpotifyTest()
        spotify_class_instance.signIn()
        assert spotify_class_instance.Is_loggedin == True
        ActionChains(spotify_class_instance.driver).key_down(Keys.ESCAPE).perform()

    def test_searchArtist(self):

        spotify_class_instance = SpotifyTest()
        res = spotify_class_instance.searchArtist()
        assert res == True

    def test_Playsong(self):

        spotify_class_instance = SpotifyTest()
        spotify_class_instance.playSong()
        assert spotify_class_instance.Is_page == True

    def test_createPlaylist(self):

        spotify_class_instance = SpotifyTest()
        res = spotify_class_instance.createPlaylist()
        assert res  == True

    def test_addSong(self):

        spotify_class_instance = SpotifyTest()
        spotify_class_instance.addSong()
        assert spotify_class_instance.added_song == True
    
    def test_playLoopPlaylist(self):

        spotify_class_instance = SpotifyTest()
        res= spotify_class_instance.playLoopPlaylist()
        assert res == True

    def test_checkProfile(self):

        spotify_class_instance = SpotifyTest()
        spotify_class_instance.checkProfile()
        assert spotify_class_instance.IsProfile == True

    def test_followProfile(self):
        spotify_class_instance = SpotifyTest()
        spotify_class_instance.followProfile()
        assert spotify_class_instance.is_followed == True

    def test_logout(self):
        spotify_class_instance = SpotifyTest()
        lo = spotify_class_instance.logout()
        assert lo == True

