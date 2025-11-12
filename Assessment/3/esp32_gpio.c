#define BUTTON_PIN  15   
#define LED_PIN     2    

volatile bool buttonPressed = false;


void IRAM_ATTR handleButtonInterrupt() {
  buttonPressed = true;   

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);

  
  attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), handleButtonInterrupt, FALLING);
}

void loop() {
  if (buttonPressed) {
    buttonPressed = false;  
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));  
  }

  delay(10); 
}
