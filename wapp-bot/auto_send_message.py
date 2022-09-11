# Abre o Chrome e Acessa o WhatsApp Web;
# Escreve o nome do contato na busca;
# Aperta ENTER para acessar o chat com o contato buscado;
# Escreve a mensagem no campo de texto do chat;
# Aperta a tecla ENTER para enviar a mensagem ao contato.

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
log = []
count = 0

# Lendo os números dos contatos e salvando em uma lista
def save_contact_names(file_name):
    contact_numbers = []
    with open(file_name, 'r') as file:
        for row in file:
            number = row.split(',')[1]
            contact_numbers.append(number)
    return contact_numbers


contacts = save_contact_names('contatos.csv')

# Acessa a página do WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Tempo de espera para a leitura do QR code
time.sleep(30)

# Digitar o número do contato na busca e enviar mensagem
message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ornare eros quis risus vehicula, id dignissim libero dictum. Morbi maximus ligula sit amet ullamcorper scelerisque. Integer scelerisque sed magna a bibendum. Curabitur arcu lacus, egestas in aliquam condimentum, luctus eu turpis. Pellentesque vulputate sed ligula ac ultricies. Pellentesque vel pellentesque diam. Mauris posuere dapibus ipsum, sit amet vestibulum elit ullamcorper ut. Curabitur sit amet orci sapien. https://imgur.com/a/Khgfs3z'

def search_contact(contact):
    search_box = driver.find_element(By.XPATH, '//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    search_box.click()
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)

def send_message(message):
    input_text_box = driver.find_element(By.XPATH, '//div[contains(@class,"fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv")]')
    time.sleep(3)
    input_text_box.click()
    input_text_box.send_keys(message)
    time.sleep(3)
    input_text_box.send_keys(Keys.ENTER)

for contact in contacts:
    search_contact(contact)
    send_message(message)
    time.sleep(3)
    count = count + 1
    log.append({
        "count": count,
        "contact_sent": contact
    })
print('LOG: {0}'.format(log))