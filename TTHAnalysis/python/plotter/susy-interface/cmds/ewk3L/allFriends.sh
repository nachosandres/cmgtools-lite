S="/scratch/cheidegg"

#T="/mnt/t3nfs01/data01/shome/cheidegg/o/2017-02-25_ewktrees80X_M17_bkg"
#F="-q all.q --direct"
#R="/pnfs/psi.ch/cms/trivcat/store/user/cheidegg/sea/11/2017-02-25-10-00-00"

T="/mnt/t3nfs01/data01/shome/cheidegg/o/2017-02-18_ewktrees80X_M17_signals"
F="-q all.q --nosplit --direct --accept TChiSlepSnux0p"
R="/pnfs/psi.ch/cms/trivcat/store/user/cheidegg/sea/11/2017-02-05-11-37-00"
#
#F="-q all.q --nosplit --direct --accept T6ttHZ --accept T6bbll"
#R="/pnfs/psi.ch/cms/trivcat/store/user/cheidegg/sea/11/2017-02-18-17-00-00"

T="/mnt/t3nfs01/data01/shome/cheidegg/o/2017-02-23_ewkskims80X_M17_3l_data"
F="-q all.q --nosplit --direct"


#python susy-interface/friendmaker.py 3l 3lA $T $S --bk --log $F --flags "--remote '$R'" --modules leptonJetReCleanerSusyEWK3L
#python susy-interface/friendmaker.py 3l 3lA $T $S --bk --log $F --flags "--remote '$R'" --modules leptonBuilderEWK
#python susy-interface/friendmaker.py 3l 3lA $T $S --bk --log $F --flags "--remote '$R'" --modules leptonJetReCleanerSusyEWK2L
python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules TrivialPUWModule
#python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules ISRWeightModule
#python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules ISRPtWeightModule
#python susy-interface/friendmaker.py 3l 3lA $T $S --bk --log $F --modules bTagEventWeightFullSim3L --flags "-F sf/t {RP}/leptonJetReCleanerSusyEWK3L/evVarFriend_{cname}.root --remote '$R'" 
#python susy-interface/friendmaker.py 3l 3lA $T $S --bk --log $F --modules bTagEventWeightFastSim3L --flags "-F sf/t {RP}/leptonJetReCleanerSusyEWK3L/evVarFriend_{cname}.root --remote '$R'" 
#python susy-interface/friendmaker.py 3l 3lA $T $S --bk --log $F --modules bTagEventWeightFullSim2L --flags "-F sf/t {RP}/leptonJetReCleanerSusyEWK2L/evVarFriend_{cname}.root --remote '$R'" 
#python susy-interface/friendmaker.py 3l 3lA $T $S --bk --log $F --modules bTagEventWeightFastSim2L --flags "-F sf/t {RP}/leptonJetReCleanerSusyEWK2L/evVarFriend_{cname}.root --remote '$R'" 



#T="/mnt/t3nfs01/data01/shome/cheidegg/o/2016-10-04_leptonMVAtraining/trees_80X/"
#F="-q all.q --direct" #"-F" 
#python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules mvaSUSY_80X_TTZ_decoupleAndBTagCut
