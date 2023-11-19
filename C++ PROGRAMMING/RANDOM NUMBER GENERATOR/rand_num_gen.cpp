/*                  NUMBER GUESSING GAME
    Create a program that generates a random number and asks the
    user to guess it. Provide feedback on whether the guess is too
    high or too low until the user guesses the correct number     */

#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
#include <algorithm>

// Function to check if the string is numeric
bool isNumericString(const std::string &str)
{
    return !str.empty() && std::all_of(str.begin(), str.end(), ::isdigit);
}

// Function to generate a random number between 1 and 100
int generateRandomNumber()
{
    srand(time(0));
    return rand() % 100 + 1;
}

// Function to get user input
std::string getUserInput()
{
    std::string guess;
    std::cout << "Guess a number between 1 and 100: ";
    getline(std::cin, guess);
    return guess;
}

// Function to check the user's guess
void checkGuess(const std::string &guess, int number, int &nguesses)
{
    try
    {
        if (isNumericString(guess))
        {
            int num = std::stoi(guess);
            if (num < 1 || num > 100)
            {
                std::cout << "Invalid input. Please enter a number between 1 and 100." << std::endl;
            }
            else if (num > number)
            {
                std::cout << "Too high! Try a lower number." << std::endl;
                nguesses++;
            }
            else if (num < number)
            {
                std::cout << "Too low! Try a higher number." << std::endl;
                nguesses++;
            }
            else
            {
                nguesses++;
                std::cout << "\nCongratulations! You guessed it in " << nguesses << " valid attempts." << std::endl;
            }
        }
        else
        {
            std::cout << "Invalid input. Please enter a valid number." << std::endl;
        }
    }
    catch (const std::invalid_argument &ia)
    {
        std::cout << "Invalid input. Please enter a valid number." << std::endl;
    }
}

// Main function
int main()
{
    int number = generateRandomNumber();
    int nguesses = 0;
    std::string guess;
    do
    {
        guess = getUserInput();
        checkGuess(guess, number, nguesses);
    } while (guess != std::to_string(number));
    return 0;
}
