# Best practices

### TL;DR

* **Fint** supplies PCI‑compliant iframes + token APIs; raw card data never hits your servers.
* **You** keep tokens and logs safe and isolate card data from AI.

---

### Core Principles

* Never commit or log `sk_live_*` keys.
* Card‑reveal tokens are single‑use; invoke them at checkout and discard.
* Treat PAN as toxic; hold it only in RAM during the payment call.
* AI isolation: do **not** pass PAN or tokens to LLM prompts, outputs, or screenshots.
* When in doubt, delete the data.

---

### Data Flow

1. **Frontend** – Use `@fint/wallet`; iframes keep card data off your origin.
2. **Backend** – Store only `{user_id ↔ fint_token}` + `mandate_id`, `request_id`.
3. **Checkout** – Call `revealCardDetails`, pay immediately, forget the PAN.

---

### Key Management

* Store secret keys in env vars only.
* Separate keys per env (dev, staging, prod).
* Rotate keys every 90 days or after any incident.

---

### Quick Checklist

* Frontend uses **only** `pk_live_*`.
* Backend secrets live in env vars, not source.
* `user_id` is consistent across FE/BE.
* No PAN or tokens in logs, errors, or AI prompts.
* `mandate_id` + `request_id` logged for audit.
* HTTPS enforced by default (SDK).
* Secret key rotation scheduled.

*Ship this and you’re done.*
