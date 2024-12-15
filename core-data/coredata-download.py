import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
#TODO:criar
parametros = {
  "sectors[0]": "662",
  "outputs[0]": "1927",
  "beneficiary_region[0]": "LAT",
  "biennium": "41",
  "quarter": "2023Q4",
 }

def baixar_csv_unesco(parametros):
  """
  Baixa o CSV de projetos UNESCO diretamente da página.

  Args:
      parametros: sector: Natural Sciences 662, 
                  benefeciary region: Latin America LAT,
                  outputs: Institutional and human capacities strengthened 
                  in STEM education in a gender transformative manner for sustainable development 
                  biennum: 41 (Unesco's 2022-2025 biennium),**
                  quarter: atualizacao trimestral ** 
                  ** theses have to change with time... 
  """
 

  # URL base para download do CSV
  url_base_csv = "https://core.unesco.org/en/projects/export/csv?sectors%5B0%5D=662&outputs%5B0%5D=1927&beneficionary_region%5B0%5D=LAT&biennium=41&quarter=2023Q4"
  #"https://core.unesco.org/en/projects/export/csv"
  # Parâmetros de filtragem 
  if parametros:
    url_csv = url_base_csv + "?" + "&".join([f"{chave}={valor}" for chave, valor in parametros.items()])
  else:
    url_csv = url_base_csv  # Sem parâmetros, usa a listagem completa
 # Simulando navegador Chrome
  headers = {'User-Agent': 'Chrome/109.0.0'}
 # Tentando download com requests
  try:
    resposta_csv = requests.get(url_csv, headers=headers)
  except Exception as e:
    print(f"Erro ao baixar o CSV com requests: {e}")
    return
  # Verificando se o download foi bem-sucedido
  if resposta_csv.status_code == 200:
    print(f"Download com requests falhou ({resposta_csv.status_code}). Tentando com urllib...")
    try:
      req = Request(url=url_csv, headers=headers)
      webpage = urlopen(req).read()
    except Exception as e:
      print(f"Erro ao baixar o CSV com urllib: {e}")
      return
    else:
      # Salvando o conteúdo como CSV
      with open("projetos_unesco3.csv", "wb") as csvfile:
        csvfile.write(webpage)
      print("Arquivo CSV baixado com sucesso (urllib)!")
      return
  # Se requests obtiver sucesso
  else:
    # Salvando o conteúdo como CSV
    with open("projetos_unesco3.csv", "wb") as csvfile:
      csvfile.write(resposta_csv.content)
    print("Arquivo CSV baixado com sucesso (requests)!")

# Executa o download sem parâmetros de filtragem (lista completa)
baixar_csv_unesco(None)
#baixar_csv_unesco(parametros)
