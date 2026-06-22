import os

# Atrof-muhit o'zgaruvchisini o'qish
app_mode = os.getenv("APP_MODE", "development")
db_host = os.getenv("DB_HOST", "localhost")

print(f"Ilova {app_mode} rejimida ishlamoqda...")
print(f"Bog'lanish nuqtasi: {db_host}")
