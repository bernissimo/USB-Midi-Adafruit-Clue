# midi_inoutdemo - demonstrates receiving and sending MIDI events
import usb_midi
import adafruit_midi
from adafruit_clue import clue

# TimingClock is worth importing first if present as it
# will make parsing more efficient for this high frequency event
# Only importing what is used will save a little bit of memory

# pylint: disable=unused-import
from adafruit_midi.timing_clock import TimingClock
from adafruit_midi.channel_pressure import ChannelPressure
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.polyphonic_key_pressure import PolyphonicKeyPressure
from adafruit_midi.program_change import ProgramChange
from adafruit_midi.start import Start
from adafruit_midi.stop import Stop
from adafruit_midi.system_exclusive import SystemExclusive

from adafruit_midi.midi_message import MIDIUnknownEvent

midi = adafruit_midi.MIDI(
    midi_in=usb_midi.ports[0],
    midi_out=usb_midi.ports[1],
    in_channel=(1, 2, 3),
    out_channel=0,
)

while True:
    msg_in = midi.receive()
    if isinstance(msg_in, NoteOn) and msg_in.velocity != 0:
        zahl = (440 / 32) * (2 ** ((msg_in.note - 9) / 12))
        clue.play_tone (zahl, 0.2)