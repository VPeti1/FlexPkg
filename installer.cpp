#include <chrono>
#include <cstdlib>
#include <iostream>
#include <string>
#include <thread>
#include <fstream>
#include <stdio.h>
#include <unistd.h>
#include <filesystem>
#define clear std::cout << "\033[2J\033[1;1H";
using namespace std;
namespace fs = std::filesystem;


void dw() {
    std::string distro;
    std::cout << "Enter your Linux distribution (arch/debian/fedora): ";
    std::cin >> distro;
    if (distro == "arch") {
        system("sudo pacman -S git wget");
    } else if (distro == "debian") {
        system("sudo apt-get install git wget");
    } else if (distro == "fedora") {
        system("sudo dnf install git wget");
    }
    else if (distro == "skip") {

    }
     else {
        std::cout << "Unsupported distribution. Please choose arch, debian, or fedora." << std::endl;
    }
}

int main() {
    clear;
    std::cout << "FlexPkg Installer" << std::endl;
    std::cout << "By VPeti" << std::endl;
    sleep(2);
    dw();
    system("read -p 'Press Enter to continue...'");
    system("sudo rm -rf /usr/flex/");
    system("sudo rm -rf /bin/flex");
    system("sudo mkdir /usr/flex");
    system("sudo git clone https://github.com/VPeti1/FlexPkg.git /usr/flex");
    system("sudo wget https://raw.githubusercontent.com/VPeti1/CWAcces/main/run.out -O /bin/flex");
    system("sudo chmod +x /bin/flex");
    system("sudo rm -r /usr/flex/chococ.cpp /usr/flex/chococ.exe /usr/flex/installer.cpp /usr/flex/installer.out /usr/flex/LICENSE /usr/flex/README.md /usr/flex/run.cpp /usr/flex/run.out /usr/flex/examples");
    std::cout << "FlexPkg Installer Completed!" << std::endl;
    system("exit");
}