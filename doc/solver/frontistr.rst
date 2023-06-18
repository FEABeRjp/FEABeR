FrontISTR
=========

FrontISTRはオープンソースの大規模並列計算に対応する構造解析ソルバです。
WindowsやLinuxのPCクラスタおよび超並列のスパコンにも対応可能です。

FrontISTRはこちらのサイトで公開されています。

https://www.frontistr.com/index.php

インストール
~~~~~~~~~~~~

Ubuntu（LinuxもしくはWSL）
------------------------------------

`公式ページ <https://www.frontistr.com/download/>`_ からダウンロードすることができます。
FrontISTR CommonsはFrontISTRをUbuntuで実行するインストールコマンドを用意しています。
ただし、2023年6月18日時点ではUbuntu-22.04においてコマンド実行時にエラーメッセージが表示されインストールを実行できません。

Ubuntu-20.04の場合のインストールコマンドを次に示します。

.. code-block:: 

    sudo apt update
    curl https://frontistr-commons.gitlab.io/FrontISTR/release/deb/FrontISTR_master-0+ubuntu2004_amd64.deb -O && sudo apt-get install -y ./FrontISTR_master-0+ubuntu2004_amd64.deb

計算実行
~~~~~~~~

計算を実行するためのコマンドを説明します。
コマンドを実行する際は、インプットファイルを保存したディレクトリでコマンドを実行します。
1CPUで計算を実行する際のコマンドを次に示します。

.. code-block::

    fistr1

並列計算の場合は `-t` オプションで並列数を指定します。
4CPUでの並列計算実行のコマンドを次に示します。

.. code-block:: 

    fistr1 -t 4