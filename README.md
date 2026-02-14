# DHCP Rogue / Spoofing Attack - Scapy

## Autor
Nombre: Stephan Cedano 
Matrícula: 2024-1404

---

## Video demostrativo

[Ver video demostrativo] (https://youtu.be/XlFxx-4FgPU)


---

## Objetivo

Crear un programa en Python empleando la librería Scapy que permita emular, dentro de un entorno de laboratorio, un servidor DHCP no legítimo. Este servidor responderá a las solicitudes DHCP Discover de los clientes entregando parámetros de red manipulados o maliciosos.

---

## Topología
- 1 Router
- 1 Switch
- 1 Host Atacante (ubuntu server)
- 1 Host Víctima (Window 10)
  
---
  

---

### Direccionamiento IP
Red: 202.4.14.1/24
Atacante: 202.4.14.2
IP Ofrecida: 202.4.14.100

---

## Parámetros utilizados
- Interfaz: ens3
- Python
- Scapy

---

## Ejecución
```bash
sudo python dhcp_rogue_spoofing.py
```

---

## Medidas de mitigación
- DHCP Snooping
- Port Security
- Segmentación VLAN
- 802.1X
