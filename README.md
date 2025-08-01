# Shopping List Manager

A Python-based shopping list management system that uses AI agents and Model Context Protocol (MCP) to provide an intelligent shopping list assistant.

## Features

- 🤖 **AI-Powered Assistant**: Uses OpenAI's GPT models to understand natural language commands
- 📝 **Shopping List Management**: Add, remove, mark items as purchased, and view your list
- 🔧 **MCP Integration**: Uses Model Context Protocol for tool integration
- 🔒 **Secure**: API keys stored in environment variables
- 🚀 **Easy to Use**: Simple natural language interface

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Required Python packages (see Installation)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd shopping_List_Manager
   ```

2. **Install required packages:**
   ```bash
   pip install agents mcp python-dotenv
   ```

3. **Set up your environment:**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your OpenAI API key
   nano .env
   ```

4. **Add your OpenAI API key to `.env`:**
   ```
   OPENAI_API_KEY=your-openai-api-key-here
   ```

## Usage

### Running the Shopping List Manager

```bash
python3 agent_client.py
```

### Example Commands

The AI assistant understands natural language commands:

- **View your list**: "Show me my shopping list"
- **Add items**: "Add 3 bananas to my shopping list"
- **Mark as purchased**: "Mark bread as purchased"
- **Remove items**: "Remove coffee from my shopping list"
- **Update quantities**: "Change milk quantity to 1"

## Project Structure

```
shopping_List_Manager/
├── agent_client.py      # Main client that runs the AI agent
├── mcp_server.py        # MCP server with shopping list tools
├── shopping_list.py     # Shopping list service implementation
├── connection.py        # Connection utilities
├── material.txt         # Project documentation
├── .env                 # Environment variables (not in repo)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## How It Works

1. **Agent Client** (`agent_client.py`): 
   - Creates an AI agent using the OpenAI API
   - Connects to the MCP server
   - Handles user queries and responses

2. **MCP Server** (`mcp_server.py`):
   - Provides tools for shopping list operations
   - Handles add, remove, mark purchased, and list operations
   - Communicates with the shopping list service

3. **Shopping List Service** (`shopping_list.py`):
   - Manages the actual shopping list data
   - Handles CRUD operations for shopping items
   - Maintains item states (purchased/not purchased)

## Available Tools

The MCP server provides these tools:

- `fetch_items()`: Retrieve all shopping list items
- `add_item()`: Add a new item to the list
- `remove_item()`: Remove an item from the list
- `mark_purchased()`: Mark an item as purchased or not purchased

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

### Model Configuration

You can change the AI model in `agent_client.py`:
```python
model="gpt-4.1"  # or "gpt-3.5-turbo", "gpt-4o", etc.
```

## Security

- API keys are stored in `.env` file (not committed to git)
- `.gitignore` is configured to exclude sensitive files
- Use `.env.example` as a template for required environment variables

## Troubleshooting

### Common Issues

1. **API Key Error**: Make sure your OpenAI API key is correct and has sufficient credits
2. **Import Errors**: Ensure all required packages are installed
3. **MCP Connection Issues**: Check that `mcp_server.py` is in the same directory

### Getting Help

If you encounter issues:
1. Check that your API key is valid
2. Ensure all dependencies are installed
3. Verify the project structure is correct

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with OpenAI's GPT models
- Uses Model Context Protocol (MCP) for tool integration
- Inspired by modern AI agent architectures 