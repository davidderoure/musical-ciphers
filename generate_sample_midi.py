"""
generate_sample_midi.py

Generates a sample MIDI file for the musical ciphers tutorial.

The piece is a short Bach-style melodic line that embeds the B-A-C-H
motif (Bb-A-C-B) at three known positions, surrounded by conjunct
stepwise motion to make it sound like a real melody.

Run this once to produce:  sample_bach_melody.mid
"""

from midiutil import MIDIFile

# ---------------------------------------------------------------------------
# B-A-C-H in MIDI pitch numbers (octave 4)
#   Bb4 = 70,  A4 = 69,  C4 = 60,  B4 = 71
# ---------------------------------------------------------------------------
Bb4, A4, C4, B4 = 70, 69, 60, 71

# A few neighbouring notes used as connective tissue
D4, E4, F4, G4 = 62, 64, 65, 67
C5, D5, E5     = 72, 74, 76
G3, A3, B3     = 55, 57, 59

# ---------------------------------------------------------------------------
# The melody: list of (pitch, duration_in_beats)
# BACH motif occurrences are at beat positions 0, 8, and 20
# ---------------------------------------------------------------------------
melody = [
    # --- First statement of BACH (beat 0) ---
    (Bb4, 1), (A4, 1), (C4, 1), (B4, 1),

    # Connective passage
    (C5, 1), (D5, 1), (E5, 1), (D5, 1),

    # --- Second statement of BACH (beat 8), up a step ---
    (Bb4, 1), (A4, 1), (C4, 1), (B4, 1),

    # Connective passage
    (A4, 1), (G4, 1), (F4, 1), (E4, 1),
    (D4, 1), (E4, 1), (F4, 1), (G4, 1),

    # --- Third statement of BACH (beat 20) ---
    (Bb4, 1), (A4, 1), (C4, 1), (B4, 1),

    # Closing cadence
    (A4, 1), (G4, 1), (F4, 1), (E4, 1),
    (D4, 1), (C4, 2),
]

# ---------------------------------------------------------------------------
# Write to MIDI
# ---------------------------------------------------------------------------
def write_melody(melody, filename, tempo=72):
    midi = MIDIFile(1)
    midi.addTempo(0, 0, tempo)

    time = 0
    for pitch, duration in melody:
        midi.addNote(
            track=0, channel=0,
            pitch=pitch,
            time=time,
            duration=duration * 0.9,   # slight articulation gap
            volume=90
        )
        time += duration

    with open(filename, 'wb') as f:
        midi.writeFile(f)
    print(f"Written: {filename}  ({time} beats, tempo {tempo} bpm)")

    # Report known positions
    beat = 0
    print("\nB-A-C-H motif embedded at beat positions:")
    for pitch, duration in melody:
        if pitch == Bb4:
            # Check if next three form BACH
            idx = melody.index((pitch, duration))
            window = [p for p, _ in melody[idx:idx+4]]
            if window == [Bb4, A4, C4, B4]:
                print(f"  Beat {beat}  →  Bb-A-C-B")
        beat += duration

if __name__ == '__main__':
    write_melody(melody, 'sample_bach_melody.mid')
