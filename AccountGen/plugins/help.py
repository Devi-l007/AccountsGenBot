#    AccountsGenBot
#    Copyright (C) 2021 xditya

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    See < https://github.com/xditya/AccountsGenBot/blob/master/LICENSE > 
#    for the license.

from . import *

@BotzHub.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="I am an Netflix Generator Bot!\nI generate working accounts for you.\n\nClick generate accounts to get your account!! Make sure to join my channel and support us!"
    await event.edit(text,
                     buttons=[
                         [Button.url("Channel", url=ltc)],
                         [Button.inline("Generate Accounts", data="gen")]
                     ])
