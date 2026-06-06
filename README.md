# Musical Ciphers

A Python tutorial for the **Humanities Programming** class exploring musical ciphers — secret messages hidden inside music.

We begin with one of the most famous examples in Western music: **J.S. Bach's own name**, encoded as four notes and woven into his final, unfinished fugue.

---

## What is a musical cipher?

A **musical cipher** maps letters of the alphabet onto musical notes. Composers have used them to sign their works, pay homage to colleagues, or hide messages in plain hearing.

Bach's name encodes perfectly using the **German note-naming system**, where:

| Letter | Note |
|:---:|:---:|
| **B** | B♭ (B-flat) |
| **A** | A |
| **C** | C |
| **H** | B♮ (B-natural) |

So **B – A – C – H** becomes the four-note motif **B♭ – A – C – B♮**.

Bach embedded this in the final fugue of *The Art of Fugue* (BWV 1080, Contrapunctus XIV). The manuscript breaks off — possibly at the very moment he signed it with his own name.

---

## Contents

| File | Description |
|---|---|
| [`bach_cipher.ipynb`](bach_cipher.ipynb) | Main tutorial notebook (start here) |
| [`sample_bach_melody.mid`](sample_bach_melody.mid) | Sample MIDI file with the B-A-C-H motif hidden inside |
| [`generate_sample_midi.py`](generate_sample_midi.py) | Script that generated the sample MIDI |

---

## The notebook

The tutorial has five parts:

1. **Encoding and Decoding** — represent the German cipher in Python; encode and decode BACH as MIDI note numbers
2. **Extending the Cipher** — map the full A–Z alphabet onto the 12-note chromatic scale using modular arithmetic
3. **Playing the Cipher** — write encoded messages to real `.mid` files you can open in GarageBand or MuseScore
4. **Searching a MIDI File** — given a piece of music, search for a hidden motif using pitch-class matching
5. **The Hard Problem** — show why brute-force cipher recovery requires checking ~10²⁸ mappings, and how frequency analysis offers a smarter approach

---

## Getting started

### Prerequisites

- Python 3.9+
- Jupyter (Notebook or Lab)

### Installation

```bash
git clone https://github.com/davidderoure/musical-ciphers.git
cd musical-ciphers
pip install midiutil pretty_midi jupyter
jupyter notebook bach_cipher.ipynb
```

### Running the notebook

Open `bach_cipher.ipynb` and run all cells in order (**Cell → Run All**). Each part builds on the one before.

To regenerate the sample MIDI file:

```bash
python generate_sample_midi.py
```

---

## Listening to the cipher

The notebook writes `.mid` files you can open in:

- **macOS** — GarageBand (drag and drop) or QuickTime Player
- **All platforms** — [MuseScore](https://musescore.org) (free) renders MIDI as notation
- **Online** — [Signal MIDI editor](https://signal.vercel.app) plays MIDI in the browser

---

## Discussion questions

1. Bach's cipher works because of the German naming convention. What does this tell us about how **cultural context** shapes what counts as a hidden message?
2. The B-A-C-H motif appears in works by Schumann, Liszt, and Busoni as homage. Is that still a *cipher*, or something else?
3. What additional constraints could make the brute-force search tractable?
4. Could a composer today design a cipher that resists both frequency analysis *and* musical convention?

---

## Further reading

- Keller, H. (1965). *The Well-Tempered Clavier by Johann Sebastian Bach*
- Tatlow, R. (2015). *Bach's Numbers: Compositional Proportion and Significance*. Cambridge University Press
- [B-A-C-H motif — Wikipedia](https://en.wikipedia.org/wiki/BACH_motif)
- [The Art of Fugue — Wikipedia](https://en.wikipedia.org/wiki/The_Art_of_Fugue)

---

*Humanities Programming class — University of Oxford*
