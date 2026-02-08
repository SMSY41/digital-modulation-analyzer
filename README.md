# Digital Modulation Analyzer

A Django-based web application for analyzing and visualizing digital and analog modulation techniques. The system generates random message signals, applies various modulation schemes, and displays the resulting waveforms graphically.

## Overview

The Digital Modulation Analyzer is an educational project designed to help students and engineers understand how different communication modulation techniques work. Users can input custom parameters and instantly generate modulated signals with visual output.

## Supported Modulation Types

- AM – Amplitude Modulation  
- FM – Frequency Modulation  
- ASK – Amplitude Shift Keying  
- FSK – Frequency Shift Keying  
- BPSK – Binary Phase Shift Keying  
- QPSK – Quadrature Phase Shift Keying  

## Features

- Interactive web interface  
- Real-time signal generation  
- Graphical visualization of signals  
- Support for multiple modulation schemes  
- Adjustable input parameters  
- Downloadable waveform images  
- Simple and clean UI design  

## Technologies Used

- Python  
- Django  
- HTML  
- CSS  
- JavaScript  
- Matplotlib  
- NumPy  

## Installation Guide

Follow these steps to run the project on your local machine:

### Step 1 – Clone Repository



### Step 2 – Create Virtual Environment

```
python -m venv venv
```

### Step 3 – Activate Virtual Environment

Windows:
```
venv\Scripts\activate
```

Linux/Mac:
```
source venv/bin/activate
```

### Step 4 – Install Required Packages

```
pip install django matplotlib numpy
```

### Step 5 – Run the Application

```
python manage.py runserver
```

### Step 6 – Open in Browser

```
http://127.0.0.1:8000/
```

## How the System Works

1. User selects modulation type and enters required parameters.  
2. System generates a random digital message signal.  
3. Selected modulation algorithm is applied.  
4. Input signal and modulated signal are plotted.  
5. User can download both signal images from the interface.  

## Input Parameters

The application allows customization of:

- Sample rate  
- Duration  
- Carrier frequency  
- Number of bits  
- Modulation type  

## Project Structure

```
modulation_project/
│
├── analyzer/
│   ├── templates/
│   │   └── analyzer.html
│   ├── static/
│   │   └── analyzer/style.css
│   ├── views.py
│   ├── forms.py
│   ├── utils.py
│   └── urls.py
│
├── modulation_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

## Future Improvements

- Add demodulation functionality  
- Implement noise channel simulation  
- Bit Error Rate calculation  
- PDF report generation  
- More advanced modulation schemes  

## Author

Shafi Yamin  
Communication Systems Project  

## License

This project is developed for academic and learning purposes and is free to use and modify.
