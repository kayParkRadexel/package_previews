# Pros and cons of SimpleITK
# pros : Strong image handling, well organized documentation
# cons : Complicated

import SimpleITK as sitk
import matplotlib.pyplot as plt

filename = "../../dicom_samples/0002.dcm"
images = sitk.ReadImage(filename)

images_list = sitk.GetArrayFromImage(images)

print(len(images_list))
print(images)
plt.imshow(images_list[1], cmap=plt.cm.bone)
plt.show()