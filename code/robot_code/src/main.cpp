#include <Arduino.h>
#include <WiFi.h>
#include <WiFiClient.h>
#include <WebServer.h>
#include <LEAmDNS.h>
#include <hardware/adc.h>

#ifndef STASSID
#define STASSID "Dino IoT"
#define STAPSK "D1n0W1f1@"
#endif

int CTime = 0;

const char* ssid = STASSID;
const char* password = STAPSK;

WebServer server(80);
#define leftMotorPin_forward 2
#define leftMotorPin_backward 3
#define rightMotorPin_forward 4
#define rightMotorPin_backward 5



const String postForms = "<html>\
  <head>\
    <title>Robocup demo robot: BoB (Barely operational Bob) handling</title>\
    <style>\
      body { background-color: #cccccc; font-family: Arial, Helvetica, Sans-Serif; Color: #000088; }\
    </style>\
  </head>\
  <body>\
    <h1>Forward (sec)</h1><br>\
    <form method=\"post\" enctype=\"text/plain\" action=\"/postForward/\">\
      <input type=\"text\" name=\'{\"hello\": \"world\", \"trash\": \"\' value=\'\"}\'><br>\
      <input type=\"submit\" value=\"Submit\">\
    </form>\
    <h1>Backwards</h1><br>\
    <form method=\"post\" enctype=\"text/plain\" action=\"/postBackward/\">\
      <input type=\"text\" name=\'{\"hello\": \"world\", \"trash\": \"\' value=\'\"}\'><br>\
      <input type=\"submit\" value=\"Submit\">\
    </form>\
    <h1>Turn left</h1><br>\
    <form method=\"post\" enctype=\"text/plain\" action=\"/postTurnLeft/\">\
      <input type=\"text\" name=\'{\"hello\": \"world\", \"trash\": \"\' value=\'\"}\'><br>\
      <input type=\"submit\" value=\"Submit\">\
    </form>\
    <h1>Turn right</h1><br>\
    <form method=\"post\" enctype=\"text/plain\" action=\"/postTurnRight/\">\
      <input type=\"text\" name=\'{\"hello\": \"world\", \"trash\": \"\' value=\'\"}\'><br>\
      <input type=\"submit\" value=\"Submit\">\
    </form>\
  </body>\
</html>";

const String postForms1 = "<html>\
  <head>\
    <title>Robocup demo robot: BoB (Barely operational Bob) handling</title>\
    <style>\
      body { background-color: #cccccc; font-family: Arial, Helvetica, Sans-Serif; Color: #000088; }\
    </style>\
  </head>\
  <body>\
    <h1>Forward (sec)</h1><br>\
    <h1>";
const String postForms2 = "
    </h1><br>\
    <form method=\"post\" enctype=\"text/plain\" action=\"/postForward/\">\
      <input type=\"text\" name=\'{\"hello\": \"world\", \"trash\": \"\' value=\'\"}\'><br>\
      <input type=\"submit\" value=\"Submit\">\
    </form>\
    <h1>Backwards</h1><br>\
    <form method=\"post\" enctype=\"text/plain\" action=\"/postBackward/\">\
      <input type=\"text\" name=\'{\"hello\": \"world\", \"trash\": \"\' value=\'\"}\'><br>\
      <input type=\"submit\" value=\"Submit\">\
    </form>\
    <h1>Turn left</h1><br>\
    <form method=\"post\" enctype=\"text/plain\" action=\"/postTurnLeft/\">\
      <input type=\"text\" name=\'{\"hello\": \"world\", \"trash\": \"\' value=\'\"}\'><br>\
      <input type=\"submit\" value=\"Submit\">\
    </form>\
    <h1>Turn right</h1><br>\
    <form method=\"post\" enctype=\"text/plain\" action=\"/postTurnRight/\">\
      <input type=\"text\" name=\'{\"hello\": \"world\", \"trash\": \"\' value=\'\"}\'><br>\
      <input type=\"submit\" value=\"Submit\">\
    </form>\
  </body>\
</html>";

void test_leftMotor()
{
  
  digitalWrite(leftMotorPin_forward, HIGH);
  digitalWrite(leftMotorPin_backward, LOW);
  delay(1000);
  digitalWrite(leftMotorPin_forward, LOW);
  digitalWrite(leftMotorPin_backward, HIGH);
  delay(1000);
  digitalWrite(leftMotorPin_forward, LOW);
  digitalWrite(leftMotorPin_backward, LOW);
  delay(1000);
}

void test_rightMotor()
{
  digitalWrite(rightMotorPin_forward, HIGH);
  digitalWrite(rightMotorPin_backward, LOW);
  delay(1000);
  digitalWrite(rightMotorPin_forward, LOW);
  digitalWrite(rightMotorPin_backward, HIGH);
  delay(1000);
  digitalWrite(rightMotorPin_forward, LOW);
  digitalWrite(rightMotorPin_backward, LOW);
  delay(1000);
}

void test_bothMotors()
{
  digitalWrite(leftMotorPin_forward, HIGH);
  digitalWrite(leftMotorPin_backward, LOW);
  digitalWrite(rightMotorPin_forward, HIGH);
  digitalWrite(rightMotorPin_backward, LOW);
  delay(1000);
  digitalWrite(leftMotorPin_forward, LOW);
  digitalWrite(leftMotorPin_backward, HIGH);
  digitalWrite(rightMotorPin_forward, LOW);
  digitalWrite(rightMotorPin_backward, HIGH);
  delay(1000);
  digitalWrite(leftMotorPin_forward, LOW);
  digitalWrite(leftMotorPin_backward, LOW);
  digitalWrite(rightMotorPin_forward, LOW);
  digitalWrite(rightMotorPin_backward, LOW);
  delay(1000);
}

void handleRoot() {
  float voltage = analogRead(A2)*0.008;
  String postFormsNew = postForms1 + String(voltage) + postForms2;
  server.send(200, "text/html", postFormsNew);

}



void handleForm() {
  if (server.method() != HTTP_POST) {

    server.send(405, "text/plain", "Method Not Allowed");

  } else {

    String message = "POST form was:\n";
    for (uint8_t i = 0; i < server.args(); i++) {
      message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
    }
    server.send(200, "text/plain", message);

  }
}

void handleForward() {
  CTime = millis() +1000;
  while (CTime > millis())
  {
    digitalWrite(leftMotorPin_forward, HIGH);
    digitalWrite(leftMotorPin_backward, LOW);
    digitalWrite(rightMotorPin_forward, HIGH);
    digitalWrite(rightMotorPin_backward, LOW);
  }
    digitalWrite(leftMotorPin_forward, LOW);
    digitalWrite(leftMotorPin_backward, LOW);
    digitalWrite(rightMotorPin_forward, LOW);
    digitalWrite(rightMotorPin_backward, LOW);
    server.send(200 , "text/plain", "Forward");
}

void handleBackward() {
    CTime = millis() +1000;
    while (CTime > millis()) {
      digitalWrite(leftMotorPin_forward, LOW);
      digitalWrite(leftMotorPin_backward, HIGH);
      digitalWrite(rightMotorPin_forward, LOW);
      digitalWrite(rightMotorPin_backward, HIGH);
    }
  digitalWrite(leftMotorPin_forward, LOW);
  digitalWrite(leftMotorPin_backward, LOW);
  digitalWrite(rightMotorPin_forward, LOW);
  digitalWrite(rightMotorPin_backward, LOW);
  server.send(200 , "text/plain", "Backward");
}
void handleTurnLeft() {
  CTime = millis() +1000;
  while (CTime > millis()) {
    digitalWrite(leftMotorPin_forward, LOW);
    digitalWrite(leftMotorPin_backward, HIGH);
    digitalWrite(rightMotorPin_forward, HIGH);
    digitalWrite(rightMotorPin_backward, LOW);
  }
    digitalWrite(leftMotorPin_forward, LOW);
    digitalWrite(leftMotorPin_backward, LOW);
    digitalWrite(rightMotorPin_forward, LOW);
    digitalWrite(rightMotorPin_backward, LOW);
    server.send(200 , "text/plain", "Turn Left");
}

void handleTurnRight() {
  CTime = millis() +1000;
  while (CTime > millis()) {
    digitalWrite(leftMotorPin_forward, HIGH);
    digitalWrite(leftMotorPin_backward, LOW);
    digitalWrite(rightMotorPin_forward, LOW);
    digitalWrite(rightMotorPin_backward, HIGH);
  }
    digitalWrite(leftMotorPin_forward, LOW);
    digitalWrite(leftMotorPin_backward, LOW);
    digitalWrite(rightMotorPin_forward, LOW);
    digitalWrite(rightMotorPin_backward, LOW);
    server.send(200 , "text/plain", "Turn Right");
}


void handleNotFound() {
  
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  
}

void setup(void) {
    // put your setup code here, to run once:
  pinMode(leftMotorPin_forward, OUTPUT);
  pinMode(leftMotorPin_backward, OUTPUT);
  pinMode(rightMotorPin_forward, OUTPUT);
  pinMode(rightMotorPin_backward, OUTPUT);
  pinMode(A2, INPUT);

  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  if (MDNS.begin("picow")) {
    Serial.println("MDNS responder started");
  }
  
  server.on("/", handleRoot);

  server.on("/postform/", handleForm);

  server.on("/postForward/", handleForward);

  server.on("/postBackward/", handleBackward);

  server.on("/postTurnLeft/", handleTurnLeft);

  server.on("/postTurnRight/", handleTurnRight);

  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("HTTP server started");
}


void loop(void) {
  while (analogRead(A2)*0.008 > 7)
  {
    server.handleClient();
  }
}