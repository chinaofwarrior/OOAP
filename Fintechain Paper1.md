# Fintechain Agent

## Abstract

Financial inclusion has long been regarded as a critically important objective for human society. Yet, due to productivity constraints failing to reach a necessary threshold and deep structural inequities embedded in prevailing production relations, it has remained peripheral within mainstream financial infrastructure. Since the first generation of financial inclusion advocates—most notably Muhammad Yunus of the Grameen Bank—efforts have largely remained programmatic rather than infrastructural, failing to integrate financial inclusion as a native capability of the global financial system.

Human society is now undergoing a structural transition. Artificial intelligence and blockchain are jointly addressing the two binding constraints that historically limited financial inclusion: the cost of economic coordination and the rigidity of production relations. Using a Problem-Oriented Technique, the Fintechain research program decomposes this transition into a sequence of twelve papers.

If small and medium-sized enterprises (SMEs) are included as first-order beneficiaries of financial inclusion, commerce businesses become the most observable and measurable unit of economic activity. This paper focuses on Commerce Agents operating in procurement and payment-adjacent scenarios, and on the methodologies required to train and evaluate such agents. The objective of this paper is not credit access itself, but the precondition for it: whether agent-mediated commerce can generate transaction behavior that is stable, auditable, and economically interpretable. How such transaction traces can be transformed into capital access mechanisms is addressed in the subsequent paper.

---

## 1. Introduction

Commerce is undergoing a structural transformation. AI-powered shopping and procurement assistants are transitioning from experimental tools to operational agents [13]. Industry leaders have begun to acknowledge this shift; for example, Walmart’s CTO has explicitly warned that third-party AI agents may bypass traditional merchandising and advertising mechanisms¹. In this setting, product discovery, comparison, and selection are increasingly delegated from humans to autonomous systems.

Recent “computer-use” agents—such as OpenAI’s browser-based agents or Google’s Project Mariner—demonstrate the ability to complete end-to-end procurement workflows, including browsing, form filling, and checkout. As these systems proliferate, a foundational question emerges: how do such agents actually make economic decisions?

AI agents can dramatically reduce search costs by scanning and evaluating product spaces far beyond human cognitive limits. However, it is not obvious that they behave as the fully rational optimizers assumed in classical economic models. Instead, they may constitute a distinct class of economic actors with systematic biases, provider-specific heuristics, and version-dependent behavior. If so, the delegation of commerce to agents may fundamentally alter market dynamics rather than merely automate existing ones.

Parallel changes occur on the supply side. Sellers increasingly adapt product listings in anticipation of algorithmic evaluation rather than human perception, suggesting the emergence of a new optimization regime distinct from traditional SEO. Together, these developments motivate a core research question:

**What do Commerce Agents buy—and why?**

This paper examines four dimensions of this question:
(1) baseline rationality and instruction-following;
(2) induced product market shares under full delegation;
(3) sensitivity to product attributes and platform levers;
(4) strategic interactions between buyer agents and seller-side optimization.

The first dimension establishes minimum viability. Without basic rationality, higher-order design and policy questions are irrelevant. The remaining dimensions characterize agent-mediated markets as a distinct economic system rather than a scaled version of human e-commerce.

---

## 2. The Commerce Agent Simulator (CAS)

Studying agent-mediated commerce presents a methodological challenge: realistic commerce decisions are inherently unlabeled. There is no canonical “correct” product choice in most procurement contexts. CAS (Commerce Agent Simulator) addresses this by converting the commerce environment itself into an experimental instrument.

CAS is a controlled agent–platform sandbox that pairs multimodal large language models with fully programmable simulated commerce applications. It enables randomized experiments by independently varying product attributes and platform-level presentation factors, allowing causal identification of how these variables influence agent decisions.

Each task instance consists of:
(i) a procurement prompt;
(ii) a fixed-size product set (typically eight items);
(iii) randomized assignment of attributes, ranks, and labels;
(iv) an execution mode (web-based computer-use or headless/API).

The outcome is a single discrete choice. This one-shot abstraction is deliberate: repeated choices aggregate directly into market shares in a delegated procurement regime.

Product attributes include price, ratings, review counts, and textual descriptions. Platform levers include ranking position and labels such as “Sponsored,” “Platform-endorsed,” or “Limited stock.” Randomization ensures that observed choice effects are attributable to these variables rather than hidden correlations.

CAS is inspired by behavioral economics rather than leaderboard-style benchmarks. In domains such as commerce, causal behavior must be recovered through randomized environments rather than objective labels. While CAS supports full visual webpage interaction, the same methodology applies to headless settings where agents receive structured product lists via API, allowing isolation of interface effects from model-level decision rules.

---

## 3. Baseline Rationality

We first evaluate minimum rationality through instruction-following and dominance tests. Choice sets are constructed such that exactly one option satisfies a constraint or strictly dominates others on a single attribute.

Earlier-generation models occasionally violate dominance under small margins, such as failing to select the cheapest item when price differences are minimal. Newer models exhibit near-perfect performance on these tasks. By late 2025, frontier models reliably satisfy one-dimensional constraints.

However, dominance rationality does not generalize to realistic multi-attribute environments. Models that pass constraint tests may still exhibit strong positional or labeling biases when no uniquely correct answer exists. Rationality is therefore a necessary but insufficient condition for stable agent-mediated commerce.

---

## 4. Market Shares Under Delegation

Using generic procurement prompts, we estimate selection frequencies as proxies for market shares in a fully delegated setting. Identical product catalogs yield dramatically different market shares across model providers.

We observe strong concentration effects. In many categories, a small subset of products absorbs the majority of selections, while others are effectively never chosen. Model upgrades can induce abrupt reordering of these shares, even when prompts and product sets are held constant.

This implies that market structure under delegation is partially determined by the agent policy itself. Model choice and model upgrades function as implicit economic interventions rather than neutral technical decisions.

---

## 5. Choice Behavior and Bias

Randomized experiments reveal persistent position bias. Agents disproportionately select higher-ranked items even when rank is uncorrelated with price or quality. This effect persists in headless environments, indicating that it is not purely visual salience but an internalized heuristic treating rank as a latent endorsement.

Platform labels exert strong influence. “Sponsored” markers reduce selection probability, while endorsement labels increase it. The magnitude and direction of these effects vary across model providers and across versions, undermining the assumption that disclosure mechanisms have uniform behavioral impact.

Sensitivity to price, ratings, and reviews differs substantially across models. Textual descriptions exert non-trivial influence, enabling small wording changes to materially shift outcomes. These sensitivities are not stable across upgrades, producing behavioral drift even when prompts are unchanged.

---

## 6. Buyer–Seller Agent Interactions

When sellers deploy optimization-oriented agents to modify product descriptions in response to procurement queries, market shares shift significantly. Even simple, query-conditioned edits can increase selection probability.

This indicates the emergence of a new optimization regime: sellers optimize for model heuristics rather than human interpretation. Agent-mediated markets therefore risk converging toward adversarial text dynamics unless constrained by platform design.

---

## 7. Robustness: Headless Interaction

To test whether observed biases are interface artifacts, we repeat experiments in headless settings where agents receive structured product lists without visual layout.

Position bias, label effects, and cross-model heterogeneity persist. This demonstrates that the core phenomena are decision-rule-level properties rather than UI artifacts. Consequently, UI design alone is insufficient to govern agent behavior; direct auditing of agent decision policies is required.

---

## 8. Implications for Financial Inclusion

Agent-mediated commerce intersects with financial inclusion through transaction generation. If Commerce Agents mediate procurement and payments, transaction histories become partially endogenous to model behavior.

Market concentration, price sensitivity, and upgrade-induced drift directly affect SME cashflows. If such transaction traces are used for credit assessment, their reliability depends on the stability and interpretability of the agent layer that generated them.

CAS therefore serves not only as an e-commerce evaluation tool but as a prerequisite auditing layer for any financial inclusion system that relies on agent-generated economic data.

---

## 9. Conclusion

This paper introduces CAS as a framework for evaluating Commerce Agents and studies the behavior of agent-mediated commerce. While baseline rationality improves rapidly, agent-mediated markets exhibit structural volatility: market shares depend on model family, upgrades reorder outcomes, and persistent biases shape procurement behavior.

Delegated commerce is not simply automated e-commerce. It is a distinct economic regime with its own decision rules and instabilities. For platforms, this necessitates continuous auditing. For financial inclusion, it establishes a critical requirement: before transaction data can support capital access, the agents generating that data must be auditable, stable, and economically interpretable.

The subsequent paper examines how audited transaction traces produced by Commerce Agents can be transformed into credit personas and capital access mechanisms without reintroducing the structural inequities that financial inclusion seeks to resolve.

