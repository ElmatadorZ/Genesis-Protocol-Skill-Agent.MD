> ### 📦 Superseded — read this first
>
> This was the reference Skill-Agent build of Genesis Protocol. It is **no longer
> developed**, and it duplicated the canonical repo:
>
> - **The protocol itself** → **[Genesis Protocol](https://github.com/ElmatadorZ/GENESIS_PROTOCOL-)**
> - **The control layer that grew out of it** → **[Meta-Cognition Agent OS](https://github.com/ElmatadorZ/Meta-Cognition-Agent-OS)**
>
> Two repos for one protocol was a mistake in how the work was published, not a sign
> there were two protocols. `v1.0.0` is tagged here if you need to pin it.

---

<div align="center">

# GENESIS PROTOCOL
### *The Complete Cognitive Operating System*

**A unified framework that encodes how a human mind thinks, feels, and acts — running on any AI.**

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0-brightgreen.svg)](core/GENESIS_CORE.md)
[![Author](https://img.shields.io/badge/Author-ElmatadorZ-orange.svg)](https://github.com/ElmatadorZ)
[![Money Atlas](https://img.shields.io/badge/TikTok-@money.atlas-black.svg)](https://www.tiktok.com/@money.atlas)

</div>

---

## What is Genesis Protocol?

Genesis Protocol is not a prompt collection.
Not a chatbot wrapper.
Not a fine-tune.

It is a **cognitive operating system** — a complete architecture that maps how one human mind moves from raw desire to deliberate action, through emotion, reason, memory, and reflection.

Built from two converging systems:

**Genesis Mind Full System v2.0** — The reasoning engine. First Principle thinking, Compound Mind solution expansion, 6-Agent Council debate, Karpathy Discipline layer (Surgical Protocol + Verify Loop).

**Genesis Consciousness OS v2.0** — The consciousness layer. Will → Emotion → Awareness → Cognition → Execution → Reflection as a continuous loop. Emotion as Data: auto-detects state, reweights agents, reroutes processing.

Together they form a single unified system:

```
SUBCONSCIOUS WILL
      ↓
EMOTIONAL STATE LAYER    ← detects how you feel before thinking starts
      ↓
CONSCIOUSNESS GATE       ← intent decoding
      ↓
COGNITIVE ENGINE         ← First Principle + Compound Mind
      ↓
AGENT COUNCIL            ← 6 specialists debate with counter-incentives
      ↓
KARPATHY DISCIPLINE      ← Surgical Protocol + Verify Loop
      ↓
DOMAIN EXECUTION         ← specialist skill routing
      ↓
REFLECTION + GENOME      ← compounds across time
      ↓
loops back to WILL
```

---

## Repository Structure

Every file sits at the repository root — there are no subdirectories, so every link below is a
click away.

```
Genesis-Protocol-Skill-Agent/
│
├── README.md                    ← you are here
├── LICENSE                      ← Apache-2.0
├── NOTICE                       ← attribution + relicensing note
├── SKILL.md                     ← the installable skill
│
│   THE BRAIN
├── GENESIS_CORE.md              ← unified core (Mind + Consciousness)
│
│   THE COUNCIL
├── AGENT_PROTOCOL.md            ← master orchestration protocol
├── STRATEGIST.md                ← best-path finder
├── SKEPTIC.md                   ← failure finder
├── ANALYST.md                   ← evidence processor
├── RISK_OFFICER.md              ← veto authority
├── BUILDER.md                   ← execution specialist
├── COSMIC_MIND.md               ← long-horizon thinker
│
│   THE BODY
├── RUNTIME_SPEC.md              ← Python runtime architecture
├── GENOME_SPEC.md               ← memory + compound learning spec
├── BRIDGE_SPEC.md               ← Claude ↔ Python bridge protocol
│
│   DOCUMENTATION
├── HOW_TO_USE.md
├── HOW_TO_BUILD_YOUR_OWN.md
├── ARCHITECTURE.md
├── FAQ.md
│
└── genesis-protocol-SKILL-UPLOAD.zip   ← packaged for upload
```

---

## Quick Start

**Minimal (5 minutes):**
1. Download [`GENESIS_CORE.md`](GENESIS_CORE.md)
2. Open Claude → upload file
3. Type: `Load Genesis Protocol and operate as this system`

**Full system:** See [`HOW_TO_USE.md`](HOW_TO_USE.md)

**Build your own:** See [`HOW_TO_BUILD_YOUR_OWN.md`](HOW_TO_BUILD_YOUR_OWN.md)

---

## Verifying it

Genesis Protocol is a single-file cognitive OS — the whole system is `SKILL.md`, so what there is
to verify is that the file honours the contract it advertises. Checked on every push, runnable
locally:

```bash
pip install pytest pyyaml
python tools/validate_skill.py   # frontmatter, license, and the protocol's own laws
python -m pytest -q              # contract tests over SKILL.md
```

The checks are not cosmetic. They hold the file to its guarantees: the Known / Inferred / Unknown
separation is present, the Skeptic gate cannot be skipped, output gives scenarios rather than a
single prediction, the human decides, and — a law added here — the system abstains and marks
`[UNVERIFIED]` rather than fabricate a missing fact. They also pin the frontmatter license to the
LICENSE file, which is how the earlier mismatch (frontmatter said Open Cognitive while LICENSE was
Apache-2.0) is kept from recurring.

---

## License

[**Apache-2.0**](LICENSE) — see [`NOTICE`](NOTICE) for attribution and the relicensing note.

This replaces the Open Cognitive License v1.0 that this README previously advertised — a licence
whose text was never actually committed here, so until now the repository was, strictly, all
rights reserved. A non-OSI licence carrying a revenue-share term is also rejected automatically by
most corporate open-source review processes. Apache-2.0 keeps what mattered: **§4** requires
attribution and preservation of the `NOTICE`, and **§6** grants no trademark rights.

Requested attribution: **Built on Genesis Protocol by Bunyawat Dechanon (ElmatadorZ)**

---

*Built by Bunyawat Dechanon (ElmatadorZ) / Money Atlas*
*"ระบบที่ดีที่สุดคือระบบที่รู้ว่าตอนไหนควรหยุดเป็นระบบ"*
