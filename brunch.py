from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://pikabu.ru/')

tabs = ['Главная', 'Популярное', 'Новое', 'Сообщества', 'Каналы', 'Хабы', 'Картинки', 'Видео', 'Интересно', 'new tab']
for tab in tabs:
    driver.find_element_by_link_text(tab).click()
    assert tab in driver.title, f'Ошибка: не удалось перейти на вкладку {tab}'
    time.sleep(2)

driver.quit()