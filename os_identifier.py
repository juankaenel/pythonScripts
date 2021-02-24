#!/usr/bin/python3

#Script para consultar el ttl de una dirección ip y en base a eso sacar si es windows o linux

import subprocess, re, sys

if len(sys.argv) != 2: # 2 porque el primer argumento es el nombre del programa, el segundo sería la ip a pasar, si no se cumple salta el error
    print("\n[!] Uso: python3 " + sys.argv[0] + " <dirección-ip>\n") 
    sys.exit(1) # cerrar el programa así no entra al main

def return_ttl_os_name(ttl_num):
    if ttl_num >= 0 and ttl_num <= 64:
        return "Sistema Operativo Linux"
    elif ttl_num >= 65 and ttl_num <= 128:
        return "Sistema Operativo Windows"
    else:
        return "Sistema Operativo desconocido"

def return_ttl(ip_address):
    proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()

    out = out.split() # lo paso a lista a la salida
    out = out[12].decode('utf-8') # lo paso a strings debido a que estaba en bytes
    
    ttl_value = re.findall(r"\d{1,3}", out)[0]#utilizo la libreria re de expresiones regulares, con d le digo que voy a filtrar por digitos del 1 al 3 y que sea el out en la posicion 12 que es el ttl
    #print(ttl_value)
    return ttl_value

if __name__ == '__main__':
    ip_address = sys.argv[1]

    ttl = return_ttl(ip_address)
        
    try:
         print("\n %s -> %s" % (ip_address, return_ttl_os_name(int(ttl))))
    except:
         print("error")
