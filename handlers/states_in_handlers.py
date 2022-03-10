from aiogram.dispatcher.filters.state import StatesGroup, State


class TodoHandlerState(StatesGroup):
	"""
	For todo_handl
	"""
	todo = State()
	reception_todo = State()


class PasswordHandlerState(StatesGroup):
	"""
	For storing_passwords_handl
	"""
	check_personal_code = State()
	successful_auth_for_pass = State()
	set_name_pass = State()


class UserSettingHandlerState(StatesGroup):
	"""
	For:
		user_settings
		day_todo_notification
		weather_status_handl
		changing_stikerpack_handl
		start_handl
	"""
	settings = State()
	time_todo = State()
	weather_on = State()


