"""Чистая логика расчётов. Никаких импортов GUI."""


def calc_mix(C1, V1, C2, V2):
    """Смешивание двух жидкостей.
    C1, C2 — крепость в процентах, V1, V2 — объём в л.
    Возвращает (крепость_%, объём_л).
    """
    total_volume = V1 + V2
    if total_volume == 0:
        raise ValueError("Общий объём не может быть нулевым.")
    final_strength = (V1 * C1 + V2 * C2) / total_volume
    return final_strength, total_volume


def calc_dilution(A, B, C):
    """Разбавление спирта/самогона водой.
    A — крепость исходного (%), B — желаемая крепость (%), C — объём (литры).
    Возвращает объём воды в литрах.
    """
    if B <= 0:
        raise ValueError("Желаемая крепость должна быть больше 0.")
    if B >= A:
        raise ValueError("Желаемая крепость должна быть меньше исходной.")
    water = (C * A / 100.0) / (B / 100.0) - C
    if water < 0:
        raise ValueError("Результат отрицательный — проверьте ввод.")
    return water

def calc_fractional_distillation(volume_raw, strength_raw, strength_target=60, head_pct=10, tail_pct=15):
    """
    Расчёт дробной перегонки.

    Параметры:
        volume_raw (float): объём спирта-сырца, л
        strength_raw (float): крепость спирта-сырца, %
        strength_target (float): желаемая крепость тела, %
        head_pct (float): доля голов, % от объёма абсолютного спирта
        tail_pct (float): доля хвостов, % от объёма абсолютного спирта

    Возвращает:
        dict: {
            'heads': float,  # объём голов, л
            'body': float,   # объём тела, л
            'tails': float,  # объём хвостов, л
            'total': float   # суммарный объём фракций, л
        }
    """
    # Базовые проверки
    if volume_raw <= 0:
        raise ValueError("Объём спирта-сырца должен быть больше нуля.")
    if not (0 < strength_raw < 100):
        raise ValueError("Крепость сырья должна быть в диапазоне (0, 100).")
    if not (0 < strength_target < 100):
        raise ValueError("Целевая крепость должна быть в диапазоне (0, 100).")
    if strength_target <= strength_raw:
        raise ValueError("Целевая крепость не может быть меньше или равна крепости сырья.")
    if not (0 <= head_pct <= 100):
        raise ValueError("Доля голов должна быть в диапазоне [0, 100].")
    if not (0 <= tail_pct <= 100):
        raise ValueError("Доля хвостов должна быть в диапазоне [0, 100].")

    # 1. Абсолютный спирт (АС) — это «чистый» этанол в сырце
    absolute_alcohol = volume_raw * (strength_raw / 100.0)

    # 2. Объём голов и хвостов — считаем как процент от исходного объёма
    heads = absolute_alcohol * (head_pct / 100.0)
    tails = absolute_alcohol * (tail_pct / 100.0)

    # 3. Объём тела — считаем через абсолютный спирт и целевую крепость
    # Формула: объём = АС / (целевая крепость в долях)
    body = absolute_alcohol / (strength_target / 100.0)

    return {
        'heads': round(heads, 2),
        'body': round(body, 2),
        'tails': round(tails, 2),
        'total': round(absolute_alcohol, 2)
    }
