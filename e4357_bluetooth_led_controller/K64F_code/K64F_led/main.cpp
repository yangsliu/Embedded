#include "mbed.h"

// create LED Objects
DigitalOut ledRed(LED_RED);
DigitalOut ledGreen(LED_GREEN);
DigitalOut ledBlue(LED_BLUE);

// initialize uart connection for HC-06 BT extension board
Serial myBT(PTC15, PTC14);
// initialize uart to pc connection for debug purpose
Serial pc(USBTX, USBRX);

Ticker tickRed;
Ticker tickGreen;
Ticker tickBlue;

uint8_t cmd[20];
int32_t cmdIdx;

int32_t process_cmd(uint8_t *cmd);
void flip_redLed(void);
void flip_greenLed(void);
void flip_blueLed(void);


int main() {
	uint8_t rcvdCmd;
	
	// turn off all the LEDs during initialization
	ledRed = 1;
	ledGreen = 1;
	ledBlue = 1;
	
	cmdIdx = 0;
	
	while (1) {
		if (myBT.readable()) {
			rcvdCmd = myBT.getc();
			pc.putc(rcvdCmd);
			
			if (rcvdCmd == 0x0D || rcvdCmd == 0x0A) {	// CR or LF
				cmd[cmdIdx] = 0;
				cmdIdx = 0;
				process_cmd(cmd);
			} else {
				cmd[cmdIdx] = rcvdCmd;
				cmdIdx++;
			}
			
		}
	}
	
}


int32_t process_cmd(uint8_t *cmd) {
	uint8_t color = cmd[0];
	uint8_t status = cmd[1] - '0';
	int32_t timeInterval = 0;
	
	for (int i = 2; cmd[i] != 0; i++) {
		timeInterval = timeInterval * 10 + (cmd[i] - '0');
	}
	
	pc.printf("Color: %1c Status: %1d TimeInterval: %d\n", color, status, timeInterval);

	switch(color) {
		case 'R' :
			tickRed.detach();
			if (status == 1) {
				ledRed = 1;
			} else {
				ledRed = 0;
				if (timeInterval != 0) {
					tickRed.attach(&flip_redLed, timeInterval);
				}
			}
			break;
		case 'G' :
			tickGreen.detach();
			if (status == 1) {
				ledGreen = 1;
			} else {
				ledGreen = 0;
				if (timeInterval != 0) {
					tickGreen.attach(&flip_greenLed, timeInterval);
				}
			}			
			break;
		case 'B' :
			tickBlue.detach();
			if (status == 1) {
				ledBlue = 1;
			} else {
				ledBlue = 0;
				if (timeInterval != 0) {
					tickBlue.attach(&flip_blueLed, timeInterval);
				}
			}
			break;
		default:
			return -1;
	}
	
	return 1;

}


void flip_redLed(void) {
	ledRed = 1 - ledRed;
}


void flip_greenLed(void) {
	ledGreen = 1- ledGreen;
}


void flip_blueLed(void) {
	ledBlue = 1 - ledBlue;
}

