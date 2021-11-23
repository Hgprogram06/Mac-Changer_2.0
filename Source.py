import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()

    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help="Intrface para cambiar dirección MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-]Por favor introduzca la intrfáz, usa --help para obtener más ayuda")
    elif not options.New_mac:
        parser.error("[-]Por favor introduzca la dirección MAC, usa --help para obtener más ayuda")
        return options

def change_mac(interface, New_mac):
    print(" [+] Cambiando su mac. " + interface + " cambiado a " + New_mac,)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", New_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()

change_mac(options.interface,  options.New_mac)
