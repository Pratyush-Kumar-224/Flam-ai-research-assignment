# AI Research and Development Assignment

## 1. Final Parametric Equation (Submission Format)

$$\left(t*\cos(0.524295)-e^{0.030030\left|t\right|}\cdot\sin(0.3t)\sin(0.524295)\+55.058001,42+\t*\sin(0.524295)+e^{0.030030\left|t\right|}\cdot\sin(0.3t)\cos(0.524295)\right)$$

## 2. Discovered Unknown Variables

* **$\theta$ (theta):** `0.524295` (radians)
* **M:** `0.030030`
* **X:** `55.058001`

## 3. L1 Distance Score

The final L1 distance  achieved by the optimization to find these parameters was:

**`0.028902`**

## 4. Explanation of Process and Steps

The primary challenge was that the $t$ value for each $(x, y)$ coordinate was unknown, making direct fitting impossible. The problem was solved using the following approach:

1.  **Algebraic Transformation:** The original parametric equations were mathematically rearranged. This process, equivalent to an inverse coordinate rotation, served to isolate the parameter $t$. This manipulation resulted in a new system of two equations:
    * **Equation 1:** $t = (x - X) \cos(\theta) + (y - 42) \sin(\theta)$
    * **Equation 2:** $e^{M|t|} \sin(0.3t) = (y - 42) \cos(\theta) - (x - X) \sin(\theta)$

2.  **Error Function:** An objective function was built to quantify the error for any trial set of parameters $(\theta, M, X)$. For any given data point $(x_i, y_i)$, this function performs several checks:
    * It uses **Equation 1** to compute the hypothetical $t$ value, labeled $t_{calc}$.
    * It validates that $t_{calc}$ falls within the required range ($6 < t < 60$). A large penalty is added to the error score if it falls outside this range, steering the optimizer away from invalid solutions.
    * It then computes the left-hand side and right-hand side of **Equation 2** using this $t_{calc}$.
    * The final error for that point is the L1 distance (absolute difference) between these two calculated sides.

3.  **Optimization:** The `scipy.optimize.minimize` function was employed to find the specific values of $(\theta, M, X)$ that minimized the *average* of this error across all 1500 points. The 'SLSQP' method was chosen as it efficiently handles the defined bounds for each parameter. This process converged on the final parameters, which make the two equations consistent for the entire dataset.

## 5. Submitted Code

The Python script (`solve.py`) and the data file (`xy_data.csv`) used to perform this analysis are included in this repository.
