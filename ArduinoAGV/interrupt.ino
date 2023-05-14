
void interrupt1(){
 (digitalRead(interruptPin1) == digitalRead(channelPin1))?varInt1++:varInt1--;
}

void interrupt2(){
  (digitalRead(interruptPin2) == digitalRead(channelPin2))?varInt2--:varInt2++;
}


void cekpulsamotor(){
  Serial.print("Pulsa 1= "); Serial.print(varInt1);
  Serial.print(" Pulsa 2= "); Serial.print(varInt2);

  delay(100);
}
void cekotomatis(int u, int varInt){
  Serial.print("  U: "); Serial.print(u);
  Serial.print(" Pulsa= "); Serial.print(varInt);
  delay(100);
  }
