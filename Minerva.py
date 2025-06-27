try:
    from src import show_logo 
except:
    import show_logo
    
show_logo.print_description()



try:
    from src.pipelines.execution_pipeline import task_execution
    from src.pipelines.extraction_pipeline import task_extraction
    from src.pipelines.exploit_pipeline import attacker

except:
    from .pipelines.execution_pipeline import task_execution
    from .pipelines.extraction_pipeline import task_extraction
    from .pipelines.exploit_pipeline import attacker
    
import argparse


from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich.prompt import Prompt
from rich import print
import json
import requests

show_logo.print_logo()



def runAgent(URL):
    
    print(Panel(f"[bold cyan]Using URL: {URL}[/bold cyan]", title="🎯 Target Configuration", border_style="cyan"))
    requests.post("http://localhost:8000/update_status", json={"step": "Agent Initialization", "detail": f"Starting multi-stage agent execution for URL: {URL}"})

    print(Panel("[bold green]INITIALIZING STAGE 1/3: EXTRACTOR AGENT[/bold green]", title="🚀 Stage 1 Startup", border_style="bright_green"))
    requests.post("http://localhost:8000/update_status", json={"step": "Stage 1 - Extractor Agent", "detail": "Initializing task extraction agent for workflow discovery"})

    combined_response, tasks_response, detailed_workflows, WORKFLOW_DIR, workflow_paths, visited_urls = task_extraction.main(URL=URL)
    requests.post("http://localhost:8000/update_status", json={"step": "Stage 1 - Extractor Agent", "detail": f"Task extraction completed. Generated {len(workflow_paths) if workflow_paths else 0} workflows from {len(visited_urls) if visited_urls else 0} visited URLs"})
    
    print(Panel("[bold red]CLOSING EXTRACTOR AGENT LOOP[/bold red]", title="🔚 Stage 1 Shutdown", border_style="bright_red"))
    requests.post("http://localhost:8000/update_status", json={"step": "Stage 1 Complete", "detail": f"Extractor agent completed successfully. Workflows saved to: {WORKFLOW_DIR}"})

    print(" \n\n\n\n\n")

    print(Panel("[bold green]INITIALIZING STAGE 2/3 : EXECUTOR AGENT[/bold green]", title="🚀 Stage 2 Startup", border_style="bright_green"))
    requests.post("http://localhost:8000/update_status", json={"step": "Stage 2 - Executor Agent", "detail": f"Initializing task execution agent for {len(workflow_paths)} workflows"})

    states, failed = task_execution.batch_execution(workflow_paths=workflow_paths, url=URL)
    requests.post("http://localhost:8000/update_status", json={"step": "Stage 2 - Executor Agent", "detail": f"Task execution completed. Processed {len(states)} states with {len(failed)} total failures"})

    print(Panel("[bold red]CLOSING EXECUTOR AGENT LOOP[/bold red]", title="🔚 Stage 2 Shutdown", border_style="bright_red"))

    # Pretty-print the failed dict with indentation
    if failed:
        failed_str = json.dumps(failed, indent=4)
        print(Panel(Text(failed_str, style="red"), title="⚠️ Failed Details", border_style="red"))
        requests.post("http://localhost:8000/update_status", json={"step": "Stage 2 Failures", "detail": f"Execution failures detected: {len(failed)} failed operations"})
    else:
        print(Panel(Text("No failures reported.", style="bright_green"), title="✅ Success Status", border_style="bright_green"))
        requests.post("http://localhost:8000/update_status", json={"step": "Stage 2 Success", "detail": "All task executions completed successfully with no failures"})

    print(Panel("[bold green]INITIALIZING STAGE 3/3 : EXPLOITING AGENT[/bold green]", title="🚀 Stage 3 Startup", border_style="bright_green"))
    requests.post("http://localhost:8000/update_status", json={"step": "Stage 3 - Exploit Agent", "detail": f"Initializing exploit agent with {len(failed)} previous failures and {len(visited_urls)} visited URLs"})

    states, failed_dict = attacker.batch_execution(url=URL, failed=failed, visited_urls=visited_urls)
    requests.post("http://localhost:8000/update_status", json={"step": "Stage 3 - Exploit Agent", "detail": f"Exploit execution completed. Final states: {len(states)}, exploit failures: {len(failed_dict)}"})

    print(Panel("[bold red]CLOSING EXPLOIT AGENT LOOP[/bold red]", title="🔚 Stage 3 Shutdown", border_style="bright_red"))
    requests.post("http://localhost:8000/update_status", json={"step": "Multi-Stage Agent Complete", "detail": f"All 3 agent stages completed successfully. Final results: {len(states)} states, {len(failed_dict)} exploit outcomes"})

    return states, failed_dict, combined_response, tasks_response, detailed_workflows, WORKFLOW_DIR, workflow_paths, visited_urls

if __name__ == "__main__":
    

    # parser = argparse.ArgumentParser(description="Optional URL argument with default")


    # parser.add_argument(
    #         '--url',
    #         type=str,
    #         default='http://127.0.0.1:5000',
    #         help='Base URL of the server (default: http://127.0.0.1:5000)'
    #     )

    #     # Parse the arguments
    # args = parser.parse_args()

    # Use the URL
    # URL = args.url


    URL = Prompt.ask("[bold cyan]Enter your URL[/bold cyan]")
    
    runAgent(URL=URL)