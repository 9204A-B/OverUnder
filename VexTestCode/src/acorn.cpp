#include "vex.h"
using namespace vex;

void acorn_distance(void)
{
    while (true)
    {
        if (acorn_sense.objectDistance(mm) <= 70 && acorn)
        {
            intake.stop();
        }
        else if (acorn_sense.objectDistance(mm) >= 240 && !acorn)
        {
            intake.stop();
        }
        wait (20, msec);
    }
}

void acorn_release(void)
{
    if (y == 0)
    {
        acorn = false;
        intake.spin(reverse);
    }
    else
    {
        intake.stop();
    }
    wait(5, msec);
}

void acorn_grab(void)
{
    if (x == 0)
    {
        acorn = true;
        intake.setVelocity(100, percent);
        intake.spin(forward);
    }
    else
    {
        intake.stop();
    }
    wait(5, msec);
}

void R1_release(void)
{
    if (x == 0)
    {
        x = 1;
    }
    else
    {
        x = 0;
    }
    wait(5, msec);
}

void R2_release(void)
{
    if (y == 0)
    {
        y = 1;
    }
    else
    {
        y = 0;
    }
    wait(5, msec);
}