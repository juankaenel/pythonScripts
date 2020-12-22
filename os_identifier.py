# -*- coding: utf-8 -*-
#Script para consultar el ttl de una dirección ip y en base a eso sacar si es windows o linux
#Créditos a s4vitar

import subprocess, re, sys

def return_ttl(address):
    proc = subprocess.Popen(["ping -c 1 %s" % address, ""], stdout=subprocess.PIPE, shell= True)
    (out, err) = proc.communicate()
    out = out.split()
    out = re.findall(r"\d{1,3}", out[12]) #utilizo la libreria re de expresiones regulares, con d le digo que voy a filtrar por digitos del 1 al 3 y que sea el out en la posicion 12 que es el ttl
    return out[0] #retorno solo el nro del ttl

def return_ttl_os_name(ttl_num):
    if ttl_num >= 0 and ttl_num <= 64:
        return "Sistema Operativo Linux"
    elif ttl_num >= 65 and ttl_num <= 128:
        return "Sistema Operativo Windows"
    else:
        return "Sistema Operativo desconocido"

if len(sys.argv) != 2: # si los argumentos que pasamos son distento de 2
    print("\n[*] Usage: python " + sys.argv[0] + " <ip-address>\n")
    sys.exit(1)

if __name__ == '__main__':
    address = sys.argv[1]
    ttl = return_ttl(address)
    
    try:
        print "\n %s -> %s" % (address, return_ttl_os_name(int(ttl)))
    except:
        pass

