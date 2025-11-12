Start System
     ↓
Initialize RTC, GPIO, Relay
     ↓
Loop forever:
     Read current time from RTC
     If (time == 10:00:00 or 18:00:00):
           Turn ON pump
           Wait 10 sec
           Turn OFF pump
     Wait 1 sec
Repeat


Pseudo Code


while(1)
{
  currentTime = RTC_Read();

  if((currentTime.hour == 10 && currentTime.min == 0 && currentTime.sec == 0) ||
     (currentTime.hour == 18 && currentTime.min == 0 && currentTime.sec == 0))
  {
      pump = ON;
      delay(10000);  
      pump = OFF;
  }

  delay(1000); 
}
