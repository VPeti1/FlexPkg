#include <chrono>
#include <cstdlib>
#include <iostream>
#include <string>
#include <thread>
#include <fstream>
#include <stdio.h>
#include <unistd.h>
#include <filesystem>
#define wait1 std::this_thread::sleep_for(std::chrono::seconds(1));
#define clear system("cls");
using namespace std;
namespace fs = std::filesystem;

bool checkInternet() {
    int status = system("ping -c 1 google.com");
    return (status == 0);
}

void check() {
    if (checkInternet()) {
        std::cout << "Internet check passed!" << std::endl;
    }
    else {
        // No internet or admin privileges detected
        clear
        std::cout << "No internet or admin privileges detected! Please connect to the internet or rerun the program." << std::endl;
        system("pause");
        system("exit");
    }
}

void chococ() {
    ifstream ifile;
        ifile.open("C:\\ProgramData\\chocolatey\\bin\\choco.exe");
        if (ifile) {
            std::cout << "Choco detected \n";
            wait1
            clear
        }
 
        else {
            std::cout << "No choco detected \n";
            wait1
            clear
            system("pause");
            std::cout << "Installing chocolatey. \n";
            std::cout << "DO NOT DISCONNECT FROM THE INTERNET OR CLOSE THIS WINDOW! \n";
            system("powershell Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))");
            std::cout << "Chocolatey install completed\n";
            system("pause");
            clear
            wait1
        }
}

int main() {
    check();
    clear
    std::cout << "FlexPkg Installer for Windows" << std::endl;
    std::cout << "By VPeti" << std::endl;
    sleep(2);
    chococ();
    system("choco install git wget python -y");
    system("pause");
    system("mkdir C:\\Flex");
    system("git clone https://github.com/VPeti1/FlexPkg.git C:\\Flex");
    system("wget https://raw.githubusercontent.com/VPeti1/CWAcces/main/run.exe -O C:\\Windows\\System32\\flex.exe");
    system("del C:\\Flex\\chococ.cpp C:\\Flex\\chococ.exe C:\\Flex\\installer.cpp C:\\Flex\\installer.out C:\\Flex\\LICENSE C:\\Flex\\README.md C:\\Flex\\run.cpp C:\\Flex\\run.out");
    system("rmdir /s /q C:\\Flex\\examples");
    system("rmdir /s /q C:\\Flex\\wininstall");
    std::cout << "FlexPkg Installer Completed!" << std::endl;
    system("exit");
}