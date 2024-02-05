/*----------------------------------------------------------------------------*/
/*                                                                            */
/*    Module:       VEXTestCode                                               */
/*    Author:       Logan Dresel                                              */
/*    Created:      Jan 26 2024                                               */
/*    Description:  Test code                                                 */
/*                                                                            */
/*----------------------------------------------------------------------------*/

#include "vex.h"

using namespace vex;

// A global instance of competition
competition Competition;

void when_started1(void) 
{
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();
  // All activities that occur before the competition starts
  // Example: clearing encoders, setting servo positions, ...
  thread Acorn = thread(acorn_distance);
}
//
// Main will set up the competition functions and callbacks.
//
int main() 
{
  // Set up callbacks for autonomous and driver control periods.
  Competition.autonomous(auton);
  Competition.drivercontrol(drive);
  Auton_select.high(button_press);
  //system event handlers
  // Trigger buttons
  controller_1.ButtonR1.pressed(acorn_grab);
  controller_1.ButtonR1.released(R1_release);
  controller_1.ButtonR2.pressed(acorn_release);
  controller_1.ButtonR2.released(R2_release);
  //Direction buttons
  controller_1.ButtonUp.pressed(arm_direction);
  controller_1.ButtonLeft.pressed(arm_mode);
  //Letter buttons
  controller_1.ButtonA.pressed(A_press);
  controller_1.ButtonA.released(A_release);
  controller_1.ButtonB.pressed(push);
  controller_1.ButtonB.released(B_release);
// add 15ms delay to make sure events are registered correctly.
wait(15, msec);
  // Run the pre-autonomous function.
  when_started1();
  // Prevent main from exiting with an infinite loop.
  while (true) 
  {
    leftDriveSmart.setVelocity(controller_1.Axis3.position() + controller_1.Axis1.position(), percent);
    rightDriveSmart.setVelocity(controller_1.Axis3.position() - controller_1.Axis1.position(), percent);
    leftDriveSmart.spin(forward);
    rightDriveSmart.spin(forward);
    wait(20, msec);
  }
}
