import matplotlib.pyplot as plt
import numpy as np
from modules import *
import scene_constrains as sc
import random
import utility_functions as uf

scene = Scene(main_dur=60)
allocator = Allocator(server_shared_path='../shared', sr=44100,
                    client_shared_path='cazzo')
post = Postprocessing()

#constrains = only_available
'''
    def build(self, length, density, score_diversity, sel_diversity, single_model=False,
              fixed_category='rand', fixed_model='rand', fast=True, carpet=False,
              perc_particles=0, enhance_random=False, complete_random=False,
              global_rev=False, global_stretch_dir=0, global_stretch=0.6,
              global_shift_dir=0, global_shift=0.7, verbose=False):
'''
scene.gen_macro()
build = BuildScene()
mix = build.build(length=0.9,
                  density=0.1,
                  score_diversity=0.4,
                  sel_diversity=0.5,
                  single_model=False,
                  fixed_category='none',
                  fixed_model='none',
                  fast=False,
                  carpet=False,
                  perc_particles=0,
                  enhance_random=False,
                  complete_random=False,
                  globsl_rev=False,
                  global_stretch_dir=0,
                  global_stretch=1,
                  global_shift_dir=0,
                  global_shift=0,
                  verbose=False)

allocator.write_local(mix, 'coglione')
scene.plot_score(dimensions=3)
