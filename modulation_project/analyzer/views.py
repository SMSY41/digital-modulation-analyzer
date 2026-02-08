from django.shortcuts import render
from .forms import ModulationForm
from .utils import (
    generate_message_signal,
    am_modulate,
    fm_modulate,
    ask_modulate,
    fsk_modulate,
    bpsk_modulate,
    qpsk_modulate,
    plot_signal
)

def analyzer_view(request):
    form = ModulationForm(request.POST or None)
    input_plot = None
    modulated_plot = None

    if request.method == "POST" and form.is_valid():
        modulation = form.cleaned_data['modulation']
        sample_rate = form.cleaned_data['sample_rate']
        duration = form.cleaned_data['duration']
        carrier_freq = form.cleaned_data['carrier_freq']
        bit_count = form.cleaned_data['bit_count']

        t, message, bits = generate_message_signal(bit_count, duration, sample_rate)

        # Select modulation
        if modulation == "AM":
            mod_signal = am_modulate(message, carrier_freq, t)
        elif modulation == "FM":
            mod_signal = fm_modulate(message, carrier_freq, t)
        elif modulation == "ASK":
            mod_signal = ask_modulate(message, carrier_freq, t)
        elif modulation == "FSK":
            mod_signal = fsk_modulate(bits, t, bit_count, duration)
        elif modulation == "BPSK":
            mod_signal = bpsk_modulate(bits, t, bit_count)
        elif modulation == "QPSK":
            mod_signal = qpsk_modulate(bits, t, bit_count)
        else:
            mod_signal = message  # fallback

        input_plot = plot_signal(t, message, "Input Message Signal")
        modulated_plot = plot_signal(t, mod_signal, f"{modulation} Modulated Signal")

    return render(request, 'analyzer/analyzer.html', {
        'form': form,
        'input_plot': input_plot,
        'modulated_plot': modulated_plot
    })

