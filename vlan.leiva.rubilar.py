# Crear un directorio vlan.apellido1.apellido2 y script de nombre vlan.apellido1.apellido2.py
# que permita crear en un switch L2, una VLAN, agregarla a un puerto de acceso y agregarla a
# un puerto troncal, luego mostrar comandos show útiles para validar la configuración

vlan_number = input ("ingrese el numero de la vlan: ")
vlan_name = input ("ingrese el nombre de la vlan: ")
vlan_port_access = input("ingrese el puerto de acceso: ")
vlan_troncal_port = input ("ingrese la interfaz para la configuracion del puerto troncal: ")
print ("\nVlan", vlan_number)
print ("Name", vlan_name)
print ("\ninterface f0/"+ vlan_port_access )
print ("   switchport mode access")
print ("   switchport access vlan", vlan_number)
print ("   Description *** PC "+ vlan_name + " *** ")
print ("   duplex full")
print ("   speed 100")
print ("   spanning tree portfast")
print ("\ninterface f0/"+ vlan_troncal_port)
print ("   switchport trunk allowed vlan add "+ vlan_port_access)
print ("\nshow interface trunk ")
print ("show vlan")
print ("show interfaces fa/"+ vlan_port_access)


