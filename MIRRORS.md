# Mirrors and Live References

> **무결성 모델 (Integrity Model)**
>
> 본 파일(`MIRRORS.md`)은 **서명 대상이 아닙니다**. 시간에 따라 변경됩니다.
>
> 암호학적으로 서명·고정된 4개 문서는 다음과 같이 SHA-256 으로 봉인되어 있으며, 그 봉인이 [`signed_message.txt`](signed_message.txt) 에 박혀 있습니다:
>
> | 파일 | SHA-256 |
> |------|---------|
> | STATEMENT_KO.md | `d6c73c8dc51b5e0b6aa076d15a2fc9b4b9d19c3aaac0ba8ba7b3719272c27f93` |
> | STATEMENT_EN.md | `7948e26829024685245479a94c18bdc5760eccbdd34daf7f1d0ade1e6bdd09e4` |
> | EVIDENCE_KO.md  | `741390f29fdc6a847382e8762f717a7111fb2eb3b5e753af000c56b37c9039a0` |
> | EVIDENCE_EN.md  | `77681db33a7ceb8b33020b1ed913bdba48cec075345bf800ec98e5285c99b5ca` |
>
> 본 파일은 미러·CID·TXID 같은 동적 정보만 다루므로, 자유롭게 업데이트해도 서명 무결성에는 영향이 없습니다.
>
> 누구든 위 4개 파일을 `sha256sum` 으로 다시 계산하여 봉인 해시와 대조함으로써 변조 여부를 즉시 확인 가능합니다.

---

## 1. Web 미러

| 채널 | URL | 상태 |
|------|-----|------|
| GitHub Pages | <https://vanjeffing-dotcom.github.io/stolen-btc-2024> | 🔒 Phase 8 완료 후 public 전환 예정 |
| (커스텀 도메인) | (TBD) | 미정 |

## 2. IPFS

### 디렉토리 CID (사이트 전체)

```
QmXgQfGEvDBtpCsXYyJ9UkaPkaPwc6uFugcNh6qKZVAV2f
```

게이트웨이 접근:
- <https://ipfs.io/ipfs/QmXgQfGEvDBtpCsXYyJ9UkaPkaPwc6uFugcNh6qKZVAV2f>
- <https://cloudflare-ipfs.com/ipfs/QmXgQfGEvDBtpCsXYyJ9UkaPkaPwc6uFugcNh6qKZVAV2f>
- <https://dweb.link/ipfs/QmXgQfGEvDBtpCsXYyJ9UkaPkaPwc6uFugcNh6qKZVAV2f>
- <https://gateway.pinata.cloud/ipfs/QmXgQfGEvDBtpCsXYyJ9UkaPkaPwc6uFugcNh6qKZVAV2f>

### 개별 파일 CID (인라인 검증용)

| 파일 | CID |
|------|-----|
| STATEMENT_KO.md | `QmYeRRwXA1eqyi4U2BneVhrtdvZyK2QbzuhBoc5NmW3XVj` |
| STATEMENT_EN.md | `QmYUkuZKWihxcBVe4KMDZhtXHV1TZQ7W4bjWoQ5xQ5njr3` |
| EVIDENCE_KO.md | `QmVB2z5yeNHtg3mxD8GXxUhnj2YPQfobxM9ZYSsXLUtbxR` |
| EVIDENCE_EN.md | `QmTrv7oA725XPGXic3JyvTCzPrviTKRWpkAq2ds5aiaQM1` |
| signed_message.txt | `QmdZq81PXS9GozkLK3cAPjEpEBc7kSxVpCzysLAiqfQ31r` |

콘텐츠는 결정적: 누가 같은 파일을 다시 핀하더라도 위와 동일한 CID 가 나옵니다. CID = "이 콘텐츠가 변조되지 않았다" 의 영구 증명.

### 핀닝 상태

| 핀닝 노드 | 상태 | 비고 |
|-----------|------|------|
| 본인 운영 노드 (gram-jsong, Linux) | ✅ Pinned (Phase 4) | 노드 가용성에 의존 |
| Pinata | 🔒 미설정 | 사용자 가입 후 진행 예정 (van.jeffing@gmail.com) |
| web3.storage | 🔒 미설정 | 사용자 가입 후 진행 예정 |

영구성 강화를 위해 최소 2개 이상의 핀닝 서비스에 등록 권장.

## 3. 비트코인 온체인 (OP_RETURN 마커)

| 항목 | 값 |
|------|----|
| 마커 TXID | `<TBD: Phase 8 OP_RETURN 발행 후 기재>` |
| 블록 높이 | `<TBD>` |
| 페이로드 | `STOLEN-BTC TXID:e867f6973fa3 SEE:vanjeffing-dotcom.github.io/stolen-btc-2024` |
| 송신 주소 (별도 보유 BTC 지갑) | `<TBD>` |
| 수신 주소 (가해자, dust) | `1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN` |
| 발행 일시 | `<TBD>` |

확인 채널 (발행 후):
- `https://mempool.space/tx/<marker TXID>`
- `https://blockchair.com/bitcoin/transaction/<marker TXID>`
- `https://blockstream.info/tx/<marker TXID>`

## 4. 절도 사건 트랜잭션 (고정값, 참고)

| 항목 | 값 |
|------|----|
| 절도 TXID | `e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4` |
| 블록 타임 (UTC) | 2024-11-05 02:07:09 |
| 피해자 주소 | `bc1qdxlazvvxhjkflmf8jjv7sfmtx3k0jnp35ug42d` |
| 가해자 주소 | `1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN` |
| 이체 금액 | 6.318566 BTC |

## 5. 신고 접수 번호 (있는 경우)

| 기관 | 접수번호 | 일자 |
|------|----------|------|
| ECRM (한국 사이버범죄) | `<TBD>` | `<TBD>` |
| Chainabuse | `<TBD>` | `<TBD>` |
| TRM Labs | `<TBD>` | `<TBD>` |
| Chainalysis | `<TBD>` | `<TBD>` |

상세 진행은 [`reports/submission_log.md`](../reports/submission_log.md) 참조 (해당 파일도 비-서명 대상).

## 6. 마지막 업데이트

- **2026-05-19**: 초기 생성. 서명 직후 시점.
- (이후 업데이트는 위의 ISO date 와 함께 변경 사항만 한 줄로 추가)

---

## 변경 검증 방법

본 파일이 변조되었거나 의심스러우면, 위 표의 4개 파일을 `sha256sum` 으로 계산하여 [`signed_message.txt`](signed_message.txt) 의 봉인 해시와 비교하세요. 4개 봉인 해시가 일치하면 본 사건의 핵심 사실(피해자 주소, 가해자 주소, 절도 TXID, 금액, 시점)은 변조되지 않았음이 보장됩니다.

```bash
cd <이 디렉토리>
sha256sum STATEMENT_KO.md STATEMENT_EN.md EVIDENCE_KO.md EVIDENCE_EN.md
```
