def pr_data1():
    pr_data = {
        "code_diffs": """
    diff --git a/login.py b/login.py
    index 1234567..89abcde 100644
    --- a/login.py
    +++ b/login.py
    @@ -12,6 +12,10 @@ def login(username, password):
         user = find_user(username)
         if user is None:
             return False
    +    if not verify_password(password, user.password_hash):
    +        return False
    +    user.last_login = datetime.now()
    +    save_user(user)
         return create_session(user)
    """,
        "commit_history": [
            "Add password verification",
            "Update login session handling",
            "Fix invalid password response"
        ],
        "contributors": [
            "alice",
            "bob"
        ],
        "is_merge_conflict": False
    }
    return pr_data


def pr_data2():
    pr_data = {
        "code_diffs": """
diff --git a/payment.py b/payment.py
index 4567890..abcdef1 100644
--- a/payment.py
+++ b/payment.py
@@ -20,8 +20,14 @@ def process_payment(order):
     if order.total <= 0:
         return False

+    payment_method = get_payment_method(order.user_id)
+    if payment_method is None:
+        return False
+
+    transaction = create_transaction(
+        order.id,
+        payment_method
+    )
     return charge_card(order.total)
""",
        "commit_history": [
            "Add payment method lookup",
            "Create transaction before charging card",
            "Handle missing payment method"
        ],
        "contributors": [
            "charlie",
            "david"
        ],
        "is_merge_conflict": True
    }

    return pr_data


pr_all = [pr_data1(), pr_data2()]


def dummy_predicter(pr_data):
    return 0.1


output = dummy_predicter(pr_data1())

