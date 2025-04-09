from Trivago import constantes as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Trivago.trivago_filtro import Filtro
import time

class Trivago(webdriver.Chrome):
    
    def __init__(self, teardown = False):
        self.teardown = teardown        
        super(Trivago, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        


    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def homepage(self):
        self.get(const.HOMEPAGE)
        # driver = webdriver.Chrome()

        # Clicar no Botão de aceitar cookie
        time.sleep(3)
        aceitar = self.execute_script('return document.querySelector("#usercentrics-root").shadowRoot.querySelector("#focus-lock-id > div > div > div.sc-eBMEME.cJNbyl > div > div > div.sc-jsJBEP.iXSECa > div > button.sc-dcJsrY.NmLox")')
        self.execute_script('arguments[0].click();', aceitar)


        
    # FUNCAO PARA TROCAR A MOEDA DE TROCA
    def trocaMoeda(self, moeda):
        botao_moeda = self.find_element(By.CSS_SELECTOR, 'button[data-testid="header-localization-menu"]')
        botao_moeda.click()
        self.find_element(By.CSS_SELECTOR, 'select[data-testid="localization-currency-select"]').click()
        self.find_element(By.CSS_SELECTOR, f'option[value="{moeda}"]').click()
        troca = self.execute_script('return document.querySelector("#modal-root > dialog > div > div > form > div.ffSzZ4 > button")')
        self.execute_script('arguments[0].click();', troca)
    
    def pesquisar(self, lugar, entrada, saida):
        # SELECIONA O LUGAR DE VIAGEM
        self.find_element(By.CSS_SELECTOR, '.HxkFDQ.aaN4L7').send_keys(f" {lugar}")
        self.find_element(By.XPATH, "(//li[@role='option'])[1]").click()
        
        # SELECIONA A DATA DE ENTRADA
        self.find_element(By.CSS_SELECTOR, 'button[data-testid="search-form-calendar-checkin"]').click()
        self.find_element(By.CSS_SELECTOR, ".raKH_0.SwVR4I.Kv9RV2.p9Fs0q._3mkW6_").click()
        self.find_element(By.CSS_SELECTOR, f'button[data-testid="valid-calendar-day-{entrada}"]').click()
        
        # SELECIONA A DATA DE SAIDA
        time.sleep(0.5)
        leave = self.find_element(By.CSS_SELECTOR, f'button[data-testid="valid-calendar-day-{saida}"]')
        leave.click()
        
        

    def passageiros(self, adultos, quartos, pet):
        
        # ADICIONA A QUANTIDADE DE ADULTO CRIANCAS E QUARTOS
        # Diminui a quantidade de adultos para o minimo
        while True:
            valor_element = self.find_element(By.CLASS_NAME, 'h1ZWRl')
            valor = valor_element.get_attribute('value')
            if int(valor) == 1:
                break
            time.sleep(1)
            plus = self.find_element(
                By.CSS_SELECTOR, "button[data-testid='adults-amount-minus-button']")
            plus.click()
        # Adiciona a quantidade de adultos
        for _ in range(adultos - 1):
            self.find_element(
                By.CSS_SELECTOR, "button[data-testid='adults-amount-plus-button']"
                ).click()
            
        
        # Diminui a quantidades de criancas para zero
        while True:
            valor_criancas_element = self.find_element(By.CSS_SELECTOR, 'input[data-testid="children-amount"]')
            valor_criancas = valor_criancas_element.get_attribute('value')
            if int(valor_criancas) == 0:
                break
            self.find_element(
                By.CSS_SELECTOR, "button[data-testid='children-amount-minus-button']"
                ).click()
        
        # Diminui a quantidades de quartos para o minimo
        while True:
            valor_quartos_element = self.find_element(By.CSS_SELECTOR, "input[id=':r8:']")
            valor_quartos = valor_quartos_element.get_attribute('value')
            if int(valor_quartos) == 1:
                break

            self.find_element(
                By.CSS_SELECTOR, "button[data-testid='rooms-amount-minus-button']"
                ).click()
            
            
        # Adiciona a quantidade de quartos
        for _ in range(quartos - 1):
            self.find_element(
                By.CSS_SELECTOR, "button[data-testid='rooms-amount-plus-button']"
                ).click()
        if pet == True:
            petfriedly = self.execute_script('return document.querySelector("#__next > div._7Mr3YA > div.tbKdsQ.l3zn0Z > section._0MVqJA > div.FfmyqR.e4D1FP.jngrXy > div > div._2_UoGq._1Q__f1._8uGEt9 > div > section > div > div > div.HjaO9K > div > label")')
            self.execute_script('arguments[0].click();', petfriedly)
        self.find_element(By.CSS_SELECTOR, '._EtbiB._p1SKr._4ddg9O').click()
        time.sleep(3)

    def resultados(self):
        hoteis = self.find_elements(By.XPATH, "(//li[@data-testid='accommodation-list-element'])")
        for x in hoteis:
            Lhotel = x.find_element(
                By.CSS_SELECTOR, 'span[itemprop="name"]'
                ).get_attribute('title').strip()
            
            Ahotel = x.find_element(
                By.CSS_SELECTOR, 'meta[itemprop="ratingValue"]'
            ).get_attribute('content').strip()

            print(f"{Lhotel}: {Ahotel} Estrelas")

        
        
