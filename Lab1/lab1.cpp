#include <iostream>
#include <stdexcept>  // Для обработки исключений

using namespace std;

class Calculator {
public:
    // Сложение
    double add(double a, double b) {
        return a + b;
    }

    // Вычитание
    double subtract(double a, double b) {
        return a - b;
    }

    // Умножение
    double multiply(double a, double b) {
        return a * b;
    }

    // Деление
    double divide(double a, double b) {
        if (b == 0) {
            throw invalid_argument("Error: Division by zero");
        }
        return a / b;
    }

    // Обработка исключений при делении на ноль
    void test_divide(double a, double b) {
        try {
            cout << "Result of division: " << divide(a, b) << endl;
        } catch (const invalid_argument& e) {
            cout << e.what() << endl;
        }
    }
};

int main() {
    Calculator calc;
    double a, b;
    char op;
    int choice;

    while (true) {
        // Меню выбора операции
        cout << "\n=== Calculator ===\n";
        cout << "1. Add (+)\n";
        cout << "2. Subtract (-)\n";
        cout << "3. Multiply (*)\n";
        cout << "4. Divide (/)\n";
        cout << "5. Exit\n";
        cout << "Select operation: ";
        cin >> choice;

        // Если пользователь выбирает выход, программа завершится
        if (choice == 5) {
            cout << "Exiting the calculator. Goodbye!" << endl;
            break;
        }

        // Ввод двух чисел для выполнения операции
        cout << "Enter first number: ";
        cin >> a;
        cout << "Enter second number: ";
        cin >> b;

        // Выполнение выбранной операции
        switch (choice) {
            case 1: // Сложение
                cout << "Result: " << calc.add(a, b) << endl;
                break;
            case 2: // Вычитание
                cout << "Result: " << calc.subtract(a, b) << endl;
                break;
            case 3: // Умножение
                cout << "Result: " << calc.multiply(a, b) << endl;
                break;
            case 4: // Деление
                calc.test_divide(a, b);
                break;
            default:
                cout << "Invalid choice! Please select a valid option.\n";
                break;
        }
    }

    return 0;
}
