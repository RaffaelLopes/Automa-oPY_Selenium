from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
navegador.get("http://....")

navegador.find_element(By.XPATH, '//*[@id="ligar"]').click()
navegador.find_element(By.XPATH, '//*[@id="sim"]').click()

# Aguarde um curto período para garantir que a página seja carregada completamente
navegador.implicitly_wait(5)

# Executar script JavaScript para rolar para baixo
navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Aguarde um pouco para a rolagem ser concluída (você pode ajustar o tempo conforme necessário)
navegador.implicitly_wait(3)

# Exemplo: encontrar um elemento pelo XPath e clicar nele
navegador.find_element(By.XPATH, '//*[@id="root"]/main/section/section/div[2]/img').click()
navegador.find_element(By.XPATH, '//*[@id="root"]/main/header/nav/a[2]').click()
navegador.find_element(By.XPATH, '//*[@id="root"]/main/section/section/div/a/img').click()

# Aguarde um curto período para garantir que a página seja carregada completamente
navegador.implicitly_wait(2)

# Executar script JavaScript para rolar para baixo
navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Aguarde um pouco para a rolagem ser concluída (você pode ajustar o tempo conforme necessário)
navegador.implicitly_wait(3)

# Exemplo: encontrar um elemento pelo XPath e clicar nele
elemento = navegador.find_element(By.XPATH, '//*[@id="root"]/main/footer')
elemento.click()