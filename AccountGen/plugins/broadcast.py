@BotzHub.on(events.NewMessage(pattern="^/broadcast"))
async def reset(event):
    if event.sender_id != Config.OWNER_ID:
        return
    error = 0
    ds = event.text.split(" ", maxsplit=1)[1]
    ok = get_all_users()
    if not ok:
        await event.reply("Wut? No Users In Your Bot, But U Want To Broadcast. WTF")
        return
    for s in ok:
        try:
            await warnerstarkbot.send_message(int(s['user']), ds)
        except:
            error += 1
            pass
    await event.reply(f"Broadcast Done With {error} And Sucess in {len(ok) - error}!")    
        
async def clear_data():
    ok = get_all_users()
    if not ok:
        return
    for s in ok:
        try:
            await warnerstarkbot.send_message(int(s['user']), "**Limit Has Been Reset , Generate Your Accounts Now !**")
        except:
            error += 1
            pass
    dl_all_users()
