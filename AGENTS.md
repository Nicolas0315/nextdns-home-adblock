# nextdns-home-adblock

- 現在は設定・実装・CIのない運用ドキュメントリポジトリ。状態と導入順は `docs/current-state.md` を正本とする。
- Configuration ID、APIキー、実IP、端末識別子はリポジトリに記録しない。
- `scutil --dns` はローカル確認、`curl -fsS https://test.nextdns.io` はNextDNSへの認証不要な外部HTTPS read。いずれも設定変更はせず、結果をpaste/commitしない。ルーター展開の手順はここに自動化しない。
