# -*- coding: utf-8 -*-
"""
Полное решение задачи 6 по трехотраслевой модели межотраслевого баланса.

Требование: Python 3 + NumPy
Установка NumPy (если библиотека отсутствует):
    pip install numpy

Скрипт выводит все этапы решения в консоль и одновременно сохраняет их
в текстовый файл "polnoe_reshenie_mob.txt".
"""

from pathlib import Path
import numpy as np

np.set_printoptions(suppress=True, linewidth=160)


# -----------------------------------------------------------------------------
# Вспомогательные функции вывода
# -----------------------------------------------------------------------------
class Tee:
    """Одновременная печать в консоль и текстовый файл."""

    def __init__(self, filename):
        self.file = open(filename, "w", encoding="utf-8")

    def print(self, *args, **kwargs):
        print(*args, **kwargs)
        print(*args, **kwargs, file=self.file)

    def close(self):
        self.file.close()


def line(title=""):
    out.print("\n" + "=" * 92)
    if title:
        out.print(title)
        out.print("=" * 92)


def fmt(value, digits=6):
    """Форматирование числа с десятичной запятой."""
    if abs(value) < 0.5 * 10 ** (-digits):
        value = 0.0
    return f"{value:.{digits}f}".replace(".", ",")


def print_vector(name, vector, unit="", digits=6):
    values = "; ".join(fmt(v, digits) for v in vector)
    suffix = f" {unit}" if unit else ""
    out.print(f"{name} = ({values}){suffix}")


def print_matrix(name, matrix, digits=6):
    out.print(f"{name} =")
    for row in matrix:
        out.print("│ " + "  ".join(f"{fmt(v, digits):>13}" for v in row) + " │")


def print_table(headers, rows, widths=None):
    """Печать простой выровненной таблицы."""
    string_rows = [[str(cell) for cell in row] for row in rows]
    if widths is None:
        widths = [len(str(h)) for h in headers]
        for row in string_rows:
            widths = [max(w, len(cell)) for w, cell in zip(widths, row)]

    def render(row):
        return " | ".join(str(cell).rjust(width) for cell, width in zip(row, widths))

    out.print(render(headers))
    out.print("-+-".join("-" * width for width in widths))
    for row in string_rows:
        out.print(render(row))


def multiply_row_by_matrix(row_name, row, matrix, result_name):
    """Подробный вывод произведения вектора-строки на матрицу."""
    result = row @ matrix
    out.print(f"{result_name} = {row_name} · B")
    for j in range(matrix.shape[1]):
        terms = " + ".join(
            f"{fmt(row[i])}·{fmt(matrix[i, j])}" for i in range(matrix.shape[0])
        )
        out.print(f"{result_name}_{j + 1} = {terms} = {fmt(result[j])}")
    return result


# Файл результата создается рядом со скриптом.
result_file = Path(__file__).with_name("polnoe_reshenie_mob.txt")
out = Tee(result_file)

try:
    # -------------------------------------------------------------------------
    # 1. Исходные данные
    # -------------------------------------------------------------------------
    line("ПОЛНОЕ РЕШЕНИЕ ЗАДАЧИ 6 ПО ТРЕХОТРАСЛЕВОЙ МОДЕЛИ МОБ")

    A = np.array([
        [0.4, 0.1, 0.1],
        [0.3, 0.3, 0.4],
        [0.1, 0.1, 0.2]
    ], dtype=float)

    Y = np.array([90.0, 25.0, 100.0])        # млрд руб.
    change_percent = np.array([20.0, 10.0, -20.0])
    t = np.array([9.0, 5.0, 2.0])            # чел./млн руб.
    f = np.array([1.0, 4.0, 3.0])            # коэффициенты прямых затрат ОПФ
    E = np.eye(3)

    line("1. ИСХОДНЫЕ ДАННЫЕ")
    print_matrix("Матрица коэффициентов прямых материальных затрат A", A, 1)
    print_vector("Вектор конечного продукта Y", Y, "млрд руб.", 1)
    print_vector("Изменение конечного продукта", change_percent, "%", 1)
    print_vector("Прямая трудоемкость t", t, "чел./млн руб.", 1)
    print_vector("Коэффициенты прямых затрат ОПФ f", f, "", 1)

    out.print("\nПеревод процентных изменений конечного продукта в абсолютные:")
    delta_Y = Y * change_percent / 100.0
    for i in range(3):
        out.print(
            f"Δy_{i + 1} = y_{i + 1}·({fmt(change_percent[i], 1)} / 100) "
            f"= {fmt(Y[i], 1)}·({fmt(change_percent[i] / 100, 2)}) "
            f"= {fmt(delta_Y[i])} млрд руб."
        )
    Y_new = Y + delta_Y
    print_vector("ΔY", delta_Y, "млрд руб.")
    print_vector("Y' = Y + ΔY", Y_new, "млрд руб.")

    # -------------------------------------------------------------------------
    # 2. Матрица Леонтьева и обратная матрица
    # -------------------------------------------------------------------------
    line("2. МАТРИЦА ЛЕОНТЬЕВА И МАТРИЦА ПОЛНЫХ ЗАТРАТ")
    out.print("Основное уравнение МОБ:")
    out.print("X = AX + Y")
    out.print("(E − A)X = Y")
    out.print("X = (E − A)⁻¹Y")

    M = E - A
    print_matrix("Единичная матрица E", E, 0)
    print_matrix("Матрица Леонтьева E − A", M, 1)

    out.print("\nВычислим алгебраические дополнения D_ij.")
    cofactors = np.zeros_like(M)
    for i in range(3):
        for j in range(3):
            minor = np.delete(np.delete(M, i, axis=0), j, axis=1)
            minor_det = np.linalg.det(minor)
            cofactors[i, j] = ((-1) ** (i + j)) * minor_det
            sign = "+" if (i + j) % 2 == 0 else "−"
            out.print(
                f"D_{i + 1}{j + 1} = ({sign})·det"
                f"[[{fmt(minor[0, 0], 1)}; {fmt(minor[0, 1], 1)}], "
                f"[{fmt(minor[1, 0], 1)}; {fmt(minor[1, 1], 1)}]] "
                f"= {fmt(cofactors[i, j], 6)}"
            )

    print_matrix("Матрица алгебраических дополнений D", cofactors)
    adjugate = cofactors.T
    print_matrix("Присоединенная матрица adj(E − A) = Dᵀ", adjugate)

    det_M = np.linalg.det(M)
    # Разложение определителя по первой строке
    det_terms = M[0, :] * cofactors[0, :]
    out.print("\nОпределитель матрицы E − A (разложение по первой строке):")
    out.print(
        f"det(E − A) = {fmt(M[0,0],1)}·{fmt(cofactors[0,0])} "
        f"+ ({fmt(M[0,1],1)})·{fmt(cofactors[0,1])} "
        f"+ ({fmt(M[0,2],1)})·{fmt(cofactors[0,2])}"
    )
    out.print(
        f"det(E − A) = {fmt(det_terms[0])} + ({fmt(det_terms[1])}) "
        f"+ ({fmt(det_terms[2])}) = {fmt(det_M)}"
    )

    B = np.linalg.inv(M)
    out.print("\nB = (E − A)⁻¹ = adj(E − A) / det(E − A)")
    print_matrix("Матрица коэффициентов полных затрат B", B)

    identity_check = M @ B
    print_matrix("Проверка: (E − A)·B", identity_check)

    # -------------------------------------------------------------------------
    # 3. Исходный валовой выпуск
    # -------------------------------------------------------------------------
    line("3. ИСХОДНЫЙ ВАЛОВОЙ ВЫПУСК")
    out.print("X = BY")
    X = B @ Y
    for i in range(3):
        terms = [B[i, j] * Y[j] for j in range(3)]
        out.print(
            f"x_{i + 1} = "
            + " + ".join(f"{fmt(B[i,j])}·{fmt(Y[j],1)}" for j in range(3))
            + " = "
            + " + ".join(fmt(v) for v in terms)
            + f" = {fmt(X[i])} млрд руб."
        )
    print_vector("X", X, "млрд руб.")

    out.print("\nПроверка основного равенства X = AX + Y:")
    print_vector("AX + Y", A @ X + Y, "млрд руб.")

    # -------------------------------------------------------------------------
    # 4. Изменение и новый валовой выпуск
    # -------------------------------------------------------------------------
    line("4. ИЗМЕНЕНИЕ ВАЛОВОГО ВЫПУСКА")
    out.print("ΔX = BΔY")
    delta_X = B @ delta_Y
    for i in range(3):
        terms = [B[i, j] * delta_Y[j] for j in range(3)]
        out.print(
            f"Δx_{i + 1} = "
            + " + ".join(
                f"{fmt(B[i,j])}·({fmt(delta_Y[j])})" if delta_Y[j] < 0
                else f"{fmt(B[i,j])}·{fmt(delta_Y[j])}"
                for j in range(3)
            )
            + " = "
            + " + ".join(f"({fmt(v)})" if v < 0 else fmt(v) for v in terms)
            + f" = {fmt(delta_X[i])} млрд руб."
        )

    print_vector("ΔX", delta_X, "млрд руб.")
    X_new = X + delta_X
    print_vector("X' = X + ΔX", X_new, "млрд руб.")

    output_change_percent = delta_X / X * 100.0
    rows = []
    for i in range(3):
        rows.append([
            i + 1, fmt(X[i]), fmt(delta_X[i]), fmt(X_new[i]),
            fmt(output_change_percent[i], 4) + "%"
        ])
    print_table(
        ["Отрасль", "x", "Δx", "x'", "Изменение"], rows,
        [8, 14, 14, 14, 13]
    )

    out.print("\nПроверка нового выпуска: X' = B·Y'")
    print_vector("B·Y'", B @ Y_new, "млрд руб.")

    # -------------------------------------------------------------------------
    # 5. Межотраслевые потоки
    # -------------------------------------------------------------------------
    line("5. МЕЖОТРАСЛЕВЫЕ ПОТОКИ")
    out.print("Формулы: x_ij = a_ij·x_j;  Δx_ij = a_ij·Δx_j;  x'_ij = a_ij·x'_j.")

    flows = A * X[np.newaxis, :]
    delta_flows = A * delta_X[np.newaxis, :]
    flows_new = A * X_new[np.newaxis, :]

    out.print("\n5.1. Исходные межотраслевые потоки")
    for i in range(3):
        for j in range(3):
            out.print(
                f"x_{i + 1}{j + 1} = a_{i + 1}{j + 1}·x_{j + 1} "
                f"= {fmt(A[i,j],1)}·{fmt(X[j])} = {fmt(flows[i,j])} млрд руб."
            )
    print_matrix("Матрица исходных потоков (x_ij)", flows)

    out.print("\n5.2. Изменение межотраслевых потоков")
    for i in range(3):
        for j in range(3):
            out.print(
                f"Δx_{i + 1}{j + 1} = a_{i + 1}{j + 1}·Δx_{j + 1} "
                f"= {fmt(A[i,j],1)}·({fmt(delta_X[j])}) "
                f"= {fmt(delta_flows[i,j])} млрд руб."
            )
    print_matrix("Матрица изменений потоков (Δx_ij)", delta_flows)

    out.print("\n5.3. Новые межотраслевые потоки")
    for i in range(3):
        for j in range(3):
            out.print(
                f"x'_{i + 1}{j + 1} = a_{i + 1}{j + 1}·x'_{j + 1} "
                f"= {fmt(A[i,j],1)}·{fmt(X_new[j])} = {fmt(flows_new[i,j])} млрд руб."
            )
    print_matrix("Матрица новых потоков (x'_ij)", flows_new)

    # -------------------------------------------------------------------------
    # 6. Прямая потребность в трудовых ресурсах
    # -------------------------------------------------------------------------
    line("6. ИЗМЕНЕНИЕ ПОТРЕБНОСТИ В ТРУДОВЫХ РЕСУРСАХ")
    out.print("Формулы: L_j = t_j·x_j;  ΔL_j = t_j·Δx_j;  L'_j = t_j·x'_j.")
    out.print("При t в чел./млн руб. и x в млрд руб. результат получается в тыс. человек.")

    labor = t * X
    delta_labor = t * delta_X
    labor_new = t * X_new
    for j in range(3):
        out.print(f"\nОтрасль {j + 1}:")
        out.print(f"L_{j+1} = {fmt(t[j],1)}·{fmt(X[j])} = {fmt(labor[j])} тыс. чел.")
        out.print(f"ΔL_{j+1} = {fmt(t[j],1)}·({fmt(delta_X[j])}) = {fmt(delta_labor[j])} тыс. чел.")
        out.print(f"L'_{j+1} = {fmt(t[j],1)}·{fmt(X_new[j])} = {fmt(labor_new[j])} тыс. чел.")

    rows = [[i + 1, fmt(labor[i]), fmt(delta_labor[i]), fmt(labor_new[i])] for i in range(3)]
    rows.append(["Всего", fmt(labor.sum()), fmt(delta_labor.sum()), fmt(labor_new.sum())])
    print_table(["Отрасль", "До", "Изменение", "После"], rows, [8, 16, 16, 16])

    # -------------------------------------------------------------------------
    # 7. Прямая потребность в ОПФ
    # -------------------------------------------------------------------------
    line("7. ИЗМЕНЕНИЕ ПОТРЕБНОСТИ В ОСНОВНЫХ ПРОИЗВОДСТВЕННЫХ ФОНДАХ")
    out.print("Формулы: Φ_j = f_j·x_j;  ΔΦ_j = f_j·Δx_j;  Φ'_j = f_j·x'_j.")

    funds = f * X
    delta_funds = f * delta_X
    funds_new = f * X_new
    for j in range(3):
        out.print(f"\nОтрасль {j + 1}:")
        out.print(f"Φ_{j+1} = {fmt(f[j],1)}·{fmt(X[j])} = {fmt(funds[j])} млрд руб.")
        out.print(f"ΔΦ_{j+1} = {fmt(f[j],1)}·({fmt(delta_X[j])}) = {fmt(delta_funds[j])} млрд руб.")
        out.print(f"Φ'_{j+1} = {fmt(f[j],1)}·{fmt(X_new[j])} = {fmt(funds_new[j])} млрд руб.")

    rows = [[i + 1, fmt(funds[i]), fmt(delta_funds[i]), fmt(funds_new[i])] for i in range(3)]
    rows.append(["Всего", fmt(funds.sum()), fmt(delta_funds.sum()), fmt(funds_new.sum())])
    print_table(["Отрасль", "До", "Изменение", "После"], rows, [8, 16, 16, 16])

    # -------------------------------------------------------------------------
    # 8. Промежуточный, валовой, условно-чистый продукт и матзатраты
    # -------------------------------------------------------------------------
    line("8. ПРОМЕЖУТОЧНЫЙ И ВАЛОВОЙ ПРОДУКТ, МАТЕРИАЛЬНЫЕ ЗАТРАТЫ")
    out.print("Промежуточный продукт производящей отрасли: P_i = Σ_j x_ij (сумма строки).")
    out.print("Материальные затраты потребляющей отрасли: M_j = Σ_i x_ij (сумма столбца).")
    out.print("Условно-чистый продукт: z_j = x_j − M_j.")

    intermediate = flows.sum(axis=1)
    material = flows.sum(axis=0)
    net = X - material

    intermediate_new = flows_new.sum(axis=1)
    material_new = flows_new.sum(axis=0)
    net_new = X_new - material_new

    out.print("\n8.1. Показатели до изменения")
    for i in range(3):
        row_sum = " + ".join(fmt(v) for v in flows[i, :])
        col_sum = " + ".join(fmt(v) for v in flows[:, i])
        out.print(f"P_{i+1} = {row_sum} = {fmt(intermediate[i])} млрд руб.")
        out.print(f"M_{i+1} = {col_sum} = {fmt(material[i])} млрд руб.")
        out.print(f"z_{i+1} = {fmt(X[i])} − {fmt(material[i])} = {fmt(net[i])} млрд руб.\n")

    rows = []
    for i in range(3):
        rows.append([i + 1, fmt(intermediate[i]), fmt(X[i]), fmt(material[i]), fmt(net[i])])
    rows.append(["Всего", fmt(intermediate.sum()), fmt(X.sum()), fmt(material.sum()), fmt(net.sum())])
    print_table(
        ["Отрасль", "Промежут. продукт", "Валовой продукт", "Матзатраты", "Условно-чистый"],
        rows, [8, 20, 18, 16, 18]
    )

    out.print("\n8.2. Показатели после изменения")
    for i in range(3):
        row_sum = " + ".join(fmt(v) for v in flows_new[i, :])
        col_sum = " + ".join(fmt(v) for v in flows_new[:, i])
        out.print(f"P'_{i+1} = {row_sum} = {fmt(intermediate_new[i])} млрд руб.")
        out.print(f"M'_{i+1} = {col_sum} = {fmt(material_new[i])} млрд руб.")
        out.print(f"z'_{i+1} = {fmt(X_new[i])} − {fmt(material_new[i])} = {fmt(net_new[i])} млрд руб.\n")

    rows = []
    for i in range(3):
        rows.append([i + 1, fmt(intermediate_new[i]), fmt(X_new[i]), fmt(material_new[i]), fmt(net_new[i])])
    rows.append(["Всего", fmt(intermediate_new.sum()), fmt(X_new.sum()), fmt(material_new.sum()), fmt(net_new.sum())])
    print_table(
        ["Отрасль", "Промежут. продукт", "Валовой продукт", "Матзатраты", "Условно-чистый"],
        rows, [8, 20, 18, 16, 18]
    )

    # -------------------------------------------------------------------------
    # 9. Косвенные материальные затраты первого порядка
    # -------------------------------------------------------------------------
    line("9. КОЭФФИЦИЕНТЫ КОСВЕННЫХ МАТЕРИАЛЬНЫХ ЗАТРАТ 1-ГО ПОРЯДКА")
    out.print("Матрица первого порядка: A^(1) = A² = A·A.")
    A2 = A @ A
    for i in range(3):
        for j in range(3):
            terms = [A[i, k] * A[k, j] for k in range(3)]
            expression = " + ".join(f"{fmt(A[i,k],1)}·{fmt(A[k,j],1)}" for k in range(3))
            values = " + ".join(fmt(v, 2) for v in terms)
            out.print(f"a^(1)_{i+1}{j+1} = {expression} = {values} = {fmt(A2[i,j],2)}")
    print_matrix("A^(1) = A²", A2, 2)

    # -------------------------------------------------------------------------
    # 10. Полные материальные затраты
    # -------------------------------------------------------------------------
    line("10. МАТРИЦА ПОЛНЫХ МАТЕРИАЛЬНЫХ ЗАТРАТ")
    out.print("B = (E − A)⁻¹ включает единицу конечного продукта.")
    out.print("Поэтому матрица только материальных затрат C = B − E.")
    C = B - E
    print_matrix("B = (E − A)⁻¹", B)
    print_matrix("C = B − E", C)
    print_matrix("Проверка: A·B", A @ B)
    out.print("Проверка выполнена: C = B − E = A·B.")

    # -------------------------------------------------------------------------
    # 11. Совокупные затраты живого труда
    # -------------------------------------------------------------------------
    line("11. СОВОКУПНЫЕ ЗАТРАТЫ ЖИВОГО ТРУДА")
    out.print("Коэффициенты совокупной трудоемкости: T = t·(E − A)⁻¹ = t·B.")
    T = multiply_row_by_matrix("t", t, B, "T")
    print_vector("T", T, "чел./млн руб. конечного продукта")

    total_labor_by_final = T * Y
    delta_total_labor_by_final = T * delta_Y
    total_labor_by_final_new = T * Y_new

    out.print("\nСовокупные затраты труда, отнесенные к конечному продукту отраслей:")
    for j in range(3):
        out.print(
            f"Отрасль {j+1}: T_{j+1}·y_{j+1} = {fmt(T[j])}·{fmt(Y[j],1)} "
            f"= {fmt(total_labor_by_final[j])} тыс. чел."
        )
        out.print(
            f"Изменение: T_{j+1}·Δy_{j+1} = {fmt(T[j])}·({fmt(delta_Y[j])}) "
            f"= {fmt(delta_total_labor_by_final[j])} тыс. чел."
        )
        out.print(
            f"После изменения: T_{j+1}·y'_{j+1} = {fmt(T[j])}·{fmt(Y_new[j],1)} "
            f"= {fmt(total_labor_by_final_new[j])} тыс. чел.\n"
        )

    rows = [[i + 1, fmt(total_labor_by_final[i]), fmt(delta_total_labor_by_final[i]),
             fmt(total_labor_by_final_new[i])] for i in range(3)]
    rows.append(["Всего", fmt(total_labor_by_final.sum()), fmt(delta_total_labor_by_final.sum()),
                 fmt(total_labor_by_final_new.sum())])
    print_table(["Конечный продукт", "До", "Изменение", "После"], rows, [17, 16, 16, 16])

    out.print("\nКонтроль:")
    out.print(f"Σ(T_j·y_j) = {fmt(total_labor_by_final.sum())} тыс. чел.")
    out.print(f"Σ(t_j·x_j) = {fmt(labor.sum())} тыс. чел.")
    out.print(f"Разность = {fmt(total_labor_by_final.sum() - labor.sum())}")

    # -------------------------------------------------------------------------
    # 12. Совокупные затраты ОПФ
    # -------------------------------------------------------------------------
    line("12. СОВОКУПНЫЕ ЗАТРАТЫ ОСНОВНЫХ ПРОИЗВОДСТВЕННЫХ ФОНДОВ")
    out.print("Коэффициенты совокупной фондоемкости: F = f·(E − A)⁻¹ = f·B.")
    F = multiply_row_by_matrix("f", f, B, "F")
    print_vector("F", F)

    total_funds_by_final = F * Y
    delta_total_funds_by_final = F * delta_Y
    total_funds_by_final_new = F * Y_new

    out.print("\nСовокупные затраты ОПФ, отнесенные к конечному продукту отраслей:")
    for j in range(3):
        out.print(
            f"Отрасль {j+1}: F_{j+1}·y_{j+1} = {fmt(F[j])}·{fmt(Y[j],1)} "
            f"= {fmt(total_funds_by_final[j])} млрд руб."
        )
        out.print(
            f"Изменение: F_{j+1}·Δy_{j+1} = {fmt(F[j])}·({fmt(delta_Y[j])}) "
            f"= {fmt(delta_total_funds_by_final[j])} млрд руб."
        )
        out.print(
            f"После изменения: F_{j+1}·y'_{j+1} = {fmt(F[j])}·{fmt(Y_new[j],1)} "
            f"= {fmt(total_funds_by_final_new[j])} млрд руб.\n"
        )

    rows = [[i + 1, fmt(total_funds_by_final[i]), fmt(delta_total_funds_by_final[i]),
             fmt(total_funds_by_final_new[i])] for i in range(3)]
    rows.append(["Всего", fmt(total_funds_by_final.sum()), fmt(delta_total_funds_by_final.sum()),
                 fmt(total_funds_by_final_new.sum())])
    print_table(["Конечный продукт", "До", "Изменение", "После"], rows, [17, 16, 16, 16])

    out.print("\nКонтроль:")
    out.print(f"Σ(F_j·y_j) = {fmt(total_funds_by_final.sum())} млрд руб.")
    out.print(f"Σ(f_j·x_j) = {fmt(funds.sum())} млрд руб.")
    out.print(f"Разность = {fmt(total_funds_by_final.sum() - funds.sum())}")

    # -------------------------------------------------------------------------
    # 13. Новый межотраслевой баланс и контрольные равенства
    # -------------------------------------------------------------------------
    line("13. ИТОГОВЫЙ НОВЫЙ МЕЖОТРАСЛЕВОЙ БАЛАНС")
    rows = []
    for i in range(3):
        rows.append([
            i + 1,
            fmt(flows_new[i, 0]), fmt(flows_new[i, 1]), fmt(flows_new[i, 2]),
            fmt(Y_new[i]), fmt(X_new[i])
        ])
    rows.append([
        "УЧП", fmt(net_new[0]), fmt(net_new[1]), fmt(net_new[2]), "—", fmt(net_new.sum())
    ])
    rows.append([
        "Выпуск", fmt(X_new[0]), fmt(X_new[1]), fmt(X_new[2]),
        fmt(Y_new.sum()), fmt(X_new.sum())
    ])
    print_table(
        ["Производитель", "Потр. 1", "Потр. 2", "Потр. 3", "Конечный", "Выпуск"],
        rows, [15, 14, 14, 14, 14, 14]
    )

    out.print("\nКонтроль по строкам: Σ_j x'_ij + y'_i = x'_i")
    for i in range(3):
        left = flows_new[i, :].sum() + Y_new[i]
        out.print(
            f"Отрасль {i+1}: {fmt(flows_new[i,:].sum())} + {fmt(Y_new[i])} "
            f"= {fmt(left)}; x'_{i+1} = {fmt(X_new[i])}; "
            f"разность = {fmt(left-X_new[i])}"
        )

    out.print("\nКонтроль по столбцам: Σ_i x'_ij + z'_j = x'_j")
    for j in range(3):
        left = flows_new[:, j].sum() + net_new[j]
        out.print(
            f"Отрасль {j+1}: {fmt(flows_new[:,j].sum())} + {fmt(net_new[j])} "
            f"= {fmt(left)}; x'_{j+1} = {fmt(X_new[j])}; "
            f"разность = {fmt(left-X_new[j])}"
        )

    out.print("\nОбщий контроль баланса:")
    out.print(f"Сумма промежуточных потоков = {fmt(flows_new.sum())} млрд руб.")
    out.print(f"Сумма нового конечного продукта = {fmt(Y_new.sum())} млрд руб.")
    out.print(
        f"{fmt(flows_new.sum())} + {fmt(Y_new.sum())} "
        f"= {fmt(flows_new.sum() + Y_new.sum())} млрд руб."
    )
    out.print(f"Сумма нового валового выпуска = {fmt(X_new.sum())} млрд руб.")

    # -------------------------------------------------------------------------
    # 14. Краткие ответы
    # -------------------------------------------------------------------------
    line("14. КРАТКИЕ ОТВЕТЫ")
    print_vector("1) Изменение валового выпуска ΔX", delta_X, "млрд руб.")
    print_matrix("   Изменение межотраслевых потоков Δx_ij", delta_flows)
    print_vector("2) Изменение потребности в труде ΔL", delta_labor, "тыс. чел.")
    print_vector("3) Изменение потребности в ОПФ ΔΦ", delta_funds, "млрд руб.")
    print_vector("4) Новый промежуточный продукт P'", intermediate_new, "млрд руб.")
    print_vector("   Новый валовой продукт X'", X_new, "млрд руб.")
    print_vector("   Новый условно-чистый продукт z'", net_new, "млрд руб.")
    print_vector("   Новые материальные затраты M'", material_new, "млрд руб.")
    print_matrix("5) Косвенные материальные затраты 1-го порядка A²", A2, 6)
    print_matrix("   Полные материальные затраты C = B − E", C, 6)
    print_vector("6) Коэффициенты совокупной трудоемкости T", T, "чел./млн руб.")
    print_vector("7) Коэффициенты совокупной фондоемкости F", F)

    line("РЕШЕНИЕ ЗАВЕРШЕНО")
    out.print(f"Полный текст вывода сохранен в файл: {result_file}")

finally:
    out.close()
