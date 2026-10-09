# Interpolate Bad Channels in Epoched MEG/EEG Data

[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.741-blue.svg)](https://doi.org/10.25663/brainlife.app.741)

## Description

Interpolates bad channels in epoched MNE MEG/EEG data using `epochs.interpolate_bads()` (`mne.Epochs.interpolate_bads`). Channels already marked as bad in the input epochs' `info['bads']` are spatially interpolated using the available method for their channel type (e.g. spherical spline for EEG), enabling their recovery for downstream analysis.

The app generates:
- Epoched data with bad channels interpolated
- A `product.json` summary reporting which channels, if any, were interpolated

## Inputs

- **`epo`** (`neuro/meeg/mne/epochs`): epoched MEG/EEG data (`meg-epo.fif`) containing the channel(s) marked bad to interpolate (required)

## Outputs

- **`out_dir/meg-epo.fif`** (`neuro/meeg/mne/epochs`): the input epochs, with bad channels interpolated
- **`product.json`**: summary of the interpolation, reporting the number and names of channels interpolated (or that none were marked bad)

## Configuration Parameters

This app reads no configuration parameters beyond its input file (see Inputs above).

## Usage

### Running on Brainlife.io

1. Select an epoched MEG/EEG dataset (`mne.Epochs`) with bad channels marked in `info['bads']` as the `epo` input.
2. Submit the task.
3. Review the interpolation summary in `product.json` and the resulting `out_dir/meg-epo.fif`.

### Local Testing

```bash
git clone <this-repo>
cd interpolate
# edit config.json with the path to your own epoched .fif file
./main
```

## Authors
- Guiomar Niso (https://github.com/guiomar)
- Kamilya Salibayeva (https://github.com/KSalibay)

## Citations

We kindly ask that you cite the following articles when publishing papers and code using this app:

Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2

Gramfort, A. et al. MEG and EEG data analysis with MNE-Python. Front. Neurosci. 7, 267 (2013). https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement

brainlife.io is publicly funded and for the sustainability of the project we kindly ask that you acknowledge the following funding sources:

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

## License

Copyright (c) 2026 MEEG Brainlife team. Licensed under AGPL-3.0, see [license.txt](license.txt).
