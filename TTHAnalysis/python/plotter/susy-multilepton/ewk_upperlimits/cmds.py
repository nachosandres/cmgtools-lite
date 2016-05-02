import os

do = [
      "plots",
      #"effs",
      #"wz",
     ]

mod="leptonChoiceEWKtau"
jmd="leptonJetReCleanerSusyRA7"
out="/afs/cern.ch/user/c/cheidegg/www/heppy/2016-04-29_ewk8tev_upperlimits_taus" # the base output directory


## ----------- this is the script beyond this point ------------------

out = out.rstrip("/")

def cmd(cmd):
	print cmd
	os.system(cmd)


## plot the yields -----------

if "plots" in do:

	proc = [
	        #["-p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.* --plotmode norm", "_sigs"  ],
	        #["-p _standard_prompt_.* -p _standard_fakes_.*"      , "_FRappl"],
	        ["-p _standard_prompt_.* -p _matched_fakes_.*"       , ""       ],
	        #["-p _standard_prompt_.* -p _fakesappl_data -p data" , "_DATA"  ],
	       ]
	sigs = [
	        #["--sP SR_.*.-.*._.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"                               ],
	        #["--sP SR_.*.-.*._.* -p _large_sig_TChiNeu_WZ_.* -p _large_sig_TChiNeu_SlepSneu_.*"                   ],
	        #["--sP SR_201-204_a --sP SR_201-204_b -p _larger_sig_TChiNeu_WZ_.* -p _larger_sig_TChiNeu_SlepSneu_.*"],
	        #["--sP SR_205-208_c --sP SR_209-212_c -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"              ],
	        #["--sP SR_.*.-.*._a --sP SR_101-104_b --sP SR_105_108_b -p _largest_sig_TChiNeu_WZ_.* -p _largest_sig_TChiNeu_SlepSneu_.*"],
	        #["--sP SR_.*._.*"                                                                         ],
	        #["--sP SR_.*._.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"                       ],
	        #["--sP SR_.*._.* -p _large_sig_TChiNeu_WZ_.* -p _large_sig_TChiNeu_SlepSneu_.*"           ],
	        #["--sP SR_a_a --sP SR_b_a -p _larger_sig_TChiNeu_WZ_.* -p _larger_sig_TChiNeu_SlepSneu_.*"],
	        #["--sP SR_c_b --sP SR_c_c -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"              ],
	       ]
	cuts = [
	        [""                                                                                  , ""   ],
	        #["-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 33'", "_eee"],
	        #["-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 35'", "_eem"],
	        #["-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 37'", "_emm"],
	        #["-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 39'", "_mmm"],
	       ]

	base = "python mcPlots.py susy-multilepton/ewk_upperlimits/mca_ewkino.txt susy-multilepton/ewk_upperlimits/cuts_ewkino.txt susy-multilepton/ewk_upperlimits/plots_ewkino.txt -P /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/ --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --legendWidth 0.20 --legendFontSize 0.035 -F sf/t {P}/" + jmd + "/evVarFriend_{cname}.root -F sf/t {P}/" + mod + "/evVarFriend_{cname}.root --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --showMCError -l 10.0 --showIndivSigs --noStackSig -W 'vtxWeight_Loop' --pdir "
		
	for b in proc:
		for s in sigs:
			for c in cuts:
				cmd(base + out + b[1] + c[1] + " " + c[0] + " " + b[0] + " " + s[0])



## efficiency tables ----------

out = out + "/"

if "effs" in do:

	proc = [
	        "_standard_prompt_.*",
	        "_standard_fakes_.*" , 
	        "_matched_fakes_.*"  ,
	        "_sig_TChiNeu_WZ_.*" ,
	        "_sig_TChiNeu_SlepSneu_.*" ,
	       ]

	cuts = [
	        "cuts_cutflowevent",
	        #"cuts_cutflowevent1",
	        #"cuts_cutflowelectrons",
	        #"cuts_cutflowmuons"
	       ]


	base = "python mcAnalysis.py susy-multilepton/ewk_upperlimits/mca_ewkino.txt susy-multilepton/ewk_upperlimits/<CUTS>.txt -P /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/ --neg --s2v --tree treeProducerSusyMultilepton -j 8 -F sf/t {P}/" + jmd + "/evVarFriend_{cname}.root -F sf/t {P}/" + mod + "/evVarFriend_{cname}.root --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt -l 10.0 -W 'vtxWeight_Loop' -p <PLOTS> >> "

	for b in proc:
		for c in cuts:
			cmd(base.replace("<CUTS>", c).replace("<PLOTS>", b) + out + c + "_" + b.replace(".*", "ALL") + ".txt")



## WZ control region
if "wz" in do:
	print "nothing to do for now"
	#python mcPlots.py susy-multilepton/ewk_upperlimits/mca_ewkino.txt susy-multilepton/ewk_upperlimits/cuts_ewkino.txt susy-multilepton/ewk_upperlimits/plots_ewkino.txt -P /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/ --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --legendWidth 0.20 --legendFontSize 0.035 --showRatio --maxRatioRange 0 3 -F sf/t {P}/" + jmd + "/evVarFriend_{cname}.root -F sf/t {P}/" + mod + "/evVarFriend_{cname}.root --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --showMCError -l 10.0 --scaleBkgToData --showSF -W 'vtxWeight_Loop' --pdir /afs/cern.ch/user/c/cheidegg/www/heppy/2016-04-15_ewk8tev_upperlimits_WZ -p data -p _unscaled_WZ --sP met --sP mtW




