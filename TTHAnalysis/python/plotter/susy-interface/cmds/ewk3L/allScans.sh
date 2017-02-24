#!/bin/bash

## IMPORTANT REMARK: In principle, one could run all models per config/region all together,
## but this will generate a lot of jobs which are all accessing the same background ROOT file.
## This kills memory and performance. Keep in mind to split as good and effective as possible
## to optimize performance.

T="/mnt/t3nfs01/data01/shome/cheidegg/o/2017-01-27_ewkskims80X_M17_MERGED/"
TT="/mnt/t3nfs01/data01/shome/cheidegg/o/2017-01-27_ewkskims80X_M17_WZCR"
#O="/mnt/t3nfs01/data01/shome/cheidegg/o/2016-10-14_ewk80X_allCardsNoTauSF"
O="/mnt/t3nfs01/data01/shome/cheidegg/o/2017-02-02_ewk80X_preapprovalScans"
#QUEUE="--pretend" #"-q all.q"
QUEUE="-q all.q" #"-q all.q"
#QUEUE="-q all.q@t3wn20.psi.ch all.q@t3wn22.psi.ch all.q@t3wn26.psi.ch all.q@t3wn21.psi.ch all.q@t3wn10.psi.ch"
#QUEUE="-q all.q@t3wn20.psi.ch all.q@t3wn22.psi.ch all.q@t3wn26.psi.ch all.q@t3wn21.psi.ch all.q@t3wn10.psi.ch all.q@t3wn16.psi.ch all.q@t3wn17.psi.ch all.q@t3wn29.psi.ch all.q@t3wn11.psi.ch all.q@t3wn36.psi.ch all.q@t3wn13.psi.ch all.q@t3wn14.psi.ch all.q@t3wn25.psi.ch all.q@t3wn37.psi.ch all.q@t3wn40.psi.ch all.q@t3wn35.psi.ch all.q@t3wn27.psi.ch all.q@t3wn38.psi.ch all.q@t3wn33.psi.ch all.q@t3wn31.psi.ch all.q@t3wn39.psi.ch all.q@t3wn32.psi.ch"
LUMI=35.9

#QUEUE="--pretend"


## background only first
#python susy-interface/scanmaker.py crwz crwz $TT $O -l $LUMI -o SR --models TChiWZ --bkgOnly --redoBkg --flags '-X blinding' $QUEUE --pretend
#python susy-interface/scanmaker.py 3l "3lA1;3lA2;3lB;3lC;3lD;3lE;3lF" $T $O -l $LUMI -o SR --models TChiWZ --bkgOnly --redoBkg --flags '-X blinding' --mca susy-ewkino/3l/mca_forScan.txt $QUEUE 
#python susy-interface/scanmaker.py 3l "4lG;4lH;4lI;4lJ;4lK" $T $O -l $LUMI -o SR --models TChiWZ --bkgOnly --redoBkg --flags '-X blinding' --mca susy-ewkino/4l/mca_forScan.txt $QUEUE 

## TChiWH
#python susy-interface/scanmaker.py crwz crwz $TT $O -l $LUMI -o SR --models TChiWH --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpV_FL_data_comb' --check
#python susy-interface/scanmaker.py 3l "3lA1;3lA2;3lB" $T $O -l $LUMI -o SR --models TChiWH --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpM_FL_data_comb' --check
#python susy-interface/scanmaker.py 3l "3lC;3lD;3lE;3lF" $T $O -l $LUMI -o SR --models TChiWH --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_tau_EWKino_Moriond2017_36p5fb.root --frMap tauFR_data' --check

## TChiWZ
#python susy-interface/scanmaker.py crwz crwz $TT $O -l $LUMI -o SR --models TChiWZ --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpV_FL_data_comb' --check 
#python susy-interface/scanmaker.py 3l "3lA1;3lA2" $T $O -l $LUMI -o SR --models TChiWZ --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpM_FL_data_comb' --check

## TChiSlepSnu_FD
#python susy-interface/scanmaker.py crwz crwz $TT $O -l $LUMI -o SR --models TChiSlepSnu_FD --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpV_FL_data_comb' --check
#python susy-interface/scanmaker.py 3l "3lA1;3lA2" $T $O -l $LUMI -o SR --models TChiSlepSnu_FD --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpM_FL_data_comb' --check

## TChiSlepSnu_FD_05
python susy-interface/scanmaker.py crwz crwz $TT $O -l $LUMI -o SR --models TChiSlepSnu_FD_05 --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpV_FL_data_comb' --check
python susy-interface/scanmaker.py 3l "3lA1;3lA2" $T $O -l $LUMI -o SR --models TChiSlepSnu_FD_05 --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpM_FL_data_comb' --check

## TChiSlepSnu_TD
#python susy-interface/scanmaker.py crwz crwz $TT $O -l $LUMI -o SR --models TChiSlepSnu_TD --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpV_FL_data_comb' --check
#python susy-interface/scanmaker.py 3l 3lB $T $O -l $LUMI -o SR --models TChiSlepSnu_TD --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpM_FL_data_comb' --check
#python susy-interface/scanmaker.py 3l "3lC;3lD;3lE;3lF" $T $O -l $LUMI -o SR --models TChiSlepSnu_TD --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_tau_EWKino_Moriond2017_36p5fb_Summer16.root --frMap data_ratio' --check

## TChiZZ4L
#python susy-interface/scanmaker.py crwz crwz $TT $O -l $LUMI -o SR --models TChiZZ4L --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpV_FL_data_comb' --check
#python susy-interface/scanmaker.py 3l "3lA1;3lA2;3lB" $T $O -l $LUMI -o SR --models TChiZZ4L --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpM_FL_data_comb' --check
#python susy-interface/scanmaker.py 3l "3lC;3lD;3lE;3lF" $T $O -l $LUMI -o SR --models TChiZZ4L --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_tau_EWKino_Moriond2017_36p5fb_Summer16.root --frMap data_ratio' --check
#python susy-interface/scanmaker.py 3l "4lG;4lH" $T $O -l $LUMI -o SR --models TChiZZ4L --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpM_FL_data_comb' --check
#python susy-interface/scanmaker.py 3l "4lI;4lJ;4lK" $T $O -l $LUMI -o SR --models TChiZZ4L --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpM_FL_data_comb' --check



## TESTING
#python susy-interface/scanmaker.py 3l 3lA $T $O -l $LUMI -o SR --models TChiWZ --bkgOnly --redoBkg --flags '-X blinding' --mca susy-ewkino/3l/mca_forScan.txt $QUEUE 
#python susy-interface/scanmaker.py 3l 3lA $T $O -l $LUMI -o SR --models TChiSlepSnu_FD --mca susy-ewkino/3l/mca_forScan.txt --flags '-X blinding' --sigOnly $QUEUE --postfix '--postfix-pred fakes_appldata*=fixFakePredictionForZeroEvts --frFile $CMSSW_BASE/src/CMGTools/TTHAnalysis/data/fakerate/fakerate_light_EWKino_Moriond2017_36p5fb.root --frMap FR_susy_wpM_FL_data_comb' --check
