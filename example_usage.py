"""
Demonstration of First-Order Logic Resolution Prover Skill
"""

from client import ResolutionProver, Clause, Literal

def main():
    print("=== Testing First-Order Logic Resolution Refutation Prover ===")
    prover = ResolutionProver()

    # Axiom 1: All humans are mortal: ~Human(?x) v Mortal(?x)
    c1 = Clause([Literal("Human", ["?x"], is_negated=True), Literal("Mortal", ["?x"])])
    # Axiom 2: Socrates is human: Human(socrates)
    c2 = Clause([Literal("Human", ["socrates"])])
    # Goal negated: Socrates is NOT mortal: ~Mortal(socrates)
    neg_goal = Clause([Literal("Mortal", ["socrates"], is_negated=True)])

    clauses = [c1, c2, neg_goal]
    print("Knowledge Base + Negated Goal:")
    for c in clauses:
        print("  -", c)

    proved = prover.prove_refutation(clauses)
    print(f"\nRefutation Contradiction Found (Theorem Proved): {proved}")
    assert proved is True
    print("First-Order Logic Resolution Prover Verification PASS!")

if __name__ == "__main__":
    main()
