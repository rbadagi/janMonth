#kkk
#Basic Level
#1. os.getcwd / os.chdir - Working directory
import os

print(os.getcwd())          # Current working directory
os.chdir("..")               # Move up one level
print(os.getcwd())          # Verify change


#2. os.path.join - Platform-safe paths
import os

path = os.path.join("users", "data", "file.txt")
print(path)  # users\data\file.txt (Windows) or users/data/file.txt (Linux)

#3. os.listdir - List directory contents
import os

for item in os.listdir("."):
    tag = "[DIR]" if os.path.isdir(item) else "[FILE]"
    print(f"{tag} {item}")


#4. os.makedirs - Create nested directories
import os

os.makedirs("project/src/utils", exist_ok=True)  # No error if exists
print(os.path.exists("project/src/utils"))        # True


#5. sys.argv - Command line arguments
import sys

# Run: python script.py hello world
print(sys.argv)       # ['script.py', 'hello', 'world']
print(sys.argv[0])    # script.py (script name)
if len(sys.argv) > 1:
    print(f"First arg: {sys.argv[1]}")



#6. sys.platform / sys.version
import sys

print(sys.platform)       # 'win32', 'linux', 'darwin'
print(sys.version)        # '3.11.5 (main, ...)'
print(sys.version_info)   # sys.version_info(major=3, minor=11, micro=5...)


#Intermediate Level
#7. os.path utilities
import os

path = "/home/user/documents/report.pdf"

print(os.path.basename(path))    # report.pdf
print(os.path.dirname(path))     # /home/user/documents
print(os.path.splitext(path))    # ('/home/user/documents/report', '.pdf')
print(os.path.abspath("."))      # Full absolute path
print(os.path.expanduser("~"))   # Home directory
print(os.path.getsize(__file__)) # File size in bytes



#8. os.walk - Recursive directory traversal
import os

for root, dirs, files in os.walk(".", topdown=True):
    dirs[:] = [d for d in dirs if not d.startswith(".")]  # Skip hidden dirs
    level = root.replace(".", "").count(os.sep)
    indent = " " * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    for f in files:
        print(f"{indent}  {f}")


#9. os.environ - Environment variables
import os

# Read
home = os.environ.get("HOME") or os.environ.get("USERPROFILE")
path = os.environ.get("PATH", "not set")
print(f"Home: {home}")

# Set (for current process only)
os.environ["MY_APP_MODE"] = "debug"
print(os.environ["MY_APP_MODE"])  # debug



#10. os.rename / os.remove / os.rmdir
import os

# Create, rename, delete
with open("temp.txt", "w") as f:
    f.write("hello")

os.rename("temp.txt", "renamed.txt")
print(os.path.exists("renamed.txt"))  # True

os.remove("renamed.txt")
print(os.path.exists("renamed.txt"))  # False

os.makedirs("empty_dir", exist_ok=True)
os.rmdir("empty_dir")  # Only works on empty directories



#11. sys.path - Module search paths
import sys

# View module search paths
for p in sys.path:
    print(p)

# Add custom path for imports
sys.path.insert(0, "/my/custom/modules")

# Check if a module is already loaded
print("os" in sys.modules)  # True



#12. sys.stdin / stdout / stderr
import sys

# Write to stderr (won't be captured by pipe)
sys.stderr.write("Warning: something happened\n")

# Redirect stdout
original_stdout = sys.stdout
with open("output.log", "w") as f:
    sys.stdout = f
    print("This goes to file")
sys.stdout = original_stdout
print("This goes to console")



#13. sys.getsizeof - Memory usage
import sys

print(sys.getsizeof(""))          # 49 bytes (empty string)
print(sys.getsizeof("hello"))     # 54 bytes
print(sys.getsizeof([]))          # 56 bytes (empty list)
print(sys.getsizeof([1, 2, 3]))   # 88 bytes
print(sys.getsizeof({}))          # 64 bytes (empty dict)
print(sys.getsizeof(0))           # 28 bytes


#Advanced Level
#14. os.stat - Detailed file metadata
import os
import time

stat = os.stat(__file__)
print(f"Size: {stat.st_size} bytes")
print(f"Modified: {time.ctime(stat.st_mtime)}")
print(f"Created: {time.ctime(stat.st_ctime)}")
print(f"Permissions: {oct(stat.st_mode)}")
print(f"Inode: {stat.st_ino}")



#15. os.scandir - Efficient directory listing
import os

# Faster than os.listdir + os.path.isfile
with os.scandir(".") as entries:
    for entry in entries:
        info = entry.stat()
        kind = "DIR" if entry.is_dir() else "FILE"
        print(f"[{kind}] {entry.name:30s} {info.st_size:>10} bytes")


#16. os.pipe / os.fork - Inter-process communication (Unix)
import os
import sys

if sys.platform != "win32":
    r, w = os.pipe()
    pid = os.fork()

    if pid == 0:  # Child
        os.close(r)
        w_file = os.fdopen(w, "w")
        w_file.write("Hello from child!")
        w_file.close()
        os._exit(0)
    else:  # Parent
        os.close(w)
        r_file = os.fdopen(r, "r")
        message = r_file.read()
        print(f"Parent received: {message}")
        r_file.close()
        os.waitpid(pid, 0)


#17. sys.settrace - Execution tracer
import sys

def tracer(frame, event, arg):
    if event == "call":
        print(f"CALL: {frame.f_code.co_name} in {frame.f_code.co_filename}:{frame.f_lineno}")
    elif event == "return":
        print(f"RETURN: {frame.f_code.co_name} -> {arg}")
    return tracer

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

sys.settrace(tracer)
result = add(2, multiply(3, 4))
sys.settrace(None)
print(f"Result: {result}")


#18. sys.exc_info - Exception introspection
import sys
import traceback

def risky_operation():
    return 1 / 0

try:
    risky_operation()
except:
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(f"Type: {exc_type.__name__}")
    print(f"Value: {exc_value}")
    print(f"Line: {exc_tb.tb_lineno}")
    print("Full traceback:")
    traceback.print_tb(exc_tb)



#19. sys.setrecursionlimit / getrecursionlimit
import sys

print(f"Default limit: {sys.getrecursionlimit()}")  # Usually 1000

sys.setrecursionlimit(5000)

def deep_recursion(n):
    if n == 0:
        return 0
    return 1 + deep_recursion(n - 1)

print(deep_recursion(3000))  # Works with increased limit




#ExpertLevel
#20. File watcher using os.stat polling
import os
import time

def watch_file(filepath, interval=1):
    last_mtime = os.stat(filepath).st_mtime
    print(f"Watching {filepath}...")
    try:
        while True:
            time.sleep(interval)
            current_mtime = os.stat(filepath).st_mtime
            if current_mtime != last_mtime:
                print(f"[{time.strftime('%H:%M:%S')}] File changed!")
                last_mtime = current_mtime
    except KeyboardInterrupt:
        print("Stopped watching.")

# watch_file("config.yaml")



#21. Custom import hook using sys.meta_path
import sys
import importlib.abc
import importlib.machinery

class LoggingFinder(importlib.abc.MetaPathFinder):
    def find_module(self, fullname, path=None):
        print(f"[IMPORT] Attempting to import: {fullname}")
        return None  # Let normal import proceed

# Install the hook
sys.meta_path.insert(0, LoggingFinder())

import json       # [IMPORT] Attempting to import: json
import csv        # [IMPORT] Attempting to import: csv

# Remove hook
sys.meta_path.remove(sys.meta_path[0])



#22. Disk usage analyzer with os.walk
import os

def disk_usage(path, top_n=10):
    sizes = {}
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            try:
                sizes[fp] = os.path.getsize(fp)
            except OSError:
                continue

    total = sum(sizes.values())
    sorted_files = sorted(sizes.items(), key=lambda x: x[1], reverse=True)

    print(f"Total: {total / (1024**2):.2f} MB")
    print(f"\nTop {top_n} largest files:")
    for filepath, size in sorted_files[:top_n]:
        pct = (size / total * 100) if total else 0
        print(f"  {size / 1024:.1f} KB ({pct:.1f}%) - {filepath}")

# disk_usage(".")



#23. Cross-platform process launcher
import os
import sys
import subprocess

def run_command(cmd, timeout=30):
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"

    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
            cwd=os.getcwd()
        )
        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode,
            "success": result.returncode == 0
        }
    except subprocess.TimeoutExpired:
        return {"error": "timeout", "success": False}

# Platform-aware command
cmd = "dir" if sys.platform == "win32" else "ls -la"
print(run_command(cmd))


#24. Temporary file management with cleanup
import os
import sys
import tempfile
import atexit

class TempManager:
    def __init__(self, prefix="app_"):
        self.prefix = prefix
        self.temp_dir = tempfile.mkdtemp(prefix=prefix)
        self._files = []
        atexit.register(self.cleanup)

    def create(self, name, content=""):
        path = os.path.join(self.temp_dir, name)
        with open(path, "w") as f:
            f.write(content)
        self._files.append(path)
        return path

    def cleanup(self):
        for f in self._files:
            try:
                os.remove(f)
            except OSError:
                pass
        try:
            os.rmdir(self.temp_dir)
            print(f"Cleaned up {self.temp_dir}")
        except OSError:
            pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.cleanup()

# Usage
with TempManager() as tmp:
    f1 = tmp.create("data.txt", "hello world")
    f2 = tmp.create("config.json", '{"key": "value"}')
    print(f"Temp dir: {tmp.temp_dir}")
    print(os.listdir(tmp.temp_dir))
# Auto-cleanup on exit


#25. sys.audit hooks - Security monitoring (Python 3.8+)
import sys

def audit_hook(event, args):
    watched = {"open", "subprocess.Popen", "socket.connect", "exec", "compile"}
    if event in watched:
        print(f"[AUDIT] {event}: {args}")

sys.addaudithook(audit_hook)

# These will trigger audit events
open("test_audit.txt", "w").close()  # [AUDIT] open: ('test_audit.txt', 'w', ...)
import os
os.remove("test_audit.txt")


#26. Module dependency graph builder
import sys
import os

def build_dependency_graph(root_dir):
    graph = {}
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if not fname.endswith(".py"):
                continue
            filepath = os.path.join(dirpath, fname)
            module = filepath.replace(root_dir, "").replace(os.sep, ".").strip(".").replace(".py", "")
            imports = set()
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("import "):
                            imports.add(line.split()[1].split(".")[0])
                        elif line.startswith("from "):
                            imports.add(line.split()[1].split(".")[0])
            except (UnicodeDecodeError, PermissionError):
                continue
            graph[module] = imports

    # Print graph
    for module, deps in sorted(graph.items()):
        if deps:
            print(f"{module}")
            for d in sorted(deps):
                print(f"  └── {d}")
    return graph

# build_dependency_graph("./src")

"""Quick reference summary:

Function	Purpose	Level
os.getcwd / chdir	Working directory	Basic
os.path.join / basename / splitext	Path manipulation	Basic
os.listdir / scandir	Directory listing	Basic / Advanced
os.makedirs / remove / rename	File operations	Basic
os.walk	Recursive traversal	Intermediate
os.environ	Environment variables	Intermediate
os.stat	File metadata	Advanced
os.pipe / fork	IPC (Unix)	Advanced
sys.argv	CLI arguments	Basic
sys.path / modules	Import system	Intermediate
sys.stdin / stdout / stderr	I/O streams	Intermediate
sys.getsizeof	Memory inspection	Intermediate
sys.settrace	Execution tracing	Advanced
sys.exc_info	Exception details	Advanced
sys.meta_path	Import hooks	Expert
sys.addaudithook	Security auditing	Expert"""
