//interruptPin
const int interruptPin1 = 21;
const int channelPin1 = 23;
int varInt1 = 0;
const int interruptPin2 = 20;
const int channelPin2 = 25;
int varInt2 = 0;

//PID Controller
int errorPID, toleranceErr, target, scale, dir;
#define maxPIDPWM 80
#define minPIDPWM 20
#define tolerance 0.02
#define euler 2.71282
int finalPWM = 0;

//PID Calculation 1
int pos1 = 0;
long prevT1 = 0;
float eprev1 = 0;
float eintegral1 = 0;
float u1, pwr1, dedt1, e1, deltaT1;
long currT1;

//PID Calculation 2
int pos2 = 0;
long prevT2 = 0;
float eprev2 = 0;
float eintegral2 = 0;
float u2, pwr2, dedt2, e2, deltaT2;
long currT2;

float kp = 5;
float kd = 1;
float ki = 0.4;

//Mobile Robotics
int plan = 0;
int D = 9;
float ppr = 250;
float keliling = D*3.14;
float hasiljarak = keliling/ppr;
float jarakAkhir;

int pwm;
float M1, M2;

#define MP1 6
#define MP2 7

#define M2A 34
#define M2B 36
#define M1A 32
#define M1B 30  

int m1;
int m2;

void setup() {
  Serial.begin(9600);
  delay(100); 
  Serial.println("Dimulai");
  pinMode(interruptPin1, INPUT_PULLUP);
  pinMode(channelPin1, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPin1), interrupt1, RISING);

  pinMode(interruptPin2, INPUT_PULLUP);
  pinMode(channelPin2, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(interruptPin2), interrupt2, RISING);

  pinMode(MP1,OUTPUT);
  pinMode(MP2,OUTPUT);
  
  pinMode(M1A,OUTPUT);
  pinMode(M1B,OUTPUT);
  pinMode(M2A,OUTPUT);
  pinMode(M2B,OUTPUT);  
}

void loop(){
  translationTPID(1000);
}
