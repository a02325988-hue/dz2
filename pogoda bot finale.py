import asyncio
import logging
import aiohttp
from datetime import datetime
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command
logging.basicConfig(level=logging.INFO)
TOKEN = "8547347500:AAG_qhIAS57ktwoFbt5qjyMNX87jQdAMYCo"
API_KEY = "af43db2a62b9c249b30b545fffc9f8d0"
bot = Bot(token=TOKEN)
dp = Dispatcher()
user_settings = {}
WEEKDAYS = {
    "Monday": "Понеділок", "Tuesday": "Вівторок", "Wednesday": "Середа",
    "Thursday": "Четвер", "Friday": "П'ятниця", "Saturday": "Субота", "Sunday": "Неділя"
}
COUNTRIES = {
    "ukraine": {
        "label": "🇺🇦 Україна",
        "cities": {
            "Dnipro": "Дніпро", "Kyiv": "Київ", "Lviv": "Львів",
            "Zaporizhzhia": "Запоріжжя", "Odesa": "Одеса", "Kharkiv": "Харків"
        }
    },
    "poland": {
        "label": "🇵🇱 Польща",
        "cities": {"Warsaw": "Варшава", "Krakow": "Краків", "Wroclaw": "Вроцлав"}
    }
}
def get_main_menu(user_id):
    buttons = [[InlineKeyboardButton(text="🌍 Обрати країну", callback_data="start_choice")]]
    if user_id in user_settings:
        settings = user_settings[user_id]
        city_ua = settings['ua']
        buttons.insert(0, [InlineKeyboardButton(text=f"🏠 Мій прогноз: {city_ua}",
                                                callback_data=f"select_{settings['en']}_{city_ua}")])
        notif_text = "🔔 Сповіщення: Увімкнено" if settings.get('notifications') else "🔕 Сповіщення: Вимкнено"
        buttons.append([InlineKeyboardButton(text=notif_text, callback_data="toggle_notifications")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
def get_countries_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇺🇦 Україна", callback_data="country_ukraine")],
        [InlineKeyboardButton(text="🇵🇱 Польща", callback_data="country_poland")],
        [InlineKeyboardButton(text="⬅️ В меню", callback_data="back_to_main")]
    ])
def get_cities_keyboard(country_code):
    cities = COUNTRIES[country_code]["cities"]
    inline_kb = []
    temp_row = []
    for en, ua in cities.items():
        temp_row.append(InlineKeyboardButton(text=ua, callback_data=f"select_{en}_{ua}"))
        if len(temp_row) == 2:
            inline_kb.append(temp_row)
            temp_row = []
    if temp_row: inline_kb.append(temp_row)
    inline_kb.append([InlineKeyboardButton(text="⬅️ Назад", callback_data="start_choice")])
    return InlineKeyboardMarkup(inline_keyboard=inline_kb)
def get_type_keyboard(user_id, city_en, city_ua):
    buttons = [
        [InlineKeyboardButton(text="☀️ На сьогодні", callback_data=f"weather_today_{city_en}_{city_ua}")],
        [InlineKeyboardButton(text="📅 На 5 днів", callback_data=f"weather_5days_{city_en}_{city_ua}")]
    ]
    if user_id in user_settings and user_settings[user_id]['en'] == city_en:
        buttons.append([InlineKeyboardButton(text="❌ Видалити з обраного", callback_data="remove_favorite")])
    else:
        buttons.append(
            [InlineKeyboardButton(text="📌 Зберегти як моє місто", callback_data=f"save_{city_en}_{city_ua}")])
    buttons.append([InlineKeyboardButton(text="⬅️ Змінити місто", callback_data="start_choice")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
async def get_weather_report(city_en, city_ua, mode="today"):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_en}&appid={API_KEY}&units=metric&lang=ua"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=10) as response:
                if response.status != 200: return "❌ Помилка API."
                data = await response.json()
                forecast_list = data["list"]
                daily_data = {}
                days_order = []
                for item in forecast_list:
                    dt_obj = datetime.fromtimestamp(item["dt"])
                    day_name = WEEKDAYS.get(dt_obj.strftime("%A"), dt_obj.strftime("%A"))
                    date_key = dt_obj.strftime(f"%d.%m ({day_name})")
                    if date_key not in daily_data:
                        daily_data[date_key] = {"temps": [], "lines": []}
                        days_order.append(date_key)
                    temp = item["main"]["temp"]
                    daily_data[date_key]["temps"].append(temp)
                    line = f"• {dt_obj.strftime('%H:%M')} | {round(temp)}°C | {item['weather'][0]['description']}"
                    daily_data[date_key]["lines"].append(line)
                report = f"📍 **{city_ua}**\n"
                display_days = days_order[:1] if mode == "today" else days_order
                for date_key in display_days:
                    avg_temp = round(sum(daily_data[date_key]["temps"]) / len(daily_data[date_key]["temps"]), 1)
                    report += f"\n📅 __**{date_key}**__\n📊 *Середня t°: {avg_temp}°C*\n"
                    report += "\n".join(daily_data[date_key]["lines"]) + "\n"
                return report
        except Exception:
            return "⚠️ Помилка з'єднання."
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Вітаю у боті погоди!", reply_markup=get_main_menu(message.from_user.id))
@dp.callback_query(F.data == "start_choice")
async def start_choice(callback: CallbackQuery):
    await callback.message.edit_text("Оберіть країну:", reply_markup=get_countries_keyboard())
@dp.callback_query(F.data == "back_to_main")
async def back_main(callback: CallbackQuery):
    await callback.message.edit_text("Головне меню:", reply_markup=get_main_menu(callback.from_user.id))
@dp.callback_query(F.data.startswith("country_"))
async def select_country(callback: CallbackQuery):
    code = callback.data.split("_")[1]
    await callback.message.edit_text(f"Міста ({COUNTRIES[code]['label']}):", reply_markup=get_cities_keyboard(code))
@dp.callback_query(F.data.startswith("select_"))
async def select_type(callback: CallbackQuery):
    _, city_en, city_ua = callback.data.split("_")
    await callback.message.edit_text(f"Обрано {city_ua}:",
                                     reply_markup=get_type_keyboard(callback.from_user.id, city_en, city_ua))
@dp.callback_query(F.data.startswith("save_"))
async def save_city(callback: CallbackQuery):
    _, city_en, city_ua = callback.data.split("_")
    user_settings[callback.from_user.id] = {'en': city_en, 'ua': city_ua, 'notifications': False}
    await callback.answer(f"✅ {city_ua} тепер у обраному!", show_alert=True)
    await callback.message.edit_text("Місто збережено.", reply_markup=get_main_menu(callback.from_user.id))
@dp.callback_query(F.data == "remove_favorite")
async def remove_favorite(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id in user_settings:
        del user_settings[user_id]
    await callback.answer("❌ Місто видалено з обраного", show_alert=True)
    await callback.message.edit_text("Обране очищено.", reply_markup=get_main_menu(user_id))
@dp.callback_query(F.data == "toggle_notifications")
async def toggle_notif(callback: CallbackQuery):
    user_id = callback.from_user.id
    if user_id in user_settings:
        current = user_settings[user_id].get('notifications', False)
        user_settings[user_id]['notifications'] = not current
        status = "увімкнено" if not current else "вимкнено"
        await callback.answer(f"Сповіщення {status}")
        await callback.message.edit_reply_markup(reply_markup=get_main_menu(user_id))
@dp.callback_query(F.data.startswith("weather_"))
async def show_weather(callback: CallbackQuery):
    mode, city_en, city_ua = callback.data.split("_")[1:4]
    await callback.message.edit_text(f"📑 Завантаження {city_ua}...")
    result = await get_weather_report(city_en, city_ua, mode)
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text="⬅️ На головну", callback_data="back_to_main")]])
    await callback.message.answer(result, parse_mode="Markdown", reply_markup=kb)
    await callback.answer()
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())


