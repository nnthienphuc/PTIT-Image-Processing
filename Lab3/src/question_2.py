from scipy.io import loadmat
import matplotlib.pyplot as plt

data = loadmat('dataset/colorMatchingFunction.mat')
xyz_cmf = data['CMFs']  # Color matching functions from the file

# Extract X, Y, Z values for each wavelength
wavelength = xyz_cmf[:, 0]
X = xyz_cmf[:, 1]
Y = xyz_cmf[:, 2]
Z = xyz_cmf[:, 3]

# Plot the tritimulus values against wavelength
plt.figure(figsize=(10, 6))
plt.plot(wavelength, X, label="X (λ)", color="red", linewidth=4)
plt.plot(wavelength, Y, label="Y (λ)", color="lightGreen", linewidth=4)
plt.plot(wavelength, Z, label="Z (λ)", color="blue", linewidth=4)

# Add labels and title
plt.title('Tristimulus Values (X, Y, Z) vs Wavelength')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Tristimulus Values')
plt.grid(True)
plt.legend(loc="upper right")

# Show the plot
plt.show()

plt.savefig("result/question2_result.png")