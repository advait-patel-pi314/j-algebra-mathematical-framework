# j-algebra-mathematical-framework
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21337751.svg)](https://doi.org/10.5281/zenodo.21337751)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# A 5th-Order Nilpotent $j$-Algebraic Framework for Regularized Division by Zero

This repository hosts the manuscript, algebraic formulations, and structural defense for a formal algebraic extension of the real numbers designed to regularize division by zero using a 5th-order nilpotent quotient ring.

## 📄 Core Manuscript & Concepts
* **Target Field:** Abstract Algebra, Ring Theory, Non-Archimedean Systems, Mathematical Physics.
* **Core Algebraic Structure:** $\mathbb{R}[j]/\langle j^5 \rangle$
* **Primary Postulate:** Defining the mapping $x/0 = xj$ for $x \neq 0$ and $0/0 = \infty$ within a consistent ring structure.

---

## 🧮 Theoretical Architecture

### 1. The Ring Structure and Nilpotency
We define the algebraic extension by introducing an element $j$ such that its fifth power vanishes identically:
$$j^5 = 0$$
This generates a 5-dimensional vector space over $\mathbb{R}$ spanned by the basis $\{1, j, j^2, j^3, j^4\}$. Any general element $z$ in this algebra is represented as:
$$z = a_0 + a_1 j + a_2 j^2 + a_3 j^3 + a_4 j^4 \quad (\text{where } a_i \in \mathbb{R})$$

### 2. Matrix Isomorphism Proof
To guarantee absolute structural consistency and eliminate algebraic contradictions (such as $1 = 0$), the framework establishes a rigorous isomorphism mapping elements to $5 \times 5$ upper-triangular Toeplitz matrices:

$$
z \mapsto \begin{pmatrix} 
a_0 & a_1 & a_2 & a_3 & a_4 \\ 
0 & a_0 & a_1 & a_2 & a_3 \\ 
0 & 0 & a_0 & a_1 & a_2 \\ 
0 & 0 & 0 & a_0 & a_1 \\ 
0 & 0 & 0 & 0 & a_0 
\end{pmatrix}
$$

Because matrix multiplication under this configuration is associative and distributive, the ring preserves complete algebraic consistency.

### 3. The Observability Principle
To bridge the gap between intermediate nilpotent scaffolding and observable calculations, we enforce the **Observability Principle** $\mathcal{O}(z)$, which maps the full algebraic element exclusively to its real macroscopic component:
$$\mathcal{O}(z) = a_0 \in \mathbb{R}$$
This ensures that while higher-order transformations ($j$ through $j^4$) act as vital micro-regularizers to prevent coordinate infinities, they remain strictly unobservable at the boundary evaluation.

---

## 📜 License
The documentation and mathematical structures presented in this repository are available under the open-access **CC-BY 4.0** license. Included administrative files are governed by the **MIT License**.

## 📌 Citation

If you use this framework or simulation code in your research, please cite the preprint:

```bibtex
@article{patel2026jalgebra,
  author    = {Patel, Advait},
  title     = {A Non-Singular j-Algebraic Scalar-Tensor Framework},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.21337751},
  url       = {[https://doi.org/10.5281/zenodo.21321137](https://doi.org/10.5281/zenodo.21337751)}
}
