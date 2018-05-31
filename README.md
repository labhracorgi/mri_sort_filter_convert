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

### Run with:
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
Handling of duplicate series within an ID from "filter.py" left unique numbered strings as a way of differentiating them. A pre-nifit-convert correction of names by removing the last two characters in the string is thus provided. The two remaining functions are simply there to assist with creating a "working directory" and to compare IDs in folder more efficiently.

## Issues:
There has been spotted multiple reports of duplicates. After investigating the issue we concluded that the "dicomsort.py" algorithm can produce false positives; which in the end was traced back to erroneous labeling of DICOM IDs. As such it is recommended to verify the amount and the IDs of the sorted images.
A possible workaround is to use the "-k" flag when calling "dicomsort.py" from the shell.
The "-v" flag can also be used to easily create log files when piping in BaSh.

