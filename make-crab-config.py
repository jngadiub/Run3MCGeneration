import sys, optparse

parser = optparse.OptionParser()
parser.add_option("-s","--sample",dest="sample",default='',help="Process to generate")
parser.add_option("-o","--outdir",dest="outdir",default='',help="Jobs output directory (in LNF format)")
parser.add_option("-N","--njobs",dest="njobs",default=500,type=int,help="Number of jobs")
parser.add_option("-E","--eventsPerJob",dest="eventsPerJob",default=1000,type=int,help="Number of events processed per job")
(options,args) = parser.parse_args()
 
sample = options.sample
outdir = options.outdir
njobs = options.njobs
nEventsPerJob = options.eventsPerJob

print "Making crab config file for sample:",sample
print "Will use",outdir,"as job outuput directory at T2_CH_CERN"

with open('crab_%s.py'%sample, 'w') as fout:

 fout.write("from WMCore.Configuration import Configuration\n")
 fout.write("config = Configuration()\n")
 fout.write("\n")
 fout.write("config.section_('General')\n")
 fout.write("config.General.requestName = 'Run3MC_generation_%s'\n"%sample)
 fout.write("config.General.workArea = 'crab_projects'\n")
 fout.write("config.General.transferOutputs = True\n")
 fout.write("\n")
 fout.write("config.section_('JobType')\n")
 fout.write("config.JobType.pluginName = 'PrivateMC'\n")
 fout.write("config.JobType.psetName = '%s.py'\n"%sample)
 fout.write("config.JobType.numCores = 4\n")
 fout.write("config.JobType.maxMemoryMB = 6000\n")
 fout.write("\n")
 fout.write("config.section_('Data')\n")
 fout.write("config.Data.outputPrimaryDataset = '%s'\n"%sample)
 fout.write("config.Data.splitting = 'EventBased'\n")
 fout.write("config.Data.unitsPerJob = %i\n"%nEventsPerJob)
 fout.write("NJOBS = %i\n"%njobs)
 fout.write("config.Data.totalUnits = config.Data.unitsPerJob * NJOBS\n")
 fout.write("config.Data.publication = False\n")
 fout.write("config.Data.outputDatasetTag = 'Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6'\n")
 fout.write("config.Data.outLFNDirBase = '%s'\n"%outdir)
 fout.write("\n")
 fout.write("config.section_('Site')\n")
 fout.write("config.Site.storageSite = 'T2_CH_CERN'\n")
