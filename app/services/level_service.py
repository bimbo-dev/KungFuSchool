from app import app, db
from app.models import Level


def get_all_levels():
    return Level.query.filter_by(is_deleted=False).all()


def get_all_levels_by_page(page):
    return Level.query.filter_by(is_deleted=False) \
        .paginate(page, app.config['PAGE_SIZE'], False)


def get_level_by_id(levelid):
    return Level.query.get(levelid)


def save_level(level):
    if level.id != '':
        level_obj = Level.query.get(level.id)
        if level_obj is not None:
            level_obj.description = level.description
    else:
        level.id = None
        level.is_deleted = False
        db.session.add(level)
    db.session.commit()


def delete_level(levelid):
    if levelid is not None:
        level = Level.query.get(levelid)
        level.is_deleted = True
        db.session.commit()