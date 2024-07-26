# Effective Test Generation using pre-trained Large Language Models and Mutation Testing

## Overview

This repository contains the code and resources for integrating Google's Gemini language model into the MuTAP (Mutation Testing-based Augmented Prompting) framework for automated test case generation. The goal is to leverage the capabilities of Gemini to generate, refine, and evaluate test cases using mutation testing.

## Features

- **Integration with Gemini 1.5 Flash**: Utilizes the advanced capabilities of Gemini for improved test case generation.
- **Mutation Testing**: Employs mutation testing to evaluate the effectiveness of generated test cases.
- **Automated Test Generation**: Automatically generates and refines test cases for various Python functions.
- **Comparison with Other LLMs**: Provides comparative analysis with other large language models like Codex and llama-2-chat.

## Setup

### Prerequisites

- Python 3.7 or higher
- An API key for Gemini
- Dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hojiakbar9/MuTAP_Gemini.git
   cd MuTAP_Gemini
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Set up your Gemini API key:

   ```bash
   export GEMINI_API_KEY='your_api_key_here'  # On Windows use `set GEMINI_API_KEY=your_api_key_here`
   ```
