from rich.live import Live
from rich.panel import Panel
from rich.table import Table
import requests
import time

def build_dashboard():
    try:
        res = requests.get("http://localhost:8000/status/history")
        data = res.json()

        table = Table(title="[bold green]Agent Progress History", expand=True)
        table.add_column("Time", style="cyan", no_wrap=True)
        table.add_column("Step", style="bold yellow")
        table.add_column("Detail", style="white")

        for item in data[-10:]:  # show last 10 entries
            table.add_row(item["timestamp"], item["step"], item["detail"])

        return Panel(table, title="[blue]Security Scan Status", padding=(1, 2))
    except Exception as e:
        return Panel(f"[red]Error fetching status: {e}", title="Error")

with Live(refresh_per_second=2) as live:
    while True:
        live.update(build_dashboard())
        time.sleep(1)
