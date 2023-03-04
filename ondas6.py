import tkinter as tk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class WaveformGenerator:
    def __init__(self):
        self.lines = []
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        self.var_amp = tk.StringVar()
        self.var_amp.set("1.0")
        self.var_freq = tk.StringVar()
        self.var_freq.set("1.0")
        self.var_type = tk.StringVar()
        self.var_type.set("sine")

        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.toolbar = tk.Frame(master=root)
        self.toolbar.pack(side=tk.BOTTOM)

        self.btn_generate = tk.Button(master=self.toolbar, text="Generate Waveform", command=self.draw_waveform)
        self.btn_generate.pack(side=tk.LEFT)

        self.lbl_amp = tk.Label(master=self.toolbar, text="Amplitude:")
        self.lbl_amp.pack(side=tk.LEFT)
        self.entry_amp = tk.Entry(master=self.toolbar, textvariable=self.var_amp)
        self.entry_amp.pack(side=tk.LEFT)

        self.lbl_freq = tk.Label(master=self.toolbar, text="Frequency:")
        self.lbl_freq.pack(side=tk.LEFT)
        self.entry_freq = tk.Entry(master=self.toolbar, textvariable=self.var_freq)
        self.entry_freq.pack(side=tk.LEFT)

        self.radio_sine = tk.Radiobutton(master=self.toolbar, text="Sine", variable=self.var_type, value="sine")
        self.radio_sine.pack(side=tk.LEFT)
        self.radio_square = tk.Radiobutton(master=self.toolbar, text="Square", variable=self.var_type, value="square")
        self.radio_square.pack(side=tk.LEFT)
        self.radio_combined = tk.Radiobutton(master=self.toolbar, text="Combined", variable=self.var_type, value="combined")
        self.radio_combined.pack(side=tk.LEFT)

    def get_sine_waveform(self):
        amp = float(self.var_amp.get())
        freq = float(self.var_freq.get())
        waveform = amp * np.sin(2 * np.pi * freq * np.linspace(0, 1, 500))
        return waveform

    def get_square_waveform(self):
        amp = float(self.var_amp.get())
        freq = float(self.var_freq.get())
        waveform = amp * np.sign(np.sin(2 * np.pi * freq * np.linspace(0, 1, 500)))
        return waveform

    def get_combined_waveform(self):
        waveform1 = self.get_sine_waveform()
        waveform2 = self.get_square_waveform()
        return waveform1 + waveform2

    def draw_waveform(self):
        waveform_type = self.var_type.get()
        if waveform_type == "sine":
            waveform = self.get_sine_waveform()
        elif waveform_type == "square":
            waveform = self.get_square_waveform()
        elif waveform_type == "combined":
            waveform = self.get_combined_waveform()

        line, = self.ax.plot(waveform)
        self.lines.append(line)
        self.canvas.draw()

root = tk.Tk()
root.title("Waveform Generator")
app = WaveformGenerator()
root.mainloop()
