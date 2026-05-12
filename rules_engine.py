import pandas as pd


def run_rule(df, rule, col_map):
    """
    Generic rule executor (SAFE VERSION)
    """

    rule_name = rule.get("rule_name")

    required_fields = rule.get("required_fields", [])
    group_by_field = rule.get("group_by", [])[0] if rule.get("group_by") else None
    compare_field = rule.get("compare", [])[0] if rule.get("compare") else None

    # -----------------------------
    # STEP 1: Validate columns exist
    # -----------------------------
    missing_fields = []

    for field in required_fields:
        if field not in col_map:
            missing_fields.append(field)

    if group_by_field and group_by_field not in col_map:
        missing_fields.append(group_by_field)

    if compare_field and compare_field not in col_map:
        missing_fields.append(compare_field)

    # If anything missing → skip rule safely
    if missing_fields:
        print(f"[SKIP RULE] {rule_name} missing columns: {missing_fields}")
        return None

    # -----------------------------
    # STEP 2: Map actual columns
    # -----------------------------
    group_col = col_map[group_by_field]
    compare_col = col_map[compare_field]

    # Only required fields subset
    used_cols = []
    for f in required_fields:
        if f in col_map:
            used_cols.append(col_map[f])

    working_df = df[used_cols].copy()

    # -----------------------------
    # STEP 3: Rule execution logic
    # -----------------------------
    result_rows = []

    grouped = working_df.groupby(group_col)

    for key, group in grouped:

        if group[compare_col].nunique() > 1:
            group = group.copy()
            group["Rule"] = rule_name
            group["Group_Key"] = key
            result_rows.append(group)

    # -----------------------------
    # STEP 4: Return result
    # -----------------------------
    if result_rows:
        return pd.concat(result_rows, ignore_index=True)

    return None