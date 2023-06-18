FrontISTR
=========

FrontISTRはオープンソースの大規模並列計算に対応する構造解析ソルバです。
WindowsやLinuxのPCクラスタおよび超並列のスパコンにも対応可能です。

FrontISTRはこちらのサイトで公開されています。

https://www.frontistr.com/index.php

インストール
~~~~~~~~~~~~

Ubuntu（LinuxネイティブもしくはWSL）
------------------------------------

`公式ページ <https://www.frontistr.com/download/>`_ からダウンロードができます。
Ubuntuはdebコマンドが用意されており、コピペでインストールできます。
ただし、Ubuntu-22.04だとエラーが出てインストールは実行できませんでした。

Ubuntu-20.04の場合は次のコマンドになります。

.. code-block:: 

    sudo apt update
    curl https://frontistr-commons.gitlab.io/FrontISTR/release/deb/FrontISTR_master-0+ubuntu2004_amd64.deb -O && sudo apt-get install -y ./FrontISTR_master-0+ubuntu2004_amd64.deb

計算実行
~~~~~~~~

計算実行コマンドの例を示します。
コマンドを実行する場合はインプットを置いているフォルダに移動してからコマンドを実行します。
この場合は1CPUでの計算になります。

.. code-block::

    fistr1

並列計算の場合は次のようにコマンドを実行します。
この場合は4並列の計算を実行します。

.. code-block:: 

    fistr1 -t 4