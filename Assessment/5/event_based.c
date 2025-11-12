Start System
    ↓
Initialize Timer, Sensors, Communication
    ↓
Loop Forever:
    If (60s timer expired) → Send data
    If (Sensor event interrupt) → Read sensor
    Run State Machine:
         ├── IDLE
         ├── READ_SENSOR
         ├── SEND_DATA
         └── ERROR_HANDLING


while(1)
{
    if(timer_60s_flag) {
        timer_60s_flag = 0;
        send_data_to_server();
    }

    if(sensor_event_flag) {
        sensor_event_flag = 0;
        sensor_value = read_sensor();
    }

    run_state_machine();  
}
