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
    ]
}

def dummy_predicter(pr_data):
    return 0.1

output = dummy_predicter(pr_data)

print(output)