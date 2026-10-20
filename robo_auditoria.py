
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    try:
        # Tarefa 1: abrir três abas e verificar a quantidade
        driver.get("https://the-internet.herokuapp.com/dropdown")

        driver.execute_script(
            "window.open('https://the-internet.herokuapp.com/dynamic_loading/2', '_blank')"
        )
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) >= 2
        )

        driver.execute_script(
            "window.open('https://pt.wikipedia.org', '_blank')"
        )
        WebDriverWait(driver, 10).until(
            lambda d: len(d.window_handles) >= 3
        )

        abas = driver.window_handles
        print("Quantidade de abas:", len(abas))

        # Tarefa 2: selecionar Option 1
        driver.switch_to.window(abas[0])

        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_visible_text("Option 1")

        print("\n--- Dropdown ---")
        print("Opção selecionada:", dropdown.first_selected_option.text)
        print("Valor:", dropdown.first_selected_option.get_attribute("value"))

        # Tarefa 3: aguardar o carregamento dinâmico
        driver.switch_to.window(abas[1])
        driver.find_element(By.CSS_SELECTOR, "#start button").click()

        resultado = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        print("\n--- Carregamento dinâmico ---")
        print("Texto:", resultado.text)

        # Tarefa 4: pesquisar na Wikipédia
        driver.switch_to.window(abas[2])

        campo = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.NAME, "search"))
        )
        campo.send_keys("Automação")
        campo.submit()

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "content"))
        )

        print("\n--- Links da barra lateral da Wikipédia ---")

        links = driver.find_elements(
            By.CSS_SELECTOR,
            "#mw-panel a, #vector-toc a, #mw-navigation a"
        )

        for link in links:
            if link.is_displayed():
                texto = link.text.strip()
                endereco = link.get_attribute("href")

                if texto and endereco:
                    print(f"{texto} -> {endereco}")

        # Salvar evidência
        imagem = Path(__file__).resolve().parent / "evidencia_wiki.png"
        driver.save_screenshot(str(imagem))
        print("\nCaptura salva em:", imagem)
        print("\nAuditoria concluída!")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
