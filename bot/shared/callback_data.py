from aiogram.utils.callback_data import CallbackData

callback_product = CallbackData("callback_product", "id", "action")

callback_auth = CallbackData("callback_auth", "action")

callback_select_product = CallbackData("select_product")

callback_delete_item = CallbackData("callback_delete", "product_id")

callback_payment = CallbackData("callback_payment", "answer")
