/*                  WORD COUNT
    Develop a program that counts the number of words in a given
    text file. Prompt the user to enter the file name and display the
    total word count       */

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

// Function to count the number of words in a given file
int countWordsInFile(const std::string &fileName)
{
    // Open the file
    std::ifstream file(fileName);
    
    // Check if the file was successfully opened
    if (!file)
    {
        // If the file could not be opened, print an error message and return -1
        std::cerr << "Error: Unable to open the file." << std::endl;
        return -1;
    }

    int wordCount = 0; // Variable to hold the word count
    std::string line; // Variable to hold each line of the file
    
    // Read the file line by line
    while (std::getline(file, line))
    {
        // Use a stringstream to split the line into words
        std::stringstream ss(line);
        
        std::string word; // Variable to hold each word
        
        // Read each word from the stringstream
        while (ss >> word)
        {
            wordCount++; // Increment the word count for each word
        }
    }

    // Check for read errors
    if (file.bad())
    {
        // If there was an error reading the file, print an error message and return -1
        std::cerr << "Error reading the file." << std::endl;
        return -1;
    }

    // Return the word count
    return wordCount;
}

// Main function
int main()
{
    // Ask the user for the name/address of the text file
    std::cout << "Enter the name/address of the text file: ";
    std::string fileName;
    std::cin >> fileName;

    // Call the countWordsInFile function and store the result in the wordCount variable
    int wordCount = countWordsInFile(fileName);
    
    // If the word count is not negative (which would indicate an error), print the word count
    if (wordCount >= 0)
    {
        std::cout << "Total word count in " << fileName << " is: " << wordCount << std::endl;
    }

    return 0;
}
