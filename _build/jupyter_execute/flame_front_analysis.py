#!/usr/bin/env python
# coding: utf-8

# # Flame front analysis

# # Statistics
# 
# The goal of this notebook is to obtain the statistics regarding the flame front.
# Filippo already reported the velocity fluctuations.
# 
# ## Velocity fluctuations
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

# ## Distribution of flame front contours
# 
# ```{list-table} PDFs of flame front contours of flame 1 and 2 (top: 20 images, bottom: 5000 images).
# :header-rows: 1
# :name: tab_flames_pdf_front
# 
# * - ![flame_1_pdf_front](./images/flame_1_pdf_front_20.png)
#   - ![flame_2_pdf_front](./images/flame_2_pdf_front_20.png)
# 
# * - ![flame_1_pdf_front](./images/flame_1_pdf_front_5000.png)
#   - ![flame_2_pdf_front](./images/flame_2_pdf_front_5000.png)
# ```
# 
# test
# 
# ````{panels}
# :container: container-fluid 
# :column: col-xl col-xl col-xl
# :card: shadow-none border-0
# 
# ```{figure} ./images/flame_1_pdf_front_5000.png
# :width: 200%
# :name: example1
# 
# Sub-caption 1
# ```
# 
# ---
# 
# ```{figure} ./images/flame_2_pdf_front_5000.png
# :width: 100%
# :name: example2
# 
# Sub-caption 2
# ```
# 
# ````
