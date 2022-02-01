def on_gesture_shake():
    global nasobok
    nasobok = 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_sound_loud():
    global nasobok
    nasobok = nasobok * 2
input.on_sound(DetectedSound.LOUD, on_sound_loud)

nasobok = 0
nasobok = 1

def on_forever():
    basic.show_number(nasobok)
basic.forever(on_forever)
