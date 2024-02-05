#include "vex.h"
using namespace vex;
using signature = vision::signature;
using code = vision::code;

brain Brain;
controller controller_1 = controller(primary);

motor top_arm_joint = motor(PORT1, ratio18_1, true);
motor bottom_arm_joint = motor(PORT2, ratio18_1, true);
motor fly_wheel = motor(PORT16, ratio18_1, false);
motor left_motor_a = motor(PORT11, ratio18_1, true);
motor left_motor_b = motor(PORT12, ratio18_1, true);
motor_group leftDriveSmart = motor_group(left_motor_a, left_motor_b);
motor right_motor_a = motor(PORT19, ratio18_1, false);
motor right_motor_b = motor(PORT20, ratio18_1, false);
motor_group rightDriveSmart = motor_group(right_motor_a, right_motor_b);
drivetrain Drivetrain = drivetrain(leftDriveSmart, rightDriveSmart, 319.185798, 317.5, 254, mm, 1);
motor intake = motor(PORT3, ratio6_1, false);
digital_out left_pusher = digital_out(Brain.ThreeWirePort.G);
digital_out right_pusher = digital_out(Brain.ThreeWirePort.H);
distance acorn_sense = distance(PORT4);
digital_in Auton_select = digital_in(Brain.ThreeWirePort.F);
digital_out ratchet = digital_out(Brain.ThreeWirePort.E);
int x = 0;
int y = 0;
int pusher = 0;
int p = 0;
int c = 0;
bool acorn = false;
int selector = 0;
bool Auto = false;
bool manual = false;
bool piston = false;
bool allow_piston = false;
bool full = false;

/**
 * Used to initialize code/tasks/devices added using tools in VEXcode Pro.
 * 
 * This should be called at the start of your int main function.
 */
void vexcodeInit( void ) 
{
  top_arm_joint.setMaxTorque(100, percent);
  top_arm_joint.setVelocity(25, percent);
  bottom_arm_joint.setMaxTorque(100, percent);
  bottom_arm_joint.setMaxTorque(25, percent);
  intake.setVelocity(100, percent);
  left_pusher.set(false);
  right_pusher.set(false);
  ratchet.set(true);
  Auto = false;
  Drivetrain.setStopping(brake);
  top_arm_joint.setStopping(hold);
  bottom_arm_joint.setStopping(hold);
  select();
}