#include <chrono>
#include <cstdlib>
#include <iostream>
#include <string>
#include <thread>
#include <fstream>
#include <filesystem>
#include<stdio.h>
#define wait1 std::this_thread::sleep_for(std::chrono::seconds(1));
#define clear std::cout << "\033[2J\033[1;1H";
using namespace std;
 
int main() {
        ifstream ifile;
        ifile.open("C:\\ProgramData\\chocolatey\\bin\\choco.exe");
        if (ifile) {
            std::cout << "Choco detected \n";
            wait1
            clear
        }
 
        else {
            std::cout << "No choco detected \n";
            std::this_thread::sleep_for(std::chrono::seconds(1));
            std::cout << "\033[2J\033[1;1H";
            system("pause");
            std::cout << "Installing chocolatey. \n";
            std::cout << "DO NOT DISCONNECT FROM THE INTERNET OR CLOSE THIS WINDOW! \n";
            //install choco with BPS
            system("powershell Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))");
            //creates the file
            std::cout << "Dependency install complete\n";
            system("pause");
            clear
            main();
        }
    }
