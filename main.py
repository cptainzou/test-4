def on_button_pressed_a():
    PlanetX_AILens.clearlearn_object()
    PlanetX_AILens.learn_object(PlanetX_AILens.learnID.ID1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    PlanetX_AILens.clearlearn_object()
    PlanetX_AILens.learn_object(PlanetX_AILens.learnID.ID5)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    PlanetX_AILens.clearlearn_object()
    PlanetX_AILens.learn_object(PlanetX_AILens.learnID.ID3)
input.on_button_pressed(Button.B, on_button_pressed_b)

PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J2, True)
PlanetX_AILens.clearlearn_object()
PlanetX_AILens.init_module()
PlanetX_AILens.switchfunc(PlanetX_AILens.FuncList.THINGS)

def on_forever():
    PlanetX_AILens.camera_image()
    neZha.set_motor_speed(neZha.MotorList.M1, 25)
    neZha.set_motor_speed(neZha.MotorList.M4, 25)
    PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J2, False)
    PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J3, True)
    if PlanetX_AILens.object_check(PlanetX_AILens.learnID.ID1):
        PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J2, True)
        PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J3, False)
        neZha.set_motor_speed(neZha.MotorList.M1, 0)
        neZha.set_motor_speed(neZha.MotorList.M4, 0)
        basic.show_number(1)
    if PlanetX_AILens.object_check(PlanetX_AILens.learnID.ID3):
        PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J2, False)
        PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J3, True)
        neZha.set_motor_speed(neZha.MotorList.M1, 15)
        neZha.set_motor_speed(neZha.MotorList.M4, 0)
        basic.show_number(3)
    if PlanetX_AILens.object_check(PlanetX_AILens.learnID.ID5):
        PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J2, False)
        PlanetX_Display.led_brightness(PlanetX_Display.DigitalRJPin.J3, True)
        neZha.set_motor_speed(neZha.MotorList.M1, 0)
        neZha.set_motor_speed(neZha.MotorList.M4, 15)
        basic.show_number(5)
basic.forever(on_forever)
