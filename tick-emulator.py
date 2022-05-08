"""
Tick per interval of time with a specific frequency
"""

import pysine

DURATION_PER_FREQ = 0.1
REPETITION_PER_FREQ = 600

def to_freq(n):
  return 2 ** ((n - 49) / 12) * 440

def gen_octave_freq(start_n_C):
  octave = [
    start_n_C, start_n_C + 2, start_n_C + 4, start_n_C + 5,
    start_n_C + 7, start_n_C + 9, start_n_C + 11
  ]

  return list(map(to_freq, octave))

all_keys = [40, *gen_octave_freq(16)]  # from C3
all_keys += gen_octave_freq(28)  # from C4

# all_keys = [to_freq(39), to_freq(33)]

while True:
  for freq in all_keys:
    for _ in range(REPETITION_PER_FREQ):
      pysine.sine(frequency=freq, duration=DURATION_PER_FREQ)
