import requests


def search_by_ico():
   ico = input("Zadejte IČO subjektu: ").strip()
   adresa_api = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/"
   url = adresa_api + ico
   response = requests.get(url)
   data = response.json()
   obchodni_jmeno = data["obchodniJmeno"]
   adresa = data.get("sidlo", {}).get("textovaAdresa")
   print(f"{obchodni_jmeno}, {adresa}")
search_by_ico()


def search_by_name():
   name = input("Zadejte název subjektu: ").strip()
   url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
   headers = {
       "accept": "application/json",
       "Content-Type": "application/json",
   }
   data = f'{{"obchodniJmeno": "{name}"}}'
   response = requests.post(url, headers=headers, data=data)
   result = response.json()
   print(f"Nalezeno subjektů: {result['pocetCelkem']}")
   for subjekt in result["ekonomickeSubjekty"]:
       print(f"{subjekt['obchodniJmeno']}, {subjekt['ico']}")

search_by_name()