try:
    from . import show_logo 
except:
    import show_logo
    
show_logo.print_description()



try:
    from .pipelines.execution_pipeline import task_execution
    from .pipelines.extraction_pipeline import task_extraction
    from .pipelines.exploit_pipeline import attacker

except:
    from pipelines.execution_pipeline import task_execution
    from pipelines.extraction_pipeline import task_extraction
    from pipelines.exploit_pipeline import attacker
    
import argparse


from rich.panel import Panel
from rich.console import Group
from rich.text import Text
from rich.prompt import Prompt
from rich import print
import json


show_logo.print_logo()



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

def runAgent(URL):

    print(f"Using URL: {URL}")
        


    print(Panel("[bold green]INITIALIZING STAGE 1/3: EXTRACTOR AGENT[/bold green]", title="Startup"))

    combined_response , tasks_response , detailed_workflows , WORKFLOW_DIR , workflow_paths , visited_urls = task_extraction.main(URL = URL)
    print(Panel("[bold red]CLOSING AGENT LOOP[/bold red]", title="Shutdown"))

    print(" \n\n\n\n\n")

    print(Panel("[bold green]INITIALIZING STAGE 2/3 : EXECUTOR AGENT[/bold green]", title="Startup"))

    states  , failed = task_execution.batch_execution(workflow_paths=workflow_paths , url= URL)

    print(Panel("[bold red]CLOSING EXECUTOR AGENT LOOP[/bold red]", title="Shutdown"))

    # Pretty-print the failed dict with indentation
    if failed:
        failed_str = json.dumps(failed, indent=4)
        print(Panel(Text(failed_str, style="red"), title="Failed Details", border_style="red"))
    else:
        print(Panel(Text("No failures reported.", style="green"), title="Failed Details", border_style="green"))


    print(Panel("[bold green]INITIALIZING STAGE 3/3 : EXPLOITING AGENT[/bold green]", title="Startup"))

    states , failed_dict = attacker.batch_execution(url=URL , failed=failed , visited_urls=visited_urls)

    print(Panel("[bold red]CLOSING EXPLOIT AGENT LOOP[/bold red]", title="Shutdown"))


