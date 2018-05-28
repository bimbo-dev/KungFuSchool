from app import app, db
from app.models import Rank


def get_all_ranks():
    return Rank.query.filter_by(is_deleted=False).all()


def get_all_ranks_by_page(page):
    return Rank.query.filter_by(is_deleted=False) \
        .paginate(page, app.config['PAGE_SIZE'], False)


def get_rank_by_id(id):
    return Rank.query.get(id)


def save_rank(rank):
    if rank.id != '':
        rank_obj = Rank.query.get(rank.id)
        if rank_obj is not None:
            rank_obj.belt_colour = rank.belt_colour
    else:
        rank.id = None
        rank.is_deleted = False
        db.session.add(rank)
    db.session.commit()


def delete_rank(rankid):
    if rankid is not None:
        rank = Rank.query.get(rankid)
        rank.is_deleted = True
        db.session.commit()