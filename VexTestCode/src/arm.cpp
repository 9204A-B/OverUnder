#include "vex.h"
using namespace vex;

void arm_fold(void) // default is reverse
{
    top_arm_joint.setVelocity(100, percent);
    bottom_arm_joint.setVelocity(100, percent);
    while(true)
    {
        if (manual)
        {
            if (controller_1.ButtonL1.pressing())
            {
                top_arm_joint.setVelocity(100, percent);
                if (c == 0) { top_arm_joint.spin(reverse); }
                else { top_arm_joint.spin(forward); }
            }
            else
            {
                top_arm_joint.stop();
                top_arm_joint.setVelocity(0, percent);
            }
            if (controller_1.ButtonL2.pressing())
            {
                bottom_arm_joint.setVelocity(100, percent);
                if (c == 0) { bottom_arm_joint.spin(reverse); }
                else { bottom_arm_joint.spin(forward); }
            }
            else
            {
                bottom_arm_joint.stop();
                bottom_arm_joint.setVelocity(0, percent);
            }
        }
        else if (!manual)
        {        
            top_arm_joint.setVelocity(100, percent);
            bottom_arm_joint.setVelocity(100, percent);    
            if (controller_1.ButtonL1.pressing())
            {
                full = false;
                top_arm_joint.spinFor(reverse, 800, degrees);
                wait(500, msec);
                top_arm_joint.stop();
                top_arm_joint.setVelocity(0, percent);
            }
            else if (controller_1.ButtonL2.pressing())
            {
                full = true;
                bottom_arm_joint.spinFor(reverse, 380, degrees);
                top_arm_joint.spinFor(reverse, 1000, degrees);
                wait(500, msec);
                top_arm_joint.stop();
                top_arm_joint.setVelocity(0, percent);
                bottom_arm_joint.stop();
                bottom_arm_joint.setVelocity(0, percent);
            }
            else if (controller_1.ButtonY.pressing())
            {
                if (full)
                {
                    top_arm_joint.spinFor(forward, 400, degrees);
                    top_arm_joint.setStopping(brake);
                    bottom_arm_joint.spinFor(forward, 250, degrees);
                    bottom_arm_joint.setStopping(brake);
                    wait(250, msec);
                    top_arm_joint.setStopping(hold);
                    bottom_arm_joint.setStopping(hold);
                    full = false;
                }
                else
                {
                    top_arm_joint.spinFor(forward, 300, degrees);
                    top_arm_joint.setStopping(brake);
                    wait(250, msec);
                    top_arm_joint.setStopping(hold);
                }
            }
        }
        wait(20, msec);
    }
}

void arm_mode(void)
{
    controller_1.Screen.clearScreen();
    controller_1.Screen.setCursor(1, 1);
    if (!manual)
    {
        manual = true;
        controller_1.Screen.print("Arm is now manual");
    }
    else
    {
        manual = false;
        controller_1.Screen.print("Arm is automatic");
    }
}

void arm_direction(void)
{
    controller_1.Screen.clearScreen();
    controller_1.Screen.setCursor(1, 1);
    if (c == 0 && manual)
    {
        c = 1;
        controller_1.Screen.print("Arm will go down");
    }
    else if (c == 1 && manual)
    {
        c = 0;
        controller_1.Screen.print("Arm will go up");
    }
}

void A_press(void)
{
    if (p == 0)
    {
        fly_wheel.setVelocity(100, percent);
        fly_wheel.setMaxTorque(100, percent);
        fly_wheel.spin(reverse);
    }
    else { fly_wheel.stop(); }
    wait(5, msec);
}

void A_release(void)
{
    if (p == 0)
    {
        p = 1;
    }
    else { p = 0; }
    wait(5, msec);
}