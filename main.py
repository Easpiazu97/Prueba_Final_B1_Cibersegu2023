import random
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from db import MongoDriver

driver = webdriver.Chrome()
driver.get("https://almacenesjapon.com/51-telefon%C3%ADa")

boton = driver.find_element(By.XPATH, '//a[@rel="next"]')

mongodb = MongoDriver()

for i in range(2):
    try:
        telefonos = driver.find_elements(By.XPATH, '//article[@data-id-product-attribute="0"]')
        for telefono in telefonos:
            try:
                titulo = telefono.find_element(By.XPATH, './/h2[@itemprop="name"]').text
                precio = telefono.find_element(By.XPATH, './/span[@itemprop="offers"]').text

                telefono_guardar={
                    "titulo": titulo,
                    "precio": precio
                }
                mongodb.insert_record(record=telefono_guardar, username="Almacenes_Japon")
            except Exception as e:
                print(e)
                print("++++++++++++++++++++++++++++++++")

        boton.click()
        sleep(random.uniform(8.0, 10.0))
        boton = driver.find_element(By.XPATH, '//a[@rel="next"]')
    except:
        break


driver.close()