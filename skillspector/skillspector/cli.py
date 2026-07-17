import json
import sys
import click
from .scanner import scan_target
from .mcp_server import run_mcp_server

@click.group()
def cli():
    """Skillspector: Security scanner for AI agent skills."""
    pass

@cli.command()
@click.argument('target')
@click.option('--format', type=click.Choice(['text', 'json']), default='text', help='Output format')
@click.option('--output', type=click.Path(), help='Output file to write results to')
def scan(target, format, output):
    """Scan a skill from a local path or remote URL."""
    result = scan_target(target)
    
    if format == 'json':
        output_str = json.dumps(result, indent=2)
    else:
        # Simple text formatting
        lines = []
        if 'error' in result:
            lines.append(f"Error: {result['error']}")
        else:
            lines.append(f"Scanned target: {result['target']}")
            lines.append(f"Total issues found: {result['total_issues']}")
            for issue in result.get('issues', []):
                file_path = issue.get('file', 'Unknown')
                line = issue.get('line', '?')
                msg = issue.get('message', '')
                sev = issue.get('severity', 'unknown').upper()
                lines.append(f"[{sev}] {file_path}:{line} - {msg}")
        output_str = "\n".join(lines)
        
    if output:
        with open(output, 'w', encoding='utf-8') as f:
            f.write(output_str)
        click.echo(f"Results written to {output}")
    else:
        click.echo(output_str)
        
    # Exit with non-zero status if issues were found
    if result.get('total_issues', 0) > 0 or 'error' in result:
        sys.exit(1)

@cli.command()
def mcp():
    """Run as an MCP server."""
    run_mcp_server()

if __name__ == '__main__':
    cli()
