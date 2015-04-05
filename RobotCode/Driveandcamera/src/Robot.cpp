#include "WPILib.h"
 
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
 
	virtual float GetX(JoystickHand hand) { return -m_joystick->GetX(hand) * (-m_joystick->GetThrottle()+1)/2; }
	virtual float GetY(JoystickHand hand) { return m_joystick->GetY(hand) * (-m_joystick->GetThrottle()+1)/2; }
	virtual float GetZ() { return m_joystick->GetZ(); }
	virtual float GetTwist() { return m_joystick->GetTwist(); }
	virtual float GetThrottle() { return m_joystick->GetThrottle(); }
	virtual float GetRawAxis(uint32_t axis) { return m_joystick->GetRawAxis(axis); }
 
	virtual bool GetTrigger(JoystickHand hand) { return m_joystick->GetTrigger(hand); }
	virtual bool GetTop(JoystickHand hand) { return m_joystick->GetTop(hand); }
	virtual bool GetBumper(JoystickHand hand) { return m_joystick->GetBumper(hand); }
	virtual bool GetRawButton(uint32_t button) { return m_joystick->GetRawButton(button); }
 
	virtual int GetPOV(uint32_t pov) { return m_joystick->GetPOV(pov); }
 
private:
	GenericHID* m_joystick;
};
 
 
 
class Robot: public IterativeRobot
{
 
	RobotDrive myRobot; // robot drive system
	Joystick stick; // only joystick
	RampedJoystick rampedStick;

	LiveWindow *lw;
	Servo* nerfServo;
	int autoLoopCounter;

 
public:
	Robot() :
		myRobot(0, 1),	// these must be initialized in the same order
		stick(0),		// as they are declared above.
		rampedStick(&stick),
		lw(NULL),
		autoLoopCounter(0)
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
		nerfServo = new Servo(2);
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
 
	}
 
	void TeleopPeriodic()
	{
		myRobot.ArcadeDrive(rampedStick); // drive with arcade style (use right stick)
		nerfServo->Set((rampedStick.GetTwist()+1)/2);

	}
 
	void TestPeriodic()
	{
		lw->Run();
	}
};
 
START_ROBOT_CLASS(Robot);
