import os

base_dir = "src/arrays"

for dirname in os.listdir(base_dir):
    dir_path = os.path.join(base_dir, dirname)
    if not os.path.isdir(dir_path):
        continue
    
    # Rename solution.py
    old_solution = os.path.join(dir_path, "solution.py")
    new_solution = os.path.join(dir_path, f"{dirname}.py")
    
    if os.path.exists(old_solution):
        os.rename(old_solution, new_solution)
        print(f"Renamed {old_solution} to {new_solution}")
    
    # Fix import in test file
    test_file = os.path.join(dir_path, f"test_{dirname}.py")
    if os.path.exists(test_file):
        with open(test_file, "r") as f:
            content = f.read()
        
        new_content = content.replace("from solution import", f"from {dirname} import")
        
        with open(test_file, "w") as f:
            f.write(new_content)
        print(f"Updated imports in {test_file}")
