#region VEXcode Generated Robot Configuration
from vex import *
import urandom #type: ignore

brain=Brain()

# Robot configuration code
# top_arm_joint = Motor(Ports.PORT1, GearSetting.RATIO_18_1, True) > legacy


#Arm Punch Motor
left_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_18_1, True)

controller_1 = Controller(PRIMARY)
left_motor_b = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
left_drive_smart = MotorGroup(left_motor_a, left_motor_b)
right_motor_a = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
right_motor_b = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
right_drive_smart = MotorGroup(right_motor_a, right_motor_b)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 4, 12, 10, INCHES, 1)
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
    # if selector == 0: # Near side with hanging pole touch
    #     drivetrain.set_drive_velocity(100, PERCENT)
    #     drivetrain.set_turn_velocity(35, PERCENT)
    #     arm.set(True)
    #     drivetrain.drive_for(FORWARD, 17.5, INCHES)
    #     wait (250, MSEC)
    #     arm.set(False)
        # drivetrain.turn_for(RIGHT, 90, DEGREES)
        # drivetrain.drive_for(FORWARD, 5, INCHES)
        # acorn_release()
        # wait (200, MSEC)
        # drivetrain.drive_for(FORWARD, 4, INCHES)
        # drivetrain.drive_for(REVERSE, 6, INCHES)
        # drivetrain.turn_for(RIGHT, 180, DEGREES)
        # drivetrain.drive_for(FORWARD, 4, INCHES)
        # drivetrain.turn_for(RIGHT, 10, DEGREES)
        # arm.set(True)
        # drivetrain.turn_for(RIGHT, 115, DEGREES)
        # drivetrain.drive_for(REVERSE, 6, INCHES)
        # arm.set(False)
        # wait(150, MSEC)
        # drivetrain.turn_for(RIGHT, 250, DEGREES)
        # drivetrain.drive_for(FORWARD, 8, INCHES)
        # drivetrain.turn_for(RIGHT, 75, DEGREES)
        # drivetrain.drive_for(FORWARD, 11.25, INCHES)
        # drivetrain.turn_for(LEFT, 73.5, DEGREES)
        # drivetrain.drive_for(FORWARD, 25, INCHES)
        # arm.set(True)
    # elif selector == 1: # Far side with hanging pole touch
    #     drivetrain.drive_for(FORWARD, 17, INCHES)
    #     drivetrain.turn_for(LEFT, 45, DEGREES)
    #     drivetrain.drive_for(FORWARD, 5, INCHES)
    #     acorn_release()
    #     wait (200, MSEC)
    #     drivetrain.drive_for(FORWARD, 10, INCHES)
    #     drivetrain.drive_for(REVERSE, 10, INCHES)
    #     drivetrain.turn_for(LEFT, 180, DEGREES)
    #     drivetrain.drive_for(REVERSE, 11, INCHES)
    #     drivetrain.drive_for(FORWARD, 5, INCHES)
    #     drivetrain.set_turn_velocity(25, PERCENT)
    #     drivetrain.turn_for(RIGHT, 90, DEGREES)
    #     drivetrain.drive_for(FORWARD, 32, INCHES)
    #     drivetrain.turn_for(RIGHT, 90, DEGREES)
    #     acorn_grab()
    #     drivetrain.drive_for(FORWARD, 32, INCHES)
    #     drivetrain.turn_for(RIGHT, 100, DEGREES)
    #     acorn_release()
    #     drivetrain.set_turn_velocity(35, PERCENT)
    #     drivetrain.drive_for(FORWARD, 20, INCHES)
    #     drivetrain.drive_for(REVERSE, 10, INCHES)
    #     drivetrain.turn_for(RIGHT, 90, DEGREES)
    #     drivetrain.drive_for(FORWARD, 50, INCHES)
    #     drivetrain.turn_for(RIGHT, 90, DEGREES)
    #     drivetrain.drive_for(FORWARD, 30, INCHES)
    #     arm.set(True)
    # elif selector == 2:# Near side without hang
    #     drivetrain.set_drive_velocity(100, PERCENT)
    #     drivetrain.set_turn_velocity(35, PERCENT)
    #     drivetrain.drive_for(FORWARD, 17.5, INCHES)
    #     drivetrain.turn_for(RIGHT, 45, DEGREES)
    #     drivetrain.drive_for(FORWARD, 5, INCHES)
    #     acorn_release()
    #     wait (200, MSEC)
    #     drivetrain.drive_for(FORWARD, 4, INCHES)
    #     drivetrain.drive_for(REVERSE, 6, INCHES)
    #     drivetrain.turn_for(RIGHT, 180, DEGREES)
    #     drivetrain.drive_for(FORWARD, 4, INCHES)
    #     drivetrain.turn_for(RIGHT, 10, DEGREES)
    #     arm.set(True)
    #     drivetrain.turn_for(RIGHT, 115, DEGREES)
    #     drivetrain.drive_for(REVERSE, 6, INCHES)
    #     arm.set(False)
    #     drivetrain.turn_for(RIGHT, 125, DEGREES)
    #     drivetrain.drive_for(REVERSE, 6, INCHES)
    #     arm.set(False)
    #     wait(150, MSEC)
    #     drivetrain.turn_for(RIGHT, 250, DEGREES)
    # elif selector == 3: # Far side without hang
    #     drivetrain.drive_for(FORWARD, 17, INCHES)
    #     drivetrain.turn_for(LEFT, 45, DEGREES)
    #     drivetrain.drive_for(FORWARD, 5, INCHES)
    #     acorn_release()
    #     wait (200, MSEC)
    #     drivetrain.drive_for(FORWARD, 10, INCHES)
    #     drivetrain.drive_for(REVERSE, 10, INCHES)
    #     drivetrain.turn_for(LEFT, 180, DEGREES)
    #     drivetrain.drive_for(REVERSE, 11, INCHES)
    #     drivetrain.drive_for(FORWARD, 5, INCHES)
    #     drivetrain.set_turn_velocity(25, PERCENT)
    #     drivetrain.turn_for(RIGHT, 90, DEGREES)
    #     drivetrain.drive_for(FORWARD, 32, INCHES)
    #     drivetrain.turn_for(RIGHT, 90, DEGREES)
    #     acorn_grab()
    #     drivetrain.drive_for(FORWARD, 32, INCHES)
    #     drivetrain.turn_for(RIGHT, 100, DEGREES)
    #     drivetrain.set_turn_velocity(35, PERCENT)
    #     acorn_release()
    #     drivetrain.drive_for(FORWARD, 20, INCHES)
    #     drivetrain.drive_for(REVERSE, 5, INCHES)
    #     drivetrain.turn_for(RIGHT, 180, DEGREES)
    #     acorn_grab()
    #     drivetrain.drive_for(FORWARD, 25, INCHES)
    #     drivetrain.drive_for(REVERSE, 5, INCHES)
    #     drivetrain.turn_for(LEFT, 180, DEGREES)
    #     acorn_release()
    #     drivetrain.drive_for(FORWARD, 25, INCHES)
    #     drivetrain.drive_for(REVERSE, 5, INCHES)
    # else: # Programming skills
    #     drivetrain.set_stopping(BRAKE)
    #     drivetrain.set_turn_velocity(35, PERCENT)
    #     drivetrain.set_drive_velocity(100, PERCENT)
    #     drivetrain.drive_for(FORWARD, 12, INCHES)
    #     drivetrain.turn_for(LEFT, 90, DEGREES)
    #     drivetrain.set_drive_velocity(75, PERCENT)
    #     drivetrain.drive(FORWARD)
    #     wait(.25, SECONDS)
    #     drivetrain.stop()
    #     counter = 0
    #     while counter < 46:
    #         catapult.spin(FORWARD)
    #         if catapult_sense.object_distance() <= 65:
    #             counter += 1
    #             catapult.spin(FORWARD)
    #             wait (250, MSEC)
    #             controller_1.screen.clear_screen()
    #             controller_1.screen.set_cursor(1, 1)
    #             controller_1.screen.print(counter)
    #     catapult.stop()
    #     drivetrain.set_turn_velocity(30, PERCENT)
    #     drivetrain.set_drive_velocity(50, PERCENT)
    #     drivetrain.turn_for(LEFT, 45, DEGREES)
    #     drivetrain.drive_for(REVERSE, 14, INCHES)
    #     drivetrain.turn_for(RIGHT, 90, DEGREES)
    #     drivetrain.set_drive_velocity(100, PERCENT)
    #     drivetrain.drive(REVERSE)
    #     wait (2.25, SECONDS)
    #     pushers.set(True)
    #     drivetrain.turn_for(RIGHT, 135, DEGREES)
    #     drivetrain.drive_for(FORWARD, 40, INCHES)
    #     drivetrain.turn_for(RIGHT, 45, DEGREES)
    #     drivetrain.drive_for(FORWARD, 5, INCHES)
    #     pushers.set(False)
    #     drivetrain.drive_for(REVERSE, 5, INCHES)
    
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

# system event handlers
# controller_1.buttonL2.pressed(L2_press) > legacy

controller_1.buttonX.pressed(push)
controller_1.buttonX.released(X_released)
brain.screen.pressed(brain_touch) 
Auton_select.high(button_pressed)
competition = Competition(drive, auton)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

Thread(when_started1) # legacy; no use




"""
Driver Code Start


Naming Conventions

P_"/button/" = When the button is pressed

R_"/button/" = When the button is released

"""

#Arm Punching function

def P_X_Arm_Punch():
    global IsPunching? = 1
    while(IsPunching != 0):
        left_motor_a.set_velocity(100, PERCENT)
        
        """IMPORTANT, BEFORE RUNNING CODE SET THE SLEEP FUNCTION TO THE PUNCH DURATION, YOU WILL BURN OUT MOTOR IF YOU DON"T sleep(5)"""
        
        left_motor_a.set_velocity(-100, PERCENT)
        
        

def R_X_Arm_Punch():
    IsPunching? = 0
    
