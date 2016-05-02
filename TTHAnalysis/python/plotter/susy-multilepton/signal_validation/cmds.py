import os


# this is the base command WITHOUT --pdir, -p

## 74X
#base = "python mcPlots.py susy-multilepton/signal_validation/mca_ewkino.txt susy-multilepton/signal_validation/cuts_ewkino.txt susy-multilepton/signal_validation/plots_ewkino.txt -P /shome/cheidegg/o/2016-03-12_ewksignals_GEN --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --rspam '(13 TeV)' --legendWidth 0.20 --legendFontSize 0.035 --showRatio --maxRatioRange 0 3 --plotmode norm --sP genFlavSlep -A alwaystrue slep 'slpleg1>0'"
#base = "python mcPlots.py susy-multilepton/signal_validation/mca_ewkino.txt susy-multilepton/signal_validation/cuts_ewkino.txt susy-multilepton/signal_validation/plots_ewkino.txt -P /shome/cheidegg/o/2016-03-12_ewksignals --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --rspam '(13 TeV)' --legendWidth 0.20 --legendFontSize 0.035 --showRatio --maxRatioRange 0 3 --plotmode norm --sP genFlavChi --sP genFlavNeu"

## 76X
#base = "python mcPlots.py susy-multilepton/signal_validation/mca_ewkino.txt susy-multilepton/signal_validation/cuts_ewkino.txt susy-multilepton/signal_validation/plots_ewkino.txt -P /shome/cheidegg/o/2016-04-15_ewksignals76X --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --rspam '(13 TeV)' --legendWidth 0.20 --legendFontSize 0.035 --showRatio --maxRatioRange 0 3 --plotmode norm "
base = "python mcPlots.py susy-multilepton/signal_validation/mca_ewkino.txt susy-multilepton/signal_validation/cuts_ewkino.txt susy-multilepton/signal_validation/plots_ewkino.txt -P /shome/cheidegg/o/2016-04-15_ewksignals76X_GEN/ --neg --s2v --tree treeProducerSusyMultilepton -f -j 8 --lspam '#bf{CMS} #it{Simulation}' --rspam '(13 TeV)' --legendWidth 0.20 --legendFontSize 0.035 --showRatio --maxRatioRange 0 3 --plotmode norm --objname demo/events --sP nGenLep --sP gen.*"

outbase = "/afs/cern.ch/user/c/cheidegg/www/heppy/2016-04-16_signal_validation_76X_"
processes = [
             #["_sig_TChiNeu_SlepSneu_.*"                       , "C1N2LL"  ],
             #["_sig_TChiChi_SlepSneu_.*"                       , "C1C1LL"  ],
             #["_sig_TChiNeu_WZ_350_100 -p _sig_TChiNeu_WZ_350_20 -p _sig_TChiNeu_WZ_200_100 -p _sig_TChiNeu_WZ_150_120", "C1N2WZ"  ],
             #["_sig_TChiNeu_WZ_350_100 -p _sig_TChiNeu_WZ_350_20 -p _sig_TChiNeu_WZ_200_100 -p _sig_TChiNeu_WZ_150_120 -p _standard_prompt_WZ", "C1N2WZ"  ],
             ["_sig_TChiNeu_WZ_.*._OS"                         , "C1N2WZOS"],
             #["_sig_TChiNeu_WH_250_20 -p _sig_TChiNeu_WH_150_20", "C1N2WH"  ],
             #["_sig_TChiNeu_WH_.*._SL"                         , "C1N2WHSL"],
            ]

## ----------------- do not touch beyond this line --------------------

def cmd(cmd):
	print cmd
	os.system(cmd)

for p in processes:

	c = base + " -p " + p[0] + " --pdir " + outbase + p[1]
	cmd(c)

