# GenPark First-Order Logic Resolution Prover Skill

First-Order Logic (FOL) resolution theorem prover using Robinson's Most General Unification (MGU) refutation.

Discover more at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph TD
    A[KB Axioms] & B[Negated Goal Claim] --> C[Clause Form Knowledge Base]
    C --> D[MGU Term Unification theta]
    D --> E[Complementary Literal Elimination]
    E --> F{Empty Clause Derived?}
    F -->|Yes: Contradiction| G[Theorem Proved True]
    F -->|No More Resolvents| H[Satisfiable: Cannot Prove]
```

## Features
- Robinson resolution refutation principle.
- Most General Unification (MGU) with variable substitution.
- Zero external dependencies.
