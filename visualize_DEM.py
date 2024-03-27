import rasterio
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
file_path ='datasets/cotton_data/demdata/1__0.tif'

with rasterio.open(file_path) as src:
    topography_data = src.read(1)  # Read the first band

plt.imshow(topography_data, cmap='terrain') #show images
plt.colorbar(label='Elevation')
plt.title('Topographical Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

no_data_value = src.nodatavals[0]  # Get the no-data value for the first band
topography_data_masked = np.ma.masked_where(topography_data == no_data_value, topography_data)

plt.imshow(topography_data_masked, cmap='terrain')
plt.colorbar(label='Elevation')
#plt.title('Topographical Data (No-Data Values Masked)')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

y, x = np.mgrid[0:topography_data.shape[0], 0:topography_data.shape[1]]
no_data_value = src.nodatavals[0]  # Get the no-data value for the first band
topography_data_masked = np.ma.masked_where(topography_data == no_data_value, topography_data)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(x, y, topography_data_masked, cmap='terrain', rstride=1, cstride=1, linewidth=0, antialiased=False)
ax.set_title('Topographical 3D Surface Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Elevation')
fig.colorbar(surface, label='Elevation', shrink=0.5, aspect=10)
plt.show()
no_data_mask = topography_data == no_data_value
plt.imshow(no_data_mask, cmap='terrain')
plt.colorbar(label='Elevation')
plt.title('Digital Elevation Model')
plt.show()