"""
Interpolate bad channels in epoched MEG/EEG data.

This app loads epoched MNE data and interpolates channels marked as bad
in the data's info structure.

Inputs
------
epo : str
    Path to the input MNE epochs .fif file.

Outputs
-------
out_dir/epo.fif : str
    Epochs file with bad channels interpolated.
"""

# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

import mne

from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    require_config_keys,
)

# Setup environment
setup_matplotlib_backend()
config = load_config()
require_config_keys(config, ['epo'])

ensure_output_dirs('out_dir')

# == LOAD DATA ==
fname = config['epo']
epochs = mne.read_epochs(fname)

n_bads = len(epochs.info['bads'])
bads = list(epochs.info['bads'])

# == INTERPOLATE BAD CHANNELS ==
epochs.interpolate_bads()

# == SAVE PROCESSED EPOCHS ==
epochs.save(os.path.join('out_dir', 'meg-epo.fif'))

# == CREATE PRODUCT.JSON ==
product_items = []
if n_bads:
    add_info_to_product(product_items, f"Interpolated {n_bads} bad channel(s): {', '.join(bads)}", 'success')
else:
    add_info_to_product(product_items, "No bad channels were marked; nothing to interpolate", 'info')
create_product_json(product_items)
