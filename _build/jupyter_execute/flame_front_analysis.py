# Flame front analysis

## Read (unzip) packages from Google drive and add them to the correct directory in colab

# !unzip -o "/content/drive/MyDrive/Colab Notebooks/lib/cantera_env.zip" -d "/usr/local/lib/python3.7/site-packages/" &> /dev/null

import sys

!wget https://github.com/luukalt/data_analysis/raw/main/cantera_env.zip &> /dev/null

!unzip -o "/content/cantera_env.zip" -d "/usr/local/lib/python3.7/site-packages/" &> /dev/null

colab_package_dir = "/usr/local/lib/python3.7/site-packages/"

sys.path.append(colab_package_dir)

# Main



## Import packages

import cv2
from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt
import numpy as np
import imutils
import os

## Velocity fluctuations

This part focuses on flame 1 and flame 2 of paper 1. Data is stored under Project Data (U:): **U:\High hydrogen\ffaldella\data**

```{list-table} Specifications of flame 1 and 2
:header-rows: 1
:name: tab_flames_info

* - Flame
  - $D$ [mm]
  - $Re_{D}$ [-]
  - $\phi$ [-] 
  - $H_2\%$ 

* - **flame 1**
  - 25.7
  - 16139
  - 0.6
  - 100

* - **flame 2**
  - 25.7
  - 12005
  - 0.6 
  - 100 
```


The goal of this notebook is to obtain the statistics regarding the flame front.
Filippo already reported the velocity fluctuations.


**Flame 1**<br>
![flame_1](./images/flame_1.png)

**Flame 2**
![flame_2](./images/flame_2.png)

From left to right:  Normalized mean velocity field $\overline{u}/U_{b}$, Normalized Reynolds normal stress in the axial $\overline{u'u'}/U_{b}^2$ and radial direction $\overline{v'v'}/U_{b}^2$, respectively. The dashed line indicates the average flame front location and is used to determine the flame cone angle.


## Statistics: Flame front contours

```{list-table} Specifications of flame 1 and 2
:header-rows: 1
:name: tab_flames_info

* - Flame 1
  - Flame 2

* - ![flame_1_pdf_front](./images/flame_1_pdf_front.png)
  - ![flame_2_pdf_front](./images/flame_2_pdf_front.png)
```{