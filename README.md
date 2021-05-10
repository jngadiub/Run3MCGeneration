# Run3MCGeneration

Instruction to generate signal GEN-SIM-RAW samples for Run3Winter20DRPremixMiniAOD campaign.

## General setup

```
cmsRel CMSSW_11_0_0_patch1
cd CMSSW_11_0_0_patch1/src
cmsenv
mkdir Configuration
mkdir Configuration/GenProduction
mkdir Configuration/GenProduction/python
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init -voms cms --valid 168:0
```

The crab config file generated in the steps below runs by default 500 jobs with 1000 events each but can be changed with options `-N {NJOBS} -E {EVENTSPERJOB}`

### VBF_HToInvisible

cmsDriver sequence in the file `VBF_HToInvisible_M125_TuneCUETP8M1_14TeV_powheg_pythia8.py` taken from https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20wmLHEGS-00004&page=0&shown=1099512152191 (GEN-SIM step) and https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20DRPremixMiniAOD-00074&page=0&shown=1099527880831 (DIGI-RAW step)

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20wmLHEGS-00004/0 -o Configuration/GenProduction/python/TSG-Run3Winter20wmLHEGS-00004-fragment.py
scram b -j 8
git clone https://github.com/jngadiub/Run3MCGeneration.git
cd Run3MCGeneration
cmsRun VBF_HToInvisible_M125_TuneCUETP8M1_14TeV_powheg_pythia8.py #test sequence
python make-crab-config.py -s VBF_HToInvisible_M125_TuneCUETP8M1_14TeV_powheg_pythia8 -o {LNFJOBOUTDIR} -N {NJOBS} -E {EVENTSPERJOB}
crab submit -c crab_VBF_HToInvisible_M125_TuneCUETP8M1_14TeV_powheg_pythia8.py
```

### VBF_HH_CV_1_C2V_1_C3_1

cmsDriver sequence in the file `VBF_HH_CV_1_C2V_1_C3_1_TuneCP5_PSweights_14TeV-madgraph-pythia8.py` taken from https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20wmLHEGS-00010&page=0&shown=1099512152191 (GEN-SIM step) and https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20DRPremixMiniAOD-00079&page=0&shown=1099511629951 (DIGI-RAW step)

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20wmLHEGS-00010/0 -o Configuration/GenProduction/python/TSG-Run3Winter20wmLHEGS-00010-fragment.py
scram b -j 8
git clone https://github.com/jngadiub/Run3MCGeneration.git
cd Run3MCGeneration
cmsRun VBF_HH_CV_1_C2V_1_C3_1_TuneCP5_PSweights_14TeV-madgraph-pythia8.py #test sequence
python make-crab-config.py -s VBF_HH_CV_1_C2V_1_C3_1_TuneCP5_PSweights_14TeV-madgraph-pythia8 -o {LNFJOBOUTDIR} -N {NJOBS} -E {EVENTSPERJOB}
crab submit -c crab_VBF_HH_CV_1_C2V_1_C3_1_TuneCP5_PSweights_14TeV-madgraph-pythia8.py
```

### VectorZPrimeToQQ_M100_pT300

cmsDriver sequence in the file `VectorZPrimeToQQ_M100_pT300_TuneCP5_14TeV_madgraph_pythia8.py` taken from https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20wmLHEGS-00014&page=0&shown=1099512152191 (GEN-SIM step) and https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20DRPremixMiniAOD-00082&page=0&shown=127 (DIGI-RAW step)

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20wmLHEGS-00014/0 -o Configuration/GenProduction/python/TSG-Run3Winter20wmLHEGS-00014-fragment.py
scram b -j 8
git clone https://github.com/jngadiub/Run3MCGeneration.git
cd Run3MCGeneration
cmsRun VectorZPrimeToQQ_M100_pT300_TuneCP5_14TeV_madgraph_pythia8.py #test sequence
python make-crab-config.py -s VectorZPrimeToQQ_M100_pT300_TuneCP5_14TeV_madgraph_pythia8 -o {LNFJOBOUTDIR} -N {NJOBS} -E {EVENTSPERJOB}
crab submit -c crab_VectorZPrimeToQQ_M100_pT300_TuneCP5_14TeV_madgraph_pythia8.py
```

### VectorZPrimeToQQ_M200_pT300

cmsDriver sequence in the file `VectorZPrimeToQQ_M200_pT300_TuneCP5_14TeV_madgraph_pythia8.py` taken from https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20wmLHEGS-00015&page=0&shown=1099512152191 (GEN-SIM step) and https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20DRPremixMiniAOD-00083&page=0&shown=127 (DIGI-RAW step)

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20wmLHEGS-00015/0 -o Configuration/GenProduction/python/TSG-Run3Winter20wmLHEGS-00015-fragment.py
scram b -j 8
git clone https://github.com/jngadiub/Run3MCGeneration.git
cd Run3MCGeneration
cmsRun VectorZPrimeToQQ_M200_pT300_TuneCP5_14TeV_madgraph_pythia8.py #test sequence
python make-crab-config.py -s VectorZPrimeToQQ_M200_pT300_TuneCP5_14TeV_madgraph_pythia8 -o {LNFJOBOUTDIR} -N {NJOBS} -E {EVENTSPERJOB}
crab submit -c crab_VectorZPrimeToQQ_M200_pT300_TuneCP5_14TeV_madgraph_pythia8.py
```

### VBFHToTauTau

cmsDriver sequence in the file `VBFHToTauTau_M125_TuneCUETP8M1_14TeV_powheg_pythia8.py` taken from https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20wmLHEGS-00002&page=0&shown=1099512152191 (GEN-SIM step) and https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20DRPremixMiniAOD-00072&page=0&shown=127 (DIGI-RAW step)

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20wmLHEGS-00014/0 -o Configuration/GenProduction/python/TSG-Run3Winter20wmLHEGS-00014-fragment.py
scram b -j 8
git clone https://github.com/jngadiub/Run3MCGeneration.git
cd Run3MCGeneration
cmsRun VBFHToTauTau_M125_TuneCUETP8M1_14TeV_powheg_pythia8.py #test sequence
python make-crab-config.py -s VBFHToTauTau_M125_TuneCUETP8M1_14TeV_powheg_pythia8 -o {LNFJOBOUTDIR} -N {NJOBS} -E {EVENTSPERJOB}
crab submit -c crab_VBFHToTauTau_M125_TuneCUETP8M1_14TeV_powheg_pythia8.py
```

### GluGluToHHTo4B

cmsDriver sequence in the file  `GluGluToHHTo4B_node_SM_TuneCP5_14TeV-madgraph-pythia8.py` take from https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20wmLHEGS-00008&page=0&shown=1099512152191 (GEN-SIM step) and https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20DRPremixMiniAOD-00080&page=0&shown=127 (DIGI-RAW step)

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20wmLHEGS-00008/0 -o Configuration/GenProduction/python/TSG-Run3Winter20wmLHEGS-00008-fragment.pyscram b -j 8
git clone https://github.com/jngadiub/Run3MCGeneration.git
cd Run3MCGeneration
cmsRun GluGluToHHTo4B_node_SM_TuneCP5_14TeV-madgraph-pythia8.py #test sequence
python make-crab-config.py -s GluGluToHHTo4B_node_SM_TuneCP5_14TeV-madgraph-pythia8 -o {LNFJOBOUTDIR} -N {NJOBS} -E {EVENTSPERJOB}
crab submit -c crab_GluGluToHHTo4B_node_SM_TuneCP5_14TeV-madgraph-pythia8.py
```

### ZprimeToZH_MZprime600_MZ50_MH80_ZTouds_HTouds

cmsDriver sequence in the file `ZprimeToZH_MZprime600_MZ50_MH80_ZTouds_HTouds_narrow_TuneCP5_14TeV_madgraph_pythia8.py` taken from https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20wmLHEGS-00019&page=0&shown=1099512152191 (GEN-SIM step) and https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20DRPremixMiniAOD-00084&page=0&shown=127 (DIGI-RAW step)

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20wmLHEGS-00019/0 -o Configuration/GenProduction/python/TSG-Run3Winter20wmLHEGS-00019-fragment.py
git clone https://github.com/jngadiub/Run3MCGeneration.git
cd Run3MCGeneration
cmsRun ZprimeToZH_MZprime600_MZ50_MH80_ZTouds_HTouds_narrow_TuneCP5_14TeV_madgraph_pythia8.py #test sequence
python make-crab-config.py -s ZprimeToZH_MZprime600_MZ50_MH80_ZTouds_HTouds_narrow_TuneCP5_14TeV_madgraph_pythia8 -o {LNFJOBOUTDIR} -N {NJOBS} -E {EVENTSPERJOB}
crab submit -c crab_ZprimeToZH_MZprime600_MZ50_MH80_ZTouds_HTouds_narrow_TuneCP5_14TeV_madgraph_pythia8.py
```

### HTo2LongLivedTo4mu_MH-1000_MFF-450_CTau-10000mm

cmsDriver sequence in the file  `HTo2LongLivedTo4mu_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV_pythia8.py` taken from https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20GS-00035&page=0&shown=1099512154239 (GEN-SIM step) and https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20DRPremixMiniAOD-00052&page=0&shown=127 (DIGI-RAW step)

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20GS-00035/0 -o Configuration/GenProduction/python/TSG-Run3Winter20GS-00035-fragment.py
git clone https://github.com/jngadiub/Run3MCGeneration.git
cd Run3MCGeneration
cmsRun HTo2LongLivedTo4mu_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV_pythia8.py #test sequence
python make-crab-config.py -s HTo2LongLivedTo4mu_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV_pythia8 -o {LNFJOBOUTDIR} -N {NJOBS} -E {EVENTSPERJOB}
crab submit -c crab_HTo2LongLivedTo4mu_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV_pythia8.py
```
