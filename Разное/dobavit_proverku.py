# -*- coding: utf-8 -*-
"""Автоматически добавляет подробную проверку в существующий reshenie_mob.py.

Запуск на macOS:
    python "/путь/к/dobavit_proverku.py" "/путь/к/reshenie_mob.py"

Перед изменением создаётся резервная копия reshenie_mob.backup.py.
Патчер рассчитан на исходный подробный NumPy-скрипт из этой задачи.
"""

from pathlib import Path
import shutil
import sys

START_MARKER = "# >>> НАЧАЛО ДОБАВЛЕННОЙ ПОЛНОЙ ПРОВЕРКИ >>>"
END_MARKER = "# <<< КОНЕЦ ДОБАВЛЕННОЙ ПОЛНОЙ ПРОВЕРКИ <<<"
INSERT_BEFORE = '    line("14. КРАТКИЕ ОТВЕТЫ")'

CHECK_BLOCK = r'''    # >>> НАЧАЛО ДОБАВЛЕННОЙ ПОЛНОЙ ПРОВЕРКИ >>>
    # -------------------------------------------------------------------------
    # 13.1. Полная автоматическая проверка решения
    # -------------------------------------------------------------------------
    line("13.1. ПОЛНАЯ МАТЕМАТИЧЕСКАЯ ПРОВЕРКА РЕШЕНИЯ")
    out.print("Проверяем обратную матрицу, уравнения Леонтьева, потоки, ресурсы и баланс.")
    out.print("Допустимая абсолютная вычислительная погрешность: 10⁻⁹.\n")

    tolerance = 1e-9
    checks_total = 0
    checks_passed = 0

    def matrix_check(title, actual, expected):
        actual = np.asarray(actual, dtype=float)
        expected = np.asarray(expected, dtype=float)
        error = float(np.max(np.abs(actual - expected)))
        ok = bool(np.allclose(actual, expected, atol=tolerance, rtol=0.0))
        result = "ПРОЙДЕНА" if ok else "НЕ ПРОЙДЕНА"
        out.print(f"[ {result} ] {title}")
        out.print(f"  Максимальная абсолютная погрешность: {error:.3e}")
        if not ok:
            print_matrix("  Получено", actual)
            print_matrix("  Ожидалось", expected)
        return ok

    def vector_check(title, actual, expected):
        actual = np.asarray(actual, dtype=float)
        expected = np.asarray(expected, dtype=float)
        error = float(np.max(np.abs(actual - expected)))
        ok = bool(np.allclose(actual, expected, atol=tolerance, rtol=0.0))
        result = "ПРОЙДЕНА" if ok else "НЕ ПРОЙДЕНА"
        out.print(f"[ {result} ] {title}")
        out.print(f"  Максимальная абсолютная погрешность: {error:.3e}")
        if not ok:
            print_vector("  Получено", actual)
            print_vector("  Ожидалось", expected)
        return ok

    def scalar_check(title, actual, expected):
        error = abs(float(actual) - float(expected))
        ok = error <= tolerance
        result = "ПРОЙДЕНА" if ok else "НЕ ПРОЙДЕНА"
        out.print(f"[ {result} ] {title}")
        out.print(f"  Получено: {fmt(actual)}; ожидалось: {fmt(expected)}; погрешность: {error:.3e}")
        return ok

    def register(ok):
        nonlocal_value = int(bool(ok))
        return nonlocal_value

    def detailed_product(left_name, left, right_name, right, result_name):
        result = left @ right
        out.print(f"\nПодробное вычисление {left_name}·{right_name}:")
        for i in range(3):
            for j in range(3):
                products = [left[i, k] * right[k, j] for k in range(3)]
                formula = " + ".join(
                    f"({fmt(left[i, k])})·({fmt(right[k, j])})" for k in range(3)
                )
                values = " + ".join(
                    f"({fmt(value)})" if value < 0 else fmt(value) for value in products
                )
                out.print(
                    f"{result_name}_{i + 1}{j + 1} = {formula} = {values} "
                    f"= {fmt(result[i, j])}"
                )
        print_matrix(result_name, result)
        return result

    def add_result(ok):
        # Возвращает 1 для пройденной проверки и 0 для непройденной.
        return 1 if ok else 0

    # ---------------------------------------------------------------------
    # 1. Главная проверка преподавателя: произведение на обратную матрицу
    # ---------------------------------------------------------------------
    out.print("1) ПРОВЕРКА ОБРАТНОЙ МАТРИЦЫ")
    out.print("По определению обратной матрицы:")
    out.print("(E − A)·(E − A)⁻¹ = E и (E − A)⁻¹·(E − A) = E.")
    out.print("В решении M = E − A, B = (E − A)⁻¹, следовательно M·B = E и B·M = E.")

    MB = detailed_product("(E − A)", M, "B", B, "(E − A)·B")
    BM = detailed_product("B", B, "(E − A)", M, "B·(E − A)")

    ok = matrix_check("(E − A)·B = E", MB, E)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = matrix_check("B·(E − A) = E", BM, E)
    checks_total += 1
    checks_passed += add_result(ok)

    # ---------------------------------------------------------------------
    # 2. Восстановление исходной матрицы A
    # ---------------------------------------------------------------------
    out.print("\n2) ВОССТАНОВЛЕНИЕ ИСХОДНОЙ МАТРИЦЫ ПРЯМЫХ ЗАТРАТ")
    out.print("Так как M = E − A, то исходная матрица должна получиться из A = E − M.")
    A_restored = E - M
    print_matrix("E − (E − A)", A_restored)
    print_matrix("Исходная A", A)
    ok = matrix_check("E − (E − A) = A", A_restored, A)
    checks_total += 1
    checks_passed += add_result(ok)

    # ---------------------------------------------------------------------
    # 3. Формула обратной матрицы
    # ---------------------------------------------------------------------
    out.print("\n3) ПРОВЕРКА ФОРМУЛЫ ОБРАТНОЙ МАТРИЦЫ")
    out.print("Проверяем B = adj(E − A) / det(E − A).")
    B_formula = adjugate / det_M
    print_matrix("B, рассчитанная через присоединённую матрицу", B_formula)
    ok = matrix_check("B = adj(E − A) / det(E − A)", B, B_formula)
    checks_total += 1
    checks_passed += add_result(ok)

    # ---------------------------------------------------------------------
    # 4. Исходная модель Леонтьева
    # ---------------------------------------------------------------------
    out.print("\n4) ПРОВЕРКА ИСХОДНОГО ВАЛОВОГО ВЫПУСКА")
    X_from_BY = B @ Y
    X_from_balance = A @ X + Y
    print_vector("B·Y", X_from_BY, "млрд руб.")
    print_vector("A·X + Y", X_from_balance, "млрд руб.")
    print_vector("Рассчитанный X", X, "млрд руб.")
    ok = vector_check("X = B·Y", X, X_from_BY)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("X = A·X + Y", X, X_from_balance)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("(E − A)·X = Y", M @ X, Y)
    checks_total += 1
    checks_passed += add_result(ok)

    # ---------------------------------------------------------------------
    # 5. Изменение и новый выпуск
    # ---------------------------------------------------------------------
    out.print("\n5) ПРОВЕРКА ИЗМЕНЕНИЯ И НОВОГО ВЫПУСКА")
    ok = vector_check("ΔX = B·ΔY", delta_X, B @ delta_Y)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("X' = X + ΔX", X_new, X + delta_X)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("X' = B·Y'", X_new, B @ Y_new)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("X' = A·X' + Y'", X_new, A @ X_new + Y_new)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("(E − A)·X' = Y'", M @ X_new, Y_new)
    checks_total += 1
    checks_passed += add_result(ok)

    # ---------------------------------------------------------------------
    # 6. Межотраслевые потоки
    # ---------------------------------------------------------------------
    out.print("\n6) ПРОВЕРКА МЕЖОТРАСЛЕВЫХ ПОТОКОВ")
    flows_formula = A * X[np.newaxis, :]
    delta_flows_formula = A * delta_X[np.newaxis, :]
    flows_new_formula = A * X_new[np.newaxis, :]
    ok = matrix_check("x_ij = a_ij·x_j", flows, flows_formula)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = matrix_check("Δx_ij = a_ij·Δx_j", delta_flows, delta_flows_formula)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = matrix_check("x'_ij = a_ij·x'_j", flows_new, flows_new_formula)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = matrix_check("x'_ij = x_ij + Δx_ij", flows_new, flows + delta_flows)
    checks_total += 1
    checks_passed += add_result(ok)

    # ---------------------------------------------------------------------
    # 7. Трудовые ресурсы и основные фонды
    # ---------------------------------------------------------------------
    out.print("\n7) ПРОВЕРКА ПРЯМОЙ ПОТРЕБНОСТИ В ТРУДЕ И ОПФ")
    ok = vector_check("L = t·X поэлементно", labor, t * X)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("ΔL = t·ΔX поэлементно", delta_labor, t * delta_X)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("L' = L + ΔL", labor_new, labor + delta_labor)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("Φ = f·X поэлементно", funds, f * X)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("ΔΦ = f·ΔX поэлементно", delta_funds, f * delta_X)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("Φ' = Φ + ΔΦ", funds_new, funds + delta_funds)
    checks_total += 1
    checks_passed += add_result(ok)

    # ---------------------------------------------------------------------
    # 8. Косвенные и полные материальные затраты
    # ---------------------------------------------------------------------
    out.print("\n8) ПРОВЕРКА МАТРИЦ МАТЕРИАЛЬНЫХ ЗАТРАТ")
    ok = matrix_check("A^(1) = A² = A·A", A2, A @ A)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = matrix_check("C = B − E", C, B - E)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = matrix_check("C = A·B", C, A @ B)
    checks_total += 1
    checks_passed += add_result(ok)

    # ---------------------------------------------------------------------
    # 9. Совокупная трудоёмкость и фондоёмкость
    # ---------------------------------------------------------------------
    out.print("\n9) ПРОВЕРКА СОВОКУПНЫХ ЗАТРАТ")
    ok = vector_check("T = t·B", T, t @ B)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("F = f·B", F, f @ B)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = scalar_check("Σ(T_j·y_j) = Σ(t_j·x_j)", np.sum(T * Y), np.sum(t * X))
    checks_total += 1
    checks_passed += add_result(ok)
    ok = scalar_check("Σ(F_j·y_j) = Σ(f_j·x_j)", np.sum(F * Y), np.sum(f * X))
    checks_total += 1
    checks_passed += add_result(ok)
    ok = scalar_check("После изменения: Σ(T_j·y'_j) = Σ(t_j·x'_j)",
                      np.sum(T * Y_new), np.sum(t * X_new))
    checks_total += 1
    checks_passed += add_result(ok)
    ok = scalar_check("После изменения: Σ(F_j·y'_j) = Σ(f_j·x'_j)",
                      np.sum(F * Y_new), np.sum(f * X_new))
    checks_total += 1
    checks_passed += add_result(ok)

    # ---------------------------------------------------------------------
    # 10. Полный контроль нового межотраслевого баланса
    # ---------------------------------------------------------------------
    out.print("\n10) ПОЛНЫЙ КОНТРОЛЬ НОВОГО БАЛАНСА")
    row_balance = flows_new.sum(axis=1) + Y_new
    column_balance = flows_new.sum(axis=0) + net_new
    ok = vector_check("По строкам: Σ_j x'_ij + y'_i = x'_i", row_balance, X_new)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = vector_check("По столбцам: Σ_i x'_ij + z'_j = x'_j", column_balance, X_new)
    checks_total += 1
    checks_passed += add_result(ok)
    ok = scalar_check("Общий баланс: Σx'_ij + Σy'_i = Σx'_i",
                      flows_new.sum() + Y_new.sum(), X_new.sum())
    checks_total += 1
    checks_passed += add_result(ok)
    ok = scalar_check("Σz'_j = Σy'_j", net_new.sum(), Y_new.sum())
    checks_total += 1
    checks_passed += add_result(ok)
    ok = scalar_check("Σ промежуточного продукта = Σ материальных затрат",
                      intermediate_new.sum(), material_new.sum())
    checks_total += 1
    checks_passed += add_result(ok)

    # Итог проверки.
    out.print("\n" + "-" * 92)
    out.print(f"ИТОГ ПРОВЕРКИ: успешно пройдено {checks_passed} из {checks_total} проверок.")
    if checks_passed == checks_total:
        out.print("ВСЕ РАСЧЁТЫ КОРРЕКТНЫ. МАТЕМАТИЧЕСКИЕ И БАЛАНСОВЫЕ РАВЕНСТВА ВЫПОЛНЯЮТСЯ.")
    else:
        out.print(f"ВНИМАНИЕ: не пройдено {checks_total - checks_passed} проверок.")
        raise AssertionError("Некоторые математические проверки не пройдены.")
    out.print("-" * 92)

    # <<< КОНЕЦ ДОБАВЛЕННОЙ ПОЛНОЙ ПРОВЕРКИ <<<

'''


def main():
    if len(sys.argv) != 2:
        print("Укажите путь к работающему файлу reshenie_mob.py")
        print('Пример: python dobavit_proverku.py "/Users/artemzaharov/PycharmProjects/ЕГЭ/Разное/reshenie_mob.py"')
        raise SystemExit(2)

    source = Path(sys.argv[1]).expanduser().resolve()
    if not source.exists():
        print(f"Ошибка: файл не найден: {source}")
        raise SystemExit(1)

    text = source.read_text(encoding="utf-8")
    if START_MARKER in text:
        print("Проверка уже добавлена. Повторное изменение не требуется.")
        return
    if INSERT_BEFORE not in text:
        print("Не найдено место вставки перед разделом 14.")
        print("Убедитесь, что выбран именно исходный подробный скрипт reshenie_mob.py.")
        raise SystemExit(1)

    backup = source.with_name(source.stem + ".backup.py")
    shutil.copy2(source, backup)
    patched = text.replace(INSERT_BEFORE, CHECK_BLOCK + INSERT_BEFORE, 1)
    source.write_text(patched, encoding="utf-8")

    print("Готово: подробная проверка добавлена.")
    print(f"Изменённый файл: {source}")
    print(f"Резервная копия: {backup}")
    print("Теперь запустите reshenie_mob.py обычным способом.")


if __name__ == "__main__":
    main()
