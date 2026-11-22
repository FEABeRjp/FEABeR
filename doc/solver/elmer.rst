Elmer
=====

ElmerはフィンランドのCSCが開発しているオープンソースの有限要素解析ソフトウェアです。
音響のベンチマークでは、空気中の圧力波を計算するWaveSolverを固有値解析に使用します。

インストール
------------

配布パッケージは `Elmerの公式リリースページ <https://github.com/ElmerCSC/elmerfem/releases>`_ から入手できます。音響固有値解析にはElmer 26.2 Releaseを使用しました。

計算実行
--------

:doc:`ベンチマーク結果 </benchmark>` の「音響」から問題を選び、「計算データ」にある入力一式をダウンロードします。展開したディレクトリで次のコマンドを実行します。

.. code-block:: console

   ElmerSolver case.sif

実行後、``eigenvalues.dat`` に固有値が、``case_t0001.vtu`` に可視化用の音圧固有モードが出力されます。
