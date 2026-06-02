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

> **CID 가 두 개인 이유**: 같은 콘텐츠라도 IPFS 노드의 chunking·wrap 옵션에 따라 디렉토리 CID 가 달라집니다. 두 CID 모두 동일 콘텐츠를 가리키며, 봉인 파일의 SHA-256 무결성은 어느 쪽에서 fetch 해도 일치함이 검증되었습니다 (Phase 4 작업 시 확인).

### Primary — Pinata 핀 (Phase 8 재핀, 2026-06-02)

```
QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm
```

**브라우저 접근 (디렉토리 인덱스 — HTML 렌더링 가능한 게이트웨이)**:
- <https://ipfs.io/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/>  ← 권장 (Protocol Labs 운영)
- <https://dweb.link/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/>
- <https://4everland.io/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/>

**개별 파일 직접 링크 (Pinata 가 가장 빠름)**:
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/STATEMENT_KO.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/STATEMENT_EN.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/EVIDENCE_KO.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/EVIDENCE_EN.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/POLICE_CASE_KO.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/POLICE_CASE_EN.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/signed_message.txt>

**이전 디렉토리 CID (2026-05-19 핀, MIRRORS·POLICE_CASE 분리 이전)**:
- `QmW8rpbJ8qpEp4sRKuk25dFTLBxAcyvGMHCvr4oPzZc7mk` — 봉인 4파일 (STATEMENT/EVIDENCE) 동일 sha256, 여전히 valid. 거래소·LE에게 발송한 메일에서 참조 중이므로 핀 유지.

> Pinata 의 공용 게이트웨이는 보안상 HTML 디렉토리 인덱스 페이지를 차단합니다 (ERR_ID:00023). 디렉토리 탐색은 `ipfs.io` 또는 `dweb.link` 사용. 개별 파일 fetch 는 모든 게이트웨이 정상.

### Secondary — 본인 운영 노드 (gram-jsong)

```
QmXgQfGEvDBtpCsXYyJ9UkaPkaPwc6uFugcNh6qKZVAV2f
```

이 CID 의 개별 파일 CID (인라인 검증용):

| 파일 | CID (CIDv0, default chunking) |
|------|-----|
| STATEMENT_KO.md | `QmYeRRwXA1eqyi4U2BneVhrtdvZyK2QbzuhBoc5NmW3XVj` |
| STATEMENT_EN.md | `QmYUkuZKWihxcBVe4KMDZhtXHV1TZQ7W4bjWoQ5xQ5njr3` |
| EVIDENCE_KO.md  | `QmVB2z5yeNHtg3mxD8GXxUhnj2YPQfobxM9ZYSsXLUtbxR` |
| EVIDENCE_EN.md  | `QmTrv7oA725XPGXic3JyvTCzPrviTKRWpkAq2ds5aiaQM1` |
| signed_message.txt | `QmdZq81PXS9GozkLK3cAPjEpEBc7kSxVpCzysLAiqfQ31r` |

### 핀닝 상태

| 노드 | CID (디렉토리) | 상태 | 비고 |
|------|---------------|------|------|
| Pinata (가입자 `van.jeffing@gmail.com`) — **Phase 8 재핀** | `QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm` | ✅ Pinned 2026-06-02 | 28 files, ~2.6 MB. MIRRORS·POLICE_CASE 분리본 포함 |
| Pinata — 이전 핀 (보존) | `QmW8rpbJ8qpEp4sRKuk25dFTLBxAcyvGMHCvr4oPzZc7mk` | ✅ Pinned 2026-05-19 | 거래소·LE 발송 메일에서 참조 중. 봉인 4파일 sha256 동일 |
| 본인 운영 노드 (gram-jsong, Linux) | `QmXgQfGEvDBtpCsXYyJ9UkaPkaPwc6uFugcNh6qKZVAV2f` | ✅ Pinned 2026-05-19 | 노드 가용성에 의존 |
| web3.storage | — | 🔒 미설정 | 영구성 강화 위해 추가 권장 |

봉인 파일의 SHA-256 무결성은 어느 CID·게이트웨이로 접근하든 항상 [`signed_message.txt`](signed_message.txt) 의 봉인 해시와 일치해야 함. 일치하지 않으면 그 게이트웨이의 콘텐츠는 변조된 것.

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
