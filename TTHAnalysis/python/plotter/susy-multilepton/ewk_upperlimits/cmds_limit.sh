#!/bin/bash


T="/mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees"
L="10."
O="/afs/cern.ch/user/c/cheidegg/www/heppy/2016-04-25_ewk8tev_upperlimits_pt/limit10fb"
D="susy-multilepton/ewk_upperlimits"
C="SR"
B="60,.5,60.5"
#B="36,.5,36.5"

# default: MC fakes, RA7 lepton ID
OPTIONS=" --asimov -P $T --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --neg --s2v --tree treeProducerSusyMultilepton -F sf/t {P}/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWK/evVarFriend_{cname}.root -f -j 8 --od $O -W 'vtxWeight_Loop' -l $L -p data -p _standard_prompt_.* -p _matched_fakes_.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"
# FR method on MC
#OPTIONS=" --asimov -P $T --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --neg --s2v --tree treeProducerSusyMultilepton -F sf/t {P}/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWK_good/evVarFriend_{cname}.root -f -j 8 --od $O -W 'vtxWeight_Loop' -l $L -p data -p _standard_prompt_.* -p _standard_fakes_.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"
# TTH lepton MVA ID
#OPTIONS=" --asimov -P $T --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --neg --s2v --tree treeProducerSusyMultilepton -F sf/t {P}/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWKmva/evVarFriend_{cname}.root -f -j 8 --od $O -W 'vtxWeight_Loop' -l $L -p data -p _standard_prompt_.* -p _matched_fakes_.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"
# MET > 30
#OPTIONS=" --asimov -P $T --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --neg --s2v --tree treeProducerSusyMultilepton -F sf/t {P}/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWKmet30/evVarFriend_{cname}.root -f -j 8 --od $O -W 'vtxWeight_Loop' -l $L -p data -p _standard_prompt_.* -p _matched_fakes_.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"
# MET > 40
#OPTIONS=" --asimov -P $T --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --neg --s2v --tree treeProducerSusyMultilepton -F sf/t {P}/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWKmet40/evVarFriend_{cname}.root -f -j 8 --od $O -W 'vtxWeight_Loop' -l $L -p data -p _standard_prompt_.* -p _matched_fakes_.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"
# MET > 60
#OPTIONS=" --asimov -P $T --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --neg --s2v --tree treeProducerSusyMultilepton -F sf/t {P}/leptonJetReCleanerSusyRA7/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWKmet60/evVarFriend_{cname}.root -f -j 8 --od $O -W 'vtxWeight_Loop' -l $L -p data -p _standard_prompt_.* -p _matched_fakes_.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"
# PT CHANGE
#OPTIONS=" --asimov -P $T --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --neg --s2v --tree treeProducerSusyMultilepton -F sf/t {P}/leptonJetReCleanerSusyRA7pt/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWKpt/evVarFriend_{cname}.root -f -j 8 --od $O -W 'vtxWeight_Loop' -l $L -p data -p _standard_prompt_.* -p _matched_fakes_.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.*"



function makeCard_2lss {
    local EXPR=$1; local BINS=$2; local DIR=$3; local OUT=$4; local GO=$5

    CMD="python makeShapeCardsSusy.py $D/mca_ewkino.txt $D/cuts_ewkino.txt \"$EXPR\" \"$BINS\" $D/systs_dummy.txt -o $OUT $GO"
    echo $CMD
    eval $CMD

}

makeCard_2lss $C $B $D SR "$OPTIONS";
echo "Done at $(date)";






#if [[ "$1" == "--pretend" ]]; then
#    PRETEND=1; shift;
#fi;
#
#if [[ "$1" == "ra5" ]]; then
#
#elif [[ "$1" == "ra5_MI_highHT" ]]; then
#    SYSTS="susy-multilepton/syst/susyRa5_MI_highHT.txt"
#    CnC_expr="1"
#    CnC_bins="1,0.5,1.5"
#
#    if [[ "$3" == "HT" ]]; then
#    makeCard_2lss $CnC_expr $CnC_bins $SYSTS SR_$2_HT$4 "$OPTIONS -A alwaystrue HT300 htJet40j_Mini>300 -A alwaystrue SR_$2 SR==$2 --postfix-pred _sig_.**=normTo1Observed -A alwaystrue HT_$4 htJet40j_Mini>$4";
#    elif [[ "$3" == "MET" ]]; then
#    makeCard_2lss $CnC_expr $CnC_bins $SYSTS SR_$2_MET$4 "$OPTIONS -A alwaystrue HT300 htJet40j_Mini>300 -A alwaystrue SR_$2 SR==$2 --postfix-pred _sig_.**=normTo1Observed -A alwaystrue MET_$4 met_pt>$4";
#    fi
#    echo "Done at $(date)";
#
#function combineCardsSmart {
#    CMD=""
#    for C in $*; do
#        # missing datacards 
#        test -f $C || continue;
#        # datacards with no event yield
#        grep -q "observation 0.0$" $C && continue
#        CMD="${CMD} $(basename $C .card.txt)=$C ";
#    done
#    if [[ "$CMD" == "" ]]; then
#        echo "Not any card found in $*" 1>&2 ;
#    else
#        combineCards.py $CMD
#    fi
#}
#elif [[ "$1" == "2lss-2012" ]]; then
#    OPTIONS=" $OPTIONS -F sf/t $T/1_susyVars_2lssInc_v0/evVarFriend_{cname}.root "
#    SYSTS="syst/susyDummy.txt"
#    CnC_expr="1+4*(met_pt>120)+(htJet40j>400)+2*(nJet40>=4)"
#    CnC_bins="[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5]"
#    MOD=inc;
#
#    echo "Making individual datacards"
#    for LL in ee em mm; do for LPt in 2020; do for SR in 0X 1X 2X+; do
#        echo " --- CnC2012_${SR}_${LL} ---"
#        #makeCard_2lss $CnC_expr $CnC_bins $SYSTS CnC2012_${SR}_${LL} "$OPTIONS";
#    done; done; done
#    echo "Making combined datacards"
#    for D in $OUTDIR/T[0-9]*; do
#        test -f $D/CnC2012_0X_ee.card.txt || continue
#        (cd $D;
#            for SR in 0X 1X 2X+; do
#                combineCards.py CnC2012_${SR}_{ee,em,mm}.card.txt >  CnC2012_${SR}.card.txt
#            done
#            combineCards.py CnC2012_{0X,1X,2X+}.card.txt >  CnC2012.card.txt
#        );
#        echo "Made combined card $D/CnC2012.card.txt"
#    done
#    echo "Done at $(date)";
#
#elif [[ "$1" == "2lss-2015" ]]; then
#    OPTIONS=" $OPTIONS -F sf/t $T/1_susyVars_2lssInc_v0/evVarFriend_{cname}.root "
#    SYSTS="syst/susyDummy.txt"
#    CnC_expr="1+4*(met_pt>120)+(htJet40j>400)+2*(nJet40>=4)"
#    CnC_bins="[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5]"
#    MOD=inc;
#
#    echo "Making individual datacards"
#    for LL in ee em mm; do for LPt in hh hl ll; do for SR in 0X 1X 2X 3X 2X+; do
#    #for LL in ee em mm; do for LPt in hh hl ll ; do for SR in 0Xs 1Xs 2Xs 3Xs; do
#        echo " --- CnC2015_${SR}_${LL}_${LPt} ---"
#        makeCard_2lss $CnC_expr $CnC_bins $SYSTS CnC2015_${SR}_${LL}_${LPt} "$OPTIONS";
#    done; done; done
#    #exit
#    echo "Making combined datacards"
#    for D in $OUTDIR/T[0-9]*; do
#        test -f $D/CnC2015_0X_ee_hh.card.txt || continue
#        (cd $D && echo "    $D";
#        for SR in 0X 1X 2X 3X 2X+; do
#        #for SR in 0Xs 1Xs 2Xs 3Xs; do
#            combineCardsSmart CnC2015_${SR}_{ee,em,mm}_hh.card.txt >  CnC2015_${SR}_hh.card.txt
#            combineCardsSmart CnC2015_${SR}_{ee,em,mm}_{hh,hl,ll}.card.txt >  CnC2015_${SR}.card.txt
#        done
#        combineCardsSmart CnC2015_{0X,1X,2X+}.card.txt   >  CnC2015_2b.card.txt
#        combineCardsSmart CnC2015_{0X,1X,2X+}_hh.card.txt   >  CnC2015_2b_hh.card.txt
#        combineCardsSmart CnC2015_{0X,1X,2X,3X}_hh.card.txt >  CnC2015_3b_hh.card.txt
#        combineCardsSmart CnC2015_{0X,1X,2X,3X}.card.txt >  CnC2015_3b.card.txt
#        #combineCardsSmart CnC2015_{0Xs,1Xs,2Xs,3Xs}_hh.card.txt >  CnC2015_3bs_hh.card.txt
#        #combineCardsSmart CnC2015_{0Xs,1Xs,2Xs,3Xs}.card.txt >  CnC2015_3bs.card.txt
#        )
#    done
#    echo "Done at $(date)";
#
#elif [[ "$1" == "2lss-2015x" ]]; then
#    OPTIONS=" $OPTIONS -F sf/t $T/1_susyVars_2lssInc_v0/evVarFriend_{cname}.root "
#    SYSTS="syst/susyDummy.txt"
#    CnC_expr="1+4*(met_pt>120)+(htJet40j>400)+2*(nJet40>=4)"
#    CnC_bins="[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5]"
#    MOD=excl;
#
#    echo "Making individual datacards"
#    for LL in ee em mm 3l; do for LPt in hh hl ll; do for SR in 0X 1X 2X 3X; do
#        echo " --- CnC2015X_${SR}_${LL}_${LPt} ---"
#        makeCard_2lss $CnC_expr $CnC_bins $SYSTS CnC2015X_${SR}_${LL}_${LPt} "$OPTIONS";
#    done; done; done
#    #exit
#    echo "Making combined datacards"
#    for D in $OUTDIR/T[0-9]*; do
#        test -f $D/CnC2015X_0X_ee_hh.card.txt || continue
#        (cd $D && echo "    $D";
#        for SR in 0X 1X 2X 3X; do
#            combineCardsSmart CnC2015X_${SR}_{ee,em,mm}_hh.card.txt >  CnC2015X_${SR}_hh.card.txt
#            combineCardsSmart CnC2015X_${SR}_{ee,em,mm}_{hh,hl,ll}.card.txt >  CnC2015X_${SR}.card.txt
#            combineCardsSmart CnC2015X_${SR}_{ee,em,mm,3l}_hh.card.txt >  CnC2015X_${SR}_hh_w3l.card.txt
#            combineCardsSmart CnC2015X_${SR}_{ee,em,mm,3l}_{hh,hl,ll}.card.txt >  CnC2015X_${SR}_w3l.card.txt
#        done
#        combineCardsSmart CnC2015X_{0X,1X,2X,3X}_hh.card.txt >  CnC2015X_3b_hh.card.txt
#        combineCardsSmart CnC2015X_{0X,1X,2X,3X}.card.txt >  CnC2015X_3b.card.txt
#        combineCardsSmart CnC2015X_{0X,1X,2X,3X}_hh_w3l.card.txt >  CnC2015X_3b_hh_w3l.card.txt
#        combineCardsSmart CnC2015X_{0X,1X,2X,3X}_w3l.card.txt >  CnC2015X_3b_w3l.card.txt
#        )
#    done
#    echo "Done at $(date)";
#fi

