# 「ニュースを自動収集してくれるTwitterbot」

## 概要
自分のTwitterアカウントのツイートを取得し、そのツイートに関連する
ニュース記事を集め、そのURLを自分のアカウントに送る。

## bot側でのツイート取得
本アカウントの最新ツイート 20 件を取得する。

## 関連するとは
取得したツイートを形態素解析し、その結果の中の固有名詞をキーワードとす
る。ツイートを取得した日とその一日前のニュース記事の中から、そのキーワー
ドが関連するニュース記事を集める。キーワードと関連するどうかは、記事の
トピックと一致するかで判断する。記事のトピックは、記事の本文を取り出し、
形態素解析して取り出した固有名詞とする。

## 使用するアプリケーション
・TwitterAPI
・形態素解析のためのMeCab


## 参考文献
[1]Jared(2013),"How To Write a Twitter Bot with Python and tweepy",
<https://getpocket.com/redirect?url=http%3A%2F%2Fwww.dototot.com%2Fhow-to-write-a-twitter-bot-with-python-and-tweepy%2F>

[2]YoshihitoAso「Ubuntu環境にMecabをインストールする方法」,
<https://gist.github.com/YoshihitoAso/9048005>

[3]"Package lxml :: Module etree :: Class _Element",
<http://lxml.de/api/lxml.etree._Element-class.html>

[4]HirofumiYashima(2014)「tweepy を使って、Python から Twitter API で遊ん
でみる」,<http://qiita.com/HirofumiYashima/items/9c826ef19dca9d4f9b32>

[5]Joshua Roesslein(2009)"tweepy.api ? Twitter API wrapper",
<http://tweepy.readthedocs.org/en/v3.4.0/api.html>

[6]aidiary(2010)「WindowsでMeCab Pythonを使う」,
<http://aidiary.hatenablog.com/entry/20101121/1290339360>

[7]mykysyk(2013)「python 現在時刻取得」,
<http://qiita.com/mykysyk@github/items/e15d7b2b1a988b8e29d4>

[8](2010,python-izm)「日付」,
<http://www.python-izm.com/contents/basis/date.shtml>

[9]kozo-ni(2009)「リストを引数sizeのリストに分割して、そのリストのリスト
を返す関数」,<http://d.hatena.ne.jp/kozo-ni/20090303>

[10]beatinaniwa(2014)「PythonでさくっとWebスクレイピングする (JavaScript読み込
みにも対応しつつ)」,<http://qiita.com/beatinaniwa/items/72b777e23ef2390e13f8>

[11]Dr_KayAi(2014)「Python: urllibはやっぱりなし。requestsを使いましょう」,
<http://dr-kayai.hatenablog.com/entry/2014/09/17/135359>
