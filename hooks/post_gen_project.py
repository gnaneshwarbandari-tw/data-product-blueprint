import os
import shutil
import sys

def move_workflows_to_root():
    # The directory where the project was just created
    project_dir = os.getcwd()
    # The parent directory (cli_script root)
    root_dir = os.path.dirname(project_dir)
    
    source = os.path.join(project_dir, ".github")
    destination = os.path.join(root_dir, ".github")

    if os.path.exists(source):
        # If a .github folder already exists in root, merge or handle error
        if os.path.exists(destination):
            print("Target .github folder already exists in root. Merging workflows...")
            src_workflows = os.path.join(source, "workflows")
            dest_workflows = os.path.join(destination, "workflows")
            
            os.makedirs(dest_workflows, exist_ok=True)
            
            for filename in os.listdir(src_workflows):
                shutil.move(os.path.join(src_workflows, filename), 
                            os.path.join(dest_workflows, filename))
            # Clean up the empty template .github folder
            shutil.rmtree(source)
        else:
            shutil.move(source, destination)
            print(f"Successfully moved .github to {root_dir}")

if __name__ == "__main__":
    try:
        move_workflows_to_root()
    except Exception as e:
        print(f"Error moving workflow: {e}")
        sys.exit(1)