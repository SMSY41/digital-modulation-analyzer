from django import forms

MODULATION_CHOICES = [
    ('AM', 'AM'),
    ('FM', 'FM'),
    ('ASK', 'ASK'),
    ('FSK', 'FSK'),
    ('BPSK', 'BPSK'),
    ('QPSK', 'QPSK'),
]

class ModulationForm(forms.Form):
    modulation = forms.ChoiceField(
        choices=MODULATION_CHOICES,
        label="Select Modulation Type"
    )
    bit_count = forms.IntegerField(
        min_value=1,
        max_value=64,
        initial=8,
        label="Number of Bits"
    )
    duration = forms.FloatField(
        min_value=0.1,
        max_value=10.0,
        initial=1.0,
        label="Signal Duration (seconds)"
    )
    sample_rate = forms.IntegerField(
        min_value=100,
        max_value=10000,
        initial=1000,
        label="Sample Rate (Hz)"
    )
    carrier_freq = forms.FloatField(
        min_value=1.0,
        max_value=100.0,
        initial=10.0,
        label="Carrier Frequency (Hz)"
    )
