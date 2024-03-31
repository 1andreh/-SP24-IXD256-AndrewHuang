#include <LiquidCrystal.h>
#include <Arduino.h>

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
  Menu();
  pinMode(buttonTop, INPUT);
  pinMode(buttonBottom, INPUT);
}

void loop() {
  if (bottomButton.isTopButtonPressed()) {
    lcd.clear();
    lcd.print("TOP");
  }

  if (bottomButton.isBottomButtonPressed()) {
    lcd.clear();
    lcd.print("BOTTOM");
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
