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

To test it: `cmsRun VBF_HToInvisible_M125_TuneCUETP8M1_14TeV_powheg_pythia8.py`

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20wmLHEGS-00004/0 -o Configuration/GenProduction/python/TSG-Run3Winter20wmLHEGS-00004-fragment.py
scram b -j 8
git clone https://github.com/jngadiub/Run3MCGeneration.git
cd Run3MCGeneration
python make-crab-config.py -s VBF_HToInvisible_M125_TuneCUETP8M1_14TeV_powheg_pythia8 -o {LNFJOBOUTDIR} -N {NJOBS} -E {EVENTSPERJOB}
crab submit -c crab_VBF_HToInvisible_M125_TuneCUETP8M1_14TeV_powheg_pythia8.py
```

### VBF_HH_CV_1_C2V_1_C3_1

cmsDriver sequence in the file `VBF_HH_CV_1_C2V_1_C3_1_TuneCP5_PSweights_14TeV-madgraph-pythia8.py` taken from https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20wmLHEGS-00010&page=0&shown=1099512152191 (GEN-SIM step) and https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20DRPremixMiniAOD-00079&page=0&shown=1099511629951 (DIGI-RAW step)

To test it: `cmsRun VBF_HH_CV_1_C2V_1_C3_1_TuneCP5_PSweights_14TeV-madgraph-pythia8.py`

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20wmLHEGS-00010/0 -o Configuration/GenProduction/python/TSG-Run3Winter20wmLHEGS-00010-fragment.py
scram b -j 8
git clone https://github.com/jngadiub/Run3MCGeneration.git
cd Run3MCGeneration
python make-crab-config.py -s VBF_HH_CV_1_C2V_1_C3_1_TuneCP5_PSweights_14TeV-madgraph-pythia8 -o {LNFJOBOUTDIR} -N {NJOBS} -E {EVENTSPERJOB}
crab submit -c crab_VBF_HH_CV_1_C2V_1_C3_1_TuneCP5_PSweights_14TeV-madgraph-pythia8.py
```

### VectorZPrimeToQQ_M100_pT300

cmsDriver sequence in the file `VectorZPrimeToQQ_M100_pT300_TuneCP5_14TeV_madgraph_pythia8.py` taken from https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20wmLHEGS-00014&page=0&shown=1099512152191 (GEN-SIM step) and https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20DRPremixMiniAOD-00082&page=0&shown=127 (DIGI-RAW step)

To test it: `cmsRun .VectorZPrimeToQQ_M100_pT300_TuneCP5_14TeV_madgraph_pythia8.py`

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20wmLHEGS-00014/0 -o Configuration/GenProduction/python/TSG-Run3Winter20wmLHEGS-00014-fragment.py
scram b -j 8
git clone https://github.com/jngadiub/Run3MCGeneration.git
cd Run3MCGeneration
python make-crab-config.py -s VectorZPrimeToQQ_M100_pT300_TuneCP5_14TeV_madgraph_pythia8 -o {LNFJOBOUTDIR} -N {NJOBS} -E {EVENTSPERJOB}
crab submit -c crab_VectorZPrimeToQQ_M100_pT300_TuneCP5_14TeV_madgraph_pythia8.py
```
