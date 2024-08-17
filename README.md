<a href="https://x.com/alxfazio" target="_blank">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="images/crewai-quick-start-cover.png">
    <img alt="OpenAI Cookbook Logo" src="images/crewai-quick-start-cover.png" width="400px" style="max-width: 100%; margin-bottom: 20px;">
  </picture>
</a>

[![Build GitHub Docs On Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new/?repo=crewAI-quickstart)

CrewAI Quickstart offers a cookbook of code templates and guides designed to help developers build with CrewAI. It includes easily copy-able code snippets that you can seamlessly integrate into your own projects.


## Prerequisites

To make the most of the examples in this quickstart guide, you'll need to be familiar with CrewAI. We recommend reviewing the official CrewAI documentation at https://docs.crewai.com/ to understand the basic concepts and functionality. You'll also need an API key from one of the major Language Model providers such as Anthropic, OpenAI, Groq, or Cohere.


## Table of Contents

- [Quickstart Templates](#quickstart-templates)
  - [Basic Notebooks](#basic-notebooks)
  - [Notebooks with Tool Use](#notebooks-with-tool-use)
  - [Extra Notebooks](#extra-notebooks)
  - [Python Scripts](#python-scripts)
  - [GUI with Streamlit](#gui-with-streamlit)
  - [Local LLMs](#local-llms)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Quickstart Templates

### Basic Notebooks

- [Sequential Google Colab Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_quickstart.ipynb)
- [Hierarchical Google Colab Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_hierarchical_quickstart.ipynb)

### Notebooks with Tool Use

| Tool Name | Description | Notebook Link |
|-----------|-------------|---------------|
| TXTSearchTool | RAG tool for searching within text (.txt) files | [Sequential `.txt` Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_TXTSearchTool_quickstart.ipynb) |
| CodeDocsSearchTool | RAG tool for searching through code documentation | [Sequential Code Docs Search Tool Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_CodeDocsSearchTool_quickstart.ipynb) |
| CodeInterpreterTool | Tool for interpreting Python code | [Sequential Code Interpreter Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_CodeInterpreterTool_quickstart.ipynb) |
| ComposioTool | Enables use of Composio tools | [Sequential Composio SDK Tool Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_composio_core_quickstart.ipynb) |
| CSVSearchTool | RAG tool for searching within CSV files | [Sequential CSV lookup Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_CSVSearchTool_quickstart.ipynb) |
| DirectoryReadTool | Facilitates reading of directory structures | [Sequential Directory Read Tool Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_DirectoryReadTool_quickstart.ipynb) |
| DOCXSearchTool | RAG tool for searching within DOCX documents | [Sequential DOCX Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_DOCXSearchTool_quickstart.ipynb) |
| GithubSearchTool | RAG tool for searching within GitHub repositories | [Sequential GitHub Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_GithubSearchTool_quickstart.ipynb) |
| BrowserbaseLoadTool | Tool for interacting with web browsers | [Sequential Headless Browser Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_BrowserbaseLoadTool_quickstart.ipynb) |
| JSONSearchTool | RAG tool for searching within JSON files | [Sequential JSON Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_JSONSearchTool_quickstart.ipynb) |
| MDXSearchTool | RAG tool for searching within Markdown (MDX) files | [Sequential MDX Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_MDXSearchTool_quickstart.ipynb) |
| PDFSearchTool | RAG tool for searching within PDF documents | [Sequential PDF Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_PDFSearchTool_quickstart.ipynb) |
| PGSearchTool | RAG tool for searching within PostgreSQL databases | [Sequential PostgreSQL Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_PGSearchTool_quickstart.ipynb) |
| ScrapeWebsiteTool | Facilitates scraping entire websites | [Sequential Web Scraping Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_ScrapeWebsiteTool_quickstart.ipynb) |
| SeleniumScrapingTool | Web scraping tool using Selenium | [Sequential Web Scraping (Selenium) Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_SeleniumScrapingTool_quickstart.ipynb) |
| SerperDevTool | Specialized tool for development purposes | [Sequential Web Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_SerperDevTool_quickstart.ipynb) |
| WebsiteSearchTool | RAG tool for searching website content | [Sequential Website Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_WebsiteSearchTool_quickstart.ipynb) |
| XMLSearchTool | RAG tool for searching within XML files | [Sequential XML Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_XMLSearchTool_quickstart.ipynb) |
| YoutubeChannelSearchTool | RAG tool for searching within YouTube channels | [Sequential YouTube Channel Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_YoutubeChannelSearchTool_quickstart.ipynb) |
| YoutubeVideoSearchTool | RAG tool for searching within YouTube videos | [Sequential YouTube Video Search Notebook](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_sequential_YoutubeVideoSearchTool_quickstart.ipynb) |

### Extra Notebooks

- [Custom Tool Template](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai_custom_tool_template_quickstart.ipynb)
- [Example Task: Event Planning](https://github.com/alexfazio/crewAI-quickstart/blob/main/crewai-example-task-event-planning-quickstart.ipynb)

### Python Scripts

- [Sequential](https://github.com/alexfazio/crewAI-quickstart/tree/main/crewai-sequential-quickstart)
- [Hierarchical](https://github.com/alexfazio/crewAI-quickstart/tree/main/crewai-hierarchical-quickstart)

### GUI with Streamlit

- [Streamlit GUI Sequential](https://github.com/alexfazio/crewAI-quickstart/tree/main/crewai-streamlit-sequential-quickstart)
- [Streamlit GUI Hierarchical](https://github.com/alexfazio/crewAI-quickstart/tree/main/crewai-hierarchical-quickstart)

### Local LLMs

- [Sequential Ollama with `llama2`](https://github.com/alexfazio/crewAI-quickstart/tree/main/crewai-sequential-ollama2-quickstart)
- [Sequential Ollama with `llama3`](https://github.com/alexfazio/crewAI-quickstart/tree/main/crewai-sequential-ollama3-quickstart)

## Contributing

The CrewAI Quickstart thrives on the contributions of the developer community. We value your input, whether it's submitting an idea, fixing a typo, adding a new guide, or improving an existing one. By contributing, you help make this resource even more valuable for everyone.

To avoid duplication of efforts, please review the existing issues and pull requests before contributing.

If you have ideas for new examples or guides, share them on the [issues page](https://github.com/alexfazio/crewAI-quickstart/issues).

## Credits

Thanks to [@AbubakrChan](https://github.com/AbubakrChan) for his contribution to the **🖼️ GUI w/ Streamlit `.py`** templates.

## License

This project is licensed under the [MIT License](LICENSE).

Happy learning and coding with CrewAI!
