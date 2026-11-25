"""c-chart for weekly counts, built on SIMULATED data.

All numbers are made up; no real data is used. Run: python c_chart.py
"""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
weeks = np.arange(1, 53)
counts = rng.poisson(15, size=52)
counts[[9, 10, 11]] += [14, 16, 20]          # a simulated special-cause burst

c_bar = counts.mean()                         # centre line
ucl = c_bar + 3 * np.sqrt(c_bar)              # upper control limit
lcl = max(0.0, c_bar - 3 * np.sqrt(c_bar))    # lower control limit (not below 0)
out = (counts > ucl) | (counts < lcl)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(weeks, counts, marker="o", color="#1F3A6E", label="Count per week")
ax.plot(weeks[out], counts[out], "o", color="#C0392B", ms=8, label="Signal")
ax.axhline(c_bar, color="#2E8B57", label=f"Centre line {c_bar:.1f}")
ax.axhline(ucl, color="#C0392B", ls="--", label=f"UCL {ucl:.1f}")
ax.axhline(lcl, color="#C0392B", ls="--", label=f"LCL {lcl:.1f}")
ax.set(title="c-chart of weekly counts (simulated data)", xlabel="Week", ylabel="Count")
ax.legend(ncol=5, fontsize=8, loc="upper right")
fig.tight_layout()
fig.savefig("c_chart_example.png", dpi=150)
print(f"centre {c_bar:.2f}, UCL {ucl:.2f}, LCL {lcl:.2f}, signals in weeks {weeks[out].tolist()}")
