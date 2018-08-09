#!/bin/sh
LVL_3_LOC="EMD_201804"
LVL_2_LOC="SIG_201804"
LVL_1_LOC="CTPRVN_201804"
LVL_3_NM="kor_admin_3.topojson"
LVL_2_NM="kor_admin_2.topojson"
LVL_1_NM="kor_admin_1.topojson"
# UNJOINED = "unjoined"; # output unjoined
UNJOINED=""
INT_LOC="interim"
FIN_LOC="plot"
ENC_CD="euc-kr"
LVL_3_SIMP="3%"
LVL_2_SIMP="1%"
LVL_1_SIMP="0.1%"

cd data/original/$LVL_3_LOC; echo "Joining" *.shp
mapshaper encoding=$ENC_CD *.shp \
    -simplify keep-shapes $LVL_3_SIMP \
    -proj latlong \
    -join ../../$INT_LOC/kor_admin_3_ref_w_en.csv keys=EMD_CD,LVL_3_CD $UNJOINED \
    -o format=topojson ../../$INT_LOC/$LVL_3_NM

cd ../$LVL_2_LOC; echo "Joining" *.shp
mapshaper encoding=$ENC_CD *.shp \
    -simplify keep-shapes $LVL_2_SIMP \
    -proj latlong \
    -join ../../$INT_LOC/kor_admin_2_ref_w_en.csv keys=SIG_CD,LVL_2_CD $UNJOINED \
    -o format=topojson ../../$INT_LOC/$LVL_2_NM

cd ../$LVL_1_LOC; echo "Joining" *.shp
mapshaper encoding=$ENC_CD *.shp \
    -simplify keep-shapes $LVL_1_SIMP \
    -proj latlong \
    -join ../../$INT_LOC/kor_admin_1_ref_w_en.csv keys=CTPRVN_CD,LVL_1_CD $UNJOINED \
    -o format=topojson ../../$INT_LOC/$LVL_1_NM

cd ../..
mv -fv $INT_LOC/$LVL_3_NM $FIN_LOC/$LVL_3_NM
mv -fv $INT_LOC/$LVL_2_NM $FIN_LOC/$LVL_2_NM
mv -fv $INT_LOC/$LVL_1_NM $FIN_LOC/$LVL_1_NM
