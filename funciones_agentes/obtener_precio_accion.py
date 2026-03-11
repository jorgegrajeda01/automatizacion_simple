# importar la función By de selenium.webdriver.common.by,
# misma que permite seleccionar elementos de una página web
# por medio de selectores CSS.
from selenium.webdriver.common.by import By

# Función para obtener el precio de una acción mediante búsqueda y regex
# Parámetros:
# - driver: objeto de Selenium WebDriver
# - consulta: cadena de texto que contiene la consulta del usuario
def obtener_precio_accion(driver, consulta):
    driver.get(f"https://www.google.com/search?q=precio+acción+{consulta}")

    try:
        texto = driver.find_element(By.TAG_NAME, "body").text
        import re
        # primer intento: buscar frase típica "hoy es 260.83" para evitar coincidencias de encabezado
        m = re.search(r"hoy\s+es\s*([\d\.,]+)", texto, re.IGNORECASE)
        if not m:
            # fallback: cualquier número después de la palabra precio
            m = re.search(r"precio.*?([\d\.,]+)", texto, re.IGNORECASE | re.DOTALL)
        if not m:
            raise ValueError("no se encontró precio en el cuerpo de la página")
        precio = m.group(1)
        nombre = consulta.title()
        return f"{nombre}: {precio}"
    except Exception as e:
        return f"No se pudo obtener el precio de la acción: {e}"