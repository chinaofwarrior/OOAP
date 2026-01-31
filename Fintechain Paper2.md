# Fintechain Protocol

## Abstract

The democratization of Commerce Agents inevitably raises a fundamental challenge: how to ensure that a commerce business obtains an asset if and only if the upstream wholesaler is compensated, without revealing sensitive information.
AI agents and custodial services are increasingly trusted and delegated as intermediaries to execute transactions on behalf of institutions. The stakes are high: the digital asset market is projected to exceed USD 16 trillion by 2030, with a significant fraction of value exchange involving proprietary and time-sensitive goods. While industry initiatives—such as Google’s Agent-to-Payments (AP2) protocol—have standardized how agents authorize payments, they do not address the core problem of fair exchange: guaranteeing that a commerce business receives an asset if and only if the wholesaler receives payment, all without exposing sensitive data.
We introduce Proxy Adaptor Signatures (PAS), a cryptographic primitive for proxy-based fair exchange under delegation. A stateless Commerce Agent issues a single request and maintains minimal state; a set of proxies and the wholesaler execute the exchange on its behalf. If the wholesaler obtains payment, then the protocol guarantees that proxies can derive a *blinded* delivery artifact that only the commerce business can unblind into the purchased witness; if payment does not finalize, then delivery cannot complete. We formalize PAS in an (n, t) threshold model tolerating up to (t−1) colluding proxies, give an efficient construction from standard adaptor signatures (Schnorr/EdDSA), and show immediate compatibility with Bitcoin, Ethereum, and Solana. A Rust prototype supports up to 30 proxies: buyer and seller computation completes in microseconds, proxies in milliseconds, and on-chain costs match standard transactions.

---

## 1. Introduction

By 2030, the digital asset market is projected to reach USD 16.1 trillion [31], with data markets—encompassing datasets, trained AI models, and streaming telemetry—driving a substantial portion of this growth [7,29]. These transactions introduce challenges that differ fundamentally from those of traditional finance: digital assets are proprietary, copyable, and often time-sensitive. Once a digital good is revealed, it can be duplicated at near-zero cost; dispute resolution after leakage is ineffective.

Consider a supplier selling short-lived trading signals to a hedge fund. The fund wants assurance that the signal is valid before paying; the supplier wants assurance of payment before revealing the signal. Neither can safely move first. This is the fair exchange problem: deliver the asset if and only if payment is received.

Existing approaches impose trade-offs. Centralized intermediaries can enforce fairness but require custody and trust. Smart-contract-based settlement can be atomic, but is costly and not uniformly deployable across heterogeneous rails (Bitcoin, private ledgers, off-chain venues). Protocol-level fair exchange without contracts exists [6,25,44], but typically requires synchronous, multi-round interaction between buyer and seller—an adoption barrier in institutional settings where procurement is automated and delegated.

At the same time, deployment realities are shifting. MPC wallets and wallet-as-a-service models distribute signing across providers [4], and agent-mediated payments increasingly delegate execution to AI agents or custodians [42]. Delegation improves usability but adds intermediaries that must not learn the purchased asset. This creates a gap: we lack a fair exchange framework that supports delegation end-to-end while preserving confidentiality of the exchanged good.

To meet institutional requirements, a proxy-based fair exchange protocol should satisfy:
Atomicity. No party obtains its outcome while preventing the counterparty from obtaining theirs.
Witness privacy. Only the buyer learns the purchased witness; proxies do not learn it by participating.
Scalability. Seller work is independent of the number of proxies and ideally oblivious to them.
No buyer–seller interaction. Buyer and seller communicate only through proxies and an asynchronous marketplace.
Lightweight buyer. The buyer maintains minimal state and can go offline after posting a request.

### Technical Challenges

A naïve approach delegates the buyer’s signing authority to proxies, who then run a standard fair exchange protocol. This fails because delegation of signing does not constrain information flow: any intermediary who sees a deliverable artifact can leak it to the buyer before payment. Encrypting the asset to the buyer does not fix fairness, since ciphertext can be forwarded early and decryption is unilateral.

Thus, we require a mechanism that (i) binds payment finalization to the emergence of *delivery capability*, (ii) allows proxies to complete delivery without learning the asset, and (iii) keeps the buyer’s role minimal. This calls for a primitive that combines adaptor-signature atomicity with a threshold blinding structure that survives proxy collusion.

Our solution is Proxy Adaptor Signatures (PAS): proxies can trigger delivery only after the seller posts an on-chain payment signature, and what they derive is *blinded* so that only the buyer can recover the witness.

---

## 1.1 Our Contributions

### Formal Model

We formalize Proxy Adaptor Signatures (PAS), a primitive enabling a commerce business to delegate the purchase of a digital good—modeled as a witness *wit* for an NP statement *stmt*—to a set of proxies. PAS builds on adaptor signatures [25] and is inspired by proxy signatures [40] and proxy re-encryption [5], but addresses a distinct goal: end-to-end fair exchange under delegation with *witness privacy against the proxies themselves*.

PAS operates in an (n, t) threshold model that tolerates up to (t−1) corrupted proxies, and is defined via game-based security notions that capture collusion among buyers, sellers, and subsets of proxies. The model separates (i) *payment authorization* from (ii) *asset recovery*, and requires that recovery becomes possible if and only if payment finalizes.

At a high level, a buyer posts a request *req* to a public bulletin board or marketplace. A seller replies with an advertisement that includes a proof of knowledge of *wit*. Proxies execute a threshold protocol to produce an adaptor value τ that binds the payment message *m* to the sale. The seller uses τ and *wit* to adapt and broadcast a standard signature σ on *m*, thereby receiving payment. From τ and σ, proxies can extract a blinded witness *wit*τ and deliver it to the buyer; the buyer then unblinds locally to obtain *wit*. The buyer may go offline after posting *req*.

### Efficient Construction

We present an efficient PAS construction using standard primitives in a black-box manner, particularly adaptor signatures compatible with Schnorr and EdDSA. The resulting on-chain artifact is a standard signature σ on a standard payment transaction, enabling immediate deployment on Bitcoin, Ethereum, and Solana with existing verification logic. PAS avoids complex contracts, keeps on-chain costs unchanged, and preserves fungibility.

### Performance Evaluation

We provide an open-source Rust implementation [3] and an end-to-end demonstration on the Bitcoin testnet. Using secp256k1, we benchmark configurations up to n=30 proxies. Buyer and seller computations take microseconds, proxy operations take milliseconds, and on-chain costs match standard transactions, indicating that PAS is practical for real-world deployment.

---

## 1.2 Related Work

Fair exchange protocols traditionally rely on trusted third parties or optimistic dispute resolution. More recent cryptographic protocols remove the need for a trusted party but typically require interactive, synchronous buyer–seller communication [6,44], which is incompatible with delegated procurement. Atomic swaps and HTLC-style constructions provide conditional settlement but incur timelocks and are not uniformly deployable across heterogeneous environments. Adaptor signatures generalize “pay-to-reveal” mechanisms at the signature layer [25], enabling atomicity without heavy contract logic. PAS builds on adaptor signatures but introduces a threshold blinding interface that prevents delegated proxies from learning the witness.

Proxy signatures enable constrained delegation of signing rights [40], but do not enforce fair exchange or protect the confidentiality of the exchanged good. Proxy re-encryption [5] can hide plaintext from intermediaries, yet does not enforce atomicity because ciphertext can be forwarded before payment. MPC wallets distribute signing among providers [4] but do not by themselves provide fair exchange for digital goods under delegation. Agent-mediated payment frameworks standardize authorization and consent boundaries [42], but are orthogonal to the fair exchange requirement that delivery be coupled to payment.

---

## 2. System Overview

We consider three roles: a buyer (commerce business represented by a Commerce Agent), a seller (wholesaler providing a digital asset), and n proxies that execute the protocol on the buyer’s behalf. The buyer wants to delegate *execution* without delegating *knowledge* of the asset.

Communication is asynchronous: a public bulletin board carries requests and advertisements; the payment rail is an existing blockchain or ledger. The buyer posts a single request and may go offline; proxies interact with the seller and each other. The seller’s on-chain action is standard: posting a payment signature σ on transaction *m*.

The exchanged good is modeled as a witness *wit* for a statement *stmt* in an NP relation R. This abstraction captures: (i) decryption keys for encrypted datasets, (ii) short-lived trading signals verifiable against a public commitment, and (iii) access tokens whose validity can be checked against a public policy.

---

## 3. Preliminaries

### 3.1 Adaptor Signatures (Informal)

Adaptor signatures extend a signature scheme with a pre-signature σ̃ that can be converted into a valid signature σ only by using a witness *wit*. Importantly, given σ̃ and σ, anyone can extract *wit*. This “adapt-and-extract” property enables atomicity: a seller who finalizes σ to claim funds reveals extractable witness material.

### 3.2 Threshold Sharing and Blinding

We use (t, n) threshold sharing so that a secret blinding value b is information-theoretically hidden from any coalition of fewer than t proxies. The buyer holds b locally. Proxies can compute and deliver an artifact that depends on (wit ⊕ b) (or an algebraic analogue), but cannot remove b. The buyer unblinds using b to recover wit.

---

## 4. Proxy Adaptor Signatures

### 4.1 Intuition

Adaptor signatures alone are insufficient under delegation: if proxies hold σ̃, then once σ appears on-chain they can extract wit and learn the asset. PAS modifies the extraction surface: proxies extract only a *blinded* witness witτ that is computationally useless without buyer-held information. Payment finalization yields delivery capability, but confidentiality is preserved against the proxies.

### 4.2 Syntax

A PAS scheme consists of:
Setup(1^λ) → pp
ReqGen(pp, stmt) → (req, st)
ProxGen(pp, req) ↔ proxies → {out_i}
Combine(pp, {out_i}) → τ
VerifyAdv(pp, adv) → {0,1}
Adapt(pp, τ, m, wit) → σ
ProxExt(pp, τ, σ) → witτ
ReqExt(pp, st, witτ) → wit

Correctness requires: if the seller knows wit for stmt, then Adapt outputs a valid σ on m, ProxExt outputs a corresponding witτ, and ReqExt recovers wit.

### 4.3 Security (Informal)

Atomicity: a seller can obtain payment only by posting σ; once σ exists, proxies can compute witτ and the buyer can recover wit. If σ does not exist, wit cannot be recovered.
Witness privacy: any adversary corrupting the seller and up to (t−1) proxies learns nothing about wit beyond what is implied by stmt and public transcripts.
Robustness: if at least t proxies are honest, the protocol completes and the buyer recovers wit whenever σ is posted.

---

## 5. Construction Sketch (Schnorr/EdDSA-Compatible)

We construct PAS by combining (i) an adaptor signature that reveals an extractor value upon signature finalization and (ii) a buyer-chosen blinding value b hidden from proxies via threshold sharing.

Buyer request. The buyer samples b and posts a request that commits to stmt and an associated public handle derived from b. The buyer stores b in st and may go offline.

Proxy generation. Proxies run a threshold protocol to derive τ, an adaptor input bound to the sale and to the buyer’s public handle. τ is a single value; the seller sees only τ and is oblivious to n.

Seller adaptation. The seller uses wit and τ to generate σ, a standard signature on payment transaction m. The seller broadcasts σ to claim funds.

Proxy extraction. From τ and σ, proxies derive witτ, a blinded witness that incorporates b. Proxies never learn b and cannot unblind witτ.

Buyer recovery. The buyer unblinds witτ using b to recover wit.

This construction preserves deployability: σ verifies as a standard signature; no additional on-chain logic is required beyond what the platform already supports.

---

## 6. Implementation and Evaluation

We implement PAS in Rust over secp256k1 and demonstrate an end-to-end flow on Bitcoin testnet. We measure: (i) buyer-side request and recovery, (ii) seller adaptation, and (iii) proxy threshold operations. In configurations up to n=30, buyer and seller operations complete in microseconds, while proxy operations complete in milliseconds dominated by networking and threshold combination. On-chain costs match standard transactions because σ is standard.

---

## 7. Discussion and Limitations

PAS assumes a threshold trust model: fewer than t proxies may collude without violating witness privacy, but if t or more proxies collude they may recover the buyer’s blinding and thus the witness. This matches the operational assumptions of multi-provider custody and MPC wallets, where providers are selected to reduce correlated compromise.

PAS provides fair exchange of a witness wit for stmt. It does not by itself guarantee that stmt captures the buyer’s full notion of value, nor does it hide ledger-level metadata such as payment timing or address linkage. These issues are orthogonal and can be addressed via standard market design and privacy techniques.

---

## 8. Conclusion

We introduced Proxy Adaptor Signatures (PAS), enabling proxy-based fair exchange under delegation while preserving atomicity, witness privacy against intermediaries, and deployability across heterogeneous rails. PAS lets a commerce business post a single request, go offline, and later recover a purchased witness if and only if payment finalizes, without requiring smart contracts or increasing on-chain costs. A Rust prototype demonstrates that PAS is practical at realistic proxy scales.
