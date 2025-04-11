
from sympy import Matrix, simplify, init_printing, latex, eye, prod
from IPython.display import display, Math

init_printing(use_latex=True)

def lu_linsolve(A,b):
    L, U, perm = A.LUdecomposition()
    n = A.rows
    P = eye(n)

    # Fix: perm adalah daftar pasangan [i, j] yang harus ditukar
    for swap in perm:
        if isinstance(swap, (list, tuple)) and len(swap) == 2:
            i, j = swap
            P.row_swap(i, j)

    Pb = P @ b
    y = L.solve(Pb)
    x = U.solve(y)

    display(Math(r"A = " + latex(A) + r", \mathbf{{b}} = " + latex(b)))
    display(Math(r"P = " + latex(P) + r", PA = " + latex(P@A)))
    display(Math(r"L = " + latex(L) + r", U = " + latex(U)))
    display(Math(r"LU = " + latex(L @ U) + r", P\mathbf{{b}} = " + latex(Pb)))
    display(Math(r"\mathbf{{y}} = " + latex(y) + r", \mathbf{{x}} = " + latex(x)))

    return x
