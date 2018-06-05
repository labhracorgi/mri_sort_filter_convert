# Repository name: "mri_sort_filter_convert"

## Purpose:
To document the process of sorting, filtering and converting files.
This repository's contribution is such that it provides a filter for removing data deemed unnecessary to convert to NIFTI as that process in itself is time consuming. Especially on projects that have a horde of scans from patients.

## How to run successfully:
The steps:
- 1: Use "dicomsort.py" (from: https://github.com/pieper/dicomsort) on the raw and extracted MR data. Modifications may be necessary; just look to for instance our "dicomsort_safemod.py".
- 2: Use "filter.py" on the sorted data. (Remember to specify the correct paths.)
- 3: Use a DICOM to NIFTI converter. (DCM2NIIX from: http://neuro.debian.net/pkgs/dcm2niix.html)

As of now, the series that are kept after the filtration algorithm is run are:
- T1
- T2 FLAIR
- SWI
- TOF

### Tested with the following software:
- Debian 9
- Python 2.7.X

## Regarding reusability:
The algorithms may as well only be applicable to (our) TOS7 MR data, as it is tested on these data. This narrow applicability is due to unique or local scanner naming convention paired with the "dicomsort.py" algorithm; which further changes the name of folders.

Finally, the data should be sorted similarly to BIDS (http://bids.neuroimaging.io/) with a structure as:
".../study/subject_ID/series_X/*.dcm"

Or more specifcally the "dicomsort.py" pattern used in our case:
"Destination/%PatientName/%SeriesNumber-%SeriesDescription/%InstanceNumber.dcm"

If the files are structured as illustrated then "filter.py" should be usable if also the identification "keys" are renamed to match the local naming convention.

## The "other" functions:
- "rename_wrong_series_dir.py": Handles duplicate series within an ID from "filter.py" left unique numbered strings as a way of differentiating them. A pre-nifit-convert correction of names by removing the last two characters in the string is thus provided. 
- "copy_from_to.py": Assists in creating a copy & working directory of original/back-up copy.
- "read_ids_to_txt.py": Reads the folder IDs (e.g. per BIDS style) such that they can be used more easily for future comparison. 
- "extract_dicom.py": Is a pydicom (https://github.com/pydicom/pydicom) based script to retrieve the DICOM files' meta information for further verification and correction checks.
- "PID_controll.R": Is simply a script that is supposed to verify Norwegian personal security numbers.
- "ubo_cns_copyfier_workspace.py": Is a function similar to "copy_from_to.py" and also assumes BIDS, but this is designed such that it creates a workspace as required by a WMH segmentation algorithm, named UBO (https://cheba.unsw.edu.au/content/quick-start-manual and https://doi.org/10.1016/j.neuroimage.2018.03.050).

All these other functions may be necessary to use depending on how much of the data is manually entered. Such data entries are obviously more prone to errors and are often required to be validated somehow.

## Issues:
There has been spotted multiple reports of duplicates. After investigating the issue we concluded that the "dicomsort.py" algorithm can produce false positives; which in the end was traced back to erroneous labeling of DICOM IDs. As such it is recommended to verify the amount and the IDs of the sorted images.
A possible workaround is to use the "-k" flag when calling "dicomsort.py" from the shell.
The "-v" flag can also be used to easily create log files when piping in BaSh.

