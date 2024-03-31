#include <LiquidCrystal.h>
#include <Arduino.h>
#include <string> 

// LCD Pins
const int rs = 2;
const int e = 3;
const int d4 = 4;
const int d5 = 5;
const int d6 = 6;
const int d7 = 7;

// Button Pins
const int buttonTop = 8;
const int buttonBottom = 9;
String currentState = "MENU";
bool stateChanged = true; // Variable to track state changes

LiquidCrystal lcd(rs, e, d4, d5, d6, d7);

// Forward declaration of Button class
class Button {
public:
    bool isBottomButtonPressed();
    bool isTopButtonPressed();
};

// Declaration of bottomButton and topButton objects
Button bottomButton;
Button topButton;

void setup() {
  pinMode(buttonTop, INPUT);
  pinMode(buttonBottom, INPUT);
  Menu(); // Call Menu function
}

void loop() {
  if (currentState == "MENU") {
    Menu();
    if (stateChanged) {
      if (bottomButton.isTopButtonPressed()) {
        lcd.clear();
        currentState = "START";
        stateChanged = true; // State changed, set flag
      }
      if (bottomButton.isBottomButtonPressed()) {
        lcd.clear();
        currentState = "TIMER";
        stateChanged = true; // State changed, set flag
      }
    }
  }

  if (currentState == "START") {
    if (stateChanged) {
      lcd.clear();
      lcd.print("stop 1:17:24");
      lcd.setCursor(0, 1);
      lcd.print("> BACK");
      stateChanged = false;
    }
    if (bottomButton.isBottomButtonPressed()) {
        lcd.clear();
        currentState = "MENU";
        stateChanged = true;
        // stateChanged = false; // Reset state change flag
      }
  }

  if (currentState == "TIMER") {
    if (stateChanged) {
      lcd.clear();
      lcd.print("+30 1:00:00");
      lcd.setCursor(0, 1);
      lcd.print("> Start");
      stateChanged = false; // Reset state change flag
    }
  }
}

void Menu() {
  lcd.begin(16,2);
  lcd.print("> Start Session");
  lcd.setCursor(0, 1);
  lcd.print("> Study Timer");
}

// Definition of Button class methods
bool Button::isBottomButtonPressed() {
  return digitalRead(buttonBottom) == HIGH;
}

bool Button::isTopButtonPressed() {
  return digitalRead(buttonTop) == HIGH;
}
