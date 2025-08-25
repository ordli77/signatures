# Signature Methods for Optimal Execution

This repository contains the implementation, experiments, and results associated with my thesis on **signature-based methods for optimal execution in financial markets**. The project applies ideas from **rough path theory** and **tensor algebra** to model market paths and optimize liquidation strategies.

---

## 📖 Overview

- **Problem:**  
  Optimal execution is the task of liquidating a large asset position over a fixed horizon, balancing **market impact** and **price risk**.  

- **Challenge:**  
  Classical models rely heavily on distributional assumptions (e.g., Brownian motion). Real market prices often exhibit **roughness**, **long-memory**, and **non-Markovian** features.  

- **Contribution:**  
  We approximate the solution of the optimal execution problem using **path signatures**, which encode the statistical structure of price paths in a linear and tractable way.  

---

## 🔬 Methodology

1. **Path Signatures**  
   - Each midprice path is represented by its **signature**, i.e., the collection of its iterated integrals.  
   - Signatures provide a rich, algebraic representation of path-dependent information.  

2. **Trading Strategy**  
   - Trading speed \(\theta_t\) is modeled as a **linear functional** of the truncated signature:  
     ```
     θ_t = <ℓ, 𝑿̂_[0,t]>
     ```
   - Optimization reduces to a convex quadratic program in the coefficients ℓ.  

3. **Simulation & Optimization**  
   - Midprice modeled as Brownian motion and fractional Brownian motion.  
   - Expected signatures estimated using **Monte Carlo simulation**.  
   - Optimization solved via [gurobipy](https://pypi.org/project/gurobipy/).  

4. **Benchmarks**  
   - Results compared with **TWAP** (Time-Weighted Average Price) and, when available, the **exact expected signature**.

---

## 📊 Experiments

- **Time Discretization:**  
  Increasing execution steps generally improves performance (not strictly monotonic).  

- **Volatility (σ):**  
  Higher volatility improves performance, but Monte Carlo error grows proportionally.  

- **Hurst Parameter (H):**  
  - \(H < 0.5\): rougher paths, signature captures structure well.  
  - \(H = 0.5\): standard Brownian motion, weaker performance (no increment correlation).  

- **Truncation Level (N):**  
  Higher truncation increases accuracy, but cost grows factorially in \(N\).  

---

## ⚙️ Requirements

- Python 3.8+  
- [NumPy](https://numpy.org/)  
- [gurobipy](https://pypi.org/project/gurobipy/)  
- [Matplotlib](https://matplotlib.org/)  
- [scikit-learn](https://scikit-learn.org/)
- [iisignature](https://pypi.org/project/iisignature/) 

Install dependencies via:  
```bash
pip install -r requirements.txt
```


## 📚 References

Lyons, T. J. (1998). Differential equations driven by rough signals.

Mandelbrot, B. B. (1997). Fractals and Scaling in Finance.

Gatheral, J., Jaisson, T., & Rosenbaum, M. (2018). Volatility is rough.
