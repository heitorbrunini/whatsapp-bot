# Analysis of Feature: src--whatsapp-bot--bot--scripts

## Architecture and Functionality Overview

# High-Level Analysis of the Feature

## 1. **Feature Purpose**
The primary goal of this feature is to enable automated interaction with customers via WhatsApp. It integrates a chatbot powered by a language model (LLM) to respond to customer messages, process orders, and handle notifications. The feature allows the end-user (likely a business owner or operator) to automate customer communication, including responding to inquiries, registering orders, and generating JSON files for further processing.

---

## 2. **Core Components**
### **File: `test_api.py`**
- **Responsibility**: This file interacts with an external API to fetch configuration data (e.g., notification identifiers, message content). It serves as a utility to retrieve and parse API responses, which are later used by other components.

### **File: `model_requests.py`**
- **Responsibility**: This file handles interactions with the LLM (Language Model). It provides functions to send user messages to the model, maintain conversation history, and retrieve responses. It also includes functionality to clean up the model's output and manage errors during communication.

### **File: `worker_bot.py`**
- **Responsibility**: This file implements the main bot logic using PyQt5 for threading and signaling. It continuously monitors WhatsApp Web for new notifications, captures incoming messages, and uses the LLM to generate responses. It also handles JSON generation for specific commands and manages the browser instance for WhatsApp Web automation.

### **File: `application_bot.py`**
- **Responsibility**: This file contains helper functions for interacting with WhatsApp Web via Selenium. It includes methods for detecting notifications, capturing contact and message details, sending responses, saving contacts, and processing scheduled messages. It also provides utility functions for cleaning text and handling CSV/Excel files.

---

## 3. **Data and Interaction Flow**
1. **Configuration Retrieval**:
   - `test_api.py` fetches configuration data (e.g., notification identifiers) from an external API.
   - This data is used by `worker_bot.py` to identify new notifications on WhatsApp Web.

2. **Notification Handling**:
   - `worker_bot.py` uses Selenium (via `application_bot.py`) to detect new notifications on WhatsApp Web.
   - When a notification is found, it captures the contact and message details.

3. **Message Processing**:
   - The captured message is sent to the LLM via `model_requests.py` to generate a response.
   - The response is either sent back to the customer or used to trigger specific actions (e.g., JSON generation).

4. **Response Delivery**:
   - The generated response is sent to the customer using Selenium functions in `application_bot.py`.

5. **Additional Features**:
   - Contacts can be saved to a CSV file for future use.
   - Scheduled messages are processed and sent based on data in an Excel file.

---

## 4. **External Dependencies**
- **Libraries**:
  - **Selenium**: Used for browser automation to interact with WhatsApp Web.
  - **PyQt5**: Provides threading and signaling for the bot's execution.
  - **Requests**: Used for API communication.
  - **Pandas**: Handles CSV and Excel file operations.
  - **Ollama**: Used for LLM interaction.
- **External Systems**:
  - **WhatsApp Web**: The bot interacts with WhatsApp Web to send and receive messages.
  - **LLM API**: The feature relies on an external language model for generating responses.
  - **EditaCodigo API**: Provides configuration data for notifications.

---

## 5. **Architecture Summary**
This feature follows a modular architecture with clear separation of concerns:
- **Bot Logic**: Implemented in `worker_bot.py`, which acts as the central controller for the feature.
- **Helper Functions**: Encapsulated in `application_bot.py` to handle specific tasks like message sending and notification detection.
- **LLM Integration**: Managed by `model_requests.py`, which abstracts the interaction with the language model.
- **Configuration Retrieval**: Handled by `test_api.py`, which fetches and parses data from an external API.

The feature can be classified as an **event-driven system** with elements of **MVC (Model-View-Controller)**:
- **Model**: The LLM and data files (CSV/Excel) act as the data layer.
- **View**: WhatsApp Web serves as the user interface.
- **Controller**: `worker_bot.py` orchestrates the interactions between the model and view.

The use of threading (via PyQt5) ensures the bot can run continuously without blocking other operations. Dependency injection is partially used, as components like the LLM model name and conversation history are passed as parameters.

---

---

## Detailed Analysis: `test_api.py`
> Analysis generated on: 2025-08-18 12:27:22

# Technical Analysis of `test_api.py`

## 1. **File's Core Responsibility**
The primary responsibility of `test_api.py` is to interact with an external API (`EditaCodigo API`) to fetch configuration data related to WhatsApp notifications and message content. This data is parsed and stored in variables for use by other components of the feature.

---

## 2. **Analysis of Key Functions/Methods**
This file does not define any functions or methods; instead, it executes procedural logic directly. Below is an analysis of the key operations:

### **API Request**
```python
api = requests.get(f"https://editacodigo.com.br/index/api-whatsapp/{token_api}", headers=agent)
```
- **Purpose**: Sends a GET request to the `EditaCodigo API` to retrieve configuration data.
- **Parameters**:
  - `url`: The API endpoint, dynamically constructed using the `token_api` variable.
  - `headers`: A dictionary containing the `User-Agent` string to simulate a browser request.
- **Return**: The response object from the API call.

### **Response Parsing**
```python
api = api.text
api = api.split('.n.')
bolinha_notificacao = api[3].strip()
contcaixa_msg = api[5].strip()
msg_cliente = api[6].strip()
```
- **Purpose**: Processes the API response to extract specific configuration values.
- **Steps**:
  1. **Convert Response to Text**: `api.text` converts the raw response object into a string.
  2. **Split Response**: `api.split('.n.')` splits the string into a list using `.n.` as the delimiter.
  3. **Extract Values**:
     - `bolinha_notificacao`: The fourth element in the list (`api[3]`), stripped of leading/trailing whitespace.
     - `contcaixa_msg`: The sixth element in the list (`api[5]`), stripped of leading/trailing whitespace.
     - `msg_cliente`: The seventh element in the list (`api[6]`), stripped of leading/trailing whitespace.
- **Return**: The extracted values are stored in variables for further use.

### **Debugging Output**
```python
print (f"msg_cliente: {msg_cliente}")
```
- **Purpose**: Prints the value of `msg_cliente` to the console for debugging purposes.
- **Parameters**: None.
- **Return**: Outputs the value of `msg_cliente` to the standard output.

---

## 3. **Important or Complex Logic**
### **Response Parsing Logic**
The parsing logic assumes that the API response is consistently formatted with `.n.` as the delimiter and that specific indices (`3`, `5`, `6`) correspond to meaningful data. This is a fragile approach because:
- If the API response format changes, the parsing logic will break.
- There is no error handling for cases where the indices are out of range or the response is malformed.

### **Hardcoded Token**
The `token_api` variable is hardcoded in the script:
```python
token_api = "Ezm597rhhnUH0zcnBhk772z1MZqhqgNC"
```
This approach is insecure and inflexible. If the token changes, the script must be manually updated. A better approach would be to load the token from an environment variable or configuration file.

---

## 4. **UI Interaction**
This file does not interact with any UI elements directly. It is purely a backend utility for API communication and data parsing.

---

## 5. **Backend Communication**
The file communicates with the `EditaCodigo API` using the `requests` library. The API call is made via the following line:
```python
api = requests.get(f"https://editacodigo.com.br/index/api-whatsapp/{token_api}", headers=agent)
```
- **Endpoint**: `https://editacodigo.com.br/index/api-whatsapp/{token_api}`
- **Headers**: Includes a `User-Agent` string to mimic a browser request.
- **Response Handling**: The response is converted to text and parsed into specific configuration values.

---

## Recommendations for Improvement
1. **Error Handling**:
   - Add error handling for the API call using `try-except` blocks to manage network issues or invalid responses.
   - Validate the structure of the API response before attempting to parse it.

2. **Dynamic Token Management**:
   - Replace the hardcoded `token_api` with a dynamic approach, such as loading it from an environment variable or configuration file.

3. **Response Parsing**:
   - Use a more robust method for parsing the API response, such as JSON parsing (if the API supports it) or regular expressions, instead of relying on hardcoded indices.

4. **Encapsulation**:
   - Encapsulate the logic into functions to improve readability, reusability, and testability. For example:
     ```python
     def fetch_api_data(token, agent):
         try:
             response = requests.get(f"https://editacodigo.com.br/index/api-whatsapp/{token}", headers=agent)
             response.raise_for_status()
             return response.text
         except requests.RequestException as e:
             print(f"Error fetching API data: {e}")
             return None
     ```

---

## Summary
The `test_api.py` file is a utility script for fetching and parsing configuration data from an external API. While functional, it lacks error handling, dynamic token management, and robust response parsing. Refactoring the script to address these issues would improve its reliability and maintainability.

---

---

## Detailed Analysis: `model_requests.py`
> Analysis generated on: 2025-08-18 12:27:22

# Technical Analysis of `model_requests.py`

## 1. **File's Core Responsibility**
The primary responsibility of `model_requests.py` is to manage interactions with the language model (LLM) using the `ollama` library. It provides functionality to send user messages to the model, maintain conversation history for contextual responses, and clean up the model's output. This file acts as an abstraction layer for LLM communication, ensuring seamless integration with the chatbot system.

---

## 2. **Analysis of Key Functions/Methods**

### **Function: `clean_response(content)`**
- **Purpose**: Cleans the model's response by removing specific blocks of text enclosed within `<think>...</think>` tags. This ensures that irrelevant or internal processing details are excluded from the final output.
- **Parameters**:
  - `content` (str): The raw response content from the LLM.
- **Returns**:
  - A cleaned version of the response (str) with `<think>` blocks removed.
- **Logic**:
  - Uses a regular expression (`re.sub`) to identify and remove all `<think>...</think>` blocks, including their content. The `flags=re.DOTALL` ensures that multiline blocks are handled correctly.

---

### **Function: `run_chat_interaction(model_name='pizzaria_gemma:latest')`**
- **Purpose**: Provides an interactive command-line interface for testing the LLM. It allows users to input messages, receive responses, and maintain conversation history for contextual replies.
- **Parameters**:
  - `model_name` (str, optional): The name of the LLM model to interact with. Defaults to `'pizzaria_gemma:latest'`.
- **Returns**:
  - None. This function runs indefinitely until the user exits.
- **Logic**:
  - Initializes an empty `messages` list to store conversation history.
  - Continuously prompts the user for input and appends their message to the history.
  - Sends the conversation history to the LLM using the `ollama.chat` function with `stream=True` to receive responses in chunks.
  - Accumulates the response chunks into `current_response_content` and appends the complete response to the history.
  - Handles exceptions gracefully, providing error messages if the LLM interaction fails.

---

### **Function: `get_llm_response(user_message: str, conversation_history=[], model_name='pizzaria_gemma:latest') -> str`**
- **Purpose**: Sends a single user message to the LLM and retrieves the model's response while maintaining conversation history for contextual replies.
- **Parameters**:
  - `user_message` (str): The message from the user to be sent to the LLM.
  - `conversation_history` (list, optional): A list of dictionaries representing the conversation history. Defaults to an empty list.
  - `model_name` (str, optional): The name of the LLM model to interact with. Defaults to `'pizzaria_gemma:latest'`.
- **Returns**:
  - The model's response (str), cleaned and stripped of unnecessary whitespace.
- **Logic**:
  - Appends the user's message to the `conversation_history`.
  - Sends the updated history to the LLM using `ollama.chat` with `stream=True` to receive responses in chunks.
  - Accumulates the response chunks into `freddy_full_response`.
  - Appends the complete response to the `conversation_history` for future contextual replies.
  - Handles exceptions gracefully, returning a user-friendly error message if the LLM interaction fails.

---

## 3. **Important or Complex Logic**

### **Streaming Responses from the LLM**
Both `run_chat_interaction` and `get_llm_response` use the `ollama.chat` function with `stream=True` to receive responses in chunks. This approach is particularly useful for handling large or real-time responses from the LLM. The logic for streaming involves:
- Iterating over the chunks returned by the `ollama.chat` function.
- Accumulating the content of each chunk into a single response string.
- Printing the chunks in real-time (in `run_chat_interaction`) for a dynamic user experience.

### **Conversation History Management**
The conversation history is maintained as a list of dictionaries, where each dictionary represents a message with the following structure:
- `{'role': 'user', 'content': <user_message>}` for user messages.
- `{'role': 'assistant', 'content': <model_response>}` for model responses.
This structure ensures that the LLM can provide contextual replies based on the entire conversation.

### **Error Handling**
Both functions include robust error handling to manage issues during LLM interaction:
- Exceptions are caught and logged with descriptive error messages.
- In `get_llm_response`, a fallback error message is returned to the user, ensuring the system remains functional even during failures.

---

## 4. **UI Interaction**
This file does not directly interact with a UI. However, `run_chat_interaction` provides a command-line interface for testing the LLM, allowing users to input messages and view responses dynamically.

---

## 5. **Backend Communication**
The file communicates with the LLM backend using the `ollama.chat` function. Key aspects of this communication include:
- **Model Name**: The `model_name` parameter specifies which LLM model to use (e.g., `'pizzaria_gemma:latest'`).
- **Conversation History**: The `messages` or `conversation_history` parameter provides context for the LLM to generate relevant responses.
- **Streaming**: The `stream=True` parameter enables real-time response streaming, which is processed chunk by chunk.

---

## Summary
`model_requests.py` is a critical component of the WhatsApp bot feature, responsible for managing LLM interactions. It provides functions for both interactive testing and programmatic response generation, ensuring seamless integration with the chatbot system. The file is well-structured, with robust error handling and efficient management of conversation history. Its use of streaming responses and regular expressions for cleaning output demonstrates thoughtful design for handling dynamic and complex LLM interactions.

---

---

## Detailed Analysis: `worker_bot.py`
> Analysis generated on: 2025-08-18 12:27:22

# Technical Analysis of `worker_bot.py`

## 1. **File's Core Responsibility**
The `worker_bot.py` file is responsible for implementing the main bot logic for monitoring WhatsApp Web, detecting incoming messages, processing them using an external language model (LLM), and responding to customers. It also handles JSON generation for specific commands and manages the browser instance for WhatsApp Web automation. The file uses PyQt5 for threading and signaling, enabling asynchronous execution and communication with other components.

---

## 2. **Analysis of Key Functions/Methods**

### **`__init__`**
- **Purpose**: Initializes the `BotWorker` class, setting up instance variables and preparing the bot for execution.
- **Parameters**: None.
- **Returns**: None.
- **Key Details**:
  - Initializes `self.running` to control the bot's execution loop.
  - Sets `self.driver` to `None` for later browser initialization.
  - Defines `self._iniciou_navegador` to track whether the browser has been started.

---

### **`run`**
- **Purpose**: Implements the main execution loop of the bot. Monitors WhatsApp Web for new notifications, processes incoming messages, and sends responses.
- **Parameters**: None (inherited from `QThread`).
- **Returns**: None.
- **Key Details**:
  - Maintains conversation history (`conversas`) and tracks the last sent/received messages for each contact.
  - Calls helper functions (`busca_notificacao`, `capturar_contato`, `capturar_mensagem`) to detect notifications and retrieve message details.
  - Sends the captured message to the LLM via `obter_resposta_llm` and processes the response.
  - Handles special commands like `GERAR_JSON` to generate JSON files and trigger specific actions.
  - Uses `enviar_mensagem` to send responses back to customers.
  - Includes error handling to ensure the bot continues running in case of exceptions.

---

### **`close_driver`**
- **Purpose**: Closes the browser instance and emits a signal indicating the browser has been shut down.
- **Parameters**: None.
- **Returns**: None.
- **Key Details**:
  - Ensures the browser instance (`self.driver`) is properly 
  - Emits a PyQt5 signal (`nova_mensagem_log`) to log the closure event.

---

### **`iniciar_navegador`**
- **Purpose**: Initializes the browser instance for WhatsApp Web automation and loads configuration data from an external API.
- **Parameters**: None.
- **Returns**: None.
- **Key Details**:
  - Fetches configuration data (e.g., notification identifiers) from the EditaCodigo API using the `requests` library.
  - Sets up the Edge WebDriver with user profile data for WhatsApp Web.
  - Loads a CSV file containing predefined messages into a Pandas DataFrame for later use.
  - Emits a signal (`nova_mensagem_log`) to indicate the browser has been started.

---

### **`start_bot_loop`**
- **Purpose**: Activates the bot's execution loop.
- **Parameters**: None.
- **Returns**: None.
- **Key Details**:
  - Sets `self.running` to `True` to enable the bot's main loop.
  - Emits a signal (`nova_mensagem_log`) to log the activation event.

---

### **`stop_bot_loop`**
- **Purpose**: Pauses the bot's execution loop.
- **Parameters**: None.
- **Returns**: None.
- **Key Details**:
  - Sets `self.running` to `False` to halt the bot's main loop.
  - Emits a signal (`nova_mensagem_log`) to log the pause event.

---

## 3. **Important or Complex Logic**

### **Main Execution Loop (`run`)**
- **Description**: The `run` method contains the core logic for detecting notifications, processing messages, and sending responses. Key steps include:
  - **Notification Detection**: Uses `busca_notificacao` to check for new messages on WhatsApp Web.
  - **Message Processing**: Captures the contact and message details using `capturar_contato` and `capturar_mensagem`. Sends the message to the LLM via `obter_resposta_llm` and processes the response.
  - **Command Handling**: If the response starts with `GERAR_JSON`, the bot generates a JSON file and triggers specific actions (e.g., emitting a signal for a new order).
  - **Error Handling**: Catches exceptions to prevent the bot from crashing and logs the error.

### **Browser Initialization (`iniciar_navegador`)**
- **Description**: This method sets up the browser instance for WhatsApp Web automation and retrieves configuration data from an external API. Key steps include:
  - **API Communication**: Fetches configuration data using the `requests` library and parses the response.
  - **WebDriver Setup**: Configures the Edge WebDriver with user profile data and starts the browser.
  - **CSV Loading**: Loads predefined messages into a Pandas DataFrame for later use.

---

## 4. **UI Interaction**
- The bot interacts with WhatsApp Web via Selenium. Key UI elements include:
  - **Notification Detection**: Uses the identifier (`self.BOLINHA_NOTIFICA`) retrieved from the API to locate notification elements on the page.
  - **Message Capture**: Extracts contact and message details using helper functions (`capturar_contato`, `capturar_mensagem`).
  - **Response Delivery**: Sends messages back to customers using the `enviar_mensagem` function.

---

## 5. **Backend Communication**
- **API Calls**:
  - The `iniciar_navegador` method fetches configuration data from the EditaCodigo API using the `requests` library. The API response is parsed to extract notification identifiers and other relevant data.
- **LLM Interaction**:
  - The `run` method sends customer messages to the LLM via the `obter_resposta_llm` function. The LLM generates responses based on the conversation history and the provided model name (`pizzaria_gemma:latest`).

---

## 6. **Threading and Signaling**
- The file uses PyQt5's `QThread` to run the bot's main loop asynchronously. This ensures the bot can monitor WhatsApp Web and process messages without blocking other operations.
- Signals (`nova_mensagem_log`, `novo_pedido`) are used to communicate events (e.g., new messages, JSON generation) to other components.

---

## 7. **Dependencies**
- **PyQt5**: Provides threading and signaling functionality.
- **Selenium**: Enables browser automation for interacting with WhatsApp Web.
- **Requests**: Used for API communication.
- **Pandas**: Handles CSV file operations.
- **OS**: Manages file paths and directories.

---

## 8. **Potential Improvements**
- **Error Handling**: Enhance exception handling to provide more detailed logs and recover from specific errors (e.g., WebDriver crashes).
- **Configuration Management**: Store API tokens and other sensitive data in environment variables or a secure configuration file.
- **Scalability**: Optimize the main loop to handle a larger number of conversations efficiently.

---

---

## Detailed Analysis: `application_bot.py`
> Analysis generated on: 2025-08-18 12:27:22

# Technical Analysis of `application_bot.py`

## 1. **File's Core Responsibility**
The primary responsibility of `application_bot.py` is to provide utility functions for interacting with WhatsApp Web via Selenium. These functions handle tasks such as detecting notifications, capturing contact and message details, sending responses, saving contacts, and processing scheduled messages. The file acts as a helper module for the main bot logic implemented in `worker_bot.py`.

---

## 2. **Analysis of Key Functions/Methods**

### **`busca_notificacao(driver, BOLINHA_NOTIFICA)`**
- **Purpose**: Detects and clicks on the most recent notification bubble in WhatsApp Web.
- **Parameters**:
  - `driver`: Selenium WebDriver instance used to interact with the browser.
  - `BOLINHA_NOTIFICA`: Class name of the notification bubble element.
- **Returns**: `True` if a notification is found and clicked; otherwise, no return value.
- **Key Logic**:
  - Uses `find_elements` to locate all notification bubbles.
  - Selects the most recent notification (`bolinha[-1]`) and clicks it using `ActionChains`.
  - Includes error handling to manage cases where no notifications are found.

---

### **`capturar_contato(driver)`**
- **Purpose**: Extracts the contact's phone number from the WhatsApp Web interface.
- **Parameters**:
  - `driver`: Selenium WebDriver instance.
- **Returns**: The phone number as a string.
- **Key Logic**:
  - Locates the contact's phone number using an XPath selector.
  - Includes a sleep delay to ensure the element is loaded.

---

### **`capturar_mensagem(driver)`**
- **Purpose**: Captures the most recent incoming message from the chat.
- **Parameters**:
  - `driver`: Selenium WebDriver instance.
- **Returns**: The text of the most recent message as a string, or `None` if no messages are found.
- **Key Logic**:
  - Waits for incoming messages using `WebDriverWait` and `EC.presence_of_all_elements_located`.
  - Extracts the text from the last message bubble using CSS selectors.

---

### **`enviar_mensagem(response, driver)`**
- **Purpose**: Sends a message to the active chat, splitting it into chunks if the message exceeds 500 characters.
- **Parameters**:
  - `response`: The message text to be sent.
  - `driver`: Selenium WebDriver instance.
- **Returns**: None.
- **Key Logic**:
  - Cleans the message using `remover_caracteres_invalidos`.
  - Splits the message into chunks of 500 characters.
  - Locates the text input field using XPath and sends each chunk sequentially.
  - Includes error handling for stale element references and other issues.

---

### **`obter_resposta(id_mensagem, df)`**
- **Purpose**: Retrieves a predefined response from a DataFrame based on a message ID.
- **Parameters**:
  - `id_mensagem`: The ID of the message to look up.
  - `df`: A Pandas DataFrame containing message IDs and responses.
- **Returns**: The corresponding response as a string, or a default message if the ID is not found.

---

### **`obter_resposta_llm(mensagem, model_name='pizzaria_gemma:latest', conversation_history=[])`**
- **Purpose**: Generates a response using the LLM based on the provided message.
- **Parameters**:
  - `mensagem`: The input message to be processed by the LLM.
  - `model_name`: The name of the LLM model (default: `'pizzaria_gemma:latest'`).
  - `conversation_history`: A list of previous messages for context.
- **Returns**: The response generated by the LLM.

---

### **`salvar_contato(numero, dir_path)`**
- **Purpose**: Saves a contact's phone number to a CSV file if it is not already present.
- **Parameters**:
  - `numero`: The phone number to save.
  - `dir_path`: The directory path where the CSV file is located.
- **Returns**: None.
- **Key Logic**:
  - Reads the existing contacts from the CSV file.
  - Checks if the number is already saved.
  - Appends the new contact with an incremental ID if it is not found.

---

### **`enviar_mensagem_numero(numero, mensagem, driver)`**
- **Purpose**: Sends a message to a specific phone number by searching for the contact in WhatsApp Web.
- **Parameters**:
  - `numero`: The phone number to send the message to.
  - `mensagem`: The message text to be sent.
  - `driver`: Selenium WebDriver instance.
- **Returns**: None.
- **Key Logic**:
  - Locates the search box and enters the phone number.
  - Opens the chat and sends the message using `enviar_mensagem`.
  - Handles the "cancel search" button to reset the search state.

---

### **`processar_agendamentos(dir_path)`**
- **Purpose**: Processes scheduled messages stored in an Excel file and sends them if the scheduled date matches the current date.
- **Parameters**:
  - `dir_path`: The directory path where the Excel file is located.
- **Returns**: None.
- **Key Logic**:
  - Reads the Excel file and converts the date column to datetime objects.
  - Iterates through the rows to check if the scheduled date matches the current date.
  - Sends the message using `enviar_mensagem_numero` and updates the "enviada" column to mark the message as sent.

---

### **`remover_caracteres_invalidos(texto)`**
- **Purpose**: Removes unsupported characters from the text to ensure compatibility with WebDriver.
- **Parameters**:
  - `texto`: The input text to clean.
- **Returns**: The cleaned text as a string.
- **Key Logic**:
  - Filters out characters outside the Basic Multilingual Plane (BMP).

---

## 3. **Important or Complex Logic**

### **Message Splitting in `enviar_mensagem`**
The function splits long messages into chunks of 500 characters to avoid errors with WhatsApp Web's text input field. It ensures each chunk is sent sequentially and handles potential issues like stale element references. This logic is critical for maintaining robust message delivery.

### **Scheduled Message Processing in `processar_agendamentos`**
The function reads an Excel file, checks the scheduled date for each message, and sends messages that are due. It updates the file to mark messages as sent, ensuring that the same message is not sent multiple times. This logic is essential for automating scheduled communication.

---

## 4. **UI Interaction**
The file interacts with WhatsApp Web's UI elements using Selenium. Examples include:
- Locating notification bubbles (`busca_notificacao`).
- Extracting contact and message details (`capturar_contato`, `capturar_mensagem`).
- Sending messages via the text input field (`enviar_mensagem`).

---

## 5. **Backend Communication**
The file communicates with the backend in the following ways:
- **LLM API**: The `obter_resposta_llm` function calls the `get_llm_response` method from `model_requests.py` to generate responses using the language model.
- **CSV/Excel Files**: Functions like `salvar_contato` and `processar_agendamentos` read and write data to local files for contact management and scheduled messaging.

---

## Summary
`application_bot.py` is a utility module that encapsulates the logic for interacting with WhatsApp Web and managing data files. It provides essential functions for notification handling, message processing, contact management, and scheduled messaging. The file is well-structured, with clear separation of concerns and robust error handling.

---