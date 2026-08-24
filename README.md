# NextDNS Home Adblock

NextDNSを使って、自宅ネットワークと端末のDNS広告・トラッカー遮断を管理するためのリポジトリです。

## 目的

- 広告・トラッカードメインのDNSレベル遮断
- 端末別のクエリ／ブロック状況の確認
- Allowlist／Denylistの変更履歴管理
- 導入後の疎通・遮断テストを再現可能にする

## 現在地

- GitHubリポジトリ: 作成済み
- このMacの現在のDNS: Cloudflare (`1.1.1.1`, `1.0.0.1`)
- NextDNS: 未設定（`test.nextdns.io` は `unconfigured`）
- NextDNSアカウント設定: Chrome制御の再接続待ち

詳細は [docs/current-state.md](docs/current-state.md) を参照してください。

## 最小確認

NextDNSアカウントへログインせず、現在のmacOS resolverと適用状態だけを確認できます。

```bash
scutil --dns
curl -fsS https://test.nextdns.io
```

`unconfigured` は未設定を示す観測結果であり、設定変更は行いません。導入・検証・
ルーター展開の順序は [docs/current-state.md](docs/current-state.md) を正本にします。

## セキュリティ

NextDNS Configuration ID、APIキー、認証情報、実IPアドレス、端末識別情報はコミットしません。
