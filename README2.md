# Minerva - AI-Powered Security Analysis Framework

Minerva is an advanced security analysis framework that leverages AI and machine learning to perform comprehensive security assessments of web applications and APIs. This framework is designed to automate the process of vulnerability discovery and exploitation through intelligent agents.

## Features

- Multi-stage security analysis pipeline
- AI-powered workflow extraction and analysis
- Real-time status monitoring dashboard
- Modular architecture for easy extension
- Rich console output with progress tracking

## Project Structure

- `src/` - Main source code directory containing core functionality
- `flask_demo_app/` - Demo application for testing
- `data/` - Data storage directory
- `models/` - Machine learning models
- `notebook/` - Jupyter notebooks for analysis
- `dashboard.py` - Real-time monitoring dashboard
- `Minerva.py` - Main entry point

## Core Components

### 1. Pipeline System
The framework consists of multiple interconnected pipelines:
- **Extraction Pipeline**: Discovers and extracts workflows from target applications
- **Execution Pipeline**: Performs security analysis tasks
- **Exploit Pipeline**: Identifies and exploits vulnerabilities

### 2. Status Monitoring
- Real-time dashboard showing agent progress
- Detailed status updates for each pipeline stage
- History tracking of all operations

## Setup and Usage

1. Clone the repository
2. Install dependencies (see requirements.txt)
3. Configure environment variables in `.env`
4. Run the main application using `run_minerva.sh`

## Monitoring

The framework includes a real-time dashboard that can be accessed through the Flask server. It provides:
- Progress tracking of security scans
- Detailed status updates
- Historical operation records
- Error tracking and logging

## Security Considerations

This framework is designed for security research and testing purposes only. Ensure you have proper authorization before using it against any system.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Add your license information here]

## Contact

For questions or issues, please contact the project maintainer.

---

*Note: This is an advanced security research tool that should be used responsibly and ethically.*
