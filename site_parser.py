from time import sleep
from PySide6.QtCore import Signal, QObject
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from datetime import datetime
import cv2
import numpy as np


class Model(QObject):
    sections_titles_changed = Signal(list)
    parsing_completed = Signal(str)
    change_progress_bar = Signal(int)


class Parser:
    def __init__(self, ):
        self.model = Model()
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override",
                               'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36')
        options = Options()
        options.headless = True
        self.driver = webdriver.Firefox(
            firefox_profile=profile, options=options)
        self.action = webdriver.ActionChains(self.driver)
        self.url = ''
        self.result_folder = './Result/'
        self.pages_count = 1
        self.saved_photos_count = 0
        self.sections_titles = []
        self.fast_photos_loading = False
        self.sections_titles_dictionary = {}

    def check_file_exists(self, path):
        if os.path.exists(path):
            for i in range(1, 99999):
                print(path[:-4] + f' ({i}).png')
                print(path)
                print('.')
                if not os.path.exists(path[:-4] + f' ({i}).png'):
                    return path + f' ({i}).png'
        else:
            return path

    def create_directory_if_exists(self, path):
        for i in range(1, 99999):
            try:
                os.makedirs(f'{path} ({i})')
            except OSError:
                print('Директория %a уже существует' % (f'{path} ({i})'))
            else:
                break

    def create_directory(self, section, album=''):
        directory_name = self.result_folder + section + '/' + album
        try:
            if os.path.exists(directory_name):
                self.create_directory_if_exists(directory_name)
            else:
                os.makedirs(directory_name)
        except Exception as exc:
            print(f'Создать директорию {1} не удалось \n {2}',
                  directory_name, exc)

    def parse_sections_titles(self):
        self.sections_titles = []
        temp_sections_titles = []
        self.driver.get(f'{self.url}/albums')
        try:
            pages_count_element = self.driver.find_element(
                By.XPATH, '/html/body/nav/form/span[1]')
            self.pages_count = int(((pages_count_element.text).split(' '))[2])
        except:
            pass
        for page in range(1, self.pages_count+1):
            if page != 1:
                self.driver.get(f'{self.url}/albums?page={page}')
            sections_on_page = self.driver.find_elements(
                By.CLASS_NAME, 'show-layout-category__catewrap')
            for section in sections_on_page:
                section_title = section.find_element(
                    By.TAG_NAME, 'a').get_attribute('title')
                if section_title in temp_sections_titles:
                    duplicates_count = ''.join(
                        temp_sections_titles).count(section_title)-1
                    self.sections_titles.append(
                        section_title+f'({duplicates_count})')
                else:
                    temp_sections_titles.append(section_title)
        self.sections_titles = temp_sections_titles
        self.driver.get(f'{self.url}/albums')
        self.model.sections_titles_changed.emit(self.sections_titles)

    def crop_photo(self, path):
        image = cv2.imread(path)
        y_nonzero, x_nonzero, _ = np.nonzero(image > 50)
        cropped_image = image[np.min(y_nonzero):np.max(
            y_nonzero), np.min(x_nonzero):np.max(x_nonzero)]
        cv2.imwrite(path, cropped_image)

    def save_photo(self, photo_path):
        path = self.check_file_exists(
            photo_path.encode('ascii', 'ignore').decode())
        print(path)
        try:
            self.driver.save_screenshot(path)
            self.crop_photo(path)
        except:
            print('Не удалось сохранить фото, пробую ещё раз')
            self.save_photo(photo_path)

    def parse(self):
        self.saved_photos_count = 0
        try:
            pages_count_element = self.driver.find_element(
                By.XPATH, '/html/body/nav/form/span[1]')
            self.pages_count = int(((pages_count_element.text).split(' '))[2])
        except:
            pass
        for page in range(1, self.pages_count+1):
            if page != 1:
                self.driver.get(f'{self.url}/albums?page={page}')
            sections_on_page = self.driver.find_elements(
                By.CLASS_NAME, 'show-layout-category__catetitle')
            if len(sections_on_page) > 0:
                for i in range(0, len(sections_on_page)):
                    section = self.driver.find_elements(
                        By.CLASS_NAME, 'show-layout-category__catetitle')[i]
                    section_title = section.get_attribute('title')
                    if self.sections_titles_dictionary.get(section_title) or len(self.sections_titles_dictionary) == 0:
                        section_link = section.get_attribute('href')
                        section.click()
                        albums_pages_count = 1
                        try:
                            self.driver.find_element(
                                By.XPATH, """//span[contains(text(), 'in total')]""")
                        except:
                            pass
                        else:
                            albums_pages_count_element = self.driver.find_element(
                                By.XPATH, """//span[contains(text(), 'in total')]""")
                            albums_pages_count = int(
                                ((albums_pages_count_element.text).split(' '))[2])
                        for albums_page in range(1, albums_pages_count+1):
                            if albums_page != 1:
                                self.driver.get(
                                    section_link + f'?page={albums_page}')
                            albums_in_section = self.driver.find_elements(
                                By.CLASS_NAME, 'album__main')
                            for album_num in range(0, len(albums_in_section)):
                                album = self.driver.find_elements(
                                    By.CLASS_NAME, 'album__main')[album_num]
                                is_block = album.find_element(
                                    By.CLASS_NAME, 'album__imgwrap')
                                if len(is_block.find_elements(By.TAG_NAME, 'div')) < 2:
                                    album_title = album.get_attribute('title')
                                    self.create_directory(
                                        section_title, album_title)
                                    album.click()
                                    album_link = self.driver.current_url
                                    photos_pages_count = 1
                                    try:
                                        self.driver.find_element(
                                            By.XPATH, """//span[contains(text(), 'in total')]""")
                                    except:
                                        pass
                                    else:
                                        photos_pages_count_element = self.driver.find_element(
                                            By.XPATH, """//span[contains(text(), 'in total')]""")
                                        photos_pages_count = int(
                                            ((photos_pages_count_element.text).split(' '))[2])
                                    for photos_page in range(1, photos_pages_count+1):
                                        if photos_page != 1:
                                            self.driver.get(
                                                album_link + f'&page={photos_page}')
                                        photos_on_page = self.driver.find_elements(
                                            By.CLASS_NAME, 'image__img')
                                        for photo_num in range(0, len(photos_on_page)):
                                            photos_clickhandlers_on_page = self.driver.find_elements(
                                                By.CLASS_NAME, 'image__clickhandle')
                                            try:
                                                photos_clickhandlers_on_page[photo_num].click(
                                                )
                                            except:
                                                sleep(1)
                                                photos_clickhandlers_on_page[photo_num].click(
                                                )
                                            photo_title = self.driver.find_element(
                                                By.CLASS_NAME, 'viewer__title').text
                                            photo_path = self.result_folder + \
                                                f'{section_title.replace("/", "|")}/{album_title.replace("/", "|")}/{photo_title.replace("/", "|")}.png'
                                            photo_on_full_screen_element = self.driver.find_element(
                                                By.ID, 'viewer__origin_img')
                                            self.action.key_down(Keys.CONTROL).click(
                                                photo_on_full_screen_element).key_up(Keys.CONTROL).perform()
                                            self.driver.switch_to.window(
                                                self.driver.window_handles[-1])
                                            if not self.fast_photos_loading:
                                                sleep(1)
                                            self.save_photo(photo_path)
                                            self.saved_photos_count += 1

                                            self.driver.close()
                                            self.driver.switch_to.window(
                                                self.driver.window_handles[0])
                                            self.driver.find_element(
                                                By.ID, 'viewer__close').click()
                                            sleep(0.5)
                                self.driver.get(section_link)

                    self.driver.get(
                        f'{self.url}/albums?page={page}')
            else:
                albums_in_section = self.driver.find_elements(
                    By.CLASS_NAME, 'album3__main')
                for album_num in range(0, len(albums_in_section)):
                    album = self.driver.find_elements(
                        By.CLASS_NAME, 'album3__main')[album_num]
                    is_block = album.find_element(
                        By.CLASS_NAME, 'album__imgwrap')
                    if len(is_block.find_elements(By.TAG_NAME, 'div')) < 2:
                        album_title = self.driver.find_elements(
                            By.CLASS_NAME, 'album3__title')[album_num].text
                        self.create_directory(album_title)
                        album.click()
                        album_link = self.driver.current_url
                        photos_pages_count = 1
                        try:
                            self.driver.find_element(
                                By.XPATH, """//span[contains(text(), 'in total')]""")
                        except:
                            pass
                        else:
                            photos_pages_count_element = self.driver.find_element(
                                By.XPATH, """//span[contains(text(), 'in total')]""")
                            photos_pages_count = int(
                                ((photos_pages_count_element.text).split(' '))[2])
                        for photos_page in range(1, photos_pages_count+1):
                            if photos_page != 1:
                                self.driver.get(
                                    album_link + f'&page={photos_page}')
                            photos_on_page = self.driver.find_elements(
                                By.CLASS_NAME, 'image__img')
                            for photo_num in range(0, len(photos_on_page)):
                                photos_clickhandlers_on_page = self.driver.find_elements(
                                    By.CLASS_NAME, 'image__clickhandle')
                                photos_clickhandlers_on_page[photo_num].click(
                                )
                                photo_title = self.driver.find_element(
                                    By.CLASS_NAME, 'viewer__title').text
                                photo_path = self.result_folder + \
                                    f'{album_title}/{photo_title}.png'
                                photo_on_full_screen_element = self.driver.find_element(
                                    By.ID, 'viewer__origin_img')
                                self.action.key_down(Keys.CONTROL).click(
                                    photo_on_full_screen_element).key_up(Keys.CONTROL).perform()
                                self.driver.switch_to.window(
                                    self.driver.window_handles[-1])
                                if not self.fast_photos_loading:
                                    sleep(1)
                                self.save_photo(photo_path)
                                self.saved_photos_count += 1
                                self.driver.close()
                                self.driver.switch_to.window(
                                    self.driver.window_handles[0])
                                self.driver.find_element(
                                    By.ID, 'viewer__close').click()
                                sleep(0.5)
        self.model.parsing_completed.emit('')

    def get_saved_photos_count(self):
        return self.saved_photos_count

    def clear_sections_titles(self):
        self.sections_titles = []

    def set_sections_titles_dictionary(self, dict):
        self.sections_titles_dictionary = dict

    def set_fast_photos_loading(self, value: bool):
        self.fast_photos_loading = value

    def set_url(self, url):
        self.url = url
        if self.url.endswith('com/'):
            self.url = self.url[:-1]
        if self.url.endswith('albums'):
            self.url = self.url[:-7]
        if self.url.endswith('albums/'):
            self.url = self.url[:-8]
        if not self.url.startswith('http'):
            self.url = 'https://' + self.url

    def get_sections_titles(self):
        return self.sections_titles

    def main(self):
        self.result_folder = self.result_folder + \
            ((f'{str(datetime.now()).replace(":", "-")}'[:-7]) + '/')
        os.makedirs(self.result_folder)
        self.driver.get(self.url)
        self.parse()
