import os


out="/afs/cern.ch/user/c/cheidegg/www/heppy/2016-04-15_ewk8tev_upperlimits" # the base output directory

proc = [
        ["-p _standard_prompt_.* -p _standard_fakes_.*"        , ""       ],
        ["-p _standard_prompt_.* -p _matched_fakes_.*"         , "_FRappl"],
        ["-p _standard_prompt_.* -p _fakesappl_data -p data" , "_FRapplDATA"],
       ]
sigs = [
        #["--sP SR_.*._.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"                       ],
        ["--sP SR_.*._.* -p _large_sig_TChiNeu_WZ_.* -p _large_sig_TChiNeu_SlepSneu_.*"           ],
        ["--sP SR_a_a --sP SR_b_a -p _larger_sig_TChiNeu_WZ_.* -p _larger_sig_TChiNeu_SlepSneu_.*"],
        ["--sP SR_c_b --sP SR_c_c -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"              ],
       ]
cuts = [
        [""                                                                                  , ""   ],
        #["-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 33'", "_eee"],
        #["-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 35'", "_eem"],
        #["-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 37'", "_emm"],
        #["-A anylll flav 'abs(LepGood1_pdgId)+abs(LepGood2_pdgId)+abs(LepGood3_pdgId) == 39'", "_mmm"],
       ]

base = "python mcPlots.py susy-multilepton/ewk_upperlimits/mca_ewkino.txt susy-multilepton/ewk_upperlimits/cuts_ewkino.txt susy-multilepton/ewk_upperlimits/plots_ewkino.txt -P /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/ --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --legendWidth 0.20 --legendFontSize 0.035 --showRatio --maxRatioRange 0 3 -F sf/t {P}/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWK/evVarFriend_{cname}.root --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --showMCError -l 10.0 --showIndivSigs --noStackSig -W 'vtxWeight_Loop' --pdir "

def cmd(cmd):
	print cmd
	os.system(cmd)

for b in proc:
	for s in sigs:
		for c in cuts:
			cmd(base + out + b[1] + c[1] + " " + c[0] + " " + b[0] + " " + s[0])


## WZ control region
#python mcPlots.py susy-multilepton/ewk_upperlimits/mca_ewkino.txt susy-multilepton/ewk_upperlimits/cuts_ewkino.txt susy-multilepton/ewk_upperlimits/plots_ewkino.txt -P /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/ --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --legendWidth 0.20 --legendFontSize 0.035 --showRatio --maxRatioRange 0 3 -F sf/t {P}/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWK/evVarFriend_{cname}.root --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --showMCError -l 10.0 --scaleBkgToData --showSF -W 'vtxWeight_Loop' --pdir /afs/cern.ch/user/c/cheidegg/www/heppy/2016-04-15_ewk8tev_upperlimits_WZ -p data -p _unscaled_WZ --sP met --sP mtW




