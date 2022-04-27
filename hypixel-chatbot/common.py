import datetime

from discord import Embed
from discord.colour import Color

TOKEN = "OTYxNTQ5MTE5OTc1OTk3NDYy.Yk6mZg.yR1lBK_Rh0iS4_BZ6rGtIBQSv4A"  # Discord Bot token — https://discord.com/developers
API_KEY = "47d3cb53-6674-4652-9d19-bbc73e3b989b"  # Hypixel Public API key — /api new on the Hypixel Network @ https://hypixel.net/
DATABASE_PATH = "database/database.db"

# Colors
REGULAR_COLOR = Color.gold()
SUCCESS_COLOR = Color.green()
ERROR_COLOR = Color.red()

COMMAND_PREFIX = "!"
ACTIVITY_STATUS = f"{COMMAND_PREFIX}help"

ERROR_MESSAGE = "❌ Ошибка!"

WAIT_TITLE = "🚀 Загрузка…"
WAIT_MESSAGE = "Это может занять некоторое время"
LOADING_EMBED = Embed(
    title=WAIT_TITLE,
    description=WAIT_MESSAGE,
    color=REGULAR_COLOR,
)


def get_current_month_and_year() -> tuple:
    """Возвращает текущий месяц и год"""
    current_date = datetime.date.today()
    month = current_date.month
    year = current_date.year

    return month, year


def num_to_month(num: int):
    """Возвращает название месяца по его числу"""
    month_name = {
        1: "Январь",
        2: "Февраль",
        3: "Март",
        4: "Апрель",
        5: "Май",
        6: "Июнь",
        7: "Июль",
        8: "Август",
        9: "Сентябрь",
        10: "Октябрь",
        11: "Ноябрь",
        12: "Декабрь",
    }
    return month_name[num]
