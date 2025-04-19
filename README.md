# WNBA Player Archetypes (Sample Project)

This is a **sample code project** simulating the kind of player archetyping I worked on in The Data Mine. The actual dataset is private, so this uses a small set of public WNBA stats for demonstration purposes only.

## Overview
We cluster WNBA players into 4 archetypes using:
- **Features**: Points, Assists, Rebounds, Steals, Blocks, 3PT Made, 2PT Made
- **Algorithm**: KMeans (scikit-learn)
- **Visualization**: Points vs Assists (matplotlib)

---
> However, for this mini-project, we’ve used 3PT Made and 2PT Made from an AI-generated sample WNBA dataset to preserve the privacy of the original data.

## How to Run
```bash
pip install pandas scikit-learn matplotlib
python main.py
```

## Project Structure
```
wnba_archetypes_sample/
├── data/
│   └── sample_wnba_stats.csv
├── src/
│   ├── clustering.py
│   └── visualize.py
├── main.py
└── README.md
```

---
> ⚠️ Note: This is not the full project from The Data Mine, which included private NCAA/Euro League data and deeper modeling. This sample is built only to demonstrate conceptually similar code for review.
