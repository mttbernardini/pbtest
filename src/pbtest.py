import pedalboard

# the following line fails with: Name "pedalboard.Plugin" is not defined [name-defined]
gain: pedalboard.Plugin

# the following line fails with: Module has no attribute "Gain" [attr-defined]
gain = pedalboard.Gain()

reveal_type(gain)