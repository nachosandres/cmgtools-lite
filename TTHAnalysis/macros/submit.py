import os

## this script creates a sub-directory in the tree path for a given module
## and runs the friend tree producer for this module

batch = True
queue = "all.q"
path  = "/mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/"
force = False # if the friend tree already exists, module is not run; set to True to still run it

## first: module to run, second: list of modules (comma separated) that are required to run
modules = [
          #["LepMVAFriendMoriond16"       , ""                            ],
          #["puWeightsTrue_central"       , ""                            ],
          #["leptonJetReCleanerSusyRA7"   , ""                            ], 
          #["leptonJetReCleanerSusyRA5"   , ""                            ],
          #["leptonJetReCleanerSusyRA7mva", "LepMVAFriendMoriond16"       ],
          #["leptonChoiceEWK"             , "leptonJetReCleanerSusyRA7"   ],
          ["leptonChoiceEWKtau"          , "leptonJetReCleanerSusyRA7_good"   ],
          #["leptonChoiceEWK"             , "leptonJetReCleanerSusyRA7mva"],
         ] 

## in case you want to run only specific samples
accept = [
          #"TTTT",
          #"DY",
          #"WZTo3LNu",
          #"TTW",
         ]

## in case you want to exclude specific samples
exclude = [
           #"WZTo3LNu",
           #"DoubleEG",
           #"DoubleMuon",
           #"MuonEG",
          ]

## --------------- do not touch beyond this line ---------------

def cmd(cmd):
	print cmd
	os.system(cmd)

def mkdir(path):
	if os.path.isdir(path): return
	cmd("mkdir " + path)

def submit(sample, module):
	global batch, queue, path
	super = "python prepareEventVariablesFriendTree.py " + path + " " + path + "/" + module[0] + " -d " + sample + " --tree treeProducerSusyMultilepton -m " + module[0]
	if not module[1].strip() == "":
		sm = module[1].strip().split(",")
		for f in sm: super += " -F sf/t " + path + "/" + f + "/evVarFriend_" + sample + ".root"
	if batch:
		super += " -q " + queue + " -N 50000 --log " + path + "/" + module[0] + "/log"
	cmd(super)


path = path.rstrip("/")
listdir = os.listdir(path)

for module in modules:

	mkdir(path + "/" + module[0])
	mkdir(path + "/" + module[0] + "/log")
	
	for d in listdir:
		if not os.path.isdir(path + "/" + d): continue
		if not os.path.exists(path + "/" + d + "/treeProducerSusyMultilepton/tree.root"): continue
		if not force and os.path.exists(path + "/" + module[0] + "/evVarFriend_" + d + ".root"): continue
		if accept  != [] and all([d.find(a) == -1 for a in accept ]): continue
		if exclude != [] and any([d.find(e) >  -1 for e in exclude]): continue
	
		submit(d, module)

