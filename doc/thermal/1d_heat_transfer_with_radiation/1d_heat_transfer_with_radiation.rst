One dimensional heat transfer with radiation
============================================

問題の説明
----------

1次元方向の熱伝導解析で発生する温度を確認するベンチマークです。The Standard NAFEMS BenchmarksにT2として掲載されています。

条件
----

ベンチマークに使用するメッシュは次の通りです。

.. figure:: 1d_heat_transfer_with_radiation_mesh.png

条件図を次に示します。A端は1000K、B端は300K常温への放射を定義します。その他は断熱とします。

.. figure:: 1d_heat_transfer_with_radiation_bc.png

入力する物性値は次の通りです。

.. table:: 入力した材料物性

   ======================= ==================
   材料物性                入力値
   ======================= ==================
   熱伝導率                55.6 W/m℃
   比熱                    460.0 J/kg℃
   密度                    7850 kg/m^3
   B端の放射率                  0.98
   ステファンボルツマン係数 5.67E-8 Wm^2・K^-4
   ======================= ==================

結果と考察
----------

比較する結果はB端の温度です。参照値は927Kです。比較結果を示します。

.. table:: Results using first-order triangular elements (Coarse model)
   :widths: auto

   =============== ====== ===== ===== ======= =======
   Solver          Type   Order Shape Result  Error
   =============== ====== ===== ===== ======= =======
   Reference value -      -     -     927    ‐ 
   Commercial code DC2D4  1     quad  927.009 0.00%
   Commercial code DC1D2  1     link  927.009 0.00%
   Calculix 2.18   CPS4   1     quad  927.008 0.00%
   Calculix 2.18   B31    1     bar   927.008 0.00%
   =============== ====== ===== ===== ======= =======

Calculix 2.18のCPS4を使用した場合の温度分布のコンタを参考として次に示します。

.. figure:: 1d_heat_transfer_with_radiation_result.png
