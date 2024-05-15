# Security-Voice-code-Access

## Introduction
Design and implement the software component of Security Voice-code Access. Based on the fingerprint and spectrogram concepts, the software can be trained on 8 individuals and work in two operation modes:

### Mode 1 – Security Voice code:
Access is not granted except for a specific passcode sentence. Any of the three following sentences is considered a valid passcode: “Open the middle door”, “Unlock the gate”, or “Grant me access”.

### Mode 2 – Security voice fingerprint:
Access is granted to a specific individual(s) who says the valid passcode sentence.

## Features
The UI has the following elements:
- A button to start recording the voice code,
- A spectrogram viewer for the spoken voice-code,
- A summary of the analysis results showing:
  1. A table with how much the spoken sentence matches each of the saved three passcode sentences.
  2. A table with how much the spoken voice matches each of the 8 saved individuals.
- Some UI element that indicates the results of the algorithm whether it’s “Access gained” or “Access denied”.
