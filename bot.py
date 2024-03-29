import json
import cv2
import numpy as np
import pyautogui
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

template_path = "cookie.png"  # ім'я файлу з зображенням, що ми намагаємось знайти


def capture_screen():
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_rgb = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)
    return screen_rgb


def find_image_on_screen(template_path):
    screen_rgb = capture_screen()
    screen_gray = cv2.cvtColor(screen_rgb, cv2.COLOR_BGR2GRAY)  # Convert screenshot to grayscale
    template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)

    if template is None:
        print(f"Не знайдено: {template_path}")
        return None
    if template.shape[-1] == 4:  # Check if template has an alpha channel
        template = cv2.cvtColor(template, cv2.COLOR_BGRA2BGR)

    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)  # Convert template to grayscale
    res = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    return loc


def click_on_image_position_times(loc, number):
    if loc and loc[0].size:
        point = (loc[1][0], loc[0][0])
        for _ in range(number):
            pyautogui.click(point)


def is_user_registered(user_id: int) -> bool:
    try:
        with open("users.json", "r") as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = {}
        return str(user_id) in users
    except FileNotFoundError:
        return False


def register_user(user_id: int):
    try:
        with open("users.json", "r") as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = {}
    except FileNotFoundError:
        users = {}
    users[str(user_id)] = {"registered": True}
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if not is_user_registered(user_id):

        register_user(user_id)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Привіт! За допомогою цього бота ви можете знайти зображення на вашому екрані, якщо воно там є."
        )
    else:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="З поверненням! Хочете ще поклікати?"
        )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = str(update.message.text).lower().strip("!,./@#$%^&*()")
    user_id = update.effective_user.id

    if is_user_registered(user_id) and "знайди" in user_message and "печиво" in user_message:
        loc = find_image_on_screen(template_path)
        if loc and loc[0].size:
            await update.message.reply_text("Печиво знайдено! Скільки разів ви хочете на нього клікнути? Введіть цифру:")
            context.user_data['loc'] = loc  # Store location in user_data for follow-up
        else:
            await update.message.reply_text("Печиво не знайдено на екрані :(")
    elif 'loc' in context.user_data:
        try:
            times_to_click = int(user_message)
            click_on_image_position_times(context.user_data['loc'], times_to_click)
            await update.message.reply_text(f"Натиснули на печиво {times_to_click} раз!")
            del context.user_data['loc']  # Clear the stored location after clicking
        except ValueError:
            await update.message.reply_text("Будь ласка, введіть ціле число, або вірну команду.")


# Main function setup remains largely the same...
def main() -> None:
    TOKEN = ""  # Use your actual token here

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == '__main__':
    main()
