#include <chrono>
#include <cstdlib>
#include <iostream>
#include <string>
#include <thread>
#include <fstream>
#include <stdio.h>
#include <unistd.h>
#define clear std::cout << "\033[2J\033[1;1H";
using namespace std;

int main() {
    clear;
    std::cout << "FlexPkg Installer" << std::endl;
    std::cout << "By VPeti" << std::endl;
    sleep(2);
    std::cout << "Make sure you have WGET and git installed!" << std::endl;
    system("read -p 'Press Enter to continue...'");
    system("sudo mkdir /usr/flex");
    system("sudo git clone https://github.com/VPeti1/FlexPkg.git /usr/flex");
    system("sudo wget https://raw.githubusercontent.com/VPeti1/CWAcces/main/run.out -O /usr/flex/flex.out");
    system("sudo cp -r /usr/flex/flex.out /bin/flex");
    system("sudo chmod +x /bin/flex");
    std::cout << "FlexPkg Installer Completed!" << std::endl;
    system("read -p 'Press Enter to continue...'");
    system("exit");
}