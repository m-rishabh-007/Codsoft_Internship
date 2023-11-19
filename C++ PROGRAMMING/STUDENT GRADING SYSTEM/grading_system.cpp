/*              STUDENT GRADING SYSTEM
    Create a program that manages student grades. Allow the user
    to input student names and their corresponding grades.
    Calculate the average grade and display it along with the highest
    and lowest grades       */

#include <iostream>
#include <vector>
#include <algorithm>
#include <limits>
#include <cctype>

// Constants for grade range
const double MIN_GRADE = 0.0;
const double MAX_GRADE = 100.0;

// Structure to hold student data
struct Student
{
    std::string name;
    double grade;
};

// Function to check if the input string is a valid number
bool isNumber(const std::string &inputString)
{
    // Check for an empty string
    if (inputString.empty())
        return false;        

    bool hasDecimal = false; // Flag to check for a single decimal point

    for (int i = 0; i < inputString.size(); ++i)
    {
        char c = inputString[i];
        // Check for non-digit characters and multiple decimal points
        if (!std::isdigit(c) && (c != '.' || hasDecimal)) 
        {
            return false;
        }
        if (c == '.')
        {
            hasDecimal = true;
            // Check if there is no digit after the decimal point
            if (i == inputString.size() - 1 || !std::isdigit(inputString[i + 1]))
            {
                return false;
            }
        }
        // Check for space between digits or between a decimal point and a digit
        if (std::isspace(c) && ((i > 0 && std::isdigit(inputString[i - 1])) || (i < inputString.size() - 1 && std::isdigit(inputString[i + 1]))))
        {
            return false;
        }
    }
    return true;
}

// Function to get student data
void getStudentData(std::vector<Student>& students)
{
    while (true)
    {
        std::cout << "Enter student name (or 'done' to finish): ";
        std::string name;
        std::getline(std::cin, name);

        if (name == "done")
            break;

        // Check for an empty name
        if (name.empty()) 
        {
            std::cout << "Invalid input. Please enter a non-empty name.\n";
            continue;
        }

        while (true)
        {
            std::cout << "Enter " << name << "'s grade: ";
            std::string input;
            std::getline(std::cin, input);

            // Check if the input is a valid number
            if (isNumber(input)) 
            {
                input.erase(std::remove_if(input.begin(), input.end(), ::isspace), input.end()); // Remove spaces
                double grade = std::stod(input);

                // Check if the grade is within the valid range
                if (grade >= MIN_GRADE && grade <= MAX_GRADE) 
                {
                    students.push_back({name, grade});
                    break;
                }
            }
            std::cout << "Invalid input. Please enter a valid grade between " << MIN_GRADE << " and " << MAX_GRADE << ".\n";
        }
    }
}

// Main function
int main()
{
    std::vector<Student> students; // Vector to hold student data

    // Get student data
    getStudentData(students); 

    // Check if no student data was entered
    if (students.empty()) 
    {
        std::cout << "No student data entered.\n";
        return 0;
    }

    std::cout << "\n";

    double sum = 0.0;
    double minGrade = std::numeric_limits<double>::max();
    double maxGrade = std::numeric_limits<double>::min();

    // Calculate the sum, minimum, and maximum grades, and print the student data
    for (const auto &student : students)
    {
        sum += student.grade;
        minGrade = std::min(minGrade, student.grade);
        maxGrade = std::max(maxGrade, student.grade);

        std::cout << "Student: " << student.name << ", Grade: " << student.grade << "\n";
    }

    // Calculate the average grade
    double average = sum / students.size(); 

    // Print the average, minimum, and maximum grades
    std::cout << "\nAverage grade: " << average << "\n";
    std::cout << "Lowest grade: " << minGrade << "\n";
    std::cout << "Highest grade: " << maxGrade << "\n";

    return 0;
}
