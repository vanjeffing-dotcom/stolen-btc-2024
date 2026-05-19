---
title: Evidence (anonymized)
parent_statement: STATEMENT_EN.md
published: 2026-05-18
---

# Evidence — Anonymized Edition

This document is an evidence attachment to the [public statement](STATEMENT_EN.md). The author's personal identifiers have been partially masked, while every technical fingerprint useful for tracing the attacker is preserved verbatim.

The unmasked originals are retained privately by the author and will be released only to legitimate law-enforcement, exchanges, or accredited chain-analytics firms after identity confirmation through the cryptographic signature described in [§7](STATEMENT_EN.md#7-cryptographic-proof-of-ownership).

Masking conventions:
- `j*****s@gmail.com`: author's personal email, masked
- `j***g@c******g.com`: author's corporate email, masked
- `010-****-****`: author's phone number, masked
- `<S/N redacted>` / `<IMEI redacted>`: author's device identifiers, masked
- `<victim home IP redacted>`: author's home IP, masked
- **Attacker-side fingerprints (attacker address, attacker VPN/IP, attacker device models) are kept verbatim.**

---

## E1. The Theft Transaction

- **Block time (UTC)**: 2024-11-05 02:07:09
- **KST**: 2024-11-05 11:07:09
- **TXID**: `e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4`
- **From (victim address)**: `bc1qdxlazvvxhjkflmf8jjv7sfmtx3k0jnp35ug42d`
- **To (attacker address)**: `1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN`
- **Amount**: 6.318566 BTC
- **KRW value at the time**: approx. 592,115,146 KRW
- **Confirmations**: 444 (as captured shortly after the incident)

Verifiable on:
- <https://mempool.space/tx/e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4>
- <https://blockchair.com/bitcoin/transaction/e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4>

---

## E2. Suspected Compromise Path

Around 2018, the author backed up the BIP-39 mnemonic of a hardware wallet inside an 11-character-password-encrypted ZIP archive, and stored that archive in both a personal mailbox (`j*****s@gmail.com`) and a corporate mailbox (`j***g@c******g.com`).

The most likely compromise path:

1. The attacker obtained access to the author's Google account (`j*****s@gmail.com`).
2. The 11-character password protecting the ZIP archive was retrieved either from Google Password Manager or from search within the mailbox.
3. Once the ZIP was decrypted, the BIP-39 mnemonic gave the attacker unrestricted spending authority over the victim address.

The author had **two-factor authentication (2FA) enabled on this account since 2 July 2018** (confirmed by a Google security settings screenshot). How the attacker bypassed 2FA from a device the author did not own remains the central unresolved question of this incident.

---

## E3. Prior Context — July 2024: National-Intelligence Tip-off

- **Date**: 2024-07-09
- **Summary**: An agent of the Korean National Intelligence Service (NIS) visited the author's company in person and warned that the corporate account (`j***g@c******g.com`) was the subject of a targeted attack. The theft occurred approximately four months later.

---

## E4. Prior Context — June 2024: Suspicious Domestic-IP Login During Overseas Trip

- **Date**: 2024-06-25
- **Situation**: While the author was abroad on a business trip, a login to the corporate account was logged from a Korean domestic ISP IP.
- **Logged IP**: `110.70.26.30` (Republic of Korea, KT Corporation, Daejeon, lat 36.3213 / lon 127.4200)
- **This is not an IP the author uses**, suggesting the attacker may have had access to the corporate account for at least four months before the actual theft.

---

## E5. Google Account "Recent Security Activity" (captured 2024-11-09 09:45 KST)

The author's personal account (`j*****s@gmail.com`) Recent-Activity page showed the following events:

### 2024-11-09 (four days after the theft) — Continued intrusion attempts

| Time (KST) | Event | Location | Device |
|------------|-------|----------|--------|
| 08:11 | Access granted on macOS (**new device**) | Gyeonggi-do, Korea | Mac |
| 08:07 | Password changed (**new device**) | Gyeonggi-do, Korea | Mac |
| 07:54 | Access granted on iOS | Gyeonggi-do, Korea | iPhone |
| 07:54 | New sign-in on Apple iPhone 14 Pro (**new device**) | Gyeonggi-do, Korea | iPhone |
| 01:03 | New sign-in on Apple iPhone 15 (**action required**) | — | iPhone |
| 12:55 | New sign-in on Galaxy S20 Ultra 5G (**action required**) | — | Galaxy S20 Ultra 5G |
| 12:55 | Backup code used for sign-in (**new device**) | — | — |
| 12:55 | Sign-in step changed: backup code generated (**action required**) | — | Mac |

**Apple iPhone 15** and **Galaxy S20 Ultra 5G** are not devices the author owns or has ever used, and are therefore attributed to the attacker.

The author logged in on 9 November 2024 morning, deleted the backup codes, and rotated the password.

### 2024-11-06 — Additional suspicious activity

| Time (KST) | Event | Location | Device |
|------------|-------|----------|--------|
| 16:58 | New sign-in on Mac (**new device**) | Gyeonggi-do, Korea | Mac |
| (time unclear) | Access granted on iOS | — | — |

---

## E6. Google Account Security Settings (captured 2024-11-12 14:36 KST)

| Field | Value |
|-------|-------|
| 2-step verification | ✅ Enabled (since **2018-07-02**) |
| Passkeys & security keys | 1 passkey |
| Password last changed | November 9 |
| OTP added | 2021-10-30 |
| 2FA phone | `010-****-****` |
| Recovery phone | `010-****-****` |
| Google Messages devices | 2 |

→ The fact that **2FA had been enabled since 2018** but was nevertheless bypassed is the central unresolved question of this incident.

---

## E7. Google Account Security Settings (captured 2024-11-18 15:51 KST) — Post-incident hardening

The author removed 2FA and transitioned to **passkey-only authentication**:

| Field | Value |
|-------|-------|
| Passkeys & security keys | 1 passkey |
| Password last changed | November 14 |
| "Skip password when possible" | ✅ Enabled |
| 2FA phone | `010-****-****` |
| Recovery phone | `010-****-****` |
| Recovery email | `j******0@h*****l.com` |
| Security question | (masked) |

Passkeys are bound to iCloud (Apple ID), accessible only from currently-trusted Apple devices.

---

## E8. Kraken Exchange — Suspicious Login

- **Date**: 2024-11-14 09:27 KST
- **Event**: An attempt to log in to the author's Kraken.com account from a device the author does not own.
- **Login IP**: `160.238.37.55` (German VPN)

"Connected devices" screen captured:

| Device | Location | Last activity |
|--------|----------|---------------|
| Safari (Mac) | KR | Currently active (author) |
| Chrome (Windows) | DE | 2024-11-14 09:27 (**suspected attacker**) |
| J. Song's iPhone | KR | 2023-10-27 22:08 (legacy author session) |

The author removed 2FA on Kraken and migrated to passkey-only. No further intrusion attempts have been logged since.

---

## E9. Author's Devices at the Time of the Incident — for distinguishing from attacker devices

The devices in active use by the author at the time of the theft (identifiers masked):

| Device | Model | Serial / IMEI |
|--------|-------|---------------|
| MacBook Pro 16" (work) | macOS 14.6.1 | `<S/N redacted>` |
| iPhone 14 Pro | iOS 18.2 | IMEI `<redacted>` |
| iPad Pro | iPadOS 18.2 | IMEI `<redacted>` |
| iMac 27" (personal) | macOS 15.0.1 | `<S/N redacted>` |

**Any access logged from a device other than these four was not the author.**

Therefore, sign-ins from the following device classes are all attributable to the attacker:
- Apple iPhone 15
- Galaxy S20 Ultra 5G
- Any Mac whose serial number does not match the list above
- Any Windows device

---

## E10. Post-incident Hardening — Device Rotation

| Date | Action |
|------|--------|
| 2024-11-09 | Backup codes deleted; Google password rotated |
| 2024-11-14 | Mail and Kraken 2FA removed, migrated to passkey-only |
| 2024-11-20 | iMac 27" reset to factory and re-registered (to flush any persistent threat) |
| (around) | MacBook Pro 14" newly registered; iPhone 16 Pro newly registered |

Devices in active use as of 2024-11-21:

| Device | Model |
|--------|-------|
| MacBook Pro 14" | macOS 14.6 |
| iPhone 16 Pro | iOS 18.2 |
| iMac 27" | macOS 15.1.1 (reset & re-registered) |

---

## E11. Activity on the Attacker Address

As of this publication, the attacker address (`1Jwf2JXHVPz89GJKtnNp6ocBtNC7i5U4XN`) has produced **zero outgoing transactions**. This may indicate any of:

1. The attacker is holding back, waiting for an environment where freeze risk is lower (e.g., a non-KYC venue).
2. The attacker is observing the victim's reaction to gauge investigative reach.
3. Custody of the funds has changed hands and further action is currently constrained.

The author maintains a real-time monitor on this address. Any outgoing movement will trigger an immediate public disclosure and law-enforcement filing.

---

## E12. Masking Key (Verification)

The masking used in this document is consistent across all references. The mapping (e.g., `j*****s@gmail.com` ↔ actual address) is retained privately by the author and will be provided only to parties who have completed identity verification via the cryptographic [§7 signature procedure](STATEMENT_EN.md#7-cryptographic-proof-of-ownership).

---

**File hash (tamper-evident)**:
```
sha256sum EVIDENCE_EN.md
```

**Related**:
- [Public Statement (English)](STATEMENT_EN.md)
- [공개 성명서 (한국어)](STATEMENT_KO.md)
- [사건 증거 (한국어)](EVIDENCE_KO.md)
- [Signed Message Template](signed_message_template.txt)
