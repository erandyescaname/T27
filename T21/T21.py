import requests
import json
import logging
import getpass

#key='ec1e2ebed1754f1b8c00f2b90aa15906'
key=getpass.getpass('Ingrese la API key: ')
headers={}
headers['content-type']='application/json'
headers['api-version']='3'
headers['User-Agent']='python'

#place that API key here
headers['hibp-api-key']=key

#preguntar por el correo
email=input('Ingrese el correo a investigar: ')
url='https://haveibeenpwned.com/api/v3/breachedaccount/'+email+'?truncateResponse=false'
try: 
    r=requests.get(url, headers=headers)
    if  r.status_code == 200:
        try:
            data = r.json()
        except json.JSONDecodeError:
            logging.error("No se pudo decodificar la respuesta en formato JSON")
            print("Error al procesar la respuesta. No es un JSON válido.")
        else:
            encontrados = len(data)
            with open(f'{email}_filtraciones.txt', 'w') as file:
                if encontrados > 0:
                    print(f'Los sitios en los que se ha filtrado el correo {email} son: ')
                    file.write(f'Filtraciones para el correo {email}:\n')
                    for filtracion in data:
                        print(filtracion['Name'])
                        file.write(f"- {filtracion['Name']}\n")
                else:
                    print(f'El correo {email} no ha sido filtrado')
                    file.write(f"El correo {email} no ha sido filtrado")

            msg = f"{email} - Filtraciones encontradas: {encontrados}"
            logging.info(msg)

    else:
        msg=r.text
        logging.basicConfig(filename='hibpERROR.log',
                        format="%(asctime)s %(message)s",
                        datefmt="%m/%d/%Y %H:%M:%S",
                        level=logging.ERROR)
        logging.error(msg)
except requests.exceptions.HTTPError as err:
    logging.error(f"HTTP error occurred: {err}")
    print(f"HTTP error {err}")
except requests.exceptions.RequestException as err:
    logging.error(f"Request error occurred: {err}")
    print(f"Error en la solicitud {err}")
