# Reproduction gaps


The paper claims 23 structural features, but its written enumeration identifies only 18. This package deliberately implements only those 18 as `structural_documented_18`; it does not invent five undocumented features. Its named-entity and clause-count heuristics are deterministic documented approximations because the paper does not specify them.

Other possible numerical differences include unknown original ordering, unknown CV shuffle behavior and seed, unknown scikit-learn version, unspecified text-preprocessing defaults, the five missing structural definitions, and the paper’s count discrepancy: it states 7,727 queries while printed domain counts total 7,729.
