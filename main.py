from sklearn.datasets import load_digits
import pandas as pd
import matplotlib.pyplot as plt

digits = load_digits()
print(digits.data.shape)
print(digits.feature_names)
mx = 0
for i in digits.data:
    if max(i) and max(i) > mx:
        mx = max(i)

print(mx)
for i in range(3):
    plt.imshow(digits.images[i], cmap="gray")
    plt.show()
