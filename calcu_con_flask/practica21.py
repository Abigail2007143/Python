from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializar el navegador
driver = webdriver.Chrome()

# Abrir Google
driver.get("https://www.google.com/")

# Buscar el cuadro de búsqueda
web_element = driver.find_element(By.NAME, "q")  # 'q' es el nombre del campo de búsqueda en Google

# Escribir en el cuadro de búsqueda y presionar Enter
web_element.send_keys("Selenium WebDriver")
web_element.send_keys(Keys.ENTER)

# Esperar unos segundos para visualizar los resultados
time.sleep(10)

# Cerrar el navegador
driver.quit()
