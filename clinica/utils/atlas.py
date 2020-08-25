# coding: utf8

"""
This module contains utilities to handle atlases in Clinica.

An atlas is currently defined by its name, a set of labels in a template space and
the map of this template space (e.g. T1w, FA map derived from DWI).

This current implementation has some drawbacks:
- Atlas is misleading: it is only a set of labels in a template space
- This implementation can not handle case where there are several maps (e.g. both T1w and T2w) in template space

Either a refactoring of this module or the use of an external API
(e.g. TemplateFlow - https://www.templateflow.org/) needs to be considered.
"""

import abc


class AtlasAbstract:
    """
    Abstract class for Atlas handling.

    Naming convention for children classes of AtlasAbstract:
    <name_atlas>[<resolution>][<map>]
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_name_atlas(self):
        """
        Returns the name of the atlas (as defined in BIDS/CAPS specifications).
        """
        pass

    def get_spatial_resolution(self):
        """
        Returns the spatial resolution of the atlas (in format "XxXxX" e.g.
        1x1x1 or 1.5x1.5x1.5).
        """
        import nibabel as nib

        img_labels = nib.load(self.get_atlas_labels())
        voxels_labels = img_labels.header.get_zooms()
        # Will display integers without decimals
        if int(voxels_labels[0]) == voxels_labels[0]:
            s_x = str(int(voxels_labels[0]))
        else:
            s_x = str(voxels_labels[0])
        if int(voxels_labels[1]) == voxels_labels[1]:
            s_y = str(int(voxels_labels[1]))
        else:
            s_y = str(voxels_labels[1])
        if int(voxels_labels[2]) == voxels_labels[2]:
            s_z = str(int(voxels_labels[2]))
        else:
            s_z = str(voxels_labels[2])

        return s_x + "x" + s_y + "x" + s_z

    @abc.abstractmethod
    def get_atlas_labels(self):
        """
        Returns the image with the different labels/ROIs.
        """
        pass

    @abc.abstractmethod
    def get_tsv_roi(self):
        """
        Returns the TSV file containing the ROI (regions of interest) of
        the atlas.
        """
        pass

    def get_index(self):
        import nibabel as nib
        import numpy as np
        img_labels = nib.load(self.get_atlas_labels())
        img_labels = img_labels.get_data()
        labels = list(set(img_labels.ravel()))
        index_vector = np.zeros(len(labels))
        for index, n in enumerate(labels):
            index_vector[index] = index
        return index_vector


class JHUDTI812mm(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "JHUDTI81"

    @staticmethod
    def get_atlas_labels():
        import os
        from .check_dependency import check_environment_variable
        fsl_dir = check_environment_variable('FSLDIR', 'FSL')
        return os.path.join(fsl_dir, 'data', 'atlases', 'JHU', 'JHU-ICBM-labels-2mm.nii.gz')

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases', 'JHUDTI81_FS_LUT_newformat.txt')


class JHUDTI811mm(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "JHUDTI81"

    @staticmethod
    def get_atlas_labels():
        import os
        from .check_dependency import check_environment_variable
        fsl_dir = check_environment_variable('FSLDIR', 'FSL')
        return os.path.join(fsl_dir, 'data', 'atlases', 'JHU', 'JHU-ICBM-labels-1mm.nii.gz')

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases', 'JHUDTI81_FS_LUT_newformat.txt')


class JHUTracts01mm(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "JHUTracts0"

    @staticmethod
    def get_atlas_labels():
        import os
        from .check_dependency import check_environment_variable
        fsl_dir = check_environment_variable('FSLDIR', 'FSL')
        return os.path.join(fsl_dir, 'data', 'atlases', 'JHU', 'JHU-ICBM-tracts-maxprob-thr0-1mm.nii.gz')

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases', 'JHUTract_FS_LUT_newformat.txt')


class JHUTracts02mm(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "JHUTracts0"

    @staticmethod
    def get_atlas_labels():
        import os
        from .check_dependency import check_environment_variable
        fsl_dir = check_environment_variable('FSLDIR', 'FSL')
        return os.path.join(fsl_dir, 'data', 'atlases', 'JHU', 'JHU-ICBM-tracts-maxprob-thr0-2mm.nii.gz')

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases', 'JHUTract_FS_LUT_newformat.txt')


class JHUTracts251mm(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "JHUTracts25"

    @staticmethod
    def get_atlas_labels():
        import os
        from .check_dependency import check_environment_variable
        fsl_dir = check_environment_variable('FSLDIR', 'FSL')
        return os.path.join(fsl_dir, 'data', 'atlases', 'JHU', 'JHU-ICBM-tracts-maxprob-thr25-1mm.nii.gz')

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases', 'JHUTract_FS_LUT_newformat.txt')


class JHUTracts252mm(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "JHUTracts25"

    @staticmethod
    def get_atlas_labels():
        import os
        from .check_dependency import check_environment_variable
        fsl_dir = check_environment_variable('FSLDIR', 'FSL')
        return os.path.join(fsl_dir, 'data', 'atlases', 'JHU', 'JHU-ICBM-tracts-maxprob-thr25-2mm.nii.gz')

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases', 'JHUTract_FS_LUT_newformat.txt')


class JHUTracts501mm(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "JHUTracts50"

    @staticmethod
    def get_atlas_labels():
        import os
        from .check_dependency import check_environment_variable
        fsl_dir = check_environment_variable('FSLDIR', 'FSL')
        return os.path.join(fsl_dir, 'data', 'atlases', 'JHU', 'JHU-ICBM-tracts-maxprob-thr50-1mm.nii.gz')

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases', 'JHUTract_FS_LUT_newformat.txt')


class JHUTracts502mm(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "JHUTracts50"

    @staticmethod
    def get_atlas_labels():
        import os
        from .check_dependency import check_environment_variable
        fsl_dir = check_environment_variable('FSLDIR', 'FSL')
        return os.path.join(fsl_dir, 'data', 'atlases', 'JHU', 'JHU-ICBM-tracts-maxprob-thr50-2mm.nii.gz')

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases', 'JHUTract_FS_LUT_newformat.txt')


class AAL2(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "AAL2"

    @staticmethod
    def get_atlas_labels():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases_spm', 'AAL2.nii')

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases_spm', 'lut_AAL2_newformat.txt')


class Hammers(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "Hammers"

    @staticmethod
    def get_atlas_labels():
        from clinica.utils.inputs import RemoteFileStructure, get_file_from_server
        HAMMERS_PARC = RemoteFileStructure(
            filename='atlas-Hammers_dseg.nii.gz',
            url='https://aramislab.paris.inria.fr/files/software/cat12/CAT12-Atlases/',
            checksum='c034a7bce2dcab390a0b72f4e7d04769eb3fe5b990d0e18d89b0ce73339a5376'
        )
        return get_file_from_server(HAMMERS_PARC)

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases_spm', 'lut_Hammers_newformat.txt')


class LPBA40(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "LPBA40"

    @staticmethod
    def get_atlas_labels():
        from clinica.utils.inputs import RemoteFileStructure, get_file_from_server
        LPBA40_PARC = RemoteFileStructure(
            filename='atlas-LPBA40_dseg.nii.gz',
            url='https://aramislab.paris.inria.fr/files/software/cat12/CAT12-Atlases/',
            checksum='20826b572bbbdbcdbf28bbd3801dc0c2fed28d1e54bc4fd5027e64ccc6d50374'
        )
        return get_file_from_server(LPBA40_PARC)

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases_spm', 'lut_LPBA40_newformat.txt')


class AICHA(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "AICHA"

    @staticmethod
    def get_atlas_labels():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases_spm', 'AICHA.nii')

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases_spm', 'lut_AICHA_newformat.txt')


class Neuromorphometrics(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "Neuromorphometrics"

    @staticmethod
    def get_atlas_labels():
        from clinica.utils.inputs import RemoteFileStructure, get_file_from_server
        NEUROMORPHOMETRICS_PARC = RemoteFileStructure(
            filename='atlas-Neuromorphometrics_dseg.nii.gz',
            url='https://aramislab.paris.inria.fr/files/software/cat12/CAT12-Atlases/',
            checksum='19a50136cd2f8a14357a19ad8a1dc4a2ecb6beb3fc16cb5441f4f2ebaf64a9a5'
        )
        return get_file_from_server(NEUROMORPHOMETRICS_PARC)

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases_spm', 'lut_Neuromorphometrics_newformat.txt')


class MCALT_ADIR122(AtlasAbstract):
    def __init__(self):
        AtlasAbstract.__init__(self)

    @staticmethod
    def get_name_atlas(): return "MCALT_ADIR122"

    @staticmethod
    def get_atlas_labels():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases_spm', 'MCALT_ADIR122.nii')

    @staticmethod
    def get_tsv_roi():
        from os.path import join, split, realpath
        return join(split(realpath(__file__))[0], '../resources/atlases_spm', 'MCALT_ADIR122_ROI.tsv')


class AtlasLoader:
    def __init__(self, atlases=None):
        self.atlas = {}
        if atlases:
            for atlas in atlases:
                self.add_atlas(atlas)

    def add_atlas(self, atlas):
        if not isinstance(atlas, AtlasAbstract):
            raise Exception("Atlas element must be an AtlasAbstract type")

    def get_atlases(self): return self.atlas
