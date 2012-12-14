/**
 *     ____  _       ___                      _______       __
 *    / __ )(_)___  /   |  _________ ___     / ____/ |     / /
 *   / __  / / __ \/ /| | / ___/ __ `__ \   / /_   | | /| / /
 *  / /_/ / / /_/ / ___ |/ /  / / / / / /  / __/   | |/ |/ /
 * /_____/_/\____/_/  |_/_/  /_/ /_/ /_/  /_/      |__/|__/
 *
 * This is the entry point for the biorobotic-arm's firmware.
 * You can find the repository at: https://github.com/tfeldmann/Biorobotic-Arm
 */

void setup()
{
    Serial.begin(115200);  // 8N1
    scmd_init();

    base_init();
    elbow_init();
    shoulder_init();
    hand_init();
    collision_init();

    start_control_tick(100);  // 100Hz

    tone_ready();
    Serial.println("# READY");
}

void reset()
{
    Serial.println("# RESET");
    base_set_desired_pos(512);
    elbow_set_angle(-45);
    shoulder_set_angle(45);
    wrist_set_angle(0);
    grip_open();
}

void stop()
{
    Serial.println("# STOP");
    base_set_desired_pos(base_position());
    shoulder_set_angle(shoulder_angle());
    elbow_set_angle(elbow_angle());
}

void loop()
{
    scmd_update();  // listen for commands

    /*
        send current positions to PC
        The values are separated as defined in 'separator'
        0. Base
        1. Shoulder
        2. Elbow
        3. Wrist
        4. Grip
     */
    static uint32_t timestamp = millis();
    if (millis() - timestamp > 50)  // circa every 50ms
    {
        const String separator = String(';');
        String status =
            String('P') +
            base_position() + separator + // @todo: base_angle
            shoulder_angle() + separator +
            elbow_angle() + separator +
            wrist_angle() + separator +
            grip_is_open();
        Serial.println(status);
        timestamp = millis();
    }

    // static uint32_t timestamp = millis();
    // if (millis() - timestamp > 50)
    // {
    //     Serial.print(analogRead(A0));
    //     Serial.print(",");
    //     Serial.print(analogRead(A1));
    //     Serial.print(",");
    //     Serial.println(analogRead(A2));
    //     timestamp = millis();
    // }

    static uint32_t collision_timestamp = millis();
    if (millis() - collision_timestamp > 100)
    {
        collision_update();
        collision_timestamp = millis();
    }
}

void start_control_tick(uint8_t freq)
{
    cli();
    TCCR1A = 0;  // set entire TCCRA register to 0
    TCCR1B = 0;  // same for TCCRB
    TCNT1  = 0;  // initialize counter value to 0
    OCR1A  = 15625 / freq;
    TCCR1B |= (1 << WGM12);  // turn on CTC mode
    TIMSK1 |= (1 << OCIE1A);  // enable timer compare interrupt
    TCCR1B |= (1 << CS12) | (1 << CS10); // 1024 prescaler
    sei();
}

ISR(TIMER1_COMPA_vect)
{
    base_control();
    shoulder_control();
    elbow_control();
    hand_control();
}
