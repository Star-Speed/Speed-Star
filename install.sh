#!/bin/bash

read -p "Are you sure you want to install Magic Star Robot? (Y/n): " q

if [ "$q" == "y" ] || [ "$q" == "Y" ] || [ "$q" == "" ]; then
    echo -e "\e[1;36mInstalling package\e[0m"
    #sudo apt install python-setuptools
    #sudo apt install python-pip
    #sudo apt install python-redis
    #sudo pip install pyTelegramBotAPI

    echo -e "\e[1;36mدPyTelegramBotAPI update\e[0m"
    #sudo pip install pyTelegramBotAPI --upgrade
    #sudo apt update
 
    echo -e "\e[1;36mInstalling Python 2.7 and Modules\e[0m"
    #sudo apt install python2.7
    #sudo pip install pytelegrambotapi py==1.4.29 pytest==2.7.2 requests==2.7.0 six==1.9.0 wheel==0.24.0
    chmod +x launch.sh
    echo -e "\e[1;32mInstallation was successful! You can now run Magic Star.\e[0m"
    echo " "
fi
