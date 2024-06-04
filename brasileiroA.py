from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Inicializa o driver do Selenium (neste caso, para o Chrome)
driver = webdriver.Chrome()
# Inicializa o driver do Selenium (neste caso, para o Chrome)


# Define a URL da página inicial
url = 'https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2024'

# Abre a página inicial
driver.get(url)

# Função para capturar dados de uma página
def capturar_dados():
    # Encontra os elefind_elementsmentos que contêm os dados desejados
    produtos = driver.find_elements(By.CLASS_NAME, 'expand-trigger')
    sports_headers = driver.find_element()('text-center')

    for produto in produtos:
        nome = produto.find_element(By.CLASS_NAME, 'hidden-xs').text
        ponto = produto.find_element(By.XPATH, 'th[1]').text
        Jogo = produto.find_element(By.XPATH, 'td[2]').text
        Vitoria = produto.find_element(By.XPATH, 'td[3]').text
        Estatistica =produto.find_element(By.XPATH, 'td[5]').text

    #   nome = nome.split(' - ',0)
        print("Time: "+nome+" Ponto: "+ponto+" Jogos: "+Jogo+" Vitoria: "+Vitoria+" Porcentagem: "+Estatistica+"%")
# Captura dados da primeira página
capturar_dados()

# Navega para a próxima página, se houver
pagina_atual = 1
while True:
    try:
        # Encontra o botão "Próxima página" e clica nele
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'imso-hide-overflow tb_l GSkImd tb_st'))
        )
        next_button.click()

        # Captura dados da próxima página
        pagina_atual += 1
        print(f"Capturando dados da página {pagina_atual}")
        capturar_dados()
    except Exception as e:
        print("Não tem mais Time")
        break

# Fecha o navegador
driver.quit()
