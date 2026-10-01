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


def pr_data3():
    pr_data = {
        "code_diffs": """
diff --git a/profile.py b/profile.py
index 1234567..89abcde 100644
--- a/profile.py
+++ b/profile.py
@@ -10,6 +10,10 @@
 def update_profile(user, data):
+    user.name = data["name"]
+    user.email = data["email"]
+    user.updated_at = datetime.now()
+    save_user(user)
""",
        "commit_history": [
            "Update user profile fields",
            "Add profile timestamp",
            "Save profile changes"
        ],
        "contributors": [
            "alice"
        ],
        "is_merge_conflict": False
    }

    return pr_data


def pr_data4():

    pr_data = {
        "code_diffs": """
diff --git a/settings.py b/settings.py
index 1234567..89abcde 100644
--- a/settings.py
+++ b/settings.py
@@ -20,10 +20,6 @@
 def update_settings(user, data):
-    if data["theme"] is None:
-        data["theme"] = "default"
-    if data["language"] is None:
-        data["language"] = "en"
+    user.settings.update(data)
+    save_settings(user)
""",
        "commit_history": [
            "Simplify settings update",
            "Remove default settings handling",
            "Update settings persistence"
        ],
        "contributors": [
            "bob"
        ],
        "is_merge_conflict": True
    }

    return pr_data