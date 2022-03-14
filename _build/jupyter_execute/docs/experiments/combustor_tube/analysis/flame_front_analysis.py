#!/usr/bin/env python
# coding: utf-8

# # Flame front analysis

# ## Statistics
# 
# The goal of this notebook is to obtain the statistics regarding the flame front.
# Filippo already reported the velocity fluctuations.
# 
# ### Velocity fluctuations
# 
# This part focuses on flame 1 and flame 2 of paper 1. Data is stored under Project Data (U:): **U:\High hydrogen\ffaldella\data**
# 
# ```{list-table} Specifications of flame 1 and 2.
# :header-rows: 1
# :name: tab_flames_info
# 
# * - Flame
#   - $D$ [mm]
#   - $Re_{D}$ [-]
#   - $\phi$ [-] 
#   - $H_2\%$ 
# 
# * - **flame 1**
#   - 25.7
#   - 16139
#   - 0.6
#   - 100
# 
# * - **flame 2**
#   - 25.7
#   - 12005
#   - 0.6 
#   - 100 
# ```
# 
# ```{figure} ./images/flame_1.png
# :width: 100%
# :name: flame_1_vel_fluc
# 
# Normalized mean velocity field $\overline{u}/U_{b}$, Normalized Reynolds normal stress in the axial $\overline{u'u'}/U_{b}^2$ and radial direction $\overline{v'v'}/U_{b}^2$, respectively. The dashed line indicates the average flame front location and is used to determine the flame cone angle.
# ```
# 
# ```{figure} ./images/flame_2.png
# :width: 100%
# :name: flame_2_vel_fluc
# 
# Normalized mean velocity field $\overline{u}/U_{b}$, Normalized Reynolds normal stress in the axial $\overline{u'u'}/U_{b}^2$ and radial direction $\overline{v'v'}/U_{b}^2$, respectively. The dashed line indicates the average flame front location and is used to determine the flame cone angle.
# ```

# ### Distribution of flame front contours
# 
# The flame front of the raw PIV images was detected using a self-made algorithm using Gaussian filters, enhancement of the images and eventually a binarization of the image.
# {numref}`flame_1_frame0_B00004` shows an example.
# 
# ```{figure} ./images/B00004.png
# :width: 100%
# :name: flame_1_frame0_B00004
# 
# Raw PIV image with the flame front contour as determined by the self-made algorithm (red line).
# ```
# 
# {numref}`flame_1_pdf_front_5000` and {numref}`flame_2_pdf_front_5000` show the distribution of the flame front for 5000 images.
# 
# ````{panels}
# :container: container-fluid 
# :column: col-xl-6 col-xl-6
# :card: shadow-none border-0
# 
# ```{figure} ./images/flame_1_pdf_front_5000.png
# :width: 100%
# :name: flame_1_pdf_front_5000
# 
# PDF of flame front contours of flame 1
# ```
# 
# ---
# 
# ```{figure} ./images/flame_2_pdf_front_5000.png
# :width: 100%
# :name: flame_2_pdf_front_5000
# 
# PDF of flame front contours of flame 2
# ```
# 
# ````
# 
# 
