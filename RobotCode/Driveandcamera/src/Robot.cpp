#include "WPILib.h"
#include "NetworkTables/NetworkTable.h"
#include <DriverStation.h>

class RampedJoystick : public GenericHID
{
public:
	RampedJoystick(GenericHID* joystick) :
	 m_joystick(joystick)
	{
	}
 
	virtual ~RampedJoystick()
	{
	}
	//X is steering
	virtual float GetX(JoystickHand hand) { return rampedInput(m_joystick->GetX(hand),0); }
	virtual float GetY(JoystickHand hand) { return rampedInput(m_joystick->GetY(hand),1); }
	virtual float GetZ() { return m_joystick->GetZ(); }
	virtual float GetTwist() { return m_joystick->GetTwist(); }
	virtual float GetThrottle() { return m_joystick->GetThrottle(); }
	virtual float GetRawAxis(uint32_t axis) { return m_joystick->GetRawAxis(axis); }
 
	virtual bool GetTrigger(JoystickHand hand) { return m_joystick->GetTrigger(hand); }
	virtual bool GetTop(JoystickHand hand) { return m_joystick->GetTop(hand); }
	virtual bool GetBumper(JoystickHand hand) { return m_joystick->GetBumper(hand); }
	virtual bool GetRawButton(uint32_t button) { return m_joystick->GetRawButton(button); }
 
	virtual int GetPOV(uint32_t pov = 0) { return m_joystick->GetPOV(pov); }

 
private:
	float rampGradient() {
		return (1 - m_joystick->GetThrottle()) / 2;
	}
/*	float rampedInput(float input) {
		return (rampGradient() + input * input) * input;
	}
*/
	float rampedInput(float input, bool xaxis)
	{
		if(xaxis == true)
			return rampGradient() * input; //   was ((1 + input) / 2);
		else if (xaxis == false && rampGradient() != 0)
			return input * 0.5;
		else
			return 0;
	}
	GenericHID* m_joystick;
};
 
 
 
class Robot: public IterativeRobot
{
 
	RobotDrive myRobot; // robot drive system
	Joystick stick; // only joystick
	RampedJoystick rampedStick;


	LiveWindow *lw;
	VictorSP drumMotor;
	int autoLoopCounter;
	int drumMultiplier;
	float throttleMultiplier;


	const int SingleDrumMultipier = 5;
	const int DoubleDrumMultipier = 3;
	const int TripleDrumMultipier = 4;
	const int QuadDrumMultipier = 5;

public:
	Robot() :
		myRobot(0, 1),	// these must be initialized in the same order
		stick(0),		// as they are declared above.
		rampedStick(&stick),
		lw(NULL),
		drumMotor(2),
		autoLoopCounter(0),
		throttleMultiplier(1)
	{
		myRobot.SetExpiration(0.1);
	}
 
private:
	void RobotInit()
	{
		lw = LiveWindow::GetInstance();
		CameraServer::GetInstance()->SetQuality(50);
		//the camera name (ex "cam0") can be found through the roborio web interface
		CameraServer::GetInstance()->StartAutomaticCapture("cam0");

	}
 
	void AutonomousInit()
	{
		autoLoopCounter = 0;
	}
 
	void AutonomousPeriodic()
	{
		if(autoLoopCounter < 100)//Check if we've completed 100 loops (approximately 2 seconds)
		{
			myRobot.Drive(0.3, 0.0);
			autoLoopCounter++;
		}
		else if(autoLoopCounter < 200)
		{
			myRobot.Drive(-0.3, 0.0);
			autoLoopCounter++;
		}
		else if(autoLoopCounter < 300)
		{
			myRobot.Drive(0.3, 0.0);
			autoLoopCounter++;
		}
		else
		{
			myRobot.Drive(0.0, 0.0);
		}
	}
 
	void TeleopInit()
	{
		throttleMultiplier = 1;
		drumMultiplier = 1;
		SmartDashboard::PutString("test", "test");
	}
 
	void TeleopPeriodic()
	{
		myRobot.ArcadeDrive(rampedStick); // drive with arcade style (use right stick)

		throttleMultiplier = rampedStick.GetThrottle();
		SmartDashboard::PutNumber("Drum Multiplier", drumMultiplier);

		if (rampedStick.GetRawButton(SingleDrumMultipier) == true)
		{
			drumMultiplier = 1;
		}

		if (rampedStick.GetRawButton(DoubleDrumMultipier) == true)
		{
			drumMultiplier = 2;
		}

		if (rampedStick.GetRawButton(TripleDrumMultipier) == true)
		{
			drumMultiplier = 3;
		}

		if (rampedStick.GetRawButton(QuadDrumMultipier) == true)
		{
			drumMultiplier = 4;
		}

		if (rampedStick.GetPOV() != -1)
		{
			if (rampedStick.GetPOV() != 180)
			{
				// down: drum down
				drumMotor.Set(-0.05);
			}
			else
			{
				// up: drum up
				drumMotor.Set(0.25*drumMultiplier);
			}
		}
		else {
			// not being operated
			drumMotor.Set(0.1 * drumMultiplier - 0.1);

		}
		//nerfServo.Set((rampedStick.GetTwist()+1)/2);
		//SmartDashboard.PutData("test", "test");
	}
 
	void TestPeriodic()
	{
		lw->Run();
	}
};
 
START_ROBOT_CLASS(Robot);
