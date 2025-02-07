from scapy.all import ARP, IP, sr1, conf

# Definir la dirección IP de la red
target_ip = "192.168.1.0/24"

# Configurar Scapy para utilizar la opción L3socket
conf.L3socket = True

# Crear un paquete ARP
arp = ARP(pdst=target_ip)

# Enviar el paquete y obtener la respuesta
packet = IP(dst=target_ip)/arp
result = sr1(packet, timeout=3, verbose=0)

# Imprimir la dirección IP y MAC del dispositivo que responde
if result:
    print(f"IP: {result.psrc} - MAC: {result.hwsrc}")