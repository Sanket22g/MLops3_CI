# MLops3_CI - Continuous Integration Demo

## Author
**Sanket22g** (sanketghadge122@gmail.com)

---

## 📋 Project Overview
This project demonstrates **Continuous Integration (CI)** using GitHub Actions. It includes a simple Streamlit calculator app with automated testing.

---

## 🔄 What is Continuous Integration (CI)?

**Continuous Integration** is a software development practice where developers frequently integrate their code changes into a shared repository. Each integration is automatically verified by:
1. **Building** the project
2. **Running automated tests**
3. **Detecting errors early**

### Why CI Matters?
- ✅ **Catches bugs early** - before they reach production
- ✅ **Faster development** - automated testing saves time
- ✅ **Better code quality** - ensures all tests pass before merging
- ✅ **Team collaboration** - everyone works with tested code

### CI Pipeline Flow
```
Code Push → GitHub → CI Workflow Triggers → Install Dependencies → Run Tests → ✅ Pass/❌ Fail
```

---

## 🛠️ Setup Steps & Commands

### 1. Install Dependencies Locally
```powershell
# Install Streamlit
pip install streamlit
# Output: Successfully installed streamlit-1.54.0

# Or using specific Python version
python -m pip install streamlit
```

### 2. Configure Git Identity
```powershell
# Set your name globally (for all repos)
git config --global user.name "Sanket22g"

# Set your email globally
git config --global user.email "sanketghadge122@gmail.com"

# Verify configuration
git config --global --list | Select-String "user"
# Output:
# user.name=Sanket22g
# user.email=sanketghadge122@gmail.com
```

### 3. Create Requirements File
```txt
# requirements.txt
streamlit
pytest
```

### 4. Git Commands
```powershell
# Add files to staging
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push origin main

# View commit history
git log --oneline -5
```

### 5. Run Streamlit App Locally
```powershell
streamlit run app.py
# Output: Local URL: http://localhost:8501
```

### 6. Run Tests Locally
```powershell
pytest _test.py
# Output: ===== 2 passed in 0.05s =====
```

---

## 📂 Project Structure
```
MLops3_CI/
├── .github/
│   └── workflows/
│       └── ci.yaml          # CI pipeline configuration
├── app.py                   # Streamlit calculator app
├── _test.py                 # Pytest test cases
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

---

## 🚀 CI/CD Pipeline Details

### Workflow File: `.github/workflows/ci.yaml`
```yaml
name: CI
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - Checkout code
      - Setup Python 3.8
      - Install dependencies from requirements.txt
      - Run pytest tests
```

### What Happens on Every Push?
1. GitHub Actions triggers automatically
2. Creates a virtual Ubuntu machine
3. Installs Python 3.8
4. Installs dependencies: `pip install -r requirements.txt`
5. Runs tests: `pytest _test.py`
6. Reports success ✅ or failure ❌

---

## 🎯 CI Concept Revision Questions

### Basic Level
1. **What is Continuous Integration?**
   - Automated process of integrating code changes and testing them

2. **Why do we use CI?**
   - Catch bugs early, improve code quality, faster feedback

3. **What triggers our CI pipeline?**
   - Push to main branch or Pull Request creation

4. **What does our CI workflow do?**
   - Sets up Python → Installs dependencies → Runs tests

### Intermediate Level
5. **What is the purpose of `requirements.txt`?**
   - Lists all Python dependencies needed for the project

6. **Why did we get "No such file or directory: requirements.txt" error?**
   - CI tried to install dependencies but file didn't exist in repo

7. **What is the difference between `pip install` and `python -m pip install`?**
   - `python -m pip` ensures you're using pip from the specific Python version

8. **What does `runs-on: ubuntu-latest` mean?**
   - CI runs on a Ubuntu Linux virtual machine (GitHub-hosted)

### Advanced Level
9. **What happens if a test fails in CI?**
   - CI marks the workflow as failed, prevents bad code from being merged

10. **Why test on Python 3.8 if we use Python 3.13 locally?**
    - Ensures compatibility across different Python versions

11. **What's the difference between CI and CD?**
    - **CI** = Continuous Integration (testing)
    - **CD** = Continuous Deployment (automatic deployment to production)

12. **How can you see CI workflow results?**
    - GitHub repo → Actions tab → View workflow runs

---

## 🐛 Common Issues & Solutions

### Issue 1: Module Not Found
```
Error: No module named 'streamlit'
Solution: pip install streamlit
```

### Issue 2: Wrong Git Author
```
Problem: Commits show wrong name
Solution: git config --global user.name "YourName"
```

### Issue 3: Missing requirements.txt
```
Error: Could not open requirements file
Solution: Create requirements.txt with all dependencies
```

### Issue 4: Tests Failing
```
Check: Run pytest locally first
Debug: Read error messages carefully
Fix: Update code and re-push
```

---

## 📝 Key Commands Cheatsheet

| Task | Command |
|------|---------|
| Install package | `pip install package-name` |
| Run Streamlit | `streamlit run app.py` |
| Run tests | `pytest _test.py` |
| Git status | `git status` |
| Git add all | `git add .` |
| Git commit | `git commit -m "message"` |
| Git push | `git push origin main` |
| View logs | `git log --oneline` |
| Check config | `git config --list` |

---

## 🎓 Learning Outcomes
- ✅ Understood CI/CD concepts
- ✅ Set up GitHub Actions workflow
- ✅ Created automated testing pipeline
- ✅ Configured Git properly
- ✅ Managed Python dependencies
- ✅ Debugged CI pipeline issues

---

## 📚 Next Steps
1. Add more test cases
2. Implement CD (Continuous Deployment)
3. Add code coverage reports
4. Set up linting (flake8, black)
5. Deploy to cloud (Streamlit Cloud, Heroku, Azure)

---

**Happy Learning! 🚀**
