#!/usr/bin/env python 

import ROOT
from ROOT import ExtEvent, DelphesEvent 
from ROOT import TChain, MixingSelector,  vector
from ROOT import TH1

from amva4np.samples.oxford_summer_2016 import delphes

max_events = 10000

TH1.AddDirectory(False)


sub_strs = ['QCD_pp_bbbb_13TeV']
mc_names = delphes.keys()
mc_names=[n for n in mc_names if any(s in n for s in sub_strs)]


o_dir = "./mixing/" 
p_par = "ofle={}.root;pName={}"

for name in mc_names:
    selector = MixingSelector(ExtEvent(DelphesEvent))(0)
    tchain = TChain("Delphes")
    for f in delphes[name]["files"]:
      print f
      tchain.Add(f)
    print "processing {} sample".format(name)
    if max_events > 0:
        tchain.Process(selector, p_par.format(o_dir+name, name), max_events)
    else:
        tchain.Process(selector, p_par.format(o_dir+name, name))
