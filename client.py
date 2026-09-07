"""
First-Order Logic Resolution Prover Skill Client
Pure Python Standard Library implementation of Robinson's First-Order Resolution Refutation.
Unifies atomic literals via Most General Unifier (MGU) and iteratively derives the empty clause (contradiction).
"""

from typing import List, Dict, Any, Tuple, Optional, Set


class Literal:
    def __init__(self, predicate: str, terms: List[str], is_negated: bool = False):
        self.predicate = predicate
        self.terms = terms
        self.is_negated = is_negated

    def __repr__(self):
        neg = "~" if self.is_negated else ""
        return f"{neg}{self.predicate}({', '.join(self.terms)})"

    def negate(self) -> "Literal":
        return Literal(self.predicate, list(self.terms), not self.is_negated)


class Clause:
    def __init__(self, literals: List[Literal]):
        self.literals = literals

    def __repr__(self):
        if not self.literals:
            return "FALSE (Empty Clause)"
        return " v ".join(repr(l) for l in self.literals)

    @property
    def is_empty(self) -> bool:
        return len(self.literals) == 0


class ResolutionProver:
    def __init__(self):
        pass

    @staticmethod
    def is_variable(term: str) -> bool:
        return term.startswith("?")

    def mgu(self, terms1: List[str], terms2: List[str], theta: Optional[Dict[str, str]] = None) -> Optional[Dict[str, str]]:
        """Most General Unification algorithm."""
        if theta is None:
            theta = {}
        if len(terms1) != len(terms2):
            return None
        if not terms1:
            return theta

        t1, t2 = terms1[0], terms2[0]
        # Apply current substitutions
        while t1 in theta:
            t1 = theta[t1]
        while t2 in theta:
            t2 = theta[t2]

        if t1 == t2:
            return self.mgu(terms1[1:], terms2[1:], theta)
        elif self.is_variable(t1):
            theta[t1] = t2
            return self.mgu(terms1[1:], terms2[1:], theta)
        elif self.is_variable(t2):
            theta[t2] = t1
            return self.mgu(terms1[1:], terms2[1:], theta)
        else:
            return None  # Mismatch constant

    def resolve(self, c1: Clause, c2: Clause) -> List[Clause]:
        resolvents = []
        for l1 in c1.literals:
            for l2 in c2.literals:
                if l1.predicate == l2.predicate and (l1.is_negated != l2.is_negated):
                    subst = self.mgu(l1.terms, l2.terms)
                    if subst is not None:
                        # Construct resolvent clause
                        rem_c1 = [l for l in c1.literals if l is not l1]
                        rem_c2 = [l for l in c2.literals if l is not l2]
                        new_lits = []
                        for l in rem_c1 + rem_c2:
                            applied_terms = [subst.get(t, t) for t in l.terms]
                            new_lits.append(Literal(l.predicate, applied_terms, l.is_negated))
                        resolvents.append(Clause(new_lits))
        return resolvents

    def prove_refutation(self, clauses: List[Clause], max_steps: int = 50) -> bool:
        knowledge = list(clauses)
        for _ in range(max_steps):
            new_clauses = []
            n = len(knowledge)
            for i in range(n):
                for j in range(i + 1, n):
                    res_list = self.resolve(knowledge[i], knowledge[j])
                    for r in res_list:
                        if r.is_empty:
                            return True  # Contradiction derived!
                        new_clauses.append(r)
            if not new_clauses:
                break
            knowledge.extend(new_clauses[:10])
        return False
