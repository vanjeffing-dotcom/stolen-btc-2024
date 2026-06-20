# Mirrors and Live References

> **Integrity model**
>
> This file (`MIRRORS_EN.md` / `MIRRORS_KO.md`) is **not covered by the cryptographic signature**. It changes over time.
>
> The four sealed statement files are SHA-256-bound, and that seal is committed by the BIP-322 signature in [`signed_message.txt`](signed_message.txt):
>
> | File | SHA-256 |
> |------|---------|
> | STATEMENT_KO.md | `d6c73c8dc51b5e0b6aa076d15a2fc9b4b9d19c3aaac0ba8ba7b3719272c27f93` |
> | STATEMENT_EN.md | `7948e26829024685245479a94c18bdc5760eccbdd34daf7f1d0ade1e6bdd09e4` |
> | EVIDENCE_KO.md  | `741390f29fdc6a847382e8762f717a7111fb2eb3b5e753af000c56b37c9039a0` |
> | EVIDENCE_EN.md  | `77681db33a7ceb8b33020b1ed913bdba48cec075345bf800ec98e5285c99b5ca` |
>
> This file carries only dynamic information (CIDs, TXIDs, mirror URLs). Any party can re-compute `sha256sum` over the four files and compare against the seal to detect tampering instantly.

---

## 1. Web Mirrors

| Channel | URL | Status |
|---------|-----|--------|
| GitHub Pages | <https://vanjeffing-dotcom.github.io/stolen-btc-2024> | 🔒 Goes public after Phase 8 |
| Custom domain | (TBD) | TBD |

## 2. IPFS

> **Why two CIDs?** Different IPFS nodes use different chunking and wrapping defaults, producing different directory CIDs for byte-identical content. The sealed file SHA-256 hashes are unaffected — they verify regardless of which CID/gateway you use.

### Primary — Pinata pin (Phase 8 re-pin, 2026-06-02)

```
QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm
```

**Browse the directory (HTML-rendering gateways)**:
- <https://ipfs.io/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/>  ← recommended (Protocol Labs)
- <https://dweb.link/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/>
- <https://4everland.io/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/>

**Fetch individual files (Pinata is fastest)**:
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/STATEMENT_KO.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/STATEMENT_EN.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/EVIDENCE_KO.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/EVIDENCE_EN.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/POLICE_CASE_KO.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/POLICE_CASE_EN.md>
- <https://gateway.pinata.cloud/ipfs/QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm/signed_message.txt>

**Previous directory CID (2026-05-19 pin, prior to MIRRORS/POLICE_CASE split)**:
- `QmW8rpbJ8qpEp4sRKuk25dFTLBxAcyvGMHCvr4oPzZc7mk` — sealed 4 files (STATEMENT/EVIDENCE) carry identical sha256, still valid. Kept pinned since outbound notices to exchanges and LE reference it.

> Pinata's free public gateway blocks HTML directory-index pages (`ERR_ID:00023`). Use `ipfs.io` or `dweb.link` for directory browsing; any gateway works for individual files.

### Secondary — self-hosted node (gram-jsong)

```
QmXgQfGEvDBtpCsXYyJ9UkaPkaPwc6uFugcNh6qKZVAV2f
```

Individual-file CIDs from this node (handy for inline verification):

| File | CID (CIDv0, default chunking) |
|------|-----|
| STATEMENT_KO.md | `QmYeRRwXA1eqyi4U2BneVhrtdvZyK2QbzuhBoc5NmW3XVj` |
| STATEMENT_EN.md | `QmYUkuZKWihxcBVe4KMDZhtXHV1TZQ7W4bjWoQ5xQ5njr3` |
| EVIDENCE_KO.md  | `QmVB2z5yeNHtg3mxD8GXxUhnj2YPQfobxM9ZYSsXLUtbxR` |
| EVIDENCE_EN.md  | `QmTrv7oA725XPGXic3JyvTCzPrviTKRWpkAq2ds5aiaQM1` |
| signed_message.txt | `QmdZq81PXS9GozkLK3cAPjEpEBc7kSxVpCzysLAiqfQ31r` |

### Pin status

| Node | Directory CID | Status | Notes |
|------|---------------|--------|-------|
| Pinata (`van.jeffing@gmail.com`) — **Phase 8 re-pin** | `QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm` | ✅ Pinned 2026-06-02 | 28 files, ~2.6 MB. Includes MIRRORS/POLICE_CASE split + redacted police PDF |
| Pinata — previous pin (retained) | `QmW8rpbJ8qpEp4sRKuk25dFTLBxAcyvGMHCvr4oPzZc7mk` | ✅ Pinned 2026-05-19 | Referenced by outbound exchange/LE notices. Sealed 4 files unchanged sha256 |
| Self-hosted (gram-jsong, Linux) | `QmXgQfGEvDBtpCsXYyJ9UkaPkaPwc6uFugcNh6qKZVAV2f` | ✅ Pinned 2026-05-19 | Depends on node availability |
| web3.storage | — | 🔒 Not yet configured | Recommended for added durability |

Sealed-file SHA-256 hashes must match the seal in [`signed_message.txt`](signed_message.txt) no matter which CID/gateway is used. If they don't, that gateway's content is tampered with.

## 3. Bitcoin On-chain (OP_RETURN marker)

| Field | Value |
|------|-------|
| Marker TXID | `9fb8beb4f4d9f1d8c75c0b4d36d9a296190500c00ef62a8116d91507814f0496` |
| Block height | `952275 (confirmed 2026-06-04)` |
| Payload (actual on-chain) | `STOLEN tx:e867f6973fa3 ipfs:QmfQSneNHBbaytj64bd7Q9kayf6h9HBNnBsrATX1zjBLvm` |
| Sender address (separate BTC wallet) | `bc1qjpt9vaguhy228txe39jt4vcqmtwnazttzmjmgh` |
| Recipient (attacker, dust) | `1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN` |
| Broadcast time | `2026-06-04 (KST)` |

Verification channels:
- `https://mempool.space/tx/9fb8beb4f4d9f1d8c75c0b4d36d9a296190500c00ef62a8116d91507814f0496`
- `https://blockchair.com/bitcoin/transaction/9fb8beb4f4d9f1d8c75c0b4d36d9a296190500c00ef62a8116d91507814f0496`
- `https://blockstream.info/tx/9fb8beb4f4d9f1d8c75c0b4d36d9a296190500c00ef62a8116d91507814f0496`

## 4. Theft Transaction (fixed, for reference)

| Field | Value |
|------|-------|
| Theft TXID | `e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4` |
| Block time (UTC) | 2024-11-05 02:07:09 |
| Victim address | `bc1qdxlazvvxhjkflmf8jjv7sfmtx3k0jnp35ug42d` |
| Attacker address | `1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN` |
| Amount | 6.318566 BTC |

## 4-A. Attacker Fund Movement (dormancy broken, 2026-06-20)

After **592 days of zero activity**, the attacker moved the entire balance to a new address.

| Field | Value |
|------|-------|
| Move TXID | `898de7a9b2e40367905835f1c4a236a4d869c467c97f9939dad6f79445c49da8` |
| Time | 2026-06-20 00:49:04 UTC (09:49:04 KST), block 954475 |
| From | `1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN` (original attacker) |
| To (new) | `bc1qprhghu2zvgs0emcwryx46ngkntcrtsvpp6jcsw` |
| Amount | 6.31855552 BTC (entire balance, single hop, 189 sat fee) |
| Response | tracked at hop-1 by taint_tracker (180s interval); urgent follow-up sent to exchanges + chain-analytics (2026-06-20) |

## 5. Case Numbers (where available)

| Authority | Case ID | Date |
|-----------|---------|------|
| ECRM (Korean Cybercrime Reporting System) | `<TBD>` | `<TBD>` |
| Chainabuse | `<TBD>` | `<TBD>` |
| TRM Labs | `<TBD>` | `<TBD>` |
| Chainalysis | `<TBD>` | `<TBD>` |

For detailed submission tracking, see `reports/submission_log.md` (also not covered by the signature).

## 6. Changelog

- **2026-05-19**: Initial creation, immediately after signing.
- **2026-06-04**: OP_RETURN marker broadcast (§3), confirmed block 952275.
- **2026-06-20**: Attacker moved entire balance to a new address after 592 days (§4-A). taint_tracker interval cut to 180s; urgent follow-up sent to exchanges + chain-analytics.
- (Subsequent updates should appear here in ISO date order, one line per change.)

---

## How to detect tampering

If you suspect this file or any other has been altered, re-compute `sha256sum` over the four sealed files and compare against the seal above. If the four hashes match, the core facts of this incident (victim address, attacker address, theft TXID, amount, timestamp) are intact, regardless of what other files claim.

```bash
cd <this directory>
sha256sum STATEMENT_KO.md STATEMENT_EN.md EVIDENCE_KO.md EVIDENCE_EN.md
```
