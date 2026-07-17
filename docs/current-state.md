# Current State

確認日: 2026-07-18 JST

## 参考にした構成

FabSceneの記事で紹介されたESP32-C3 DNSシンクホールの主要機能は、NextDNSで代替できます。

- DNSレベルの広告・トラッカー遮断
- 自動更新されるブロックリスト
- 端末別ログと分析
- 独自のAllowlist／Denylist

参考:

- https://fabscene.com/new/make/esp32-c3-dns-adblock-hash-in-flash/
- https://nextdns.io/

## 現在の検証結果

```text
macOS resolver: 1.1.1.1 / 1.0.0.1
NextDNS status: unconfigured
NextDNS app/CLI/profile: not found
```

## 次の作業

1. ChromeのDevTools接続を復旧する。
2. NextDNSにログインし、既存Configurationの有無を確認する。
3. 既存設定がなければ専用Configurationを作成する。
4. Privacy、Security、Loggingを最小構成で設定する。
5. macOS用の暗号化DNS構成を導入する。
6. `https://test.nextdns.io` とNextDNSログで適用を確認する。
7. ルーター全体への展開は機種・復旧手順を確認後に別途実施する。

## 変更しない情報

- Configuration ID
- APIキー／トークン
- NextDNSアカウント情報
- グローバルIPアドレス
- 個別端末名や識別子
