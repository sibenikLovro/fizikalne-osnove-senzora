import matplotlib.pyplot as plt
import numpy as np

# Data
angles = np.arange(0, 181, 1)
intensities = [
919,918,912,907,899,897,895,893,890,899,
886,885,882,876,872,869,864,860,854,849,
845,841,836,828,822,815,809,800,792,785,
779,770,761,753,744,737,729,720,711,703,
689,685,682,669,648,636,618,604,594,585,
578,565,551,538,523,516,503,488,473,462,
450,433,418,400,391,380,367,352,333,322,
305,288,272,255,238,223,200,186,167,142,
119,110,102,94,85,70,62,56,47,32,
30,32,36,41,44,70,81,93,109,117,
132,145,168,183,222,245,262,279,298,318,
327,334,350,363,380,396,411,429,438,450,
461,470,485,497,516,528,541,555,565,578,
592,603,614,625,636,646,656,671,679,689,
702,718,729,733,737,751,762,773,779,789,
792,800,808,815,821,827,835,841,845,850,
856,862,866,869,872,875,881,884,886,888,
890,893,895,896,896,897,899,900,901,903,906
]

# Smooth interpolation
angles_smooth = np.linspace(0, 180, 2000)
intensities_interp = np.interp(angles_smooth, angles, intensities)

# Malus curve
I0 = max(intensities)
malus_curve = I0 * (np.cos(np.radians(angles_smooth))**2)

# Comparison plot
plt.figure(figsize=(12,6))
plt.plot(angles_smooth, intensities_interp, label="Izmjereni podaci", linewidth=2)
plt.plot(angles_smooth, malus_curve, 'r--', linewidth=2, label="Malusova krivulja")
plt.title("Usporedba izmjerenog intenziteta i Malusovog zakona")
plt.xlabel("Kut zakreta polarizatora(°)")
plt.ylabel("Intenzitet (A.U.)")
plt.xticks([0, 30, 60, 90, 120, 150, 180])
plt.grid(True)
plt.legend()
plt.show()

# Fourier transform
ft = np.fft.fft(intensities_interp)
freq = np.fft.fftfreq(len(angles_smooth), d=(angles_smooth[1]-angles_smooth[0]))

# Only positive frequencies
pos_mask = freq >= 0
freq_pos = freq[pos_mask]
ft_mag = np.abs(ft[pos_mask])

# Frequency range limit
freq_mask = (freq_pos >= 0) & (freq_pos <= 0.5)
freq_plot = freq_pos[freq_mask]
ft_mag_plot = ft_mag[freq_mask]

# Fourier spectrum plot
plt.figure(figsize=(12,6))
plt.plot(freq_plot, ft_mag_plot, 'b', linewidth=2)
plt.title("Fourier-transformirana krivulja")
plt.xlabel("Frekvencija (1/°)")
plt.ylabel("Amplituda(A.U.)")
plt.grid(True)
plt.show()
