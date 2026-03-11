# importar la función By de selenium.webdriver.common.by,
# misma que permite seleccionar elementos de una página web
# por medio de selectores CSS.
from selenium.webdriver.common.by import By

# Función para obtener el clima (usa texto genérico y regex)
# Parámetros:
# - driver: objeto de Selenium WebDriver
# - consulta: cadena de texto que contiene la consulta del usuario
def obtener_clima(driver, consulta):
    # navegar a la búsqueda de clima en Google
    driver.get(f"https://www.google.com/search?q=clima+{consulta}")

    try:
        # leer todo el texto del <body> y buscar la primera temperatura
        texto = driver.find_element(By.TAG_NAME, "body").text
        import re
        m = re.search(r"(\d+\s*°[CF])", texto)
        if not m:
            raise ValueError("no se encontró temperatura en el cuerpo de la página")
        temp = m.group(1)
        # quitar palabra repetida "clima" si el usuario la puso
        ciudad = consulta.replace("clima", "", 1).strip().title()
        return f"{temp} en {ciudad}."
    except Exception as e:
        # incluir el mensaje real ayuda en depuración
        return f"No se pudo obtener el clima: {e}"