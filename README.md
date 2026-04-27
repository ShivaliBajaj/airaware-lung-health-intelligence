# AirAware — Lung Health Intelligence System

## Overview

AirAware is a medical AI system that connects **lung CT imaging** with **environmental exposure data** to estimate overall lung health risk in a unified and interpretable way.

It is designed to go beyond isolated prediction models by combining:
- internal lung structure (CT scans)
- external exposure factors (air pollution + lifestyle)

---

## Problem

Most healthcare ML systems work in silos:
- environmental models predict pollution risk
- imaging models detect lung abnormalities

But real lung health is shaped by both.

AirAware is built to bridge this gap.

---

## Approach

### 1. CT Imaging Pipeline
- DICOM CT scan loading
- Hounsfield Unit (HU) correction
- Lung segmentation using thresholding + morphology
- Feature extraction:
  - lung density
  - low-density region ratio

---

### 2. Exposure Modeling
- Synthetic dataset (AQI, smoking, activity)
- Feature engineering into a single **Exposure Score**
- Regression model to estimate exposure risk

---

### 3. Fusion Engine
A custom integration function combines:
- imaging-derived lung features
- exposure score

Output:
> Unified Lung Health Risk Score

---

## Tech Stack

Python · NumPy · Pandas · Scikit-learn · Matplotlib  
pydicom · Image Processing (Morphology, Thresholding) · Jupyter

---

## Project Structure

medical_imaging/   → CT processing + segmentation
notebooks/         → Experiments + pipeline
figures/           → Outputs & visualizations
utils.py           → Core logic + integration

---

## Key Highlights

- Real CT scan (DICOM) processing pipeline
- Medical imaging + ML fusion system
- Interpretable risk scoring (not black-box only)
- Modular architecture (clean separation of concerns)
- End-to-end healthcare intelligence design

---

## Limitations

- Exposure data is synthetic (used for modeling structure)
- Segmentation is classical (not deep learning-based)
- No clinical validation yet

These are intentional constraints for this version.

---

## Future Scope

AirAware is being designed as a foundation system.

Next steps:
- Deep learning-based lung segmentation (U-Net)
- Real-world longitudinal exposure datasets
- Temporal tracking of lung health changes
- Stronger multimodal fusion models
- Clinical validation pipeline exploration

Goal: move towards a **personalized lung health intelligence framework**.

---

## Note

This project focuses on building **interpretable medical intelligence systems**, not just predictive models.

It sits at the intersection of:
- medical imaging
- environmental health
- machine learning