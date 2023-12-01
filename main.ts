input.onButtonPressed(Button.A, function () {
    PlanetX_AILens.learnObject(PlanetX_AILens.learnID.ID1)
})
input.onButtonPressed(Button.AB, function () {
    PlanetX_AILens.learnObject(PlanetX_AILens.learnID.ID5)
})
input.onButtonPressed(Button.B, function () {
    PlanetX_AILens.learnObject(PlanetX_AILens.learnID.ID3)
})
PlanetX_AILens.initModule()
PlanetX_AILens.switchfunc(PlanetX_AILens.FuncList.Things)
basic.forever(function () {
    neZha.setMotorSpeed(neZha.MotorList.M1, 25)
    neZha.setMotorSpeed(neZha.MotorList.M4, 25)
    PlanetX_AILens.cameraImage()
    if (PlanetX_AILens.objectCheck(PlanetX_AILens.learnID.ID1)) {
        neZha.stopAllMotor()
    } else if (PlanetX_AILens.objectCheck(PlanetX_AILens.learnID.ID3)) {
        neZha.setMotorSpeed(neZha.MotorList.M1, 15)
        neZha.setMotorSpeed(neZha.MotorList.M4, 0)
        basic.showNumber(3)
    } else if (PlanetX_AILens.objectCheck(PlanetX_AILens.learnID.ID5)) {
        neZha.setMotorSpeed(neZha.MotorList.M1, 0)
        neZha.setMotorSpeed(neZha.MotorList.M4, 15)
        basic.showNumber(5)
    }
})