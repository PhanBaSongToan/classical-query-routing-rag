# Dataset audit

- Source: `C:\Users\ACER\Code\LLM-Semantic-Router\lightweight-query-routing\data\raw\ragrouter-dataset\data`
- SHA-256: `c3566f9dca7c322861767df5b5384b97f25fac82344ef84615027cc67f77c7a9`
- Format: directory:jsonl_in_json_extension
- Parsed / valid / invalid: 7727 / 7727 / 0
- Detected fields: query=`question`, label=`type`, domain=`domain`, id=`id`

## Integrity

- Missing or empty queries: 0
- Missing labels: 0
- Unknown labels: 0
- Unique IDs / duplicate IDs: 7727 / 0
- Exact duplicate queries: 105
- Duplicate queries with conflicting labels: 0
- Duplicate IDs with conflicting content: 0
- Duplicate queries across domains: 0

## Distribution

```json
{
  "classes": {
    "multi_hop": {
      "count": 4086,
      "percent": 52.8795
    },
    "single_hop": {
      "count": 2320,
      "percent": 30.0246
    },
    "summary": {
      "count": 1321,
      "percent": 17.0959
    }
  },
  "domains": {
    "graphragBench_medical": {
      "count": 1896,
      "percent": 24.5373
    },
    "musique": {
      "count": 3356,
      "percent": 43.4321
    },
    "quality": {
      "count": 1198,
      "percent": 15.5041
    },
    "ultraDomain_legal": {
      "count": 1277,
      "percent": 16.5265
    }
  },
  "labels_within_domain": {
    "graphragBench_medical": {
      "multi_hop": {
        "count": 509,
        "percent": 26.846
      },
      "single_hop": {
        "count": 1098,
        "percent": 57.9114
      },
      "summary": {
        "count": 289,
        "percent": 15.2426
      }
    },
    "musique": {
      "multi_hop": {
        "count": 2590,
        "percent": 77.1752
      },
      "single_hop": {
        "count": 398,
        "percent": 11.8594
      },
      "summary": {
        "count": 368,
        "percent": 10.9654
      }
    },
    "quality": {
      "multi_hop": {
        "count": 461,
        "percent": 38.4808
      },
      "single_hop": {
        "count": 454,
        "percent": 37.8965
      },
      "summary": {
        "count": 283,
        "percent": 23.6227
      }
    },
    "ultraDomain_legal": {
      "multi_hop": {
        "count": 526,
        "percent": 41.1903
      },
      "single_hop": {
        "count": 370,
        "percent": 28.9742
      },
      "summary": {
        "count": 381,
        "percent": 29.8356
      }
    }
  }
}
```

## Paper accounting note

The paper states 7,727 total queries. Its printed domain counts (3,356 + 1,200 + 1,277 + 1,896) sum to 7,729. This audit reports the discrepancy without attempting to fix it.
