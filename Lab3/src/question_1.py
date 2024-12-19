import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

# Load XYZ color matching functions from 'visibleSpectrum.mat'
data = loadmat('dataset/visibleSpectrum.mat')
xyz_cmf = data['CMFs']  # Color matching functions from the file

# Extract X, Y, Z values for each wavelength
wavelength = xyz_cmf[:, 0]
X = xyz_cmf[:, 1]
Y = xyz_cmf[:, 2]
Z = xyz_cmf[:, 3]

# Stack them into a matrix
XYZ = np.vstack([X, Y, Z]).T

# Normalize XYZ to avoid negative RGB values after transformation
XYZ = XYZ / np.max(XYZ)  # Ensure values are in [0, 1]

# Transformation matrix from XYZ to RGB (sRGB D65)
xyz2rgb = np.array([[3.2406, -1.5372, -0.4986],
                    [-0.9689, 1.8758, 0.0415],
                    [0.0557, -0.2040, 1.0570]])

# Apply the XYZ to RGB transformation
RGB = np.dot(XYZ, xyz2rgb)

# Ensure all values are within [0, 1] range by clipping
RGB = np.clip(RGB, 0, 1)

# Plot the visible spectrum
plt.figure(figsize=(10, 2))
for i, wavelength_value in enumerate(wavelength):
    plt.plot([wavelength_value, wavelength_value], [0, 1], color=RGB[i], linewidth=4)

plt.title('Visible Spectrum (380nm to 760nm)')
plt.xlabel('Wavelength (nm)')
plt.xticks(np.arange(380, 781, 40))
plt.yticks([])
plt.show()

plt.savefig("result/question1_result.png")