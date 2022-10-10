Elliptic Membrane
=================

問題の説明
----------

圧力を負荷された楕円形状に発生する応力を確認するベンチマークです。The Standard NAFEMS BenchmarksにLE1として掲載されています。

条件
----

ベンチマークに使用するメッシュパターンはCoarse modelとFine modelの2種類としました。

使用した要素は1次要素、2次要素およびそれらの低減要素です。

Coarse modelのメッシュは次の通りです。

.. figure:: elliptic_membrane_coarse.png

Fine modelのメッシュは次の通りです。

.. figure:: elliptic_membrane_fine.png

条件図を次に示します。DCはY軸並進成分を固定、ABはX軸並進成分を固定します。

.. figure:: elliptic_membrane_bc.png

圧力を分布荷重でなく、節点荷重で入力する場合は次の値を使ってください。

.. table:: Coarse modelの1次要素での節点荷重での入力値

   ================ ================ ================
   荷重負荷点          X方向荷重         Y方向荷重
   ================ ================ ================
   P1               0.22541650839261 0.89157542285781 
   P2               0.70102081859851 1.41645978746927 
   P3               1.14962590851575 0.73350821250962 
   P4               0.67402159830985 0.20862384789816 
   ================ ================ ================

.. todo::
   mfrhs.evalを使用する。

.. table:: Coarse modelの1次要素での節点荷重での入力値(GetFEM)

   ================ ================ ================ ======= =======
   荷重負荷点          X方向荷重         Y方向荷重    Error   Error
   ================ ================ ================ ======= =======
   P1               0.22539711       0.89149999       - 0.01% - 0.01%
   P2               0.70099997       1.41638279       - 0.00% - 0.01%
   P3               1.14960289       0.73350000       - 0.00% - 0.00%
   P4               0.67400002       0.20861721       - 0.00% - 0.00%
   ================ ================ ================ ======= =======

.. figure:: elliptic_membrane_force_point_number.png

.. table:: Coarse modelの2次要素での節点荷重での入力値

   ================ ================ ================
   荷重負荷点          X方向荷重         Y方向荷重
   ================ ================ ================
   P1               0.07573283517252 0.29954121383850 
   P2               0.30293134069007 1.19816485535401 
   P3               0.23539958078805 0.47575193464905 
   P4               0.63866698246212 0.70484288324220 
   P5               0.38679458389610 0.24651155939748 
   P6               0.90851135312226 0.28120335434771 
   P7               0.22712783828057 0.07030083858693 
   ================ ================ ================

.. table:: Coarse modelの2次要素での節点荷重での入力値(GetFEM)

   ================ ================ ================ ======= =======
   荷重負荷点          X方向荷重         Y方向荷重    Error   Error
   ================ ================ ================ ======= =======
   P1               1.60599000e-03   3.23130648e-01   -97.88%   7.88%
   P2               3.00529480e-01   1.18866666e+00   - 0.79% - 0.79%
   P3               2.71656828e-01   4.91136831e-01   +13.35% + 3.23%
   P4               6.34137153e-01   6.99843727e-01   - 0.71% - 0.71%
   P5               4.03582216e-01   2.67912545e-01   + 4.34% + 8.68%
   P6               8.98666700e-01   2.78156280e-01   - 1.08% - 1.08%
   P7               2.39821632e-01   1.15331000e-03   + 5.59% -98.36%
   ================ ================ ================ ======= =======

.. figure:: elliptic_membrane_force_point_number_2nd_order.png

入力する物性値は次の通りです。

.. table:: 入力した材料物性

   ========== ==========
   材料物性   入力値
   ========== ==========
   ヤング率   210000 MPa
   ポアソン比 0.3
   要素種別    平面応力要素
   厚さ       0.1 mm
   ========== ==========

結果と考察
----------

比較する結果はD点のY方向応力です。参照値は92.7MPaです。比較結果を示します。

1次三角形要素Coarse modelの結果は次の通りです。

.. table:: Results using first-order triangular elements (Coarse model)
   :widths: auto

   =============== ====== =========== ===== ===== ====== =======
   Solver          Mesh   Type        Order Shape Result Error
   =============== ====== =========== ===== ===== ====== =======
   Reference value -      -           -     -     92.7   ‐ 
   Commercial code Coarse CPS3        1     tria  52.9   -42.90%
   Calculix 2.18   Coarse CPS3        1     tria  53.3   -42.50%
   Code-Aster 14.4 Coarse C_PLAN      1     tria  52.9   -42.90%
   FrontISTR v5.2  Coarse 231         1     tria  52.9   -42.90%
   GetFEM 5.4      Coarse FEM_PK(2,1) 1     tria  91.8   - 0.01%
   =============== ====== =========== ===== ===== ====== =======
   
1次四角形要素Coarse modelの結果は次の通りです。

.. table:: Results using first-order quadrilateral elements (Coarse model)
   :widths: auto

   =============== ====== =========== ===== ===== ====== =======
   Solver          Mesh   Type        Order Shape Result Error   
   =============== ====== =========== ===== ===== ====== =======
   Reference value -      -           -     -     92.7   ‐       
   Commercial code Coarse CPS4        1     quad  70.6   -23.90% 
   Calculix 2.18   Coarse CPS4        1     quad  69.7   -24.80%
   Code-Aster 14.4 Coarse C_PLAN      1     quad  70.6   -23.90% 
   FrontISTR v5.2  Coarse 241         1     quad  70.6   -23.90% 
   GetFEM 5.4      Coarse FEM_QK(2,1) 1     quad
   =============== ====== =========== ===== ===== ====== =======

2次三角形要素Coarse modelの結果は次の通りです。

.. table:: Results using second-order triangular elements (Coarse model)
   :widths: auto

   =============== ====== =========== ===== ===== ======= ======
   Solver          Mesh   Type        Order Shape Result  Error 
   =============== ====== =========== ===== ===== ======= ======  
   Reference value -      -           -     -     92.7    ‐       
   Commercial code Coarse CPS6        2     tria  89.9    -3.00%  
   Calculix 2.18   Coarse CPS6        2     tria  90.1    -2.80%  
   Code-Aster 14.4 Coarse C_PLAN      2     tria  89.9    -3.00%  
   FrontISTR v5.2  Coarse 232         2     tria  Not run -     
   GetFEM 5.4      Coarse FEM_PK(2,2) 2     tria  99.3
   =============== ====== =========== ===== ===== ======= ======

2次四角形要素Coarse modelの結果は次の通りです。

.. table:: Results using second-order quadrilateral elements (Coarse model)
   :widths: auto

   =============== ====== ==================== ===== ===== ====== ======
   Solver          Mesh   Type                 Order Shape Result Error 
   =============== ====== ==================== ===== ===== ====== ======
   Reference value -      -                    -     -     92.7   ‐     
   Commercial code Coarse CPS8                 2     quad  85.7   -7.50%
   Calculix 2.18   Coarse CPS8                 2     quad  85.2   -8.10%
   Code-Aster 14.4 Coarse C_PLAN               2     quad  87.8   -5.30%
   FrontISTR v5.2  Coarse 242                  2     quad  86.8   -6.40%
   GetFEM 5.4      Coarse FEM_Q2_INCOMPLETE(2) 2     quad
   =============== ====== ==================== ===== ===== ====== ======

1次四角形低減要素Coarse modelの結果は次の通りです。

.. table:: Results using first-order reduced quadrilateral elements (Coarse model)
   :widths: auto

   =============== ====== ========= ========== ===== ====== ========
   Solver          Mesh   Type      Order      Shape Result Error    
   =============== ====== ========= ========== ===== ====== ========
   Reference value -      -         -          -     92.7   ‐        
   Commercial code Coarse CPS4R     1(reduced) quad  48     -48.20%  
   Calculix 2.18   Coarse CPS4R     1(reduced) quad  72.5   -21.80%  
   Code-Aster 14.4 Coarse C_PLAN_SI 1(reduced) quad  -33.1  -135.70%
   GetFEM 5.4      Coarse 
   =============== ====== ========= ========== ===== ====== ======== 

2次四角形低減要素Coarse modelの結果は次の通りです。

.. table:: Results using second-order reduced quadrilateral elements (Coarse model)
   :widths: auto

   =============== ====== ========= ========== ===== ====== ======
   Solver          Mesh   Type      Order      Shape Result Error  
   =============== ====== ========= ========== ===== ====== ======
   Reference value -      -         -          -     92.7   ‐      
   Commercial code Coarse CPS8R     2(reduced) quad  85.8   -7.50% 
   Calculix 2.18   Coarse CPS8R     2(reduced) quad  85.6   -7.70% 
   Code-Aster 14.4 Coarse C_PLAN_SI 2(reduced) quad  86.2   -7.10%
   GetFEM 5.4      Coarse
   =============== ====== ========= ========== ===== ====== ====== 

1次三角形要素Fine modelの結果は次の通りです。

.. table:: Results using first-order triangular elements (Fine model)
   :widths: auto

   =============== ==== =========== ===== ===== ====== =======
   Solver          Mesh Type        Order Shape Result Error   
   =============== ==== =========== ===== ===== ====== =======
   Reference value -    -            -    -     92.7   ‐       
   Commercial code Fine CPS3         1    tria  72.9   -21.30% 
   Calculix 2.18   Fine CPS3         1    tria  73.2   -21.00% 
   Code-Aster 14.4 Fine C_PLAN       1    tria  72.9   -21.30% 
   FrontISTR v5.2  Fine 231          1    tria  73     -21.30%
   GetFEM 5.4      Fine FEM_PK(2,1)  1    tria
   =============== ==== =========== ===== ===== ====== =======

1次四角形要素Fine modelの結果は次の通りです。

.. table:: Results using first-order quadrilateral elements (Fine model)
   :widths: auto

   =============== ==== =========== ===== ===== ====== ======
   Solver          Mesh Type        Order Shape Result Error   
   =============== ==== =========== ===== ===== ====== ======
   Reference value -    -           -     -     92.7   ‐       
   Commercial code Fine CPS4        1     quad  85.4   -7.90% 
   Calculix 2.18   Fine CPS4        1     quad  85.6   -7.70%  
   Code-Aster 14.4 Fine C_PLAN      1     quad  85.4   -7.90%  
   FrontISTR v5.2  Fine 241         1     quad  86.9   -6.30%
   GetFEM 5.4      Fine FEM_QK(2,1) 1     quad
   =============== ==== =========== ===== ===== ====== ======

2次三角形要素Fine modelの結果は次の通りです。

.. table:: Results using second-order triangular elements (Fine model)
   :widths: auto

   =============== ==== =========== ===== ===== ======= =====
   Solver          Mesh Type        Order Shape Result  Error
   =============== ==== =========== ===== ===== ======= =====
   Reference value -    -           -     -     92.7    ‐       
   Commercial code Fine CPS6        2     tria  93.5    0.90%   
   Calculix 2.18   Fine CPS6        2     tria  93.7    1.10%   
   Code-Aster 14.4 Fine C_PLAN      2     tria  93.5    0.90%   
   FrontISTR v5.2  Fine 232         2     tria  Not Run -    
   GetFEM 5.4      Fine FEM_PK(2,2) 2     tria
   =============== ==== =========== ===== ===== ======= =====   

2次四角形要素Fine modelの結果は次の通りです。

.. table:: Results using second-order quadrilateral elements (Fine model)
   :widths: auto

   =============== ==== ==================== ===== ===== ====== =======
   Solver          Mesh Type                 Order Shape Result Error   
   =============== ==== ==================== ===== ===== ====== =======
   Reference value -    -                    -     -     92.7   ‐       
   Commercial code Fine CPS8                 2     quad  92     -0.70%  
   Calculix 2.18   Fine CPS8                 2     quad  93     0.30%   
   Code-Aster 14.4 Fine C_PLAN               2     quad  92.2   -0.50%  
   FrontISTR v5.2  Fine 242                  2     quad  77.2   -16.80%
   GetFEM 5.4      Fine FEM_Q2_INCOMPLETE(2) 2     quad
   =============== ==== ==================== ===== ===== ====== =======

1次四角形低減要素Fine modelの結果は次の通りです。

.. table:: Results using first-order reduced quadrilateral elements (Fine model)
   :widths: auto

   =============== ==== =========== ========== ===== ====== =======
   Solver          Mesh Type        Order      Shape Result Error  
   =============== ==== =========== ========== ===== ====== =======
   Reference value -    -           -          -     92.7   ‐      
   Commercial code Fine CPS4R       1(reduced) quad  62.6   -32.50%
   Calculix 2.18   Fine CPS4R       1(reduced) quad  61.6   -33.50%
   Code-Aster 14.4 Fine C_PLAN_SI   1(reduced) quad  58.2   -37.20%
   GetFEM 5.4      Fine FEM_QK(2,1) 1(reduced) quad
   =============== ==== =========== ========== ===== ====== =======

2次四角形低減要素Fine modelの結果は次の通りです。

.. table:: Results using second-order reduced quadrilateral elements (Fine model)
   :widths: auto

   =============== ==== ==================== ========== ===== ====== ======
   Solver          Mesh Type                 Order      Shape Result Error 
   =============== ==== ==================== ========== ===== ====== ======
   Reference value -    -                    -          -     92.7   ‐     
   Commercial code Fine CPS8R                2(reduced) quad  92.5   -0.20%
   Calculix 2.18   Fine CPS8R                2(reduced) quad  92.6   -0.10%
   Code-Aster 14.4 Fine C_PLAN_SI            2(reduced) quad  92.5   -0.20%
   GetFEM 5.4      Fine FEM_Q2_INCOMPLETE(2) 2(reduced) quad
   =============== ==== ==================== ========== ===== ====== ======

最も誤差が少なかったCalculixを使用した2次四角形低減要素のY方向応力コンタを次に示します。

.. figure:: elliptic_membrane_ystress_contour.png
