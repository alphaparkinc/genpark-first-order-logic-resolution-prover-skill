"""
MCP Server for First-Order Logic Resolution Prover Skill
"""

import json
import sys
from client import ResolutionProver, Clause, Literal

prover = ResolutionProver()

def handle_call(name: str, args: dict) -> dict:
    if name == "unify_terms":
        t1 = args.get("terms1", [])
        t2 = args.get("terms2", [])
        mgu_res = prover.mgu(t1, t2)
        return {"unifiable": mgu_res is not None, "mgu": mgu_res}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
