input.onGesture(Gesture.Shake, function () {
    nasobok = 1
})
input.onSound(DetectedSound.Loud, function () {
    nasobok = nasobok * 2
})
let nasobok = 0
nasobok = 1
basic.forever(function () {
    basic.showNumber(nasobok)
})
