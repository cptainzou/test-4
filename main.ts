input.onButtonPressed(Button.A, function () {
    PlanetX_AILens.learnObject(PlanetX_AILens.learnID.ID1)
})
input.onButtonPressed(Button.AB, function () {
    PlanetX_AILens.learnObject(PlanetX_AILens.learnID.ID5)
})
input.onButtonPressed(Button.B, function () {
    PlanetX_AILens.learnObject(PlanetX_AILens.learnID.ID3)
})
PlanetX_Display.ledBrightness(PlanetX_Display.DigitalRJPin.J2, true)
PlanetX_AILens.ClearlearnObject()
PlanetX_AILens.initModule()
PlanetX_AILens.switchfunc(PlanetX_AILens.FuncList.Things)
PlanetX_AILens.ClearlearnObject()
neZha.setMotorSpeed(neZha.MotorList.M1, 25)
neZha.setMotorSpeed(neZha.MotorList.M4, 25)
basic.forever(function () {
    PlanetX_AILens.cameraImage()
    if (PlanetX_AILens.objectCheck(PlanetX_AILens.learnID.ID1)) {
        neZha.setMotorSpeed(neZha.MotorList.M1, 0)
        neZha.setMotorSpeed(neZha.MotorList.M4, 0)
        basic.showNumber(1)
    } else if (PlanetX_AILens.objectCheck(PlanetX_AILens.learnID.ID3)) {
        neZha.setMotorSpeed(neZha.MotorList.M1, 15)
        neZha.setMotorSpeed(neZha.MotorList.M4, 0)
        basic.showNumber(3)
    } else if (PlanetX_AILens.objectCheck(PlanetX_AILens.learnID.ID5)) {
        neZha.setMotorSpeed(neZha.MotorList.M1, 0)
        neZha.setMotorSpeed(neZha.MotorList.M4, 15)
        basic.showNumber(5)
    } else {
        neZha.setMotorSpeed(neZha.MotorList.M1, 25)
        neZha.setMotorSpeed(neZha.MotorList.M4, 25)
    }
})
