import os,sys

## to be executed in CMGTools/TTHAnalysis/python/plotter

do = [
      "rocs",  # roc curves
#      "effs",  # efficiencies
     ]

#74X
treedir = "/mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/"
publdir = "/afs/cern.ch/user/c/cheidegg/www/heppy/2016-04-19_leptons_nosel" #do NOT give a trailing /

#76X
#treedir = "/mnt/t3nfs01/data01/shome/cheidegg/o/2016-04-18_ewktrees76X/"
#publdir = "/afs/cern.ch/user/c/cheidegg/www/heppy/2016-04-19_leptons76X" #do NOT give a trailing /

base = "susy-multilepton/signal_rocs/mca_ewkino_nopresel.txt susy-multilepton/signal_rocs/<DEN>.txt susy-multilepton/signal_rocs/numerators_ewkino.txt susy-multilepton/signal_rocs/xvars_ewkino.txt -P " + treedir + " --s2v --tree treeProducerSusyMultilepton"
rocs = "python rocCurves.py " + base + " --splitSig 1 -j 8 --logx --grid --max-entries 5000000"
effs = "python mcEfficiencies.py " + base + " --groupBy process,cut"



## ----------------- do not touch beyond this line --------------------

def cmd(cmd):
	print cmd
	os.system(cmd)


## make rocs
## ---------------------------------------------------------------------
if "rocs" in do: 

	cmd("mkdir -p " + publdir + "/rocs 2> /dev/null && cp /afs/cern.ch/user/g/gpetrucc/php/index.php " + publdir + "/rocs")

	processes = [
	            #["TT_red,TT_true"      , ""],
	            #["TT_red,WZ_true"      , ""],
	            #["TT_red,T1_1200_800"  , ""],
	            #["TT_red,T1_1500_100"  , ""],
	            #["TT_red,WZ_350_100"   , ""],
	            #["TT_red,WZ_350_20"    , ""],
	            #["TT_red,WZ_200_100"   , ""],
	            #["TT_red,WZ_150_120"   , ""],
	            ###["TT_red,WH_250_20"    , ""],
	            #["TT_red,LL_750_100"   ,""],
	            #["TT_red,LL_450_300"   ,""],
	            #["TT_red,LL_300_270"   ,""],
	            #["TT_red,LL_450_300_SS",""],
	            #["TT_red,LL_300_270_SS",""],
	            ["DY_red,DY_true"      , ""],
	            ["DY_red,WZ_true"      , ""],
	            ["DY_red,T1_1200_800"  , ""],
	            ["DY_red,T1_1500_100"  , ""],
	            ["DY_red,WZ_350_100"   , ""],
	            ["DY_red,WZ_350_20"    , ""],
	            ["DY_red,WZ_200_100"   , ""],
	            ["DY_red,WZ_150_120"   , ""],
	            ##["DY_red,WH_250_20"    , ""],
	            ["DY_red,LL_750_100"   , ""],
	            ["DY_red,LL_450_300"   , ""],
	            ["DY_red,LL_300_270"   , ""],
	            ["DY_red,LL_450_300_SS", ""],
	            ["DY_red,LL_300_270_SS", ""], 
	            ]

	bins = [
           [ # denominator = LepGood + loose cuts
	         #["mu_pt_25_inf", "cuts_loose", " --xrange 0.001 1.0 --legend TL --yrange 0.8 1.0 -R pt20 pt 'LepGood_pt > 25'"                     ], \
	         ##["mu_pt_100_inf", "cuts_loose", " --xrange 0.001 1.0 --legend TL --yrange 0.8 1.0 -R pt20 pt 'LepGood_pt > 100'"                   ], \
	         ##["mu_pt_25_100" , "cuts_loose", " --xrange 0.001 1.0 --legend TL --yrange 0.8 1.0 -R pt20 pt 'LepGood_pt > 25 && LepGood_pt < 100'"], \
	         ##["mu_pt_10_25"  , "cuts_loose", " --xrange 0.001 1.0 --legend TL --yrange 0.6 1.0 -R pt20 pt 'LepGood_pt > 10 && LepGood_pt < 25'" ], \
	         ##["mu_pt_05_10"  , "cuts_loose", " --xrange 0.001 1.0 --legend TL --yrange 0.2 1.0 -R pt20 pt 'LepGood_pt > 5  && LepGood_pt < 10'" ], \
	         ###["el_pt_25_inf" , "cuts_loose", " --xrange 0.001 1.0 --legend TL --yrange 0.6 1.0 -I mu -R pt20 pt 'LepGood_pt > 25'"                   ], \
	         ##["el_pt_100_inf", "cuts_loose", " --xrange 0.001 1.0 --legend TL --yrange 0.8 1.0 -I mu -R pt20 pt 'LepGood_pt > 100'"                   ], \
	         ##["el_pt_25_100" , "cuts_loose", " --xrange 0.001 1.0 --legend TL --yrange 0.6 1.0 -I mu -R pt20 pt 'LepGood_pt > 25 && LepGood_pt < 100'"], \
	         ##["el_pt_10_25"  , "cuts_loose", " --xrange 0.001 1.0 --legend TL --yrange 0.2 1.0 -I mu -R pt20 pt 'LepGood_pt > 10 && LepGood_pt < 25'" ], \
	         ##["el_pt_05_10"  , "cuts_loose", " --xrange 0.001 1.0 --legend TL --yrange 0.0 1.0 -I mu -R pt20 pt 'LepGood_pt > 5  && LepGood_pt < 10'" ], \
	         ###["mu_pt_25_inf", "cuts_loose", " --xrange 0.7 1.0 --legend TL --yrange 0.8 1.0 -R pt20 pt 'LepGood_pt > 25'"                   ], \
	         ["mu_pt_100_inf", "cuts_loose", " --xrange 0.7 1.0 --legend TL --yrange 0.8 1.0 -R pt20 pt 'LepGood_pt > 100'"                   ], \
	         ["mu_pt_25_100" , "cuts_loose", " --xrange 0.7 1.0 --legend TL --yrange 0.8 1.0 -R pt20 pt 'LepGood_pt > 25 && LepGood_pt < 100'"], \
	         ["mu_pt_10_25"  , "cuts_loose", " --xrange 0.5 1.0 --legend TL --yrange 0.6 1.0 -R pt20 pt 'LepGood_pt > 10 && LepGood_pt < 25'"], \
	         ["mu_pt_05_10"  , "cuts_loose", " --xrange 0.1 1.0 --legend TL --yrange 0.2 1.0 -R pt20 pt 'LepGood_pt > 5  && LepGood_pt < 10'"], \
	         ##["el_pt_25_inf", "cuts_loose", " --xrange 0.3 1.0 --legend TL --yrange 0.6 1.0 -I mu -R pt20 pt 'LepGood_pt > 25'"                   ], \
	         ["el_pt_100_inf", "cuts_loose", " --xrange 0.3 1.0 --legend TL --yrange 0.8 1.0 -I mu -R pt20 pt 'LepGood_pt > 100'"                   ], \
	         ["el_pt_25_100" , "cuts_loose", " --xrange 0.3 1.0 --legend TL --yrange 0.6 1.0 -I mu -R pt20 pt 'LepGood_pt > 25 && LepGood_pt < 100'"], \
	         ["el_pt_10_25"  , "cuts_loose", " --xrange 0.1 1.0 --legend TL --yrange 0.2 1.0 -I mu -R pt20 pt 'LepGood_pt > 10 && LepGood_pt < 25'"], \
	         ["el_pt_05_10"  , "cuts_loose", " --xrange 0.1 1.0 --legend TL --yrange 0.0 1.0 -I mu -R pt20 pt 'LepGood_pt > 5  && LepGood_pt < 10'"], \
           ],
           [ # denominator = full ID - multi-Iso
	         #["mu_pt_25_inf" , "cuts_full" , " --xrange 0.001 1.0 --legend TL --yrange 0.8 1.0 -R pt20 pt 'LepGood_pt > 25'"                   ], \
	         ["mu_pt_100_inf", "cuts_full" , " --xrange 0.001 1.0 --legend TL --yrange 0.9 1.0 -R pt20 pt 'LepGood_pt > 100'"                   ], \
	         ["mu_pt_25_100" , "cuts_full" , " --xrange 0.001 1.0 --legend TL --yrange 0.8 1.0 -R pt20 pt 'LepGood_pt > 25 && LepGood_pt < 100'"], \
	         ["mu_pt_10_25"  , "cuts_full" , " --xrange 0.001 1.0 --legend TL --yrange 0.5 1.0 -R pt20 pt 'LepGood_pt > 10 && LepGood_pt < 25'" ], \
	         ["mu_pt_05_10"  , "cuts_full" , " --xrange 0.001 1.0 --legend TL --yrange 0.3 1.0 -R pt20 pt 'LepGood_pt > 5  && LepGood_pt < 10'" ], \
	         #["el_pt_25_inf" , "cuts_full" , " --xrange 0.001 1.0 --legend TL --yrange 0.6 1.0 -I mu -R pt20 pt 'LepGood_pt > 25'"                   ], \
	         ["el_pt_100_inf", "cuts_full" , " --xrange 0.001 1.0 --legend TL --yrange 0.9 1.0 -I mu -R pt20 pt 'LepGood_pt > 100'"                  ], \
	         ["el_pt_25_100" , "cuts_full" , " --xrange 0.001 1.0 --legend TL --yrange 0.8 1.0 -I mu -R pt20 pt 'LepGood_pt > 25 && LepGood_pt < 100'"], \
	         ["el_pt_10_25"  , "cuts_full" , " --xrange 0.001 1.0 --legend TL --yrange 0.5 1.0 -I mu -R pt20 pt 'LepGood_pt > 10 && LepGood_pt < 25'" ], \
	         ["el_pt_05_10"  , "cuts_full" , " --xrange 0.001 1.0 --legend TL --yrange 0.3 1.0 -I mu -R pt20 pt 'LepGood_pt > 5  && LepGood_pt < 10'" ], \
           ]
	       ]

	plots = [
	        [0, "ids" , "'mvaTTH,TTHt,RA7t,RA5t,OSt,NROSt' -F sf/t /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/leptonJetReCleanerSusyRA5/evVarFriend_{cname}.root -F sf/t /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/LepMVAFriendMoriond16/evVarFriend_{cname}.root"],
	        #[0, "ids" , "'mvaTTH,RA7t,RA7f,RA5t,RA5f,OSt,SLt,SLl,TTHt' -F sf/t /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/leptonJetReCleanerSusyRA5/evVarFriend_{cname}.root -F sf/t /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/LepMVAFriendMoriond16/evVarFriend_{cname}.root"],
	        [1, "multi", "'mini,reliso,multi_L,multi_M,multi_T,multi_VT'"]
	        #[1, "multi", "'mini,multi_L,multi_M,multi_T,multi_VT' -F sf/t /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/LepMVAMultiIso/evVarFriend_{cname}.root"]
	        ]

	## testing
	#cmd(rocs.replace("<DEN>", "cuts_loose") + " -p TT_red,TT_true -o " + publdir + "/rocs/TT_red_TT_true/mu_pt_25_inf_ids.root --legend BR --yrange 0.8 1.0 -X emu -R pt20 pt 'LepGood_pt > 25' --sP " + plots[0][2])
	#cmd(rocs.replace("<DEN>", "cuts_loose") + " -p TT_red,TT_true -o " + publdir + "/rocs/TT_red_TT_true/el_pt_25_inf_ids.root --legend BR --yrange 0.6 1.0 -I mu -R pt20 pt 'LepGood_pt > 25' --sP " + plots[0][2])
	#cmd(rocs.replace("<DEN>", "cuts_full" ) + " -p TT_red,TT_true -o " + publdir + "/rocs/TT_red_TT_true/mu_pt_25_inf_multi.root --legend BR --yrange 0.8 1.0 -R pt20 pt 'LepGood_pt > 25' --sP " + plots[1][1])
	#cmd(rocs.replace("<DEN>", "cuts_full" ) + " -p TT_red,TT_true -o " + publdir + "/rocs/TT_red_TT_true/el_pt_25_inf_multi.root --legend BR --yrange 0.6 1.0 -I mu -R pt20 pt 'LepGood_pt > 25' --sP " + plots[1][1])
	#sys.exit()

    ## cut-flow
	#cmd(rocs.replace("<DEN>", "cuts_loose") + " -p TT_red,TT_true -o " + publdir + "/rocs/TT_red_TT_true/el_pt_10_25_idsTest.root --legend BR --yrange 0.2 1.0 -I mu -R pt20 pt 'LepGood_pt > 10 && LepGood_pt < 25' --sP 'RA7none,RA7sip,RA7conv,RA7lost,RA7mva,RA7full'")
	#cmd(rocs.replace("<DEN>", "cuts_loose") + " -p TT_red,TT_true -o " + publdir + "/rocs/TT_red_TT_true/el_pt_25_inf_idsTest.root --legend BR --yrange 0.6 1.0 -I mu -R pt20 pt 'LepGood_pt > 25' --sP 'RA7none,RA7sip,RA7conv,RA7lost,RA7mva,RA7full'")
	#cmd(rocs.replace("<DEN>", "cuts_loose") + " -p TT_red,TT_true -o " + publdir + "/rocs/TT_red_TT_true/el_pt_10_25_idsTest.root --legend BR --yrange 0.2 1.0 -I mu -R pt20 pt 'LepGood_pt > 10 && LepGood_pt < 25' --sP 'RA7none,RA7sip,RA7conv,RA7lost,RA7mva,RA7full,RA5ch,RA5full'")
	#cmd(rocs.replace("<DEN>", "cuts_loose") + " -p TT_red,TT_true -o " + publdir + "/rocs/TT_red_TT_true/el_pt_25_100_idsTest.root --legend BR --yrange 0.6 1.0 -I mu -R pt20 pt 'LepGood_pt > 25 && LepGood_pt < 100' --sP 'RA7none,RA7sip,RA7conv,RA7lost,RA7mva,RA7full,RA5ch,RA5full'")
	#cmd(rocs.replace("<DEN>", "cuts_loose") + " -p TT_red,TT_true -o " + publdir + "/rocs/TT_red_TT_true/el_pt_100_inf_idsTest.root --legend BR --yrange 0.6 1.0 -I mu -R pt20 pt 'LepGood_pt > 100' --sP 'RA7none,RA7sip,RA7conv,RA7lost,RA7mva,RA7full,RA5ch,RA5full'")
	#sys.exit()

	## production
	for p in processes:
		pn = p[0].replace(",", "_")
		cmd("mkdir -p " + publdir + "/rocs/" + pn + " 2> /dev/null && cp /afs/cern.ch/user/g/gpetrucc/php/index.php " + publdir + "/rocs/" + pn)
		for s in plots:
			for b in bins[int(s[0])]:
				cmd(rocs.replace("<DEN>", b[1]) + " -p " + p[0] + " -o " + publdir + "/rocs/" + pn + "/" + b[0] + "_" + s[1] + ".root " + b[2] + " --sP " + s[2])




## make effs
## ---------------------------------------------------------------------
if "effs" in do: 

	cmd("mkdir -p " + publdir + "/effs 2> /dev/null && cp /afs/cern.ch/user/g/gpetrucc/php/index.php " + publdir + "/effs")

	processes = [
                #"TT_red,LL_750_100",
	            "TT_true,DY_true,WZ_350_20,WZ_150_120,LL_750_100,LL_300_270",
	            ##"TT_red,TT_true"      ,
	            ##"DY_red,DY_true"      ,
	            ##"TT_true,DY_true,WZ_350_100,WZ_350_20,WZ_200_100,WZ_150_120",
	            ##"TT_true,DY_true,WH_250_20",
	            ##"TT_true,DY_true,LL_750_100,LL_450_300,LL_300_270",
	            ##"TT_true,DY_true,LL_450_300_SS,LL_300_270_SS",
                ]

	bins = [
	       #["mu_eta_00_12_comp" , "cuts_loose", "-R pt20 eta 'abs(LepGood_eta) < 1.2' --yrange 0 1 --legend BR --sP pt_fine"],
	       #["mu_eta_12_21_comp" , "cuts_loose", "-R pt20 eta 'abs(LepGood_eta) > 1.2 && abs(LepGood_eta) < 2.1' --yrange 0 1 --legend BR --sP pt_fine"],
	       #["mu_eta_21_24_comp" , "cuts_loose", "-R pt20 eta 'abs(LepGood_eta) > 2.1 && abs(LepGood_eta) < 2.4' --yrange 0 1 --legend BR --sP pt_fine"],
	       #["el_eta_00_08_comp" , "cuts_loose", "-I mu -R pt20 eta 'abs(LepGood_eta) < 0.8' --yrange 0 1 --legend BR --sP pt_fine"],
	       #["el_eta_08_15_comp" , "cuts_loose", "-I mu -R pt20 eta 'abs(LepGood_eta) > 0.8 && abs(LepGood_eta) < 1.5' --yrange 0 1 --legend BR --sP pt_fine"],
	       #["el_eta_15_25_comp" , "cuts_loose", "-I mu -R pt20 eta 'abs(LepGood_eta) > 1.5 && abs(LepGood_eta) < 2.5' --yrange 0 1 --legend BR --sP pt_fine"],
	       #["mu_pt_05_10_comp"  , "cuts_loose", "-R pt20 pt 'LepGood_pt > 5 && LepGood_pt < 10' --yrange 0 1 --legend BR --sP eta_fine"],
	       #["mu_pt_10_25_comp"  , "cuts_loose", "-R pt20 pt 'LepGood_pt > 10 && LepGood_pt < 25' --yrange 0 1 --legend BR --sP eta_fine"],
	       #["mu_pt_25_100_comp" , "cuts_loose", "-R pt20 pt 'LepGood_pt > 25 && LepGood_pt < 100' --yrange 0 1 --legend BR --sP eta_fine"],
	       #["mu_pt_100_inf_comp", "cuts_loose", "-R pt20 pt 'LepGood_pt > 100' --yrange 0 1 --legend BR --sP eta_fine"],
	       ["el_pt_05_10_comp"  , "cuts_loose", "-I mu -R pt20 pt 'LepGood_pt > 5 && LepGood_pt < 10' --yrange 0 1 --legend BR --sP eta_fine"],
	       ["el_pt_10_25_comp"  , "cuts_loose", "-I mu -R pt20 pt 'LepGood_pt > 10 && LepGood_pt < 25' --yrange 0 1 --legend BR --sP eta_fine"],
	       ["el_pt_25_100_comp" , "cuts_loose", "-I mu -R pt20 pt 'LepGood_pt > 25 && LepGood_pt < 100' --yrange 0 1 --legend BR --sP eta_fine"],
	       ["el_pt_100_inf_comp", "cuts_loose", "-I mu -R pt20 pt 'LepGood_pt > 100' --yrange 0 1 --legend BR --sP eta_fine"],
	       ]

	plots = [
            ["ids", "--sP RA7t,RA7f,RA5t,RA5f,OSt,SLt,TTHt -F sf/t /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/leptonJetReCleanerSusyRA5/evVarFriend_{cname}.root -F sf/t /mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees/LepMVAFriendMoriond16/evVarFriend_{cname}.root"] 
            ]


	for p in processes:
		pn = p.replace(",", "_")
		cmd("mkdir -p " + publdir + "/effs/" + pn + " 2> /dev/null && cp /afs/cern.ch/user/g/gpetrucc/php/index.php " + publdir + "/effs/" + pn)
		for s in plots:
			for b in bins:
#			for b in bins[int(s[0])]:
				cmd(effs.replace("<DEN>", b[1]) + " -p " + p + " -o " + publdir + "/effs/" + pn + "/" + b[0] + "_" + s[0] + ".root " + b[2] + " " + s[1])





