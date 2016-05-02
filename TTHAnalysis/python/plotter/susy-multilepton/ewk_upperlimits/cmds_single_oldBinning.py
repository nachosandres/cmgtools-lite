import os


# do NOT put trailing /
O="/afs/cern.ch/user/c/cheidegg/www/heppy/2016-04-20_ewk8tev_upperlimits"
T="/mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees"

do = [
     "incl",
#     "excl",
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
	         "--sP SR_a_a --yrange 0 230",
	         "--sP SR_a_b --yrange 0 14" ,
	         "--sP SR_a_c --yrange 0 11" ,
	         "--sP SR_b_a --yrange 0 950",
	         "--sP SR_b_b --yrange 0 35" ,
	         "--sP SR_b_c --yrange 0 11 --legendCorner TC" ,
	         "--sP SR_c_a --yrange 0 75" ,
	         "--sP SR_c_b --yrange 0 7"  ,
	         "--sP SR_c_c --yrange 0 10 --legendCorner TC" ,
	        ]
	
	bunches = [
	           [""       , "-p _standard_prompt_.* -p _matched_fakes_.*"      ],
	           ["_FRappl", "-p _standard_prompt_.* -p _standard_fakes_.*"     ],
	           ["_sigs"  , "-p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"],
	          ]
	
	base = "python mcPlots.py susy-multilepton/ewk_upperlimits/mca_ewkino.txt susy-multilepton/ewk_upperlimits/cuts_ewkino.txt susy-multilepton/ewk_upperlimits/plots_ewkino.txt -P " + T + " --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --legendWidth 0.20 --legendFontSize 0.035 -F sf/t {P}/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWK/evVarFriend_{cname}.root --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --showMCError -l 10.0 -W 'vtxWeight_Loop' --pdir " + O
	
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
	         ["--sP SR_a_a --yrange 0 100"                 , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_SlepSneu_300_270"],
	         ["--sP SR_a_b --yrange 0 8"                   , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_SlepSneu_300_270"],
	         ["--sP SR_a_c --yrange 0 7"                   , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_SlepSneu_300_270"],
	         ["--sP SR_b_a --yrange 0 400"                 , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_WZ_350_20"       ],
	         ["--sP SR_b_b --yrange 0 15"                  , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_WZ_350_20"       ],
	         ["--sP SR_b_c --yrange 0 5 --legendCorner TC" , "-p _sig_TChiNeu_SlepSneu_450_300 -p _sig_TChiNeu_WZ_350_20 -p _sig_TChiNeu_WZ_350_100 -p _sig_TChiNeu_WZ_200_100"],
	         ["--sP SR_c_a --yrange 0 30"                  , "-p _sig_TChiNeu_SlepSneu_450_300"                                 ],
	         ["--sP SR_c_b --yrange 0 4"                   , "-p _sig_TChiNeu_SlepSneu_450_300"                                 ],
	         ["--sP SR_c_c --yrange 0 4 --legendCorner TC" , "-p _sig_TChiNeu_SlepSneu_750_100 -p _sig_TChiNeu_SlepSneu_450_300"],
	        ]
	
	backgrounds = [
	               [""       , "-p _standard_prompt_.* -p _matched_fakes_.*"      ],
	               ["_FRappl", "-p _standard_prompt_.* -p _standard_fakes_.*"     ],
	              ]
	
	base = "python mcPlots.py susy-multilepton/ewk_upperlimits/mca_ewkino.txt susy-multilepton/ewk_upperlimits/cuts_ewkino.txt susy-multilepton/ewk_upperlimits/plots_ewkino.txt -P " + T + " --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --legendWidth 0.20 --legendFontSize 0.035 -F sf/t {P}/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWK/evVarFriend_{cname}.root --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --showMCError --showIndivSigs --noStackSig --showRatio --maxRatioRange 0 3 -l 10. -W 'vtxWeight_Loop' --pdir " + O

	for p in plots:
		for f in flavors:
			for b in backgrounds:
				cmd(base + b[0] + f[0] + " " + b[1] + " " + " ".join(p) + " " + f[1])




