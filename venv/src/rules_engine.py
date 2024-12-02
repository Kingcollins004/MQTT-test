def calculate_winter_supplement(data):
    """
    Processes input data to determine eligibility and calculate supplement amounts.
    :param data: dict containing input JSON fields
    :return: dict containing output JSON fields
    """
    # Initialize response
    result = {
        "id": data["id"],
        "isEligible": False,
        "baseAmount": 0.0,
        "childrenAmount": 0.0,
        "supplementAmount": 0.0,
    }

    # Check eligibility
    if not data.get("familyUnitInPayForDecember", False):
        return result

    # Determine base amount
    family_type = data["familyComposition"]
    if family_type == "single":
        base_amount = 60.0
    elif family_type == "couple":
        base_amount = 120.0
    else:
        raise ValueError("Invalid familyComposition value")

    # Calculate additional amount for children
    num_children = data.get("numberOfChildren", 0)
    children_amount = 20.0 * num_children

    # Total supplement amount
    total_amount = base_amount + children_amount

    # Update result
    result.update({
        "isEligible": True,
        "baseAmount": base_amount,
        "childrenAmount": children_amount,
        "supplementAmount": total_amount,
    })
    return result
