# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""

Pre-processing PET - dynamic PET signal workflows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: petprep.workflows.bold.base
.. automodule:: petprep.workflows.bold.hmc
.. automodule:: petprep.workflows.bold.registration
.. automodule:: petprep.workflows.bold.resampling
.. automodule:: petprep.workflows.bold.confounds


"""

from .base import init_pet_preproc_wf
from .hmc import init_pet_hmc_wf
from .registration import (
    init_pet_t1_trans_wf,
    init_pet_reg_wf,
)
from .resampling import (
    init_pet_std_trans_wf,
    init_pet_surf_wf,
    init_pet_preproc_trans_wf,
)

from .confounds import (
    init_pet_confs_wf
)

__all__ = [
    'init_pet_confs_wf',
    'init_pet_hmc_wf',
    'init_pet_std_trans_wf',
    'init_pet_preproc_trans_wf',
    'init_pet_reg_wf',
    'init_pet_surf_wf',
    'init_pet_t1_trans_wf',
    'init_pet_preproc_wf'
]
