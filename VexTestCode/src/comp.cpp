#include "vex.h"
using namespace vex;

void drive(void)
{
    thread arm = thread(arm_fold);
    top_arm_joint.setStopping(hold);
    bottom_arm_joint.setStopping(hold);
    Drivetrain.setDriveVelocity(100, percent);
    timer Timer = timer();
    while (Timer.time(seconds) != 75)
    {}
    controller_1.Screen.clearScreen();
    controller_1.Screen.setCursor(1, 1);
    controller_1.rumble("..--");
    controller_1.Screen.print("30 seconds left");
    allow_piston = true;
}

void auton(void)
{
    manual = false;
    Drivetrain.setDriveVelocity(75, percent);
    Drivetrain.setTurnVelocity(35, percent);
    Drivetrain.setStopping(brake);
    top_arm_joint.setMaxTorque(100, percent);
    top_arm_joint.setVelocity(25, percent);
    bottom_arm_joint.setMaxTorque(100, percent);
    bottom_arm_joint.setVelocity(25, percent);
    top_arm_joint.setStopping(hold);
    bottom_arm_joint.setStopping(hold);
    bottom_arm_joint.spinFor(reverse, .5, seconds); //Lift intake to drop arm
    top_arm_joint.setStopping(coast);
    bottom_arm_joint.setStopping(coast);
    if (selector == 0) // Near side with hanging pole touch
    {
        wait(100, msec);
        acorn_grab();
        left_pusher.set(true);
        Drivetrain.driveFor(forward, 18.5, inches);
        wait(250, msec);
        left_pusher.set(false);
        Drivetrain.turnFor(right, 30, degrees);
        Drivetrain.driveFor(forward, 9, inches);
        acorn_release();
        wait(200, msec);
        Drivetrain.driveFor(reverse, 3, inches);
        Drivetrain.setDriveVelocity(100, percent);
        Drivetrain.driveFor(forward, 6, inches);
        acorn_release();
        wait(200, msec);
        Drivetrain.setDriveVelocity(75, percent);
        Drivetrain.driveFor(forward, 1, inches);
        Drivetrain.driveFor(reverse, 4, inches);
        Drivetrain.turnFor(right, 50, degrees);
        Drivetrain.driveFor(forward, 40, inches);
        bottom_arm_joint.setStopping(hold);
        top_arm_joint.setStopping(hold);
        bottom_arm_joint.spinFor(forward, 380, degrees);
        top_arm_joint.spinFor(forward, 560, degrees);
        Drivetrain.turnFor(right, 200, degrees);
        Drivetrain.driveFor(reverse, 3, inches);
    }
    else if (selector == 1) // Far side with hanging pole touch
    {
        wait(100, msec);
        acorn_grab();
        Drivetrain.driveFor(forward, 18.5, inches);
        wait(250, msec);
        Drivetrain.turnFor(left, 30, degrees);
        Drivetrain.driveFor(forward, 9, inches);
        acorn_release();
        wait (200, msec);
        Drivetrain.driveFor(reverse, 3, inches);
        Drivetrain.setDriveVelocity(100, percent);
        Drivetrain.driveFor(forward, 6, inches);
        acorn_release();
        wait(200, msec);
        Drivetrain.setDriveVelocity(75, percent);
        Drivetrain.driveFor(forward, 1, inches);
        Drivetrain.driveFor(reverse, 4, inches);
        Drivetrain.turnFor(left, 60, degrees);
        Drivetrain.driveFor(forward, 40, inches);
        Drivetrain.turnFor(left, 27, degrees);
        Drivetrain.driveFor(forward, 3, inches);
    }
    else if (selector == 2) // Near side without hang
    {
        wait(100, msec);
        acorn_grab();
        left_pusher.set(true);
        Drivetrain.driveFor(forward, 18.5, inches);
        wait(250, msec);
        left_pusher.set(false);
        Drivetrain.turnFor(right, 30, degrees);
        Drivetrain.driveFor(forward, 9, inches);
        acorn_release();
        wait(200, msec);
        Drivetrain.driveFor(reverse, 3, inches);
        Drivetrain.setDriveVelocity(100, percent);
        Drivetrain.driveFor(forward, 6, inches);
        acorn_release();
        wait(200, msec);
        Drivetrain.setDriveVelocity(75, percent);
        Drivetrain.driveFor(forward, 1, inches);
        Drivetrain.driveFor(reverse, 4, inches);
        Drivetrain.turnFor(right, 60, degrees);
    }
    else if (selector == 3) // Far side without hang
    {
        wait(100, msec);
        acorn_grab();
        Drivetrain.driveFor(forward, 18.5, inches);
        wait(250, msec);
        Drivetrain.turnFor(left, 30, degrees);
        Drivetrain.driveFor(forward, 9, inches);
        acorn_release();
        wait (200, msec);
        Drivetrain.driveFor(reverse, 3, inches);
        Drivetrain.setDriveVelocity(100, percent);
        Drivetrain.driveFor(forward, 6, inches);
        acorn_release();
        wait(200, msec);
        Drivetrain.setDriveVelocity(75, percent);
        Drivetrain.driveFor(forward, 1, inches);
        Drivetrain.driveFor(reverse, 4, inches);
        Drivetrain.turnFor(left, 60, degrees);
    }
    else // Programming skills
    {
        Drivetrain.setStopping(brake);
        Drivetrain.setTurnVelocity(35, percent);
        Drivetrain.setDriveVelocity(100, percent);
        Drivetrain.driveFor(forward, 12, inches);
        Drivetrain.turnFor(left, 90, degrees);
        Drivetrain.setDriveVelocity(75, percent);
        Drivetrain.drive(forward);
        wait(.25, seconds);
        Drivetrain.stop();
        bottom_arm_joint.setStopping(hold);
        top_arm_joint.setStopping(hold);
        bottom_arm_joint.spinFor(forward, 380, degrees);
        top_arm_joint.spinFor(forward, 1000, degrees);
        fly_wheel.spin(forward);
        wait(30, seconds);
        fly_wheel.stop();
        Drivetrain.setTurnVelocity(30, percent);
        Drivetrain.setDriveVelocity(50, percent);
        Drivetrain.turnFor(left, 45, degrees);
        Drivetrain.driveFor(reverse, 14, inches);
        Drivetrain.turnFor(right, 90, degrees);
        Drivetrain.setDriveVelocity(100, percent);
        Drivetrain.drive(reverse);
        wait (2.25, seconds);
        left_pusher.set(true);
        right_pusher.set(true);
        Drivetrain.turnFor(right, 135, degrees);
        Drivetrain.driveFor(forward, 40, inches);
        Drivetrain.turnFor(right, 45, degrees);
        Drivetrain.driveFor(forward, 5, inches);
        left_pusher.set(false);
        right_pusher.set(false);
        Drivetrain.driveFor(reverse, 5, inches);
    }
}

void select(void)
{
    if (selector == 0)
    {
        Brain.Screen.print("Auton 1 Selected: Near side with hanging");
        Brain.Screen.newLine();
        Brain.Screen.print("pole touch");
        Brain.Screen.newLine();
        Brain.Screen.print("Press button to change Auton");
    }
    else if (selector == 1)
    {
        Brain.Screen.print("Auton 2 Selected: Far side with hanging");
        Brain.Screen.newLine();
        Brain.Screen.print("pole touch");
        Brain.Screen.newLine();
        Brain.Screen.print("Press button to change Auton");
    }
    else if (selector == 2)
    {
        Brain.Screen.print("Auton 3 Selected: Near side without hanging");
        Brain.Screen.newLine();
        Brain.Screen.print("pole touch");
        Brain.Screen.newLine();
        Brain.Screen.print("Press button to change Auton");
    }
    else if (selector == 3)
    {
        Brain.Screen.print("Auton 4 Selected: Far side without hanging");
        Brain.Screen.newLine();
        Brain.Screen.print("pole touch");
        Brain.Screen.newLine();
        Brain.Screen.print("Press button to change Auton");
    }
    else
    {
        Brain.Screen.print("Auton 5 Selected: Programming skills");
        Brain.Screen.newLine();
        Brain.Screen.print("Press button to change Auton");
    }
}

void button_press(void)
{
    Brain.Screen.clearScreen();
    Brain.Screen.setCursor(1, 1);
    if (selector == 0) { selector = 1; }
    else if (selector == 1) { selector = 2; }
    else if (selector == 2) { selector = 3; }
    else if (selector == 3) { selector = 4; }
    else { selector = 0; }
    wait(5, msec);
    select();
}