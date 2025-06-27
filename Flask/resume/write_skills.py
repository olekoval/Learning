
from cv import app, db, Skill

with app.app_context():  # ← ОЦЕ обов'язково
    """
    Чому треба with app.app_context():
    Flask SQLAlchemy використовує так званий "application context" для того, щоб знати:
    який саме застосунок (app) зараз активний
    які в нього налаштування (config)
    до якої БД підключатись
    Без контексту — все валиться з помилкою RuntimeError: Working outside of application context.
    """
    with open ('./data/skills.csv', 'r', encoding='utf-8') as file:
        raw = [line.strip() for line in file]

    name = [i.split(';')[0] for i in raw]
    description = [i.split(';')[1] for i in raw]

    for i in range(len(name)):
        skill = Skill(
            name=name[i],
            description=description[i]
            )
        db.session.add(skill)

    db.session.commit()    
