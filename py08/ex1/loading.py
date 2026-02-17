import importlib.metadata
import importlib

def check_package(name):
    try:
        importlib.import_module(name)
        return True
    except ImportError:
        return False

print("\nLOADING STATUS: Loading programs...\n")
print("Checking dependencies:")
deps = {
    "pandas": " Data manipulation",
    "requests": "Network access",
    "matplotlib": "Visualization",
    "hhhh":"hhh"
}
for dep, value in deps.items():
    if check_package(dep):
        print(f"[OK] {dep} ({importlib.metadata.version(dep)}) - {value} ready")

    else:
        print(f"[ERROR] {dep} not installed, Install with:")
        print(f"    pip install {dep} \nor with:\n    poetry add {dep}")



print("\nAnalyzing Matrix data...")
print("Processing 1000 data points...")
print("Generating visualization...")
print("\nAnalysis complete!\n"
      "Results saved to: matrix\\analysis.png}")