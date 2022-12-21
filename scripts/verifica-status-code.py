#### Talles Alencar ####
#### 20/12/2022     ####

#### Script para verificação do status code de um site  ####


import requests 

# variável para verificação
url = "https://uol.com.br"

# Retorna o status code de uma url
response = requests.get(url)

# Printando na tela o resultado.
print(f"Resultado: {response}") 
