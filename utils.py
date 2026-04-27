import numpy as np
import pydicom

# loading CT and converting to real HU values
def load_ct_series(path):
    ds = pydicom.dcmread(path)

    # raw pixel data
    ct_data = ds.pixel_array.astype(np.int16)

    # getting conversion factors from DICOM metadata
    intercept = ds.RescaleIntercept if "RescaleIntercept" in ds else -1024
    slope = ds.RescaleSlope if "RescaleSlope" in ds else 1

    # converting to Hounsfield Units (actual medical values)
    ct_data = ct_data * slope + intercept

    return ct_data


def integrated_risk_score(exposure_score, lung_density, low_density_ratio):
    # combines exposure + lung condition into one score

    exposure_component = exposure_score * 0.5
    density_component = lung_density * 200
    structure_component = low_density_ratio * 300

    final_score = exposure_component + density_component + structure_component

    return final_score