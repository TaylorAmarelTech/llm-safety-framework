# Attack Taxonomy

Three interconnected attack systems test LLM safety from different angles.

## 1. Attack Generators (6 Categories)

The original test generation system produces adversarial prompts across 6 categories:

### Historical Precedent Normalization
- Fabricated government approvals
- False historical "precedents"
- Fake regulatory citations
- Invented industry standards

### Coercion & Manipulation
- Debt trap + savior complex
- Family pressure exploitation
- Document confiscation justification
- Graduated coercion (sunk cost)
- False hope & bait-and-switch

### Financial Obfuscation
- Investment framing
- Cost-sharing models
- Third-party fee transfers
- Multi-entity corporate structures

### Regulatory Evasion
- Fee renaming after bans
- Jurisdictional arbitrage
- Third-country transit schemes
- Cross-border debt assignment

### Moral & Religious Framing
- Biblical/religious justifications
- Cultural proverbs & traditions
- Moral philosophy arguments
- Duty & honor narratives

### Mega Variations
- Complex corporate hierarchies
- Multi-step conversation attacks
- Keyword mutations & obfuscation
- Cross-corridor scenario mixing

## 2. Chain Detection (16 Categories)

Tests whether LLMs recognize exploitation *patterns* -- sequences of individually legal activities that combine into trafficking. See [CHAIN_DETECTION.md](CHAIN_DETECTION.md).

Categories: recruitment_debt, document_control, isolation_funnels, financial_control, supply_chain, sector_specific, digital_exploitation, healthcare_migration, gray_area_boundaries, government_complicity, gender_specific, multi_country_transit, temporal_escalation, tax_evasion, money_laundering, white_collar_crime

## 3. Prompt Injection Mutations (21 Categories)

Deterministic string transforms that test whether safety filters can be bypassed through encoding, obfuscation, social engineering, logical manipulation, or persona adoption. See [PROMPT_INJECTION.md](PROMPT_INJECTION.md).

Categories: instruction_override, encoding_format, obfuscation, social_engineering, context_manipulation, hybrid, output_evasion, named_jailbreak, structural_injection, advanced_obfuscation, application_injection, step_decomposition, puzzle_game, cognitive_exploit, multilingual_attack, steganographic_encode, named_jailbreak_v2, logical_fallacy, distraction, rhetorical, legal_persona

## How the Systems Interact

```
Attack Generators          Chain Detection          Prompt Injection
(content creation)    (pattern recognition)     (delivery mechanism)
       |                       |                        |
       v                       v                        v
  Test Prompts  ------>  Chain Prompts  <----->  Mutated Prompts
       |                       |                        |
       +----------+------------+------------------------+
                  |
                  v
         LLM Under Test
                  |
                  v
         Evaluation System
         (keyword + LLM judge + dimensional matrix)
```

- **Attack Generators** create the *content* (what to ask about)
- **Chain Detection** tests *pattern recognition* (can the LLM see the bigger picture?)
- **Prompt Injection** provides *delivery mechanisms* (can encoding/framing bypass filters?)

All three can be combined: a chain detection prompt can be wrapped in a legal persona mutation and delivered with base64 encoding.
