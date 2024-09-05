from datetime import date, datetime

def get_date():
    today = date.today()

    formatted_today = today.strftime("%Y년 %m월 %d일")
    weekday_name = today.strftime('%A')

    weekday_map = {
        'Monday': '월요일',
        'Tuesday': '화요일',
        'Wednesday': '수요일',
        'Thursday': '목요일',
        'Friday': '금요일',
        'Saturday': '토요일',
        'Sunday': '일요일'
    }

    korean_weekday_name = weekday_map[weekday_name]
    return formatted_today, korean_weekday_name

def get_current_date_parsing_assistant():
    today, weekday = get_date()
    return f"오늘 날짜: {today}, 오늘 요일: {weekday}"