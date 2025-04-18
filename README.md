# Discovery Finder

このリポジトリは、ドローン航路のあり方に係る調査・研究として、ドローン航路システムに係るDiscovery Finderのサンプルを公開しています。

## 目次

- [システム概要](#システム概要)
- [構築と設定](#構築と設定)
- [起動方法](#起動方法)
- [ライセンス](#ライセンス)
- [免責事項](#免責事項)

## システム概要

Discovery Finderはドローン航路システムのドメインからドローン航路のDiscovery ServiceのURLを見つけるための機能です。

## 構築と設定

### 設定変更
以下のファイルに、ディスカバリーファインダ起動時から登録されるディスカバリーサービスの情報を記載できます。  
`data/discovery_service_db.csv`  

例
```csv
domain,url
uasl-example1.com,https://uasl-discovery-service.com
uasl-example2.com,https://uasl-discovery-service.com
```
※ドローン航路のディスカバリーサービスのURLを’https://uasl-discovery-service.com’とした例です。


## 起動方法

このパッケージのルートディレクトリで以下を実行します。

```bash
# building the image
docker build -t discovery_finder .

# starting up a container
docker run -p 8081:8080 -v $(pwd)/data:/data discovery_finder
```

## ライセンス

- 本リポジトリはMITライセンスで提供されています。
- ソースコードおよび関連ドキュメントの著作権はIntentExchange株式会社に帰属します。

## 免責事項
- 本リポジトリの内容は予告なく変更・削除する可能性があります。
- 本リポジトリの利用により生じた損失及び損害等について、いかなる責任も負わないものとします。


