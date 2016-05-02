import os


# do NOT put trailing /
O   = "/afs/cern.ch/user/c/cheidegg/www/heppy/2016-04-29_ewk8tev_upperlimits_taus"
T   = "/mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees"
lch = "leptonChoiceEWKtau"
jlr = "leptonJetReCleanerSusyRA7_good"

do = [
     "incl",
#     "excl",
#     "allSR",
     ]


## ----------- this is the script beyond this point ------------------

O = O.rstrip("/")
T = T.rstrip("/")

def cmd(cmd):
	print cmd
	os.system(cmd)




## FLAVOR INLCUSIVE

if "incl" in do:

	plots = [
	         "--sP SR_201-204_a",
	         "--sP SR_205-208_a " ,
	         "--sP SR_209-212_a" ,
	         "--sP SR_201-204_b",
	         "--sP SR_205-208_b" ,
	         "--sP SR_209-212_b --legendCorner TC" ,
	         "--sP SR_201-204_c" ,
	         "--sP SR_205-208_c"  ,
	         "--sP SR_209-212_c --legendCorner TC" ,
	         "--sP SR_101-104_a" ,
	         "--sP SR_105-108_a"  ,
	         "--sP SR_109-112_a"  ,
	         "--sP SR_101-104_b",
	         "--sP SR_105-108_b",
	         "--sP SR_109-112_b --legendCorner TC" ,
	         #"--sP SR_201-204_a --yrange 0 230",
	         #"--sP SR_205-208_a --yrange 0 14" ,
	         #"--sP SR_209-212_a --yrange 0 11" ,
	         #"--sP SR_201-204_b --yrange 0 950",
	         #"--sP SR_205-208_b --yrange 0 35" ,
	         #"--sP SR_209-212_b --yrange 0 11 --legendCorner TC" ,
	         #"--sP SR_201-204_c --yrange 0 75" ,
	         #"--sP SR_205-208_c --yrange 0 7"  ,
	         #"--sP SR_209-212_c --yrange 0 10 --legendCorner TC" ,
	         #"--sP SR_101-104_a --yrange 0 35" ,
	         #"--sP SR_105-108_a --yrange 0 5"  ,
	         #"--sP SR_109-112_a --yrange 0 4"  ,
	         #"--sP SR_101-104_b --yrange 0 1.5",
	         #"--sP SR_105-108_b --yrange 0 0.5",
	         #"--sP SR_109-112_b --yrange 0 0.5 --legendCorner TC" ,
	        ]
	
	bunches = [
	           #["_full"  , "--showIndivSigs --noStackSig -p _standard_prompt_.* -p _matched_fakes_.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"],
	           #["_fullFR"  , "--showIndivSigs --noStackSig -p _standard_prompt_.* -p _standard_fakes_.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"],
	           ["_bkgs"  , "-p _standard_prompt_.* -p _matched_fakes_.*"      ],
	           #["_FRappl", "-p _standard_prompt_.* -p _standard_fakes_.*"     ],
	           ["_sigs"  , "--emptyStack -p dummy --showIndivSigs --noStackSig -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"],
	          ]
	

	base = "python mcPlots.py susy-multilepton/ewk_upperlimits/mca_ewkino.txt susy-multilepton/ewk_upperlimits/cuts_ewkino.txt susy-multilepton/ewk_upperlimits/plots_ewkino.txt -P " + T + " --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --legendWidth 0.20 --legendFontSize 0.035 -F sf/t {P}/" + jlr + "/evVarFriend_{cname}.root -F sf/t {P}/" + lch + "/evVarFriend_{cname}.root --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --showMCError -l 10.0 -W 'vtxWeight_Loop' -A 3l 1tau 't1_Loop + t2_Loop + t3_Loop == 1' --pdir " + O
	
	for p in plots:
		for b in bunches:
			cmd(base + b[0] + " " + b[1] + " " + p)
	


## FLAVOR EXCLUSIVE
	
if "excl" in do:

	flavors = [
	           ["_eee", "-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 33'"],
	           ["_eem", "-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 35'"],
	           ["_emm", "-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 37'"],
	           ["_mmm", "-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 39'"],
	          ]

	plots = [
	         ["--sP SR_201-204_a --yrange 0 100"                 , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_SlepSneu_300_270"],
	         ["--sP SR_205-208_a --yrange 0 8"                   , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_SlepSneu_300_270"],
	         ["--sP SR_209-212_a --yrange 0 7"                   , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_SlepSneu_300_270"],
	         ["--sP SR_201-204_b --yrange 0 400"                 , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_WZ_350_20"       ],
	         ["--sP SR_205-208_b --yrange 0 15"                  , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_WZ_350_20"       ],
	         ["--sP SR_209-212_b --yrange 0 5 --legendCorner TC" , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_WZ_350_20 -p _sig_TChiNeu_WZ_350_100 -p _sig_TChiNeu_WZ_200_100"],
	         ["--sP SR_201-204_c --yrange 0 30"                  , "-p _sig_TChiNeu_SlepSneu_450_300"                                 ],
	         ["--sP SR_205-208_c --yrange 0 4"                   , "-p _sig_TChiNeu_SlepSneu_450_300"                                 ],
	         ["--sP SR_209-212_c --yrange 0 4 --legendCorner TC" , "-p _sig_TChiNeu_SlepSneu_750_100 -p _sig_TChiNeu_SlepSneu_450_300"],
	         ["--sP SR_101-104_a --yrange 0 30"                  , "-p _sig_TChiNeu_WZ_200_100"                                       ],
	         ["--sP SR_105-108_a --yrange 0 4"                   , "-p _sig_TChiNeu_SlepSneu_450_300"                                 ],
	         ["--sP SR_109-112_a --yrange 0 0.5"                 , "-p _sig_TChiNeu_SlepSneu_450_300"                                 ],
	         ["--sP SR_101-104_b --yrange 0 1"                   , "-p _sig_TChiNeu_SlepSneu_450_300"                                 ],
	         ["--sP SR_105-108_b --yrange 0 0.5"                 , "-p _sig_TChiNeu_SlepSneu_450_300"                                 ],
	         ["--sP SR_109-112_b --yrange 0 0.5"                 , "-p _sig_TChiNeu_SlepSneu_750_100 -p _sig_TChiNeu_SlepSneu_450_300"],
	         #["--sP SR_a_a --yrange 0 100"                 , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_SlepSneu_300_270"],
	         #["--sP SR_a_b --yrange 0 8"                   , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_SlepSneu_300_270"],
	         #["--sP SR_a_c --yrange 0 7"                   , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_SlepSneu_300_270"],
	         #["--sP SR_b_a --yrange 0 400"                 , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_WZ_350_20"       ],
	         #["--sP SR_b_b --yrange 0 15"                  , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_WZ_350_20"       ],
	         #["--sP SR_b_c --yrange 0 5 --legendCorner TC" , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_WZ_350_20 -p _sig_TChiNeu_WZ_350_100 -p _sig_TChiNeu_WZ_200_100"],
	         #["--sP SR_c_a --yrange 0 30"                  , "-p _sig_TChiNeu_SlepSneu_450_300"                                 ],
	         #["--sP SR_c_b --yrange 0 4"                   , "-p _sig_TChiNeu_SlepSneu_450_300"                                 ],
	         #["--sP SR_c_c --yrange 0 4 --legendCorner TC" , "-p _sig_TChiNeu_SlepSneu_750_100 -p _sig_TChiNeu_SlepSneu_450_300"],
	        ]
	
	backgrounds = [
	               [""       , "-p _standard_prompt_.* -p _matched_fakes_.*"      ],
	               #["_FRappl", "-p _standard_prompt_.* -p _standard_fakes_.*"     ],
	              ]
	
	base = "python mcPlots.py susy-multilepton/ewk_upperlimits/mca_ewkino.txt susy-multilepton/ewk_upperlimits/cuts_ewkino.txt susy-multilepton/ewk_upperlimits/plots_ewkino.txt -P " + T + " --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --legendWidth 0.20 --legendFontSize 0.035 -F sf/t {P}/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWK_newBinning/evVarFriend_{cname}.root --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --showMCError --showIndivSigs --noStackSig --showRatio --maxRatioRange 0 3 --ratioNums _sig_.* -l 10. -W 'vtxWeight_Loop' --pdir " + O

	for p in plots:
		for f in flavors:
			for b in backgrounds:
				cmd(base + b[0] + f[0] + " " + b[1] + " " + " ".join(p) + " " + f[1])



if "allSR" in do:

	plots = [
	         #"--sP SR_101_a",
	         #"--sP SR_102_a",
	         #"--sP SR_103_a",
	         #"--sP SR_104_a",
	         #"--sP SR_105_a",
	         #"--sP SR_106_a",
	         #"--sP SR_107_a",
	         #"--sP SR_108_a",
	         #"--sP SR_109_a",
	         #"--sP SR_110_a",
	         #"--sP SR_111_a",
	         #"--sP SR_112_a",
	         #"--sP SR_101_b",
	         #"--sP SR_102_b",
	         #"--sP SR_103_b",
	         #"--sP SR_104_b",
	         #"--sP SR_105_b",
	         #"--sP SR_106_b",
	         #"--sP SR_107_b",
	         #"--sP SR_108_b",
	         #"--sP SR_109_b",
	         #"--sP SR_110_b",
	         #"--sP SR_111_b",
	         #"--sP SR_112_b",
	         "--sP SR_201_a",
	         "--sP SR_202_a",
	         "--sP SR_203_a",
	         "--sP SR_204_a",
	         "--sP SR_205_a",
	         "--sP SR_206_a",
	         "--sP SR_207_a",
	         "--sP SR_208_a",
	         "--sP SR_209_a",
	         "--sP SR_210_a",
	         "--sP SR_211_a",
	         "--sP SR_212_a",
	         "--sP SR_201_b",
	         "--sP SR_202_b",
	         "--sP SR_203_b",
	         "--sP SR_204_b",
	         "--sP SR_205_b",
	         "--sP SR_206_b",
	         "--sP SR_207_b",
	         "--sP SR_208_b",
	         "--sP SR_209_b",
	         "--sP SR_210_b",
	         "--sP SR_211_b",
	         "--sP SR_212_b",
	         "--sP SR_201_c",
	         "--sP SR_202_c",
	         "--sP SR_203_c",
	         "--sP SR_204_c",
	         "--sP SR_205_c",
	         "--sP SR_206_c",
	         "--sP SR_207_c",
	         "--sP SR_208_c",
	         "--sP SR_209_c",
	         "--sP SR_210_c",
	         "--sP SR_211_c",
	         "--sP SR_212_c",
	        ]
	
	base = "python mcPlots.py susy-multilepton/ewk_upperlimits/mca_ewkino.txt susy-multilepton/ewk_upperlimits/cuts_ewkino.txt susy-multilepton/ewk_upperlimits/plots_ewkino.txt -P " + T + " --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --legendWidth 0.20 --legendFontSize 0.035 -F sf/t {P}/leptonJetReCleanerSusyRA7pt/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWKpt/evVarFriend_{cname}.root --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --showMCError -l 10.0 -W 'vtxWeight_Loop' -p dummy --emptyStack --showIndivSigs --noStackSig --pdir " + O
	
	for p in plots:
		#cmd(base + "_pt_allSR -p _sig_TChiNeu_WZ_.* " + p)
		cmd(base + "_pt_allSR -p _standard_prompt_.* -p _matched_fakes_.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.* " + p)

