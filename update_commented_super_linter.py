#!/usr/bin/env python3
# file: update_commented_super_linter.py
# version: 1.0.0
# guid: c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f

"""
Deploy the updated super-linter.env with commented VALIDATE_ options to all repositories.
"""

import os
import shutil
import subprocess
import sys

# Target repositories (relative to parent directory)
TARGET_REPOS = [
    "../ghcommon",
    "../subtitle-manager", 
    "../copilot-agent-util-rust",
    "../apt-cacher-go",
    "../audiobook-organizer",
    "../merge-srt-subtitles",
    "../public-scratch"
]

def run_command(command, cwd=None):
    """Run a command and return (success, output)"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, f"Error: {e.stderr.strip()}"

def update_repository(repo_path):
    """Update super-linter.env in a repository"""
    repo_name = os.path.basename(os.path.abspath(repo_path))
    
    print(f"\n🔄 Updating {repo_name}...")
    
    if not os.path.exists(repo_path):
        print(f"❌ Repository not found: {repo_path}")
        return False
    
    source_file = ".github/linters/super-linter.env"
    target_file = os.path.join(repo_path, ".github/linters/super-linter.env")
    
    if not os.path.exists(source_file):
        print(f"❌ Source file not found: {source_file}")
        return False
    
    target_dir = os.path.dirname(target_file)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
        print(f"📁 Created directory: {target_dir}")
    
    # Copy the updated file
    try:
        shutil.copy2(source_file, target_file)
        print(f"📄 Copied super-linter.env to {repo_name}")
    except Exception as e:
        print(f"❌ Failed to copy file: {e}")
        return False
    
    # Commit the changes
    os.chdir(repo_path)
    
    # Add the file
    success, output = run_command("git add .github/linters/super-linter.env")
    if not success:
        print(f"❌ Failed to add file: {output}")
        return False
    
    # Check if there are changes to commit
    success, output = run_command("git diff --cached --quiet")
    if success:  # No changes
        print(f"ℹ️ {repo_name} - No changes to commit")
        return True
    
    # Commit the changes
    commit_message = """chore(linter): comment out all VALIDATE_ options by default

Updated Super Linter configuration to have all VALIDATE_ options commented out by default.
This allows for selective enabling of validation rules as needed per project.

Files changed:
- .github/linters/super-linter.env - All VALIDATE_ options now commented out with instructions"""
    
    success, output = run_command(f'git commit -m "{commit_message}"')
    if not success:
        print(f"❌ Failed to commit changes: {output}")
        return False
    
    print(f"✅ {repo_name} - Changes committed")
    return True

def main():
    """Main function"""
    print("🔄 Updating Super Linter configuration with commented VALIDATE_ options...")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    success_count = 0
    total_count = len(TARGET_REPOS)
    
    for repo_path in TARGET_REPOS:
        if update_repository(repo_path):
            success_count += 1
        # Return to script directory
        os.chdir(script_dir)
    
    print("\n📊 Summary:")
    print(f"   Successfully updated: {success_count}/{total_count} repositories")
    
    if success_count == total_count:
        print("✅ All repositories successfully updated!")
        return 0
    else:
        print(f"❌ Failed to update {total_count - success_count} repositories")
        return 1

if __name__ == "__main__":
    sys.exit(main())
