---
title: Public Statement of Stolen Bitcoin
incident_date: 2024-11-05T11:07:09+09:00
published: 2026-05-18
victim_address: bc1qdxlazvvxhjkflmf8jjv7sfmtx3k0jnp35ug42d
attacker_address: 1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN
txid: e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4
amount_btc: 6.318566
amount_krw_at_time: 592115146
contact: van.jeffing@gmail.com
---

# Public Statement of Stolen Bitcoin

This is a public statement issued by the victim (hereinafter "the author") of a Bitcoin theft incident dated 5 November 2024. This statement is published permanently across GitHub, IPFS, and the Bitcoin blockchain (via OP_RETURN).

The author's real-world identity is intentionally withheld from this public statement, but can be confirmed by legitimate law-enforcement, exchanges, and accredited chain-analytics firms through the cryptographic signature procedure described in [§7](#7-cryptographic-proof-of-ownership).

## 1. Incident Summary

| Field | Value |
|------|-------|
| **Date & time** | 5 November 2024, 11:07:09 KST |
| **Block timestamp** | 2024-11-05 02:07:09 UTC |
| **Victim address** | `bc1qdxlazvvxhjkflmf8jjv7sfmtx3k0jnp35ug42d` |
| **Attacker address** | `1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN` |
| **Transaction ID** | `e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4` |
| **Amount stolen** | 6.318566 BTC |
| **KRW value at the time** | approx. 592,115,146 KRW |

Verify on a block explorer:
- Mempool: <https://mempool.space/tx/e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4>
- Blockchair: <https://blockchair.com/bitcoin/transaction/e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4>
- Blockstream: <https://blockstream.info/tx/e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4>

## 2. Formal Declaration

The author is the rightful and exclusive owner of the **victim address `bc1qdxlazvvxhjkflmf8jjv7sfmtx3k0jnp35ug42d`**, and publicly declares that:

1. **The transaction listed above was executed without the author's consent. It constitutes theft.**
2. **The receiving address `1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN`, and every descendant UTXO and address derived from it, must be treated as stolen funds.**
3. **Receiving, exchanging, laundering, or transmitting these funds may constitute a criminal offense under Korean criminal code (theft, receipt of stolen property), 18 U.S.C. § 2315 (transportation of stolen property) in the United States, and applicable anti-money-laundering (AML) law in any jurisdiction.**

Ownership of the victim address is cryptographically proven by the accompanying **signed message (`signed_message.txt`)**.

## 3. Incident Background (Summary)

- Around 2018, the author backed up the BIP-39 mnemonic of a hardware wallet inside an 11-character-password-encrypted ZIP archive, and stored it across a personal mailbox (`j*****s@gmail.com`) and a corporate mailbox (`j***g@c******g.com`).
- 9 July 2024: A Korean national intelligence agency notified the author that the corporate account was the subject of a targeted attack.
- 25 June 2024: While the author was abroad, an access to the corporate account was logged from a Korean domestic ISP IP.
- 5 November 2024: All BTC was transferred to the attacker address. **This is the incident.**
- 9 November 2024: Even after the incident, unknown devices (Apple iPhone 15, Galaxy S20 Ultra 5G) attempted to log in to the personal mailbox and create backup codes. The author immediately deleted backup codes and changed passwords.
- 14 November 2024: Kraken exchange logged a login attempt from a German VPN IP. The author migrated email and Kraken to passkey-only authentication.
- **From 5 November 2024 through the date of this statement, the attacker address has shown zero outgoing activity.**

A detailed, anonymized evidence appendix (Google account security logs, attacker IP/device fingerprints, Kraken intrusion attempt, etc.) is published as [EVIDENCE_EN.md](EVIDENCE_EN.md). The unmasked originals are retained privately by the author and will be released only through lawful investigative or legal channels, or to accredited parties after identity verification via the §7 signature procedure.

## 4. Requests to Exchanges and Chain Analytics Firms

The author formally requests that:

1. **All exchanges (centralized, and decentralized exchanges performing KYT)**: freeze any incoming deposit traceable to the attacker address and its descendant UTXOs, and notify the author or Korean law enforcement.
2. **Chain analytics firms (Chainalysis, TRM Labs, Elliptic, Crystal, Merkle Science, et al.)**: tag this address permanently as "stolen funds".
3. **Block explorers (Mempool, Blockchair, Blockstream, blockchain.com, etc.)**: register a label on the attacker address page linking to this statement.

## 5. Message to the Attacker

Off-ramping these funds through KYC exchanges, OTC desks, or mixers will become progressively harder, not easier. This statement is permanently inscribed on the Bitcoin blockchain via OP_RETURN, and is being indexed into every major risk engine.

**If you return the funds voluntarily, the author publicly commits not to pursue criminal prosecution.** Contact:

- Email: `van.jeffing@gmail.com`
- A negotiation-only bitcoin address (verifiable via signed message) will be published in a follow-up update.

## 6. Bounty

The author will pay a bounty of **up to 10% of recovered funds** to any informant who provides decisive intelligence leading to the recovery of these funds. Anonymous tips are welcome via the email address above.

## 7. Cryptographic Proof of Ownership

The companion file `signed_message.txt` contains a message signed by the private key controlling the victim address (`bc1qdxlazvvxhjkflmf8jjv7sfmtx3k0jnp35ug42d`), whose payload is the SHA-256 hash of this document. To verify:

```bash
# 1. Compute the SHA-256 of this document
sha256sum STATEMENT_EN.md

# 2. Verify the signature (Bitcoin Core)
bitcoin-cli verifymessage "bc1qdxlazvvxhjkflmf8jjv7sfmtx3k0jnp35ug42d" "<signature>" "<message=hash>"

# Alternatively, use Electrum: Tools > Sign/verify message
```

## 8. License and Permanent Publication

This document is released into the **public domain (CC0)**. Anyone may reproduce, distribute, and index it freely.

Permanent publication channels:
- GitHub Pages: <https://vanjeffing-dotcom.github.io/stolen-btc-2024>
- IPFS CID: `<TBD: to be filled after pinning>`
- Bitcoin OP_RETURN: transaction ID to be published in a follow-up update.

---

**Author**: the victim (public alias: Van Jeffing)
**Contact**: van.jeffing@gmail.com
**First published**: 2026-05-18
**Last revised**: 2026-05-18
