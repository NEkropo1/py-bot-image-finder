## Interactive Image Finder Bot

Welcome to our Interactive Image Finder Bot tutorial!  
This simple project is designed to introduce you to the fun world of programming by creating a Telegram bot  
that can find images on your screen and interact with them.  
### What You Will Learn:

    1. Basics of Python programming
    2. How to use Telegram bots for interactive applications
    3. Basics of image processing with OpenCV
    4. Automating desktop actions with PyAutoGUI

### Prerequisites

    1. Basic understanding of how to use a computer
    2. Telegram account and app installed on your device

### Setup  
**Step 1: Install Required Software**

- **Python**: Make sure you have Python installed on your computer. You can download it from: 
  [python.org](https://www.python.org/downloads/)
 
- **Telegram Bot**: Create a Telegram bot using BotFather on the Telegram app and get your bot's token.
  [BotFather](https://t.me/botfather)

**Step 2: Install Necessary Python Libraries**

Open your command line or terminal and run the following command to install the libraries needed for this project:  
```bash
pip install python-telegram-bot opencv-python numpy pyautogui
```

**Step 3: Prepare Your Project**

    Download the project code to your computer.
    Replace the placeholder TOKEN = "" in the script with your Telegram bot's token.

### How It Works

Our bot can find a specific image (like a cookie) on your screen. If it finds the image, you can tell the bot how many times to 'click' on it.   
This is a simple way to automate repetitive tasks or just have fun seeing what you can do with programming!  

**Running the Bot**

    Open a command line or terminal.
    Navigate to the folder where you saved the project.
    Run the script:
 ```bash
 python bot.py
```
### Interacting with the Bot

    Start the bot: Send /start to your bot in Telegram.
    Find and click: To find an image, send "знайди печиво" (find the cookie).   
    If the bot finds the image, respond with how many times you want to click it (like: `20`).

### Troubleshooting

    Bot doesn't respond: Make sure you've entered your bot token correctly and that the bot is running on your computer.
    Image not found: Ensure the image cookie.png is in the same directory as your script  
    and matches the image you want to find on your screen.


### Congratulations!  
You've just made your first steps into programming by creating a bot that interacts with images on your screen.  
The world of programming is vast and full of possibilities.   
**We encourage you to keep learning and exploring!**

### Contributions and Feedback

We love to collaborate and learn from our users!   
If you have any feedback, questions, or suggestions for new features, please feel free to contact me via [TG](https://t.me/NEkropolicia):

### License

This project is released under the MIT [License](https://github.com/NEkropo1/py-bot-image-finder/blob/main/LICENSE). See the LICENSE file for more details.
