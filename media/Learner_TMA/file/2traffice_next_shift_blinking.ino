// C++ code
//
int red1 = 13, yellow1 = 12, green1 = 11;
int red2=7, yellow2 = 6, green2 = 5, i;

void setup()
{
  pinMode(red1, OUTPUT);
  pinMode(red2, OUTPUT);
  pinMode(yellow1, OUTPUT);
  pinMode(yellow2, OUTPUT);
  pinMode(green1, OUTPUT);
  pinMode(green2, OUTPUT);
}

void loop()
{
  digitalWrite(yellow1, HIGH);
  digitalWrite(yellow2, HIGH);
  delay(2000);
  for(i=1; i<4; i++){
    digitalWrite(yellow1, HIGH);
    digitalWrite(yellow2, LOW);
    delay(500);
    digitalWrite(yellow1, LOW);
    digitalWrite(yellow2, HIGH);
    delay(500);
  }

  digitalWrite(yellow2, LOW);
  
  digitalWrite(green2, HIGH);
  digitalWrite(red1, HIGH);
  delay(5000);
  
  digitalWrite(yellow1, HIGH);
  digitalWrite(yellow2, HIGH);
  delay(3000);

  for(i=1; i<4; i++){
    digitalWrite(yellow1, HIGH);
    digitalWrite(yellow2, LOW);
    delay(500);
    digitalWrite(yellow1, LOW);
    digitalWrite(yellow2, HIGH);
    delay(500);
  }

  digitalWrite(yellow2, LOW);
  digitalWrite(green2, LOW);
  digitalWrite(red1, LOW);

  
  digitalWrite(green1, HIGH);
  digitalWrite(red2, HIGH);
  delay(5000);
  
  digitalWrite(yellow1, HIGH);
  digitalWrite(yellow2, HIGH);
  delay(3000);
  for(i=1; i<4; i++){
    digitalWrite(yellow1, HIGH);
    digitalWrite(yellow2, LOW);
    delay(500);
    digitalWrite(yellow1, LOW);
    digitalWrite(yellow2, HIGH);
    delay(500);
  }
  digitalWrite(yellow2, LOW);
  digitalWrite(green1, LOW);
  digitalWrite(red2, LOW);
}
