#
# mediapipe ds ChRIS plugin app
#
# (c) 2022 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp
# from distutils.dir_util import copy_tree
# import cv2
import mediapipe as mp
import urllib.request
import numpy as np
import pickle
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation
import PyQt5
from PIL import Image
from IPython.display import Video
# import nb_helpers

# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# mp_holistic = mp.solutions.holistic
# mp_pose = mp.solutions.pose
# mp_face_mesh = mp.solutions.face_mesh


Gstr_title = """
                    _ _             _            
                   | (_)           (_)           
 _ __ ___   ___  __| |_  __ _ _ __  _ _ __   ___ 
| '_ ` _ \ / _ \/ _` | |/ _` | '_ \| | '_ \ / _ \
| | | | | |  __/ (_| | | (_| | |_) | | |_) |  __/
|_| |_| |_|\___|\__,_|_|\__,_| .__/|_| .__/ \___|
                             | |     | |         
                             |_|     |_|         
"""

Gstr_synopsis = """


    NAME

       mediapipe

    SYNOPSIS

        docker run --rm fnndsc/pl-mediapipe mediapipe                     \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-mediapipe mediapipe                        \
                /incoming /outgoing

    DESCRIPTION

        `mediapipe` ...

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 
"""


class Mediapipe(ChrisApp):
    """
    An app to track brain scans with most movement
    """
    PACKAGE                 = __package__
    TITLE                   = 'A ChRIS plugin for mediapipe'
    CATEGORY                = ''
    TYPE                    = 'ds'
    ICON                    = ''   # url of an icon image
    MIN_NUMBER_OF_WORKERS   = 1    # Override with the minimum number of workers as int
    MAX_NUMBER_OF_WORKERS   = 1    # Override with the maximum number of workers as int
    MIN_CPU_LIMIT           = 2000 # Override with millicore value as int (1000 millicores == 1 CPU core)
    MIN_MEMORY_LIMIT        = 8000  # Override with memory MegaByte (MB) limit as int
    MIN_GPU_LIMIT           = 0    # Override with the minimum number of GPUs as int
    MAX_GPU_LIMIT           = 0    # Override with the maximum number of GPUs as int

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
    #    print("copying %s to %s" %(options.inputdir, options.outputdir))
    #    copy_tree(options.inputdir, options.outputdir)

        # face_url = "/home/olakra/pl-mediapipe/in/0004-1.3.12.2.1107.5.2.19.45152.2013030808110256555586033.jpeg"
        # urllib.request.urlretrieve(face_url, "brain_image.jpeg")

        im = Image.open('in/pexels-pixabay-462118.jpg')
        im.show()


    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
