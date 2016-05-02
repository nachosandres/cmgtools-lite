#!/bin/bash


T="/mnt/t3nfs01/data01/shome/cheidegg/o/2016-03-18_ewktrees"
L="10."
O="/afs/cern.ch/user/c/cheidegg/www/heppy/2016-04-25_ewk8tev_upperlimits/srscan10fb/"
D="susy-multilepton/ewk_upperlimits"
C="SR"
BS=( "1,0.5,1.5" "1,1.5,2.5" "1,2.5,3.5" "1,3.5,4.5" "1,4.5,5.5" "1,5.5,6.5" "1,6.5,7.5" "1,7.5,8.5" "1,8.5,9.5" "1,9.5,10.5" "1,10.5,11.5" "1,11.5,12.5" "1,12.5,13.5" "1,13.5,14.5" "1,14.5,15.5" "1,15.5,16.5" "1,16.5,17.5" "1,17.5,18.5" "1,18.5,19.5" "1,19.5,20.5" "1,20.5,21.5" "1,21.5,22.5" "1,22.5,23.5" "1,23.5,24.5" "1,24.5,25.5" "1,25.5,26.5" "1,26.5,27.5" "1,27.5,28.5" "1,28.5,29.5" "1,29.5,30.5" "1,30.5,31.5" "1,31.5,32.5" "1,32.5,33.5" "1,33.5,34.5" "1,34.5,35.5" "1,35.5,36.5" "1,36.5,37.5" "1,37.5,38.5" "1,38.5,39.5" "1,39.5,40.5" "1,40.5,41.5" "1,41.5,42.5" "1,42.5,43.5" "1,43.5,44.5" "1,44.5,45.5" "1,45.5,46.5" "1,46.5,47.5" "1,47.5,48.5" "1,48.5,49.5" "1,49.5,50.5" "1,50.5,51.5" "1,51.5,52.5" "1,52.5,53.5" "1,53.5,54.5" "1,54.5,55.5" "1,55.5,56.5" "1,56.5,57.5" "1,57.5,58.5" "1,58.5,59.5" "1,59.5,60.5" )
SS=( "SR1" "SR2" "SR3" "SR4" "SR5" "SR6" "SR7" "SR8" "SR9" "SR10" "SR11" "SR12" "SR13" "SR14" "SR15" "SR16" "SR17" "SR18" "SR19" "SR20" "SR21" "SR22" "SR23" "SR24" "SR25" "SR26" "SR27" "SR28" "SR29" "SR30" "SR31" "SR32" "SR33" "SR34" "SR35" "SR36" "SR37" "SR38" "SR39" "SR40" "SR41" "SR42" "SR43" "SR44" "SR45" "SR46" "SR47" "SR48" "SR49" "SR50" "SR51" "SR52" "SR53" "SR54" "SR55" "SR56" "SR57" "SR58" "SR59" "SR60" )
#B="36,.5,36.5"

# default: MC fakes, RA7 lepton ID
OPTIONS=" --asimov -P $T --mcc susy-multilepton/ewk_upperlimits/mcc_susy_2lssinc_triggerdefs.txt --neg --s2v --tree treeProducerSusyMultilepton -F sf/t {P}/leptonJetReCleanerSusyRA7_good/evVarFriend_{cname}.root -F sf/t {P}/leptonChoiceEWK_good/evVarFriend_{cname}.root -f -j 8 -W 'vtxWeight_Loop' -l $L -p data -p _standard_prompt_.* -p _matched_fakes_.* -p _sig_TChiNeu_WZ_.* -p _sig_TChiNeu_SlepSneu_.* --od $O"



function makeCard_2lss {
    local EXPR=$1; local BINS=$2; local DIR=$3; local OUT=$4; local GO=$5

    CMD="python makeShapeCardsSusy.py $D/mca_ewkino.txt $D/cuts_ewkino.txt \"$EXPR\" \"$BINS\" $D/systs_dummy.txt -o $OUT $GO"
    echo $CMD
    eval $CMD

}

i=0
for B in ${BS[@]}; do

    bb=$B
    sr=${SS[$i]}
    makeCard_2lss $C $bb $D SR "$OPTIONS$sr";
    i=`echo $i +1 | bc`

done

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

