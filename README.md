# Voice Assistant

## API Key Setup

To use certain commands (like the weather command), you need to set up API keys:

1. Copy `config/api_config_template.py` to `config/api_config.py`
2. Sign up for an account at [OpenWeatherMap](https://openweathermap.org/)
3. Get your API key from your account page
4. Replace `your_api_key_here` in `config/api_config.py` with your actual API key

Never share your `config/api_config.py` file or commit it to version control!
