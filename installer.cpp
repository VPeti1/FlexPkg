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
    clear
    std::string distro;
    std::cout << "Enter your Linux distribution (arch/debian/fedora/void/opensuse):\n";
    std::cout << "(Derivatives included)\n";
    std::cin >> distro;
    if (distro == "arch") {
        system("sudo pacman -S git wget python");
        system("sudo touch /usr/flex/arch.cw");
    } else if (distro == "debian") {
        system("sudo apt-get install git wget python");
        system("sudo touch /usr/flex/deb.cw");
    } else if (distro == "fedora") {
        system("sudo dnf install git wget python");
        system("sudo touch /usr/flex/fed.cw");
    }
    else if (distro == "void") {
        system("sudo xbps-install git wget python");
        system("sudo touch /usr/flex/void.cw");
    }
    else if (distro == "opensuse") {
        system("sudo zypper install git wget python");
        system("sudo touch /usr/flex/suse.cw");
    }
    else if (distro == "skip") {

    }
     else {
        std::cout << "Unsupported distribution. Please choose arch, debian, void, opensuse or fedora.\n";
        clear
        dw();
    }
}

int main() {
    clear;
    std::cout << "FlexPkg Installer" << std::endl;
    std::cout << "By VPeti" << std::endl;
    sleep(2);
    dw();
    clear
    system("read -p 'Press Enter to continue...'");
    system("sudo rm -rf /usr/flex/");
    system("sudo rm -rf /bin/flex");
    system("sudo mkdir /usr/flex");
    system("sudo git clone https://github.com/VPeti1/FlexPkg.git /usr/flex");
    system("sudo wget https://raw.githubusercontent.com/VPeti1/CWAcces/main/run.out -O /bin/flex");
    system("sudo chmod +x /bin/flex");
    system("sudo rm -r /usr/flex/chococ.cpp /usr/flex/chococ.exe /usr/flex/installer.cpp /usr/flex/installer.out /usr/flex/LICENSE /usr/flex/README.md /usr/flex/run.cpp /usr/flex/run.out /usr/flex/examples /usr/flex/wininstall");
    std::cout << "FlexPkg Installer Completed!" << std::endl;
    system("exit");
}
