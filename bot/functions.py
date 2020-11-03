from replit import db

async def open_account(user : str):
    if user not in db.keys():
        db[user] = '0,0'
        return True
    else:
        return False

async def save(user : str, amount : int):
    score, dc = db[user].split(',')
    amount2 = amount / 10
    db[user] = f'{int(score) +  amount},{int(dc) + int(amount2)}'
