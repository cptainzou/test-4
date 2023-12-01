def on_button_pressed_a():
    PlanetX_AILens.learn_object(PlanetX_AILens.learnID.ID1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    PlanetX_AILens.learn_object(PlanetX_AILens.learnID.ID3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    PlanetX_AILens.learn_object(PlanetX_AILens.learnID.ID2)
input.on_button_pressed(Button.B, on_button_pressed_b)

j = 0
i = 0
PlanetX_AILens.init_module()
PlanetX_AILens.switchfunc(PlanetX_AILens.FuncList.THINGS)
PlanetX_AILens.switchfunc(PlanetX_AILens.FuncList.FACE)

def on_forever():
    global i, j
    neZha.set_motor_speed(neZha.MotorList.M1, 50)
    neZha.set_motor_speed(neZha.MotorList.M4, 50)
    PlanetX_AILens.camera_image()
    if PlanetX_AILens.object_check(PlanetX_AILens.learnID.ID1) < 150:
        if PlanetX_AILens.object_check(PlanetX_AILens.learnID.ID2) < 150:
            if PlanetX_AILens.object_check(PlanetX_AILens.learnID.ID3) < 150:
                if PlanetX_AILens.object_check(PlanetX_AILens.learnID.ID1):
                    neZha.set_motor_speed(neZha.MotorList.M1, 0)
                    neZha.set_motor_speed(neZha.MotorList.M4, 0)
                    basic.show_number(1)
                if PlanetX_AILens.object_check(PlanetX_AILens.learnID.ID2):
                    neZha.set_motor_speed(neZha.MotorList.M1, 15)
                    neZha.set_motor_speed(neZha.MotorList.M4, 15)
                    basic.show_number(2)
                if PlanetX_AILens.object_check(PlanetX_AILens.learnID.ID3):
                    neZha.set_motor_speed(neZha.MotorList.M1, 15)
                    neZha.set_motor_speed(neZha.MotorList.M4, 15)
                    basic.show_number(3)
    elif PlanetX_AILens.check_face():
        if PlanetX_AILens.face_data(PlanetX_AILens.Facestatus.X) < 90:
            i += -2
        if PlanetX_AILens.face_data(PlanetX_AILens.Facestatus.X) > 150:
            i += 2
        if PlanetX_AILens.face_data(PlanetX_AILens.Facestatus.Y) > 150:
            j += -2
        if PlanetX_AILens.face_data(PlanetX_AILens.Facestatus.Y) < 90:
            j += 2
basic.forever(on_forever)
