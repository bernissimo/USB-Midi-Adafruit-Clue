from adafruit_clue import clue
import usb_midi
import adafruit_midi
from adafruit_midi.note_on import NoteOn

screen = clue.simple_text_display(text_scale=2, colors=(clue.GREEN,))

screen[0].color = clue.YELLOW
screen[1].color = clue.GREEN
screen[2].color = clue.SKY
screen[3].color = clue.BLUE
screen[4].color = clue.BLUE
screen[5].color = clue.BLUE
screen[0].text = "ORCA playing"
screen[1].text = "Popcorn on Clue"
screen[2].text = "Thanks"
screen[3].text = "@ Hundredrabbits"
screen[4].text = "@ Adafruit"
screen[5].text = "@ Gershon Kingsley"
screen.show()

midi = adafruit_midi.MIDI(
    midi_in=usb_midi.ports[0],
    in_channel=(1),)
    
while True:
    msg_in = midi.receive()
    if isinstance(msg_in, NoteOn) != 0:    
        zahl = (440 / 32) * (2 ** ((msg_in.note - 9) / 12))
        clue.play_tone (zahl, 0.1)
        screen[6].text = int(zahl), "in Hz"
        screen[7].text = msg_in.note, "Midi Note"
        screen.show()
