Signature Methods for Optimal Execution

This repository contains the implementation, experiments, and results associated with my thesis on signature-based methods for optimal execution in financial markets. The project applies ideas from rough path theory and tensor algebra to model market paths and optimize liquidation strategies.

📖 Overview

Problem:
Optimal execution is the task of liquidating a large asset position over a fixed horizon, balancing market impact and price risk.

Challenge:
Classical models rely heavily on distributional assumptions (e.g., Brownian motion). Real market prices often exhibit roughness, long-memory, and non-Markovian features.

Contribution:
We approximate the solution of the optimal execution problem using path signatures, which encode the statistical structure of price paths in a linear and tractable way.

🔬 Methodology

Path Signatures

Each midprice path is represented by its signature, i.e., the collection of its iterated integrals.

Signatures provide a rich, algebraic representation of path-dependent information.

Optimization reduces to a convex quadratic program in the coefficients 

Simulation & Optimization

Midprice modeled as Brownian motion and fractional Brownian motion.

Expected signatures estimated using Monte Carlo simulation.

Optimization solved via cvxpy
.

Benchmarks

Results compared with TWAP (Time-Weighted Average Price) and, when available, the exact expected signature.

📊 Experiments

Time Discretization:
Increasing execution steps generally improves performance (not strictly monotonic).

Volatility 
Higher volatility improves performance, but Monte Carlo error grows proportionally.

Hurst Parameter 

rougher paths, signature captures structure well.


Truncation Level 

Higher truncation increases accuracy, but cost grows factorially in 

⚙️ Requirements

Python 3.8+

NumPy

cvxpy

Matplotlib

scikit-learn
 (for utilities)

Install dependencies via:

pip install -r requirements.txt



📌 Limitations

Fractional Brownian motion is not arbitrage-free, so real market applications require caution.

Monte Carlo error grows with volatility; variance reduction methods should be explored.

Computational cost grows rapidly with truncation level 
𝑁
N.

🚀 Future Work

Apply the method directly to real market data.

Explore variance reduction techniques for signature estimation.

Investigate adaptive truncation strategies for balancing accuracy and cost.

📚 References

Lyons, T. J. (1998). Differential equations driven by rough signals.

Mandelbrot, B. B. (1997). Fractals and Scaling in Finance.

Gatheral, J., Jaisson, T., & Rosenbaum, M. (2018). Volatility is rough.

✨ Acknowledgements

This project was developed as part of my Master’s thesis. Thanks to my advisor, colleagues, and the broader rough paths community for their guidance and inspiration.
