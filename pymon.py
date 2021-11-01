import subprocess

wifi = input("Pls select an wifi adapter to enable monitor mode >> ")

print()

subprocess.call(f"ifconfig {wifi} down",shell=True)
subprocess.call(f"iwconfig {wifi} mode monitor",shell=True)
subprocess.call(f"ifconfig {wifi} up",shell=True)
subprocess.call(f"iwconfig",shell=True)
print()
print("Done monitor mode enabled check by iwconfig")
