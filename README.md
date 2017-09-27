# Repository name: "mri_sort_filter_convert"

## Purpose:
To document the process of sorting, filtering and converting files.
This repository's contribution is such that it provides a filter for removing data deemed unnecessary to convert to NIFTI as that process in itself is time consuming. Especially on projects that have a horde of scans from patients.

## How to run successfully:
The steps:
- 1: Use "dicom_sort.py" (from: https://github.com/pieper/dicomsort) on the raw and extracted MR data.
- 2: Use "filter.py" on the sorted data.
  -- Remember to specify the correct paths.
- 3: Use a DICOM to NIFTI converter.

As of now, the series that are kept after the filtration algorithm is run are:
- T1
- T2 FLAIR
- SWI
- TOF

## Regarding reusability:
The algorithms may as well only be applicable to (our) TOS7 MR data, as it is tested on these data. This narrow applicability is due to unique or local scanner naming convention paired with the "dicom_sort.py" algorithm; which further changes the name of folders.

Finally, the data should be sorted similarly to BIDS (http://bids.neuroimaging.io/) with a structure as:
".../study/subject_ID/series_X/*.dcm"

If the files are structured as illustrated, then it this "filter.py" should be usable if the identification "keys" are renamed to match the local naming convention.


