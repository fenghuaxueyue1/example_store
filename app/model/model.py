import time

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class TbAddres(db.Model):
    __tablename__ = 'tb_address'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('tb_user.id'), index=True)
    country = db.Column(db.String(20), info='国家')
    province = db.Column(db.String(30), info='省份')
    city = db.Column(db.String(30), info='市')
    county = db.Column(db.String(30), info='县')
    detailed = db.Column(db.String(50), info='详细地址')
    contact_name = db.Column(db.String(20), info='联系人姓名')
    contact_phone = db.Column(db.String(11), info='联系人电话')
    sort = db.Column(db.Integer, info='排序')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    create_timestamp = db.Column(db.Integer, info='创建时间')

    user = db.relationship('TbUser', primaryjoin='TbAddres.user_id == TbUser.id', backref='tb_address')


class TbBanner(db.Model):
    __tablename__ = 'tb_banner'

    id = db.Column(db.Integer, primary_key=True)
    commodity_id = db.Column(db.ForeignKey('tb_commodity.id'), index=True, info='商品id')
    full_cover = db.Column(db.String, info='封面')
    sort = db.Column(db.Integer, info='排序')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    create_timestamp = db.Column(db.Integer, info='创建时间')

    commodity = db.relationship('TbCommodity', primaryjoin='TbBanner.commodity_id == TbCommodity.id',
                                backref='tb_banners')


class TbCategory(db.Model):
    __tablename__ = 'tb_category'

    id = db.Column(db.Integer, primary_key=True)
    named = db.Column(db.String(30), info='名称')
    cover = db.Column(db.String, info='封面')
    sort = db.Column(db.Integer, info='排序')


class TbComment(db.Model):
    __tablename__ = 'tb_comment'

    id = db.Column(db.Integer, primary_key=True)
    commodity_id = db.Column(db.ForeignKey('tb_commodity.id'), index=True, info='商品id')
    user_id = db.Column(db.ForeignKey('tb_user.id'), index=True, info='用户id')
    content = db.Column(db.String(100), info='内容')
    is_anonymity = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否匿名')
    is_show = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否显示')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    create_timestamp = db.Column(db.Integer, info='创建时间')

    commodity = db.relationship('TbCommodity', primaryjoin='TbComment.commodity_id == TbCommodity.id',
                                backref='tb_comments')
    user = db.relationship('TbUser', primaryjoin='TbComment.user_id == TbUser.id', backref='tb_comments')


class TbCommodity(db.Model):
    __tablename__ = 'tb_commodity'

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.ForeignKey('tb_category.id'), index=True, info='分类标题')
    title = db.Column(db.String(30), info='标题')
    cover = db.Column(db.Integer, info='封面')
    intro = db.Column(db.String, info='简介')
    origin_price = db.Column(db.Integer, info='原价')
    current_price = db.Column(db.Integer, info='现价')
    inventory_count = db.Column(db.Integer, info='库存')
    sort = db.Column(db.Integer, info='排序')
    is_upload = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否上架')
    is_delete = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    upload_timestamp = db.Column(db.Integer, info='上架时间')
    create_timestamp = db.Column(db.Integer, info='创建时间')
    last_update_timestamp = db.Column(db.Integer, info='修改时间')

    category = db.relationship('TbCategory', primaryjoin='TbCommodity.category_id == TbCategory.id',
                               backref='tb_commodities')


class TbCoupon(db.Model):
    __tablename__ = 'tb_coupon'

    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, info='类型0:抵扣金额 / 类型1:万分比例(10000 = 100%)')
    kind = db.Column(db.Integer, info='类型(0:抵扣卷 / 1:折扣劵)')
    valid_time = db.Column(db.Integer, info='有效时间(单位为分钟)')
    is_deleted = db.Column(db.Integer, info='是否删除')
    create_timestamp = db.Column(db.Integer, info='创建时间')


class TbFavorite(db.Model):
    __tablename__ = 'tb_favorite'

    id = db.Column(db.Integer, primary_key=True)
    commodity_id = db.Column(db.ForeignKey('tb_commodity.id'), index=True, info='商品id')
    user_id = db.Column(db.ForeignKey('tb_user.id'), index=True, info='用户id')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    join_timestamp = db.Column(db.Integer, info='加入时间')

    commodity = db.relationship('TbCommodity', primaryjoin='TbFavorite.commodity_id == TbCommodity.id',
                                backref='tb_favorites')
    user = db.relationship('TbUser', primaryjoin='TbFavorite.user_id == TbUser.id', backref='tb_favorites')


class TbOrder(db.Model):
    __tablename__ = 'tb_order'

    id = db.Column(db.Integer, primary_key=True)
    commodity_id = db.Column(db.ForeignKey('tb_commodity.id'), index=True, info='商品id')
    user_id = db.Column(db.ForeignKey('tb_user.id'), index=True, info='用户id')
    address_id = db.Column(db.ForeignKey('tb_address.id'), index=True, info='地址id')
    user_coupon_id = db.Column(db.ForeignKey('tb_user_coupon.id'), index=True, info='惠卷id')
    deal = db.Column(db.Integer, info='交易价格')
    logistics_number = db.Column(db.String(15), info='物流号码')
    stat = db.Column(db.Integer, info='状态')
    is_deleted = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='是否删除')
    create_timestamp = db.Column(db.Integer, info='创建时间')
    last_update_timestamp = db.Column(db.Integer, info='修改时间')

    address = db.relationship('TbAddres', primaryjoin='TbOrder.address_id == TbAddres.id', backref='tb_orders')
    commodity = db.relationship('TbCommodity', primaryjoin='TbOrder.commodity_id == TbCommodity.id',
                                backref='tb_orders')
    user_coupon = db.relationship('TbUserCoupon', primaryjoin='TbOrder.user_coupon_id == TbUserCoupon.id',
                                  backref='tb_orders')
    user = db.relationship('TbUser', primaryjoin='TbOrder.user_id == TbUser.id', backref='tb_orders')


class TbShopping(db.Model):
    __tablename__ = 'tb_shopping'

    id = db.Column(db.Integer, primary_key=True)
    commodity_id = db.Column(db.ForeignKey('tb_commodity.id'), index=True, info='商品id')
    user_id = db.Column(db.ForeignKey('tb_user.id'), index=True, info='用户id')
    number = db.Column(db.Integer, info='数量')
    join_timestamp = db.Column(db.Integer, info='加入时间')

    commodity = db.relationship('TbCommodity', primaryjoin='TbShopping.commodity_id == TbCommodity.id',
                                backref='tb_shoppings')
    user = db.relationship('TbUser', primaryjoin='TbShopping.user_id == TbUser.id', backref='tb_shoppings')


class TbTrack(db.Model):
    __tablename__ = 'tb_track'

    id = db.Column(db.Integer, primary_key=True)
    commodity_id = db.Column(db.ForeignKey('tb_commodity.id'), index=True, info='商品id')
    user_id = db.Column(db.ForeignKey('tb_user.id'), index=True, info='用户id')
    join_timestamp = db.Column(db.Integer, info='加入时间')

    commodity = db.relationship('TbCommodity', primaryjoin='TbTrack.commodity_id == TbCommodity.id',
                                backref='tb_tracks')
    user = db.relationship('TbUser', primaryjoin='TbTrack.user_id == TbUser.id', backref='tb_tracks')


class TbUser(db.Model):
    __tablename__ = 'tb_user'

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), info='昵称')
    portrait = db.Column(db.String, info='头像')
    gender = db.Column(db.String(2), nullable=False, server_default=db.FetchedValue(), info='性别')
    email = db.Column(db.String(50), info='邮箱')
    create_timestamp = db.Column(db.Integer, info='创建时间')

    def __init__(self, email):
        self.email = email
        self.create_timestamp = time.time().__int__()


class TbUserCoupon(db.Model):
    __tablename__ = 'tb_user_coupon'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('tb_user.id'), index=True, info='用户id')
    coupon_id = db.Column(db.ForeignKey('tb_coupon.id'), index=True, info='惠卷id')
    is_used = db.Column(db.Integer, info='是否已使用')
    join_timestamp = db.Column(db.Integer, info='加入时间')

    coupon = db.relationship('TbCoupon', primaryjoin='TbUserCoupon.coupon_id == TbCoupon.id', backref='tb_user_coupons')
    user = db.relationship('TbUser', primaryjoin='TbUserCoupon.user_id == TbUser.id', backref='tb_user_coupons')
