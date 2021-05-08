# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/TSG-Run3Winter20GS-00035-fragment.py --python_filename=HTo2LongLivedTo4mu_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV_pythia8.py --fileout file:HTo2LongLivedTo4mu_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV_pythia8_GENSIMDIGIRAW.root --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 110X_mcRun3_2021_realistic_v6 --beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step GEN,SIM,DIGI,DATAMIX,L1,DIGI2RAW,HLT:GRun --geometry DB:Extended --pileup_input dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/PREMIX --procModifiers premix_stage2 --nThreads 4 --datamix PreMix --era Run3 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3
from Configuration.ProcessModifiers.premix_stage2_cff import premix_stage2

process = cms.Process('HLT',Run3,premix_stage2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRun3RoundOptics25ns13TeVLowSigmaZ_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.DigiDM_cff')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
    FailPath = cms.untracked.vstring(),
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    SkipEvent = cms.untracked.vstring(),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(

        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(1)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    makeTriggerResults = cms.obsolete.untracked.bool,
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(1),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/TSG-Run3Winter20GS-00035-fragment.py nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXRAWoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:HTo2LongLivedTo4mu_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV_pythia8_GENSIMDIGIRAW.root'),
    outputCommands = process.PREMIXRAWEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.XMLFromDBSource.label = cms.string("Extended")
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mixData.input.fileNames = cms.untracked.vstring(['/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/40000/2484B3E7-252D-AB40-A900-DDCF83A78DFB.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/40000/7E5D2DEF-D325-4549-AB4A-2E256E2C60B6.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/40001/AA01099C-E100-D848-ABB4-6D0324D6DF1F.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/40000/E3B74C94-84DF-5941-8C01-3DE7B920146D.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/40007/CD9241ED-6FFC-4149-9544-27C100235DDC.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/40008/BDDA34B9-4643-3543-87BF-B14AA863CE8D.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/40000/799FCD7A-E63B-AC40-967C-D83E3E454329.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/40008/AB54F3EE-D4DA-1947-8941-5AD38044A503.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230000/A50ADD8C-44C2-9342-B9A0-B9DFA029D588.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230000/25E536EB-DB8D-2741-8339-66B38BF55E2C.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230001/FD8317A0-6A0B-7642-857A-A9FF7241345B.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230002/B234D62B-D380-334E-AA23-D4C622059271.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230005/BA01A08A-FD1B-C042-AD44-6FABEEE62734.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230006/E092D06C-0460-FD48-A132-A7979823A23C.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230007/5AD443EE-C9FB-E54D-8A6F-FF1E2234103E.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230000/7E46FD48-EB0B-D942-822D-A365A81B1610.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230000/46266175-8B69-A24F-BA7F-2A6C426924B7.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230001/EC8111B6-4650-6B4C-A2FC-1154C2559A8A.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230001/FBF93C25-4DBE-954B-93EE-B5B42B793B5F.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230001/781E7A81-F752-4940-A97C-C916B629C545.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230003/E4A98B16-1E4B-D34B-8ACB-AEFD255F51C5.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230004/4C011FD0-EDCD-534A-A710-B54555664259.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230005/212AD5E5-28B8-ED44-B4B5-0194D04CC1A1.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230005/72BF3439-741A-854D-BC5C-F2304DE557AF.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230005/2DC9607F-068F-3845-86C0-609E37C4E19B.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/230006/D2471FD3-838D-D14C-93B6-35A0D0F76E14.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/240000/D39F1516-81B2-0145-B5AD-68A85F03EBD8.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/240003/F580B330-A5A3-6D4E-B3BB-F532ACDEE007.root', '/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/PREMIX/PURun3Winter20_110X_mcRun3_2021_realistic_v6-v1/240014/611F14E2-71AE-DE41-A5B2-268225AADC33.root'])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '110X_mcRun3_2021_realistic_v6', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'pythia8CP5Settings', 
            'pythia8PSweightsSettings', 
            'processParameters'
        ),
        processParameters = cms.vstring(
            'Higgs:useBSM = on', 
            'HiggsBSM:all = off', 
            'HiggsBSM:gg2H2 = on', 
            '6000111:new = LL_nunu LLbar_nunu 1 0 0', 
            '6000111:m0 = 450', 
            '6000111:mWidth = 1.973269788e-17', 
            '6000111:tau0 = 10000', 
            '6000111:isResonance = on', 
            '6000111:mayDecay = on', 
            '6000111:oneChannel = 1  0.333 100 12 -12', 
            '6000111:addChannel = 1  0.333 100 14 -14', 
            '6000111:addChannel = 1  0.333 100 16 -16', 
            '6000113:new = LL_mu LLbar_mu 1 0 0', 
            '6000113:m0 = 450', 
            '6000113:mWidth = 1.973269788e-17', 
            '6000113:tau0 = 10000', 
            '6000113:isResonance = on', 
            '6000113:mayDecay = on', 
            '6000113:oneChannel = 1 1.0 100 13 -13', 
            '35:m0 = 1000', 
            '35:mWidth = 27.0', 
            '35:2:bRatio = 0.0', 
            '35:3:bRatio = 0.0', 
            '35:4:bRatio = 0.0', 
            '35:5:bRatio = 0.0', 
            '35:7:bRatio = 0.0', 
            '35:8:bRatio = 0.0', 
            '35:10:bRatio= 0.0', 
            '35:12:bRatio= 0.0', 
            '35:13:bRatio= 0.0', 
            '35:15:bRatio= 0.0', 
            '35:18:bRatio= 0.0', 
            '35:36:bRatio= 0.0', 
            '35:2:meMode = 100', 
            '35:3:meMode = 100', 
            '35:4:meMode = 100', 
            '35:5:meMode = 100', 
            '35:7:meMode = 100', 
            '35:8:meMode = 100', 
            '35:10:meMode= 100', 
            '35:12:meMode= 100', 
            '35:13:meMode= 100', 
            '35:15:meMode= 100', 
            '35:18:meMode= 100', 
            '35:20:meMode= 100', 
            '35:addChannel = 1 1. 100 6000113 6000113', 
            '35:onMode = off', 
            '35:onIfAny = 6000113 6000113'
        ),
        pythia8CP5Settings = cms.vstring(
            'Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118', 
            'SigmaTotal:mode = 0', 
            'SigmaTotal:sigmaEl = 21.89', 
            'SigmaTotal:sigmaTot = 100.309', 
            'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'
        ),
        pythia8PSweightsSettings = cms.vstring(
            'UncertaintyBands:doVariations = on', 
            'UncertaintyBands:List = {isrRedHi isr:muRfac=0.707,fsrRedHi fsr:muRfac=0.707,isrRedLo isr:muRfac=1.414,fsrRedLo fsr:muRfac=1.414,isrDefHi isr:muRfac=0.5,fsrDefHi fsr:muRfac=0.5,isrDefLo isr:muRfac=2.0,fsrDefLo fsr:muRfac=2.0,isrConHi isr:muRfac=0.25,fsrConHi fsr:muRfac=0.25,isrConLo isr:muRfac=4.0,fsrConLo fsr:muRfac=4.0,fsr_G2GG_muR_dn fsr:G2GG:muRfac=0.5,fsr_G2GG_muR_up fsr:G2GG:muRfac=2.0,fsr_G2QQ_muR_dn fsr:G2QQ:muRfac=0.5,fsr_G2QQ_muR_up fsr:G2QQ:muRfac=2.0,fsr_Q2QG_muR_dn fsr:Q2QG:muRfac=0.5,fsr_Q2QG_muR_up fsr:Q2QG:muRfac=2.0,fsr_X2XG_muR_dn fsr:X2XG:muRfac=0.5,fsr_X2XG_muR_up fsr:X2XG:muRfac=2.0,fsr_G2GG_cNS_dn fsr:G2GG:cNS=-2.0,fsr_G2GG_cNS_up fsr:G2GG:cNS=2.0,fsr_G2QQ_cNS_dn fsr:G2QQ:cNS=-2.0,fsr_G2QQ_cNS_up fsr:G2QQ:cNS=2.0,fsr_Q2QG_cNS_dn fsr:Q2QG:cNS=-2.0,fsr_Q2QG_cNS_up fsr:Q2QG:cNS=2.0,fsr_X2XG_cNS_dn fsr:X2XG:cNS=-2.0,fsr_X2XG_cNS_up fsr:X2XG:cNS=2.0,isr_G2GG_muR_dn isr:G2GG:muRfac=0.5,isr_G2GG_muR_up isr:G2GG:muRfac=2.0,isr_G2QQ_muR_dn isr:G2QQ:muRfac=0.5,isr_G2QQ_muR_up isr:G2QQ:muRfac=2.0,isr_Q2QG_muR_dn isr:Q2QG:muRfac=0.5,isr_Q2QG_muR_up isr:Q2QG:muRfac=2.0,isr_X2XG_muR_dn isr:X2XG:muRfac=0.5,isr_X2XG_muR_up isr:X2XG:muRfac=2.0,isr_G2GG_cNS_dn isr:G2GG:cNS=-2.0,isr_G2GG_cNS_up isr:G2GG:cNS=2.0,isr_G2QQ_cNS_dn isr:G2QQ:cNS=-2.0,isr_G2QQ_cNS_up isr:G2QQ:cNS=2.0,isr_Q2QG_cNS_dn isr:Q2QG:cNS=-2.0,isr_Q2QG_cNS_up isr:Q2QG:cNS=2.0,isr_X2XG_cNS_dn isr:X2XG:cNS=-2.0,isr_X2XG_cNS_up isr:X2XG:cNS=2.0}', 
            'UncertaintyBands:nFlavQ = 4', 
            'UncertaintyBands:MPIshowers = on', 
            'UncertaintyBands:overSampleFSR = 10.0', 
            'UncertaintyBands:overSampleISR = 10.0', 
            'UncertaintyBands:FSRpTmin2Fac = 20', 
            'UncertaintyBands:ISRpTmin2Fac = 1'
        )
    ),
    comEnergy = cms.double(14000.0),
    crossSection = cms.untracked.double(1),
    filterEfficiency = cms.untracked.double(1),
    maxEventsToPrint = cms.untracked.int32(10),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXRAWoutput_step = cms.EndPath(process.PREMIXRAWoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.PREMIXRAWoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)
process.options.numberOfConcurrentLuminosityBlocks=cms.untracked.uint32(1)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
