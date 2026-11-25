# DMAIC tools: when and how I use them

## Scatter plot (Analyze)
**When:** to see whether two continuous variables move together, before calling something a root cause.
**How:** collect X and Y pairs, plot one dot per pair, read direction, strength, shape and outliers. It shows association, not cause.

## Regression and correlation (Analyze)
**When:** after a scatter plot shows a roughly straight-line pattern, to measure the link and predict Y from X.
**How:** read r (direction and strength), R² (variation explained) and the p-value (below 0.05 is significant); write Y = b0 + b1·X; check the residuals; predict only inside the data range.

## Pareto chart (Analyze)
**When:** to find the few causes that matter most.
**How:** count each cause, sort the bars from largest to smallest, add a cumulative line, focus on the causes that make up about 80% of the total.

## Decision matrix (Improve)
**When:** to choose the best option after testing several.
**How:** set the purpose, criteria and targets, record each option's results, compare them against the targets, pick the best or ask for more data.

## Test Planner (Improve)
**When:** before a pilot, to plan how a change will be tested.
**How:** state the purpose, what will be measured and how, list sources of measurement noise, define the input levels, note the inputs that can't be controlled.

## Process control plan (Control)
**When:** after the change, so the gain lasts and nobody over-adjusts the process.
**How:** list the key steps and their inputs and outputs, set the specifications, say how each is measured, who checks it, where and how often, and what to do when a result is out of spec.

## c-chart (Control)
**When:** to watch a count per period (for example breakdowns per week) and tell a real signal from normal variation.
**How:** centre line = average count; limits = centre ± 3 × √centre; a point outside the limits or a long run on one side of the centre is a signal. See the [Python example](../02_data-analysis/c-chart-example/).
