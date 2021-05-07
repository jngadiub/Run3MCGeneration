# Run3MCGeneration

Instruction to generate signal GEN-SIM-RAW samples for Run3Winter20DRPremixMiniAOD campaign.

## General setup

```
cmsRel CMSSW_11_0_0_patch1
cd CMSSW_11_0_0_patch1/src
mkdir Configuration
mkdir Configuration/GenProduction
mkdir Configuration/GenProduction/python
source /cvmfs/cms.cern.ch/crab3/crab.sh
voms-proxy-init -voms cms --valid 168:0
```

### VBF_HToInvisible

CmsDriver sequence from https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20wmLHEGS-00004&page=0&shown=1099512152191 (GEN-SIM step) and https://cms-pdmv.cern.ch/mcm/requests?prepid=TSG-Run3Winter20DRPremixMiniAOD-00074&page=0&shown=1099527880831 (DIGI-RAW step)

```
curl https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/TSG-Run3Winter20wmLHEGS-00004/0 -o Configuration/GenProduction/python/TSG-Run3Winter20wmLHEGS-00004-fragment.py
scram b -j 8
```

