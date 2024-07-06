# Discord Bot Examples

This repository contains various examples of Discord bots, demonstrating different functionalities using Python.

## Examples

1. **ex1-hello.py**: Basic bot with a simple greeting command.
2. **ex2-periodic-message-bot.py**: Bot that sends periodic messages and responds to basic commands.
3. **ex3-bitcoin-bot.py**: Bot that provides real-time Bitcoin price updates.
4. **ex4-openai-chatbot.py**: Chatbot using OpenAI's GPT-3.5-turbo model.

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/makepluscode/discordbot-examples.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with:
   ```
   DISCORD_TOKEN=your_discord_bot_token
   CHANNEL_ID=your_discord_channel_id
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run each example independently:

```
python ex1-hello.py
```

Key commands:
- ex1: `$hello`
- ex2: `!안녕`, `!정보`
- ex3: `!start`, `!stop`
- ex4: `!chat [message]`

## Contributing

Contributions are welcome. Please fork the repository and create a pull request with your features or fixes.

## License

This project is licensed under the MIT License.

---

For questions or issues, please open an issue in the GitHub repository.
