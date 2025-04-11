<h1><b>sympy-lu-linsolve</b></h1> 
<p align="justify">
Implementasi fungsi Python untuk menyelesaikan sistem persamaan linear menggunakan metode dekomposisi LU dengan pivoting parsial, memanfaatkan library SymPy.
</p>

<h2><b>Deskripsi</b></h2> 
<p align="justify">
Repositori ini berisi file <code>lu_linsolve.py</code> yang mengimplementasikan fungsi <code>lu_linsolve(A, b)</code>. Fungsi ini menerima matriks koefisien $A$ dan vektor konstanta $\mathbf{b}$ dari sistem persamaan linear $A\mathbf{x} = \mathbf{b}$ sebagai input. Metode dekomposisi LU (Lower-Upper) dengan pivoting parsial dari library SymPy digunakan untuk mencari solusi vektor $\mathbf{x}$.
</p>
<p align="justify">
Langkah-langkah dekomposisi dan penyelesaian sistem ditampilkan secara visual menggunakan format $\LaTeX$, yang sangat berguna dalam lingkungan IPython atau Jupyter Notebook untuk pemahaman yang lebih baik.
</p>

## File

* **`lu_linsolve.py`**: Berisi implementasi fungsi `lu_linsolve(A, b)`.

## Cara Penggunaan

1.  Pastikan Anda telah menginstal library SymPy dan IPython. Anda dapat menginstalnya menggunakan pip:
    ```bash
    pip install sympy ipython
    ```

2.  Impor fungsi `lu_linsolve` dari file `lu_linsolve.py` dalam skrip Python atau Jupyter Notebook Anda:
    ```python
    from sympy import Matrix
    from lu_linsolve import lu_linsolve
    ```

3.  Buat matriks koefisien `A` dan vektor konstanta `b` menggunakan `sympy.Matrix`.

4.  Panggil fungsi `lu_linsolve` dengan matriks `A` dan vektor `b`:
    ```python
    # Contoh sistem persamaan linear:
    # 2x + y + z = 4
    # x + 3y + 2z = 5
    # x + 2y - z = 0

    A = Matrix([[2, 1, 1], [1, 3, 2], [1, 2, -1]])
    b = Matrix([4, 5, 0])

    # Menyelesaikan sistem menggunakan fungsi lu_linsolve
    x = lu_linsolve(A, b)

    print("\nSolusi sistem:")
    print(x)
    ```
    
    Output akan menampilkan matriks $A$, vektor $\mathbf{b}$, matriks permutasi $P$, hasil perkalian $PA$, matriks $L$ dan $U$ dari dekomposisi LU, hasil perkalian $LU$, vektor $P\mathbf{b}$, vektor antara $\mathbf{y}$, dan vektor solusi $\mathbf{x}$ dalam format $\LaTeX$. Selain itu, solusi vektor $\mathbf{x}$ juga akan dicetak di konsol.

## Contoh

Anda dapat melihat contoh penggunaan yang lebih detail dalam file `examples.py` (jika Anda membuatnya). File tersebut mungkin berisi berbagai kasus sistem persamaan linear untuk diuji dengan fungsi `lu_linsolve`.

## Ketergantungan

* **SymPy**: Library Python untuk matematika simbolik.
* **IPython**: Untuk menampilkan output LaTeX yang kaya (khususnya fungsi `display` dan kelas `Math`).

## Kontribusi

Kontribusi dalam bentuk *issue* atau *pull request* dipersilakan. Jika Anda menemukan bug atau memiliki saran untuk perbaikan, jangan ragu untuk memberitahu.

## Lisensi

[Education@Math]
