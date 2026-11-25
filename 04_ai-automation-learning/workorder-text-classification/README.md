# Work-order text classification (planned)

**Goal:** sort free-text maintenance notes (for example "chain off again" or "replaced bearing on infeed") into part families and failure modes automatically.

**Why:** maintenance notes describe the same failure in many different ways, so finding repeat failures by hand is slow. A text classifier could keep a repeat-failure list up to date each week.

**Plan:**
1. Build a small labeled sample of made-up notes.
2. Try a Hugging Face text-classification model and compare it with simple keyword rules.
3. Measure agreement against hand labels before trusting it.

Status: learning stage. Files will follow the pattern `YYYY-MM-DD_workorder-classifier_vN`.
