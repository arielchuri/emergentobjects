# Development Environment Setup

**Type:** Lab (Complete/Incomplete)

## Overview
Set up your development environment for Python programming using Visual Studio Code (VS Code).

## Requirements

### 1. Install Python
- **Download:** [python.org/downloads](https://www.python.org/downloads/)
- Install Python 3.10 or newer
- **Important:** On Windows, check "Add Python to PATH" during installation

**Verify installation:**
```bash
python --version
```
or
```bash
python3 --version
```

### 2. Install Visual Studio Code
- **Download:** [code.visualstudio.com](https://code.visualstudio.com/)
- Available for Windows, macOS, and Linux
- Install using default settings

### 3. Install Python Extension for VS Code

**Method 1: Within VS Code**
1. Open VS Code
2. Click the Extensions icon in the sidebar (or press `Ctrl+Shift+X` / `Cmd+Shift+X`)
3. Search for "Python"
4. Install the extension by Microsoft (usually the first result)

**Method 2: Direct Link**
- [Python Extension on VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### 4. Create and Test a Python File

1. Create a new folder for your Python work
2. Open the folder in VS Code (`File → Open Folder`)
3. Create a new file called `hello.py`
4. Add this code:
```python
print("Hello, world!")
```
5. Run the file:
   - Right-click in the editor and select "Run Python File in Terminal"
   - Or use the play button in the top-right corner
   - Or press `Ctrl+F5` / `Cmd+F5`

## Additional Resources

### VS Code Python Documentation
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python in VS Code (Official Docs)](https://code.visualstudio.com/docs/languages/python)

### Python Learning Resources
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)
- [Real Python Tutorials](https://realpython.com/)

### Troubleshooting
- [Python Interpreter Selection](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
- [Python Extension FAQ](https://code.visualstudio.com/docs/python/python-tutorial#_troubleshooting)

## Completion Criteria
- [ ] Python installed and version verified
- [ ] VS Code installed
- [ ] Python extension installed in VS Code
- [ ] Successfully ran a "Hello, world!" Python program
