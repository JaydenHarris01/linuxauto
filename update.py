import os


while True:
    def options():
        print("\n")
        print(" Update = 1\n")
        print(" Upgrade = 2\n")
        print(" Distro upgrade = 3\n")
        
        print(" Update and Upgrade = 12\n")
        print(" Update and Distro Upgrade = 13\n")
        print(" Upgrade and Distro Upgrade = 23\n")
        print(" All = 0\n")
        

    options()

    option = str(input(" Enter a value > "))

    if option == '1':
        os.system("sudo apt-get update")

    if option == '2':
        os.system("sudo apt-get upgrade -y")

    if option == '3':
        os.system("sudo apt-get dist-upgrade -y")

    if option == '12':
        os.system("sudo apt-get update && sudo apt-get upgrade -y")

    if option == '13':
        os.system("sudo apt-get update && sudo apt-get dist-upgrade -y")
    
    if option == '23':
        os.system("sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y")

    if option == '0':
        os.system("sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y")

   
    