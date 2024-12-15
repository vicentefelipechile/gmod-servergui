from os import system

print("Starting server...")
print("> python server/manage.py runserver")
try:
    system("python server/manage.py runserver")
except KeyboardInterrupt:
    print("Server stopped.")
    exit(0)