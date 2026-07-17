import os
import ast
import re
import tempfile
import subprocess
import shutil
from pathlib import Path
from typing import List, Dict, Any, Optional

def clone_repo(url: str, dest_dir: str) -> bool:
    try:
        subprocess.run(["git", "clone", "--depth", "1", url, dest_dir], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def scan_python_file(filepath: str) -> List[Dict[str, Any]]:
    issues = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        tree = ast.parse(content, filename=filepath)
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id in ('eval', 'exec'):
                        issues.append({
                            "type": "dangerous_function",
                            "severity": "high",
                            "message": f"Found use of {node.func.id}()",
                            "line": node.lineno
                        })
                elif isinstance(node.func, ast.Attribute):
                    if isinstance(node.func.value, ast.Name):
                        if node.func.value.id == 'os' and node.func.attr == 'system':
                            issues.append({
                                "type": "dangerous_function",
                                "severity": "medium",
                                "message": "Found use of os.system()",
                                "line": node.lineno
                            })
                        elif node.func.value.id == 'subprocess' and node.func.attr in ('run', 'Popen', 'call', 'check_call', 'check_output'):
                            issues.append({
                                "type": "subprocess_call",
                                "severity": "low",
                                "message": f"Found use of subprocess.{node.func.attr}()",
                                "line": node.lineno
                            })
    except SyntaxError:
        issues.append({
            "type": "syntax_error",
            "severity": "low",
            "message": "Failed to parse Python file"
        })
    except Exception as e:
        issues.append({
            "type": "scan_error",
            "severity": "low",
            "message": f"Error scanning Python file: {str(e)}"
        })
    return issues

def scan_shell_file(filepath: str) -> List[Dict[str, Any]]:
    issues = []
    dangerous_patterns = [
        (r'curl\s+.*\|\s*(?:bash|sh)', 'curl_pipe_bash', 'high', 'Curl piping to bash found'),
        (r'wget\s+.*\|\s*(?:bash|sh)', 'wget_pipe_bash', 'high', 'Wget piping to bash found'),
        (r'rm\s+-rf\s+/', 'rm_rf_root', 'high', 'rm -rf / found'),
        (r'rm\s+-rf\s+~', 'rm_rf_home', 'high', 'rm -rf ~ found'),
    ]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f, 1):
                for pattern, issue_type, severity, msg in dangerous_patterns:
                    if re.search(pattern, line):
                        issues.append({
                            "type": issue_type,
                            "severity": severity,
                            "message": msg,
                            "line": i
                        })
    except Exception as e:
         issues.append({
            "type": "scan_error",
            "severity": "low",
            "message": f"Error scanning shell file: {str(e)}"
        })
    return issues

def scan_target(target: str) -> Dict[str, Any]:
    issues = []
    temp_dir = None
    
    try:
        if target.startswith("http://") or target.startswith("https://"):
            temp_dir = tempfile.mkdtemp()
            success = clone_repo(target, temp_dir)
            if not success:
                return {"target": target, "error": "Failed to clone repository", "issues": []}
            scan_path = temp_dir
        else:
            scan_path = os.path.expanduser(target)
            if not os.path.exists(scan_path):
                 return {"target": target, "error": f"Path not found: {target}", "issues": []}
            
        base_path = Path(scan_path)
        
        for path in base_path.rglob('*'):
            if path.is_file() and not '.git' in path.parts:
                if path.suffix == '.py':
                    file_issues = scan_python_file(str(path))
                    for issue in file_issues:
                        issue['file'] = str(path.relative_to(base_path))
                        issues.append(issue)
                elif path.suffix in ('.sh', '.bash'):
                    file_issues = scan_shell_file(str(path))
                    for issue in file_issues:
                        issue['file'] = str(path.relative_to(base_path))
                        issues.append(issue)
                elif path.name == 'SKILL.md':
                    # Add specific SKILL.md checks here if needed
                    pass
                    
        return {
            "target": target,
            "issues": issues,
            "total_issues": len(issues)
        }
    finally:
        if temp_dir and os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
