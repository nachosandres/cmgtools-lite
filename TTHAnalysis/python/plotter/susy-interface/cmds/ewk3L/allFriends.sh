## NEW DATA
#T="/mnt/t3nfs01/data01/shome/cheidegg/o/2017-01-24_signalMerger"
T="/mnt/t3nfs01/data01/shome/cheidegg/o/2017-01-24_signalSplitter/done"
#T="/mnt/t3nfs01/data01/shome/cheidegg/o/Prod23Jan"
#T="/mnt/t3nfs01/data01/shome/cheidegg/o/Signals26Jan"
#T="/mnt/t3nfs01/data01/shome/cheidegg/o/Signals05Feb"
#T="/mnt/t3nfs01/data01/shome/cheidegg/o/2017-01-27_ewkskims80X_M17_MERGED/"
#T="/mnt/t3nfs01/data01/shome/cheidegg/o/2017-01-27_ewkskims80X_M17_WZCR"
#T="/mnt/t3nfs01/data01/shome/cheidegg/o/2015-11-29_ewktrees80X_M17"
F="-F --direct -q all.q --nosplit"
#F="--direct --nosplit -q all.q"
#F="-F --accept DoubleMuon_Run2016F_23Sep2016_v1_runs_271036_284044 --direct"
#F="--accept TChiNeuSlepSneu_FD --direct --nosplit -q all.q" #"-F" 
#F="--accept DoubleEG_Run2016C_23Sep2016_v1_runs_271036_284044_part2 --exclude MET --exclude Tau --exclude JetHT -q 8nh --direct" #"-F" 

#python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules leptonJetReCleanerSusyEWK3L
#python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules leptonBuilderEWK
#python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules eventBTagWeight             --pretend

#python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules leptonJetReCleanerSusyEWK2L
python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules ISRWeightModule
#python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules bTagEventWeightFullSim --flags "-F sf/t {P}/leptonJetReCleanerSusyEWK2L/evVarFriend_{cname}.root" --accept TChi
#python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules bTagEventWeightFastSim --flags "-F sf/t {P}/leptonJetReCleanerSusyEWK2L/evVarFriend_{cname}.root" --accept TChi



#T="/mnt/t3nfs01/data01/shome/cheidegg/o/2016-10-04_leptonMVAtraining/trees_80X/"
#F="-q all.q --direct" #"-F" 
#python susy-interface/friendmaker.py 3l 3lA $T $T --bk --log $F --modules mvaSUSY_80X_TTZ_decoupleAndBTagCut
