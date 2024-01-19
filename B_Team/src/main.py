#region VEXcode Generated Robot Configuration
from vex import *
import urandom #type: ignore

brain=Brain()

# Robot configuration code
# top_arm_joint = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True) > legacy


#Arm Punch Motor
punch = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True)

controller_1 = Controller(PRIMARY)
left_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)
left_motor_b = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
right_motor_b = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.185798, 368.3, 254, MM, 1)
drivetrain.set_stopping(BRAKE)

wait(30, MSEC)

# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, remote_control_code_enabled, tank
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3
            # right = axis2
            drivetrain_left_side_speed = controller_1.axis3.position()
            drivetrain_right_side_speed = controller_1.axis2.position()
            
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
# 	Project:      OverUnder Arcade B Team
#	Author:       B Team Authors
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

x = 0
y = 0
i = 0
p = 0
c = 0
acorn = False
selector = 0
auto = False
top = False
bottom = False
 
def auton():
    global selector
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(35, PERCENT)
    drivetrain.set_stopping(BRAKE)
    if selector == 0:
        drivetrain.drive_for(FORWARD, 25, INCHES)
        drivetrain.drive_for(REVERSE, 7, INCHES)
    # Legacy A Team Auton code removed - visible on original if need to see
    
    
def select():
    global selector
    if selector == 0:
        brain.screen.print("Only Auton Selected: Push")
    else:
        brain.screen.print("BONUS Auton Selected: Programming Skills")

    #old selector on A team code - find there if needed
    wait (10, MSEC)

def drive():
    timer = Timer()
    while not timer.time(SECONDS) == 75:
        pass
    controller_1.screen.clear_screen()
    controller_1.screen.set_cursor(1, 1)
    controller_1.rumble("..--")
    controller_1.screen.print("30 seconds left")

def when_started1():
    # top_arm_joint.set_max_torque(100, PERCENT)
    # top_arm_joint.set_velocity(25, PERCENT)
    # bottom_arm_joint.set_max_torque(100, PERCENT)
    # bottom_arm_joint.set_velocity(25, PERCENT)
    # top_arm_joint.set_stopping(HOLD)
    # bottom_arm_joint.set_stopping(HOLD)
    # intake.set_velocity(100, PERCENT)
    # pushers.set(False)
    select()

def brain_touch():
    # brain.screen.print("Port 1: left catapult motor")
    # brain.screen.new_line()
    brain.screen.print("LEGACY; NOT APPLICABLE")
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
    # Only one auton program, so unneeded selection
    """
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
    """
    selector = 0
    wait (5, MSEC)
    select()





"""
Driver Code Start


Naming Conventions

P_"/button/" = When the button is pressed

R_"/button/" = When the button is released

"""

#Arm Punching function

def P_X_Arm_Punch():    
    punch.set_velocity(100, PERCENT)
    punch.spin(FORWARD)

def R_X_Arm_Punch():
     punch.set_velocity(0, PERCENT)
     punch.stop()

# system event handlers
brain.screen.pressed(brain_touch) 
competition = Competition(drive, auton)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)
controller_1.buttonX.pressed(P_X_Arm_Punch)
controller_1.buttonX.released(R_X_Arm_Punch)
    
