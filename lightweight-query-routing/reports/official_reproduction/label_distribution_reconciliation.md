# Label-distribution reconciliation

**The official local dataset has multi_hop as the majority class at 52.8795%, while the lightweight paper describes single_hop as the majority class at 52.9%.**

| Local label | Local count | Local % | Paper-implied count | Paper % | Difference (pp) | Local rank | Paper rank | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| single_hop | 2320 | 30.0246 | 4087.583 | 52.9 | -22.8754 | 2 | 1 | MISMATCH |
| multi_hop | 4086 | 52.8795 | 1321.317 | 17.1 | 35.7795 | 1 | 3 | MISMATCH |
| summary | 1321 | 17.0959 | 2318.100 | 30.0 | -12.9041 | 3 | 2 | MISMATCH |

The same proportions approximately align under an inferred cyclic name permutation:

- local `multi_hop` → paper `single_hop`

- local `single_hop` → paper `summary`

- local `summary` → paper `multi_hop`

This is an audit observation only. It is not proven ground truth and is not used by the primary protocol.
