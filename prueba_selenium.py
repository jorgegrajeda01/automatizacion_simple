from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
sleep(2)
driver.get("https://hybridge.education")
sleep(2)
driver.get("https://openai.com")

#Lo que hace: Navega a la página de Google, luego a la página de Hybridge Education y finalmente a la página de OpenAI, con una pausa de 2 segundos entre cada navegación, luego cierra el navegador.