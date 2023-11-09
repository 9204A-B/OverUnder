
# Vex Over Under VRC 9204A Code

## Changelog and notes
* Made separate programs for Arcade and Tank drive
* Set drivetrain stopping to brake

Avoid driving reverse because the robot can be unstable and lift possibly could affect Auton

### 11/2
* Added button selector to cycle through Auton
* Intake automatically stops after releasing Triball

### 11/3
* Added Auton: Near side with hanging pole touch

Auton is consistent in scoring Preloads. Needs more testing on descoring matchload - try testing more specific placement and rotation of matchload

### 11/6
* Renamed R2_pressed() to acorn_release()
* Renamed L1_pressed() to catapult_launch()
* Renamed R1_pressed() to acorn_grab()
* Renamed X_pressed() to push()
* Renamed A_pressed() to arm_drop()

### 11/7
* Added automatic and manual controls for catapult launching
* Added Auton: Far side without hanging pole touch

Far side Auton still needs testing

### 11/8
* Added Auton: Near side without hanging pole touch
* Added Auton: Programming skills
* Best matchload Triball position is slightly offset to the right - see image
[Near side starting position](https://github.com/coollogan876/OverUnder/assets/119338946/c50e58dd-a937-4684-a02a-7422326a28f2)

Programming skills needs more testing on barrier jumping

### 11/9
* Added Auton: Far side with hanging pole touch!

* Corrected automatic catapult launching
* Corrected Auton code

Make sure that functions like ...set_turn_velocity() is set as (x, PERCENT) otherwise it will be in RPM and will behave differently from expected
Programming skills barrier jumping works

## Authors

- [Logan Dresel](https://www.github.com/coollogan876)
- [Daniel Milan](https://github.com/Alcryst)
