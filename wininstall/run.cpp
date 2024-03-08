#include <iostream>
#include <cstdlib>
#include <filesystem>
#include <vector> // Include the vector header
#include <thread> // For std::this_thread::sleep_for

namespace fs = std::filesystem;

int main() {
    fs::path sourceDir = "C:\\Flex"; 
    fs::path currentDir = fs::current_path();

    std::vector<fs::path> copiedFiles; // Store copied file paths

    for (const auto& entry : fs::directory_iterator(sourceDir)) {
        try {
            fs::path destPath = currentDir / entry.path().filename();
            fs::copy_file(entry.path(), destPath, fs::copy_options::overwrite_existing);
            copiedFiles.push_back(destPath); // Store the copied file path
        } catch (const std::exception& e) {
            std::cout << "Error copying file: " << e.what() << std::endl;
        }
    }

    system("python C:\\Flex\\main.py");

    // Delete the copied files
    for (const auto& file : copiedFiles) {
        try {
            fs::remove(file);
        } catch (const std::exception& e) {
        }
    }

}
