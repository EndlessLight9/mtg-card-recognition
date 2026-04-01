import os
import requests
import time

from pathlib import Path

def baixar_carta_especifica(nome_da_carta, pasta_destino):
    print(f"Buscando '{nome_da_carta}' no Scryfall...")
    
    url = f"https://api.scryfall.com/cards/named?exact={nome_da_carta}"
    
    headers = {
        "User-Agent": "ProjetoVisaoComputacionalFaculdade/1.0",
        "Accept": "application/json"
    }
    
    resposta = requests.get(url, headers=headers)
    
    #(Código 200 = Sucesso)
    if resposta.status_code == 200:
        dados_carta = resposta.json()
        
        if 'image_uris' in dados_carta and 'normal' in dados_carta['image_uris']:
            url_imagem = dados_carta['image_uris']['normal']
            
            nome_limpo = nome_da_carta.replace("/", "_").replace(":", "").replace('"', '')
            caminho_arquivo = os.path.join(pasta_destino, f"{nome_limpo}.jpg")
            
            imagem_bytes = requests.get(url_imagem, headers=headers).content
            with open(caminho_arquivo, 'wb') as arquivo:
                arquivo.write(imagem_bytes)
                
            print(f"✅ Success, image saved at path: {caminho_arquivo}")
        else:
            print("Card found but without the standard 'image_uris' property (might be a double-faced card).")
            
    elif resposta.status_code == 404:
        print("Error 404: Card not found. Check card name.")
    else:
        print(f"Error in API: Código {resposta.status_code}")

if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent.parent
    pasta_banco = project_root / "scryfall_data"
    pasta_banco.mkdir(parents=True, exist_ok=True)
    
    #nome da carta EM INGLES
    lista_de_cartas = ["The Ur-Dragon",
                       "Black Lotus"
                       ]
    
    for carta in lista_de_cartas:
        baixar_carta_especifica(carta, pasta_banco)
        time.sleep(0.1)
    
    print("All done!")

