# Day 31 - Tip Calculator (2026-11-06)
# Restaurant er bill er upor tip hisab kore, ar bondhuder majhe
# bill bhag kore dewar sohoj tool. Khaoa-daoar por ke koto dibe,
# eta diye ek minute e ber kora jay - sobar jonno kaje lage.
# Kono external library lage na, shudhu plain Python.

def calculate_tip(bill_amount, tip_percent):
    """Bill amount ar tip percent dile tip er taka ar mot bill ber kore."""
    if bill_amount < 0:
        raise ValueError("Bill er taka 0 ba tar beshi hote hobe.")
    if tip_percent < 0:
        raise ValueError("Tip percent 0 ba tar beshi hote hobe.")
    tip_amount = bill_amount * tip_percent / 100
    total_amount = bill_amount + tip_amount
    return round(tip_amount, 2), round(total_amount, 2)


def split_bill(bill_amount, tip_percent, people):
    """Bill + tip sobai mile soman bhag kore protteke koto dibe ber kore."""
    if people <= 0:
        raise ValueError("Manusher sonkha 1 ba tar beshi hote hobe.")
    tip_amount, total_amount = calculate_tip(bill_amount, tip_percent)
    per_person = total_amount / people
    return {
        "tip": tip_amount,
        "total": total_amount,
        "per_person": round(per_person, 2),
    }


def suggest_tip(bill_amount, service_rating):
    """Service kemon chilo (1-5) tar upor base kore tip percent suggest kore."""
    suggestions = {1: 5, 2: 10, 3: 15, 4: 18, 5: 20}
    if service_rating not in suggestions:
        raise ValueError("Service rating 1 theke 5 er moddhe hote hobe.")
    tip_percent = suggestions[service_rating]
    tip_amount, total_amount = calculate_tip(bill_amount, tip_percent)
    return tip_percent, tip_amount, total_amount


if __name__ == "__main__":
    # Example 1: 1200 takar bill e 10% tip
    tip, total = calculate_tip(1200, 10)
    print(f"Bill: 1200 taka, Tip (10%): {tip} taka, Mot: {total} taka")

    # Example 2: 4 jon bondhu mile 2000 takar bill, 15% tip
    result = split_bill(2000, 15, 4)
    print(f"4 joner bill: Tip {result['tip']} taka, Mot {result['total']} taka, "
          f"Protteke dibe {result['per_person']} taka")

    # Example 3: Service khub bhalo (5/5) chilo, 800 takar bill e koto tip?
    percent, tip, total = suggest_tip(800, 5)
    print(f"Service 5/5: Tip {percent}% = {tip} taka, Mot: {total} taka")
