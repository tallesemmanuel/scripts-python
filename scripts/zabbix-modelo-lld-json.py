#### Talles Alencar ####
#### 20/12/2022     ####
#### Feito por: https://gist.github.com/isaqueprofeta/bbf39c4640fc1d8163eea23c07d656bf 
#### Script para modelo descoberta lld zabbix json ####

### Bibliotecas necessárias para o projeto
import json,collections

# Prepara container lld do zabbix
# Versão < 4.2: 
# lld = { 'data' : [] }
# Versão >= 4.2:
lld = []

# Lógica de acesso a fonte dos dados do LLD
# O array de dicionario funciona como teste para esse exemplo
# Sua lógica pode ser mais complexa
dados = [
  { 'indice': '1', 'descricao': 'Indice A'},
  { 'indice': '2', 'descricao': 'Indice B'},
  { 'indice': '3', 'descricao': 'Indice C'},
]

# Popula container lld do zabbix com os dados
# Faz um loop lendo os dados do array de dicionários do exemplo
for dado in dados:
  # Versão < 4.2: 
  # lld['data'].append( 
  # Versão >= 4.2: 
  lld.append( 
      collections.OrderedDict([
          ('{#MEU_INDICE}', dado['indice']),
          ('{#MEU_DESCRICAO}', dado['descricao']),
      ])
  )


json_lld = json.dumps(lld, ensure_ascii=False)

# Retorna json lld no formato do zabbix
print(json_lld)


