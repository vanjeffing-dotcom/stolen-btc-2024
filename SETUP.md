# Setup — publishing the public statement repo

이 디렉토리(`recovery/site/`)는 `vanjeffing-dotcom/stolen-btc-2024` 리포의 콘텐츠입니다. 본 가이드는 리포 생성부터 GitHub Pages 활성화, MIRRORS 업데이트까지의 전체 흐름을 설명합니다.

## ⚠️ 무결성 (절대 깨지지 말 것)

다음 4개 파일은 **BIP-322 서명에 SHA-256 으로 봉인됨**. 수정 금지:

| 파일 | SHA-256 |
|------|---------|
| STATEMENT_KO.md | `d6c73c8dc51b5e0b6aa076d15a2fc9b4b9d19c3aaac0ba8ba7b3719272c27f93` |
| STATEMENT_EN.md | `7948e26829024685245479a94c18bdc5760eccbdd34daf7f1d0ade1e6bdd09e4` |
| EVIDENCE_KO.md  | `741390f29fdc6a847382e8762f717a7111fb2eb3b5e753af000c56b37c9039a0` |
| EVIDENCE_EN.md  | `77681db33a7ceb8b33020b1ed913bdba48cec075345bf800ec98e5285c99b5ca` |

업데이트가 필요한 모든 살아있는 정보(IPFS CID, OP_RETURN TXID, 미러 URL, 신고 접수번호 등)는 [`MIRRORS.md`](MIRRORS.md) 에만 기록. 푸시 전 매번 위 4개 해시가 일치하는지 확인.

## 1. GitHub 리포 생성

```bash
# 빈 private 리포를 vanjeffing-dotcom 계정에 만들기
gh repo create vanjeffing-dotcom/stolen-btc-2024 --private --description "Public statement of BTC theft 2024-11-05" --confirm

# 또는 웹 UI: https://github.com/new
#   - Repository name: stolen-btc-2024
#   - Owner: vanjeffing-dotcom
#   - Private: ✅
#   - Initialize: README/license/.gitignore 모두 ☐ (우리가 직접 제공)
```

## 2. 초기 푸시

```bash
cd /home/jsong/dev/jsong1230-github/20241106/recovery/site

# 봉인 파일 무결성 확인 (해시 4줄이 위 표와 정확히 일치해야 함)
sha256sum STATEMENT_KO.md STATEMENT_EN.md EVIDENCE_KO.md EVIDENCE_EN.md

git init -b main
git add .
git commit -m "Initial public statement (private — Phase 1-7 prep)"
git remote add origin git@github.com:vanjeffing-dotcom/stolen-btc-2024.git
git push -u origin main
```

## 3. GitHub Pages 활성화 (Phase 8 — 모든 신고가 자리잡은 후)

이 단계는 **즉시 실행하지 마세요**. 리포가 public 으로 전환되고, OP_RETURN 발행 직전에 활성화합니다.

```bash
# 리포 가시성 변경: private → public
gh repo edit vanjeffing-dotcom/stolen-btc-2024 --visibility public

# Pages 활성화
gh api repos/vanjeffing-dotcom/stolen-btc-2024/pages \
    --method POST \
    -F source.branch=main -F source.path=/
```

또는 웹 UI: Settings → Pages → Source: Deploy from a branch → main / root → Save.

활성화 후 1분 이내 라이브: `https://vanjeffing-dotcom.github.io/stolen-btc-2024`

## 4. 서명 메시지 (이미 완료됨)

`signed_message.txt` 가 이미 본 디렉토리에 포함되어 있으며, 검증 가능한 BIP-322 서명을 담고 있습니다. 추가 작업 없음.

검증:
```bash
python3 -c "
from bitcoinlib.keys import verify_message
msg = '''<signed_message.txt 의 [1] 블록 그대로>'''
sig = '<[2] 블록의 base64>'
print(verify_message(msg, sig, 'bc1qdxlazvvxhjkflmf8jjv7sfmtx3k0jnp35ug42d'))
"
```

## 5. IPFS 핀닝 → MIRRORS.md 업데이트

[../scripts/pin_to_ipfs.md](../scripts/pin_to_ipfs.md) 따라 Pinata + web3.storage + (선택)본인 노드 에 핀.

CID 획득 후:

```bash
# MIRRORS.md 의 IPFS 섹션에 CID 삽입 (자세한 sed 명령은 pin_to_ipfs.md 참조)
$EDITOR MIRRORS.md

# 봉인 파일 변경 없는지 다시 확인
sha256sum STATEMENT_KO.md STATEMENT_EN.md EVIDENCE_KO.md EVIDENCE_EN.md

# 푸시
git add MIRRORS.md
git commit -m "Add IPFS CID to MIRRORS.md (Pinata)"
git push
```

## 6. OP_RETURN 마커 발행 → MIRRORS.md 업데이트

[../scripts/op_return_builder.py](../scripts/op_return_builder.py) 로 PSBT 생성 → 서명 → 브로드캐스트.

마커 TXID 확보 후 MIRRORS.md 의 OP_RETURN 섹션 채우고 푸시.

## 7. 외부 통보

`../reports/` 디렉토리의 신고 양식 사용:

- Chainabuse, TRM Labs, Chainalysis
- ECRM (한국 사이버범죄 신고시스템)
- 국내 5대 거래소, 글로벌 6사
- 블록체인 익스플로러 (Blockchair 코멘트, Twitter 멘션)

각 통보에는 다음을 인용:
- 본 사이트 URL (Phase 8 후 public)
- IPFS CID (Phase 5 후)
- OP_RETURN 마커 TXID (Phase 6 후)
- 봉인 4개 파일의 해시 (수사기관·체인 분석 회사용 본인 확인 보조)
