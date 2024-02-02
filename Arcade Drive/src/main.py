#region VEXcode Generated Robot Configuration
from vex import *
import urandom #type: ignore

brain=Brain()
# Robot configuration code
top_arm_joint = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)
bottom_arm_joint = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
fly_wheel = Motor(Ports.PORT16, GearSetting.RATIO_6_1, False)
controller_1 = Controller(PRIMARY)
left_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
left_motor_b = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
right_motor_b = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.185798, 317.5, 254, MM, 1)
intake = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
left_pusher = DigitalOut(brain.three_wire_port.g)
right_pusher = DigitalOut(brain.three_wire_port.h)
acorn_sense = Distance(Ports.PORT4)
Auton_select = DigitalIn(brain.three_wire_port.f)
drivetrain.set_stopping(BRAKE)

wait(30, MSEC)

# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3 + axis1
            # right = axis3 - axis1
            drivetrain_left_side_speed = controller_1.axis3.position() + controller_1.axis1.position()
            drivetrain_right_side_speed = controller_1.axis3.position() - controller_1.axis1.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)

#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      OverUnder Arcade
#	Author:       Logan Dresel and DM
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

x = 0
y = 0
pusher = 0
p = 0
c = 0
acorn = False
selector = 0
manual = False
top = False
bottom = False
timer = Timer()
time_alert = False
down = False
printing = False
minutes = 0
seconds = 0

# to update auton
# change arm commands to left_pusher commands
# change pusher commands to commands for both left and right pushers
def when_started1():
    global auto
    top_arm_joint.set_max_torque(100, PERCENT)
    top_arm_joint.set_velocity(25, PERCENT)
    bottom_arm_joint.set_max_torque(100, PERCENT)
    bottom_arm_joint.set_velocity(25, PERCENT)
    top_arm_joint.set_stopping(HOLD)
    bottom_arm_joint.set_stopping(HOLD)
    intake.set_velocity(100, PERCENT)
    left_pusher.set(False)
    right_pusher.set(False)
    select()
    auto = False

def drive():
    global timer, time_alert
    controller_1.screen.clear_screen()
    Thread(arm_fold)
    Thread(screen_timer)
    Screen()
    top_arm_joint.set_stopping(HOLD)
    bottom_arm_joint.set_stopping(HOLD)
    drivetrain.set_drive_velocity(100, PERCENT)
    timer.clear()
    while not timer.time(SECONDS) == 75:
        pass
    time_alert = True
    controller_1.rumble("..--")

def auton():
    global selector, manual
    manual = False
    drivetrain.set_drive_velocity(75, PERCENT)
    drivetrain.set_turn_velocity(35, PERCENT)
    drivetrain.set_stopping(BRAKE)
    top_arm_joint.set_max_torque(100, PERCENT)
    top_arm_joint.set_velocity(25, PERCENT)
    bottom_arm_joint.set_max_torque(100, PERCENT)
    bottom_arm_joint.set_velocity(25, PERCENT)
    top_arm_joint.set_stopping(HOLD)
    bottom_arm_joint.set_stopping(HOLD)
    bottom_arm_joint.spin_for(REVERSE, .5, SECONDS) #Lift intake to drop arm
    top_arm_joint.set_stopping(COAST)
    bottom_arm_joint.set_stopping(COAST)
    if selector == 0: # Near side with hanging pole touch
        wait(100, MSEC)
        acorn_grab()
        left_pusher.set(True)
        drivetrain.drive_for(FORWARD, 18.5, INCHES)
        wait(250, MSEC)
        left_pusher.set(False)
        drivetrain.turn_for(RIGHT, 30, DEGREES)
        drivetrain.drive_for(FORWARD, 9, INCHES)
        acorn_release()
        wait(200, MSEC)
        drivetrain.drive_for(REVERSE, 3, INCHES)
        drivetrain.set_drive_velocity(100, PERCENT)
        drivetrain.drive_for(FORWARD, 6, INCHES)
        acorn_release()
        wait(200, MSEC)
        drivetrain.set_drive_velocity(75, PERCENT)
        drivetrain.drive_for(FORWARD, 1, INCHES)
        drivetrain.drive_for(REVERSE, 4, INCHES)
        drivetrain.turn_for(RIGHT, 50, DEGREES)
        drivetrain.drive_for(FORWARD, 40, INCHES)
        bottom_arm_joint.set_stopping(HOLD)
        top_arm_joint.set_stopping(HOLD)
        bottom_arm_joint.spin_for(FORWARD, 380, DEGREES)
        top_arm_joint.spin_for(FORWARD, 560, DEGREES)
        drivetrain.turn_for(RIGHT, 200, DEGREES)
        drivetrain.drive_for(REVERSE, 3, INCHES)
    elif selector == 1: # Far side with hanging pole touch
        wait(100, MSEC)
        acorn_grab()
        drivetrain.drive_for(FORWARD, 18.5, INCHES)
        wait(250, MSEC)
        drivetrain.turn_for(LEFT, 30, DEGREES)
        drivetrain.drive_for(FORWARD, 9, INCHES)
        acorn_release()
        wait (200, MSEC)
        drivetrain.drive_for(REVERSE, 3, INCHES)
        drivetrain.set_drive_velocity(100, PERCENT)
        drivetrain.drive_for(FORWARD, 6, INCHES)
        acorn_release()
        wait(200, MSEC)
        drivetrain.set_drive_velocity(75, PERCENT)
        drivetrain.drive_for(FORWARD, 1, INCHES)
        drivetrain.drive_for(REVERSE, 4, INCHES)
        drivetrain.turn_for(LEFT, 60, DEGREES)
        drivetrain.drive_for(FORWARD, 40, INCHES)
        drivetrain.turn_for(LEFT, 27, DEGREES)
        drivetrain.drive_for(FORWARD, 3, INCHES)
    elif selector == 2:# Near side without hang
        wait(100, MSEC)
        acorn_grab()
        left_pusher.set(True)
        drivetrain.drive_for(FORWARD, 18.5, INCHES)
        wait(250, MSEC)
        left_pusher.set(False)
        drivetrain.turn_for(RIGHT, 30, DEGREES)
        drivetrain.drive_for(FORWARD, 9, INCHES)
        acorn_release()
        wait(200, MSEC)
        drivetrain.drive_for(REVERSE, 3, INCHES)
        drivetrain.set_drive_velocity(100, PERCENT)
        drivetrain.drive_for(FORWARD, 6, INCHES)
        acorn_release()
        wait(200, MSEC)
        drivetrain.set_drive_velocity(75, PERCENT)
        drivetrain.drive_for(FORWARD, 1, INCHES)
        drivetrain.drive_for(REVERSE, 4, INCHES)
        drivetrain.turn_for(RIGHT, 60, DEGREES)
    elif selector == 3: # Far side without hang
        wait(100, MSEC)
        acorn_grab()
        drivetrain.drive_for(FORWARD, 18.5, INCHES)
        wait(250, MSEC)
        drivetrain.turn_for(LEFT, 30, DEGREES)
        drivetrain.drive_for(FORWARD, 9, INCHES)
        acorn_release()
        wait (200, MSEC)
        drivetrain.drive_for(REVERSE, 3, INCHES)
        drivetrain.set_drive_velocity(100, PERCENT)
        drivetrain.drive_for(FORWARD, 6, INCHES)
        acorn_release()
        wait(200, MSEC)
        drivetrain.set_drive_velocity(75, PERCENT)
        drivetrain.drive_for(FORWARD, 1, INCHES)
        drivetrain.drive_for(REVERSE, 4, INCHES)
        drivetrain.turn_for(LEFT, 60, DEGREES)
    else: # Programming skills
        drivetrain.set_stopping(BRAKE)
        drivetrain.set_turn_velocity(35, PERCENT)
        drivetrain.set_drive_velocity(100, PERCENT)
        drivetrain.drive_for(FORWARD, 12, INCHES)
        drivetrain.turn_for(LEFT, 90, DEGREES)
        drivetrain.set_drive_velocity(75, PERCENT)
        drivetrain.drive(FORWARD)
        wait(.25, SECONDS)
        drivetrain.stop()
        bottom_arm_joint.set_stopping(HOLD)
        top_arm_joint.set_stopping(HOLD)
        bottom_arm_joint.spin_for(REVERSE, 380, DEGREES)
        top_arm_joint.spin_for(REVERSE, 1000, DEGREES)
        fly_wheel.spin(FORWARD)
        wait(30, SECONDS)
        fly_wheel.stop()
        top_arm_joint.spin_to_position(20, DEGREES, False)
        bottom_arm_joint.spin_to_position(20, DEGREES, False)
        drivetrain.set_turn_velocity(30, PERCENT)
        drivetrain.set_drive_velocity(50, PERCENT)
        drivetrain.turn_for(LEFT, 45, DEGREES)
        drivetrain.drive_for(REVERSE, 14, INCHES)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.set_drive_velocity(100, PERCENT)
        drivetrain.drive(REVERSE)
        wait (2.25, SECONDS)
        left_pusher.set(True)
        right_pusher.set(True)
        drivetrain.turn_for(RIGHT, 135, DEGREES)
        drivetrain.drive_for(FORWARD, 40, INCHES)
        drivetrain.turn_for(RIGHT, 45, DEGREES)
        drivetrain.drive_for(FORWARD, 5, INCHES)
        left_pusher.set(False)
        right_pusher.set(False)
        drivetrain.drive_for(REVERSE, 5, INCHES)

def select():
    global selector
    if selector == 0:
        brain.screen.print("Auton 1 Selected: Near side with hanging")
        brain.screen.new_line()
        brain.screen.print("pole touch")
        brain.screen.new_line()
        brain.screen.print("Press button to change Auton")
    elif selector == 1:
        brain.screen.print("Auton 2 Selected: Far side with hanging")
        brain.screen.new_line()
        brain.screen.print("pole touch")
        brain.screen.new_line()
        brain.screen.print("Press button to change Auton")
    elif selector == 2:
        brain.screen.print("Auton 3 Selected: Near side without hanging")
        brain.screen.new_line()
        brain.screen.print("pole touch")
        brain.screen.new_line()
        brain.screen.print("Press button to change Auton")
    elif selector == 3:
        brain.screen.print("Auton 4 Selected: Far side without hanging")
        brain.screen.new_line()
        brain.screen.print("pole touch")
        brain.screen.new_line()
        brain.screen.print("Press button to change Auton")
    else:
        brain.screen.print("Auton 5 Selected: Programming skills")
        brain.screen.new_line()
        brain.screen.print("Press button to change Auton")
    wait (10, MSEC)

def acorn_distance():
    global acorn
    while True:
        if acorn_sense.object_distance() <= 70 and acorn:
            intake.stop()
            wait(20, MSEC)
        elif acorn_sense.object_distance() >= 240 and acorn == False:
            intake.stop()
            wait (20, MSEC)

def acorn_release():
    global y, acorn
    if y == 0:
        acorn = False
        intake.spin(REVERSE)
        wait(5, MSEC)
    elif y == 1:
        intake.stop()
        wait(5, MSEC)

def acorn_grab():
    global x, acorn
    if x == 0:
        acorn = True
        intake.set_velocity(100, PERCENT)
        intake.spin(FORWARD)
        wait(5, MSEC)
    elif x == 1:
        intake.stop()
        wait(5, MSEC)

def arm_fold(): # default is reverse
    global c, manual, down
    while True:
        if manual:
            top_arm_joint.set_velocity(100, PERCENT)
            if controller_1.buttonL1.pressing():
                Screen()
                if c == 0:
                    top_arm_joint.spin(REVERSE)
                else:
                    top_arm_joint.spin(FORWARD)
            else:
                top_arm_joint.stop()
                top_arm_joint.set_velocity(0, PERCENT)
            if controller_1.buttonL2.pressing():
                Screen()
                bottom_arm_joint.set_velocity(100, PERCENT)
                if c == 0:
                    bottom_arm_joint.spin(REVERSE)
                else:
                    bottom_arm_joint.spin(FORWARD)
            else:
                bottom_arm_joint.stop()
                bottom_arm_joint.set_velocity(0, PERCENT) 
        else:
            top_arm_joint.set_velocity(100, PERCENT)
            bottom_arm_joint.set_velocity(100, PERCENT)
            if controller_1.buttonL1.pressing():
                Screen()
                top_arm_joint.spin_for(REVERSE, 500, DEGREES)
                wait(500, MSEC)
                top_arm_joint.stop()
                top_arm_joint.set_velocity(0, PERCENT)
            if controller_1.buttonL2.pressing():
                Screen()
                bottom_arm_joint.spin_for(REVERSE, 380, DEGREES)
                top_arm_joint.spin_for(REVERSE, 1000, DEGREES)
                wait(500, MSEC)
                top_arm_joint.stop()
                top_arm_joint.set_velocity(0, PERCENT)
                bottom_arm_joint.stop()
                bottom_arm_joint.set_velocity(0, PERCENT)
            if controller_1.buttonY.pressing():
                top_arm_joint.spin_to_position(20, DEGREES, False)
                bottom_arm_joint.spin_to_position(20, DEGREES, True)
        wait(20, MSEC)

def Left_pressed():
    global manual
    if not manual:
        manual = True
    else:
        manual = False
    Screen()

def Up_pressed():
    global c, manual, down # default 0 (reverse)    
    if c == 0 and manual:
        c = 1
        down = True
        Screen()        
    elif c == 1 and manual:
        c = 0
        down = False
        Screen()

def R2_released():
    global y, acorn
    if y == 0:
        y = 1
        wait(5, MSEC)
    else:
        y = 0
        wait(5, MSEC)

def R1_released():
    global x
    if x == 0:
        x = 1
        wait(5, MSEC)
    else:
        x = 0
        wait(5, MSEC)

def push():
    global pusher
    if pusher == 0:
        left_pusher.set(True)
        right_pusher.set(True)
        wait(5, MSEC)
    elif pusher == 1:
        left_pusher.set(False)
        right_pusher.set(False)
        wait(5, MSEC)
    
def B_release():
    global pusher
    if pusher == 0:
        pusher = 1
        wait(5, MSEC)
    else:
        pusher = 0
        wait(5, MSEC)

def A_press():
    global p
    if p == 0:
        fly_wheel.set_velocity(100, PERCENT)
        fly_wheel.set_max_torque(100, PERCENT)
        fly_wheel.spin(REVERSE)
    else:
        fly_wheel.stop()

def A_release():
    global p
    if p == 0:
        p = 1
        wait(5, MSEC)
    else:
        p = 0
        wait(5, MSEC)

def brain_touch():
    brain.screen.print("Port 1: left catapult motor")
    brain.screen.new_line()
    brain.screen.print("Port 2: right catapult motor")
    brain.screen.new_line()
    brain.screen.print("Port 3: intake motor")
    brain.screen.new_line()
    brain.screen.print("Port 4: intake sensor")
    brain.screen.new_line()
    brain.screen.print("Port 5: catapult sensor")
    brain.screen.new_line()
    brain.screen.print("Port 11: left drive motor")
    brain.screen.new_line()
    brain.screen.print("Port 12: left drive motor")
    brain.screen.new_line()
    brain.screen.print("Port 19: right drive motor")
    brain.screen.new_line()
    brain.screen.print("Port 20: right drive motor")
    brain.screen.set_cursor(1, 1)
    wait (60, SECONDS)
    brain.screen.clear_screen()

def button_pressed():
    global selector
    brain.screen.clear_screen()
    brain.screen.set_cursor(1, 1)
    if selector == 0:
        selector = 1
        wait (5, MSEC)
    elif selector == 1:
        selector = 2
        wait (5, MSEC)
    elif selector == 2:
        selector = 3
        wait (5, MSEC)
    elif selector == 3:
        selector = 4
        wait (5, MSEC)
    else:
        selector = 0
        wait (5, MSEC)
    select()

def screen_timer():
    global timer, time_alert, printing, seconds, minutes
    while True:
        Time = "Time: " + str(minutes) + ":0" + str(seconds)
        if not printing:
            controller_1.screen.set_cursor(1, 1)
            if time_alert:
                controller_1.screen.clear_screen()
                controller_1.screen.print("30 seconds left!")
                wait(1, SECONDS)
                time_alert = False
                Screen()
            if seconds > 9:
                Time = "Time: " + str(minutes) + ":" + str(seconds)
            if seconds >= 60:
                minutes += 1
                seconds = 0
            controller_1.screen.clear_line(1)
            controller_1.screen.print(Time)
            controller_1.screen.clear_line(2)
            controller_1.screen.set_cursor(2, 1)
            controller_1.screen.print("Temps: " + str(math.trunc(bottom_arm_joint.temperature())) +
                                       ", " + str(math.trunc(top_arm_joint.temperature())))
        seconds += 1
        wait(1, SECONDS)

def Screen():
    global timer, time_alert, manual, down, arm, printing
    printing = True
    arm = "Arm: Automatic"
    if manual and down:
        arm ="Arm: Down"
    if manual and not down:
        arm = "Arm: Up"
    controller_1.screen.set_cursor(3, 1)
    controller_1.screen.clear_line(3)
    controller_1.screen.print(arm)
    wait(20, MSEC)
    printing = False

# system event handlers
#Trigger buttons
controller_1.buttonR1.pressed(acorn_grab)
controller_1.buttonR1.released(R1_released)
controller_1.buttonR2.pressed(acorn_release)
controller_1.buttonR2.released(R2_released)
# Direction buttons
controller_1.buttonUp.pressed(Up_pressed)
controller_1.buttonLeft.pressed(Left_pressed)
# Letter buttons
controller_1.buttonA.pressed(A_press)
controller_1.buttonA.released(A_release)
controller_1.buttonB.pressed(push)
controller_1.buttonB.released(B_release)

brain.screen.pressed(brain_touch) 
Auton_select.high(button_pressed)
competition = Competition(drive, auton)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

Thread(when_started1)
Thread(acorn_distance)
