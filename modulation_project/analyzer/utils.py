import matplotlib
matplotlib.use('Agg')  # <--- CRITICAL FIX: Must be before importing pyplot
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

def generate_message_signal(bit_count, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration))
    bits = np.random.randint(0, 2, bit_count)
    # Repeat bits to match the length of time array t
    samples_per_bit = int(len(t) / bit_count)
    
    # Trim t slightly if necessary to match the repeated bits length perfectly
    message = np.repeat(bits, samples_per_bit)
    t = t[:len(message)] 
    
    return t, message, bits

def am_modulate(message, carrier_freq, t):
    carrier = np.sin(2 * np.pi * carrier_freq * t)
    # (1 + m(t)) * c(t) - Simple Amplitude Modulation
    return (1 + 0.5 * message) * carrier

def fm_modulate(message, carrier_freq, t):
    kf = 20  # Frequency sensitivity
    # FIX: Proper integration requires multiplying by the time step (dt)
    dt = t[1] - t[0]
    integral = np.cumsum(message) * dt
    return np.sin(2 * np.pi * carrier_freq * t + 2 * np.pi * kf * integral)

def ask_modulate(message, carrier_freq, t):
    carrier = np.sin(2 * np.pi * carrier_freq * t)
    return message * carrier

def fsk_modulate(bits, t, bit_count, duration):
    f1, f0 = 5, 15
    signal = np.zeros_like(t)
    
    # Calculate exact samples per bit based on the actual t array
    samples_per_bit = len(t) // bit_count
    
    for i, bit in enumerate(bits):
        start = i * samples_per_bit
        # Ensure the last bit goes to the very end of the array
        end = (i + 1) * samples_per_bit if i < bit_count - 1 else len(t)
        
        freq = f1 if bit == 1 else f0
        # Slicing t ensures we use the correct time value for the sine wave
        signal[start:end] = np.sin(2 * np.pi * freq * t[start:end])
        
    return signal

def plot_signal(t, signal, title):
    # USE OBJECT-ORIENTED PLOTTING (Thread Safe)
    fig, ax = plt.subplots(figsize=(8, 3))
    
    ax.plot(t, signal)
    ax.set_title(title)
    ax.grid(True)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Amplitude')

    # Save to buffer
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    plt.close(fig)  # Explicitly close the specific figure object
    
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return img_base64

def bpsk_modulate(bits, t, bit_count):
    """
    BPSK: 0 -> -1, 1 -> +1
    """
    signal = np.zeros_like(t)
    samples_per_bit = len(t) // bit_count

    for i, bit in enumerate(bits):
        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit if i < bit_count - 1 else len(t)
        # Map bit to -1 or +1
        signal[start:end] = (2 * bit - 1) * np.sin(2 * np.pi * 10 * t[start:end])  # carrier freq = 10 Hz

    return signal


def qpsk_modulate(bits, t, bit_count):
    """
    QPSK: Map two bits at a time to phase shifts
    00 -> 0, 01 -> pi/2, 11 -> pi, 10 -> 3pi/2
    """
    signal = np.zeros_like(t)
    # Ensure even number of bits
    if len(bits) % 2 != 0:
        bits = np.append(bits, 0)
        bit_count += 1

    samples_per_symbol = len(t) // (bit_count // 2)

    for i in range(0, len(bits), 2):
        b1, b2 = bits[i], bits[i + 1]
        start = (i // 2) * samples_per_symbol
        end = ((i // 2) + 1) * samples_per_symbol if i < len(bits) - 2 else len(t)

        # Map to phase
        if (b1, b2) == (0, 0):
            phase = 0
        elif (b1, b2) == (0, 1):
            phase = np.pi / 2
        elif (b1, b2) == (1, 1):
            phase = np.pi
        else:  # (1,0)
            phase = 3 * np.pi / 2

        signal[start:end] = np.sin(2 * np.pi * 10 * t[start:end] + phase)  # carrier freq = 10 Hz

    return signal
