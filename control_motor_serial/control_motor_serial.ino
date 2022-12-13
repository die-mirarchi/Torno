#define dirPin 2
#define stepPin 5
#define STEP 3
int dist = 0;

/////////////////////////////

void setup()
{
  Serial.begin(9600);

  pinMode(dirPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
}

void loop()
{

  Serial.println("-----Ingresar desplazamiento en mm-----");
  Serial.flush();
  while (Serial.available() == 0) {}
  dist = Serial.parseInt(); //tomo el valor del serial directamente como un float
  Serial.println("Desplazamiento: " + String(dist) + '\n' + "Sentido: " + String((dist > 0) ? "Derecha" : "Izquierda"));

  if (dist > 0)
  {
    digitalWrite(dirPin, HIGH);
    for (int i = 0; i < dist * 160; i++)
    {
      digitalWrite(stepPin, HIGH);
      delay(STEP);
      digitalWrite(stepPin, LOW);
      delay(STEP);
    }

  } else if (dist < 0)
  {
    digitalWrite(dirPin, LOW);
    for (int i = 0; i < -dist * 160; i++)
    {
      digitalWrite(stepPin, HIGH);
      delay(STEP);
      digitalWrite(stepPin, LOW);
      delay(STEP);
    }
  }
}
