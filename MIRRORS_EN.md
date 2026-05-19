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

### Primary — Pinata pin

```
QmcERhYD61tHnsZpyFbPzdc5471pJjVGU2ixrEmfbWmKnN
```

**Browse the directory (HTML-rendering gateways)**:
- <https://ipfs.io/ipfs/QmcERhYD61tHnsZpyFbPzdc5471pJjVGU2ixrEmfbWmKnN/>  ← recommended (Protocol Labs)
- <https://dweb.link/ipfs/QmcERhYD61tHnsZpyFbPzdc5471pJjVGU2ixrEmfbWmKnN/>
- <https://4everland.io/ipfs/QmcERhYD61tHnsZpyFbPzdc5471pJjVGU2ixrEmfbWmKnN/>

**Fetch individual files (Pinata is fastest)**:
- <https://gateway.pinata.cloud/ipfs/QmcERhYD61tHnsZpyFbPzdc5471pJjVGU2ixrEmfbWmKnN/STATEMENT_KO.md>
- <https://gateway.pinata.cloud/ipfs/QmcERhYD61tHnsZpyFbPzdc5471pJjVGU2ixrEmfbWmKnN/STATEMENT_EN.md>
- <https://gateway.pinata.cloud/ipfs/QmcERhYD61tHnsZpyFbPzdc5471pJjVGU2ixrEmfbWmKnN/EVIDENCE_KO.md>
- <https://gateway.pinata.cloud/ipfs/QmcERhYD61tHnsZpyFbPzdc5471pJjVGU2ixrEmfbWmKnN/EVIDENCE_EN.md>
- <https://gateway.pinata.cloud/ipfs/QmcERhYD61tHnsZpyFbPzdc5471pJjVGU2ixrEmfbWmKnN/signed_message.txt>

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
| Pinata (`van.jeffing@gmail.com`) | `QmcERhYD61…WmKnN` | ✅ Pinned 2026-05-19 | Free plan, 1 GB limit, payload ~58 KB |
| Self-hosted (gram-jsong, Linux) | `QmXgQfGEvD…KZVAV2f` | ✅ Pinned 2026-05-19 | Depends on node availability |
| web3.storage | — | 🔒 Not yet configured | Recommended for added durability |

Sealed-file SHA-256 hashes must match the seal in [`signed_message.txt`](signed_message.txt) no matter which CID/gateway is used. If they don't, that gateway's content is tampered with.

## 3. Bitcoin On-chain (OP_RETURN marker)

| Field | Value |
|------|-------|
| Marker TXID | `<TBD: filled in after Phase 8 broadcast>` |
| Block height | `<TBD>` |
| Payload | `STOLEN-BTC TXID:e867f6973fa3 SEE:vanjeffing-dotcom.github.io/stolen-btc-2024` |
| Sender address (separate BTC wallet) | `<TBD>` |
| Recipient (attacker, dust) | `1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN` |
| Broadcast time | `<TBD>` |

Verification channels (post-broadcast):
- `https://mempool.space/tx/<marker TXID>`
- `https://blockchair.com/bitcoin/transaction/<marker TXID>`
- `https://blockstream.info/tx/<marker TXID>`

## 4. Theft Transaction (fixed, for reference)

| Field | Value |
|------|-------|
| Theft TXID | `e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4` |
| Block time (UTC) | 2024-11-05 02:07:09 |
| Victim address | `bc1qdxlazvvxhjkflmf8jjv7sfmtx3k0jnp35ug42d` |
| Attacker address | `1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN` |
| Amount | 6.318566 BTC |

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
- (Subsequent updates should appear here in ISO date order, one line per change.)

---

## How to detect tampering

If you suspect this file or any other has been altered, re-compute `sha256sum` over the four sealed files and compare against the seal above. If the four hashes match, the core facts of this incident (victim address, attacker address, theft TXID, amount, timestamp) are intact, regardless of what other files claim.

```bash
cd <this directory>
sha256sum STATEMENT_KO.md STATEMENT_EN.md EVIDENCE_KO.md EVIDENCE_EN.md
```
