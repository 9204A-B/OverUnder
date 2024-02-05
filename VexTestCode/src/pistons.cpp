#include "vex.h"
using namespace vex;

void push(void)
{
    if (pusher == 0)
    {
        left_pusher.set(true);
        right_pusher.set(true);
    }
    else
    {
        left_pusher.set(false);
        right_pusher.set(false);
    }
    wait(5, msec);
}

void B_release(void)
{
    if (pusher == 0)
    {
        pusher = 1;
    }
    else
    {
        pusher = 0;
    }
    wait(5, msec);
}