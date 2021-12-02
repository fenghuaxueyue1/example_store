# 示例电商开发文档


|版本|注释|时间|
|---|---|---|
|v_0.1|数据库初始设计|2021/11/24 13:00:00|
||接口框架设计|2021/11/25 00:30:00|
||tb_user.phone改为email|2021/11/25 12:30:00|
||||
||||



##  数据库设计
***数据库名称: db_example_store***



### 约定

- 金额字段以分为单位存入

---



### 用户表 tb_user

| 字段名称         | 字段类型 | 字段注释                   |
| ---------------- | -------- | -------------------------- |
| id               | Integer  |                            |
| nickname         | varchar  | 昵称                       |
| portrait         | longtext | 头像                       |
| gender           | integer  | 性别(Null: 保密/0:女/1:男) |
| email            | varchar  | 邮箱                       |
| create_timestamp | Integer  | 创建时间                   |

---



### 身份表 tb_identity

| 字段名称       | 字段类型 | 字段注释   |
| -------------- | -------- | ---------- |
| user_id        | integer |            |
| id_crad_name   | varchar | 身份证姓名 |
| id_crad_number | char | 身份证号码 |
| create_timestamp | Integer | 创建时间 |

---



### 地址表 tb_address

| 字段名称      | 字段类型 | 字段注释   |
| ------------- | -------- | ---------- |
| id            | integer |            |
| user_id       | integer |            |
| country       | varchar | 国家       |
| province      | varchar | 省份       |
| city          | varchar | 市         |
| county        | varchar | 县         |
| detailed      | varchar | 详细地址   |
| contact_name  | varchar | 联系人姓名 |
| contact_phone | char | 联系人手机 |
| sort       | Integer | 排序   |
| is_deleted    | int(0=否,1=是) | 是否删除   |
| create_timestamp | Integer | 创建时间 |

---



### 分类表 tb_category

| 字段名称 | 字段类型 | 字段注释 |
| -------- | -------- | -------- |
| id       | integer |          |
| named    | varchar | 名称     |
| cover    | longtext | 封面     |
| sort        | Integer | 排序 |

---



### 商品表 tb_commodity

| 字段名称         | 字段类型 | 字段注释 |
| ---------------- | -------- | -------- |
| id               | integer |          |
| category_id      | integer | 分类ID |
| title            | vachar | 标题     |
| covor            | longtext | 封面     |
| intro            | longtext | 简介     |
| origin_price     | Integer        | 原价     |
| current_price    | Integer        | 现价 |
| inventory_count | integer | 库存  |
| sort        | Integer | 排序 |
| is_upload        | int(0=否,1=是) | 是否上架 |
| is_deleted    | int(0=否,1=是) | 是否删除   |
| upload_timestamp | Integer | 上架时间 |
| create_timestamp | Integer | 创建时间 |
| last_update_timestamp | Integer | 修改时间 |

---



### 选购表 tb_shopping

| 字段名称       | 字段类型 | 字段注释 |      |
| -------------- | -------- | -------- | ---- |
| id             | integer  |          |      |
| commodity_id   | integer  | 商品id   |      |
| user_id        | integer  | 用户id   |      |
| number         | integer  | 数量     |      |
| join_timestamp | Integer  | 加入时间 |      |

---


### 收藏表 tb_favorite

| 字段名称       | 字段类型 | 字段注释 |
| -------------- | -------- | -------- |
| id               | integer |          |
| commodity_id   | integer | 商品id   |
| user_id        | integer | 用户id   |
| is_deleted    | int(0=否,1=是) | 是否删除   |
| join_timestamp | integer | 加入时间 |



### 惠卷表 tb_coupon

| 字段名称       | 字段类型 | 字段注释 |
| ---------------- | -------- | -------- |
| id               | integer |          |
| num | Integer | 类型0:抵扣金额 / 类型1:万分比例(10000 = 100%) |
| kind | Integer | 类型(0:抵扣卷 / 1:折扣劵) |
| valid_time | Integer | 有效时间(单位为分钟) |
| is_deleted    | int(0=否,1=是) | 是否删除   |
| create_timestamp | Integer | 创建时间 |

---



### 用户惠卷表 tb_user_coupon

| 字段名称       | 字段类型 | 字段注释 |
| ---------------- | -------- | -------- |
| id               | integer |          |
| user_id |integer|用户id|
| coupon_id |integer|惠卷id|
| is_used|integer|是否已使用|
| join_timestamp | Integer | 加入时间 |

---



### 订单表 tb_order

| 字段名称         | 字段类型 | 字段注释 |
| ---------------- | -------- | -------- |
| id               | integer |          |
| commodity_id |integer|商品id|
| user_id |integer|用户id|
| address_id |integer|地址id|
| user_coupon_id|integer|惠卷id|
| deal                  | Integer        |交易价格|
| logistics_number | varchar        |物流号码|
| state |Integer|状态|
| is_deleted    | int(0=否,1=是) | 是否删除   |
| create_timestamp | Integer | 创建时间 |
| last_update_timestamp | Integer | 修改时间 |

---



### 评论表 tb_comment

| 字段名称         | 字段类型 | 字段注释 |
| ---------------- | -------- | -------- |
| id               | integer |          |
| commodity_id |integer|商品id|
| user_id |integer|用户id|
| content|string|内容|
|is_anonymity| int(0=否,1=是) |是否匿名|
| is_show| int(0=否,1=是) |是否显示|
| is_deleted    | int(0=否,1=是) | 是否删除   |
| create_timestamp | Integer | 创建时间 |

---



### 横幅表 tb_banner

| 字段名称         | 字段类型 | 字段注释 |
| ---------------- | -------- | -------- |
| id               | integer |          |
| commodity_id |integer|商品id|
| full_cover |longtext|封面|
| sort        | Integer | 排序 |
| is_deleted    | int(0=否,1=是) | 是否删除   |
| create_timestamp | Integer | 创建时间 |

---



### 足迹表 tb_track

| 字段名称         | 字段类型 | 字段注释 |
| ---------------- | -------- | -------- |
| id               | integer |          |
| commodity_id |integer|商品id|
| user_id |integer|用户id|
| join_timestamp | Integer | 加入时间 |

---



### 建表SQL

```sql
CREATE DATABASE IF NOT EXISTS db_example_store;

-- 展示现有的数据库,查看是否创建成功
SHOW DATABASES; 

-- 创建一个tb_user 用户表
CREATE TABLE IF NOT EXISTS tb_user (
											id INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
											nickname VARCHAR(20)  COMMENT'昵称',
											portrait LONGTEXT COMMENT'头像',
											gender CHAR(2) DEFAULT'保密' NOT NULL COMMENT'性别',
											email VARCHAR(50) COMMENT'邮箱',
											create_timestamp INTEGER COMMENT'创建时间'
);

-- 创建一个tb_identity 身份表
CREATE TABLE IF NOT EXISTS tb_identity (
													user_id INTEGER UNSIGNED,
													id_crad_name VARCHAR(20) COMMENT'身份证姓名',
													id_crad_number CHAR(18) COMMENT'身份证号码',
													create_timestamp INTEGER COMMENT'创建时间',
constraint fk_user_identity foreign key (user_id) references tb_user(id)
);

-- 创建一个tb_address 地址表
CREATE TABLE IF NOT EXISTS tb_address(
												id INTEGER UNSIGNED PRIMARY KEY,
												user_id INTEGER UNSIGNED,
												country VARCHAR(20) COMMENT'国家',
												province VARCHAR(30) COMMENT'省份',
												city VARCHAR(30) COMMENT'市',
												county VARCHAR(30) COMMENT'县',
												detailed VARCHAR(50) COMMENT'详细地址',
												contact_name VARCHAR(20) COMMENT'联系人姓名',
												contatc_phone char(11) COMMENT'联系人电话',
												sort INTEGER COMMENT'排序',
												is_deleted INT NOT NULL DEFAULT'0' COMMENT '是否删除',
												create_timestamp INTEGER COMMENT'创建时间',
CONSTRAINT fk_user_address FOREIGN KEY (user_id) REFERENCES tb_user(id)
);

-- 创建一个tb_category分类表
CREATE TABLE IF NOT EXISTS tb_category(
												 id INTEGER UNSIGNED PRIMARY KEY,
												 named VARCHAR(30) COMMENT'名称',
												 cover LONGTEXT COMMENT'封面',
												 sort INTEGER COMMENT'排序'
);

-- 创建一个tb_commodity商品表
CREATE TABLE IF NOT EXISTS tb_commodity(
													id INTEGER UNSIGNED PRIMARY KEY,
													category_id INTEGER UNSIGNED COMMENT'分类标题',
													title VARCHAR(30) COMMENT'标题',
													covor INTEGER COMMENT'封面',
													intro LONGTEXT COMMENT'简介',
													origin_price INTEGER COMMENT'原价',
													current_price INTEGER COMMENT'现价',
													inventory_count INTEGER COMMENT'库存',
													sort INTEGER COMMENT'排序',
													is_uplad INT NOT NULL DEFAULT'0' COMMENT'是否上架',
													is_delete INT NOT NULL DEFAULT'0' COMMENT'是否删除',
													upload_timestamp INTEGER COMMENT'上架时间',
													create_timestamp INTEGER COMMENT'创建时间',
													last_update_timestamp INTEGER COMMENT'修改时间',
CONSTRAINT fk_category_commodity FOREIGN KEY (category_id) REFERENCES tb_category(id)
);

-- 创建一个tb_shopping选购表
CREATE TABLE IF NOT EXISTS tb_shopping (
													id INTEGER UNSIGNED PRIMARY KEY,
													commodidy_id INTEGER UNSIGNED COMMENT'商品id',
													user_id INTEGER UNSIGNED COMMENT'用户id',
													number INTEGER COMMENT'数量',
													join_timestamp INTEGER COMMENT'加入时间',
CONSTRAINT fk_user_shopping FOREIGN KEY (user_id) REFERENCES tb_user(id),
CONSTRAINT fk_commodity_shopping FOREIGN KEY (commodidy_id) REFERENCES tb_commodity(id)
);

-- 创建一个tb_favorite收藏表
CREATE TABLE IF NOT EXISTS tb_favorite(
												 id INTEGER UNSIGNED PRIMARY KEY,
												 commodity_id INTEGER UNSIGNED COMMENT'商品id',
												 user_id INTEGER UNSIGNED COMMENT'用户id',
												 is_deleted INT NOT NULL DEFAULT'0' COMMENT'是否删除',
												 join_timestamp INTEGER COMMENT'加入时间',
CONSTRAINT fk_commodity_favorite FOREIGN KEY (commodity_id) REFERENCES tb_commodity(id),
CONSTRAINT fk_user_favorite FOREIGN KEY (user_id) REFERENCES tb_user(id) 										 
);

-- 创建一个tb_coupon惠卷表
CREATE TABLE IF NOT EXISTS tb_coupon(
											 id INTEGER UNSIGNED PRIMARY KEY,
											 num INTEGER COMMENT'类型0:抵扣金额 / 类型1:万分比例(10000 = 100%)',
											 kind INTEGER COMMENT'类型(0:抵扣卷 / 1:折扣劵)',
											 valid_time INTEGER COMMENT'有效时间(单位为分钟)',
											 is_deleted INTEGER COMMENT'是否删除',
											 create_timestamp INTEGER COMMENT'创建时间'
);

-- 创建一个tb_user_coupon用户惠卷表
CREATE TABLE IF NOT EXISTS tb_user_coupon(
														id INTEGER UNSIGNED PRIMARY KEY,
														user_id INTEGER UNSIGNED COMMENT'用户id',
														coupon_id INTEGER UNSIGNED COMMENT'惠卷id',
														is_used INTEGER COMMENT'是否已使用',
														join_timestamp INTEGER COMMENT'加入时间',
CONSTRAINT fk_user_user_coupon FOREIGN KEY (user_id) REFERENCES	tb_user(id),
CONSTRAINT fk_coupon_user_coupon FOREIGN KEY (coupon_id) REFERENCES tb_coupon(id)
);

-- 创建一个tb_order订单表
CREATE TABLE IF NOT EXISTS tb_order(
											id INTEGER UNSIGNED PRIMARY KEY,
											commodity_id INTEGER UNSIGNED COMMENT'商品id',
											user_id INTEGER UNSIGNED COMMENT'用户id',
											address_id INTEGER UNSIGNED COMMENT'地址id',
											user_coupon_id INTEGER UNSIGNED COMMENT'惠卷id',
											deal INTEGER COMMENT'交易价格',
											logistics_number CHAR(15) COMMENT'物流号码',
											stat INTEGER COMMENT'状态',
											is_deleted INT NOT NULL DEFAULT'0' COMMENT'是否删除',
											create_timestamp INTEGER COMMENT'创建时间',
											last_update_timestamp INTEGER COMMENT'修改时间',
CONSTRAINT fk_commodity_order FOREIGN KEY (commodity_id) REFERENCES tb_commodity(id),
CONSTRAINT fk_user_order FOREIGN KEY (user_id) REFERENCES tb_user(id),
CONSTRAINT fk_address_order FOREIGN KEY (address_id) REFERENCES tb_address(id),
CONSTRAINT fk_user_coupon_order FOREIGN KEY (user_coupon_id) REFERENCES tb_user_coupon(id)
);

-- 创建一个tb_comment评论表
CREATE TABLE IF NOT EXISTS tb_comment(
												id INTEGER UNSIGNED PRIMARY KEY,
												commodity_id INTEGER UNSIGNED UNSIGNED COMMENT'商品id',
												user_id INTEGER UNSIGNED COMMENT'用户id',
												content VARCHAR(100) COMMENT'内容',
												is_anonymity INT NOT NULL DEFAULT'0' COMMENT'是否匿名',
												is_show INT NOT NULL DEFAULT'0' COMMENT'是否显示',
												is_deleted INT NOT NULL DEFAULT'0' COMMENT'是否删除',
												create_timestamp INTEGER COMMENT'创建时间',
CONSTRAINT fk_commodity_comment FOREIGN KEY (commodity_id) REFERENCES tb_commodity(id),
CONSTRAINT fk_user_comment FOREIGN KEY (user_id) REFERENCES tb_user(id)
);

-- 创建一个tb_banner横幅表
CREATE TABLE IF NOT EXISTS tb_banner (
												id INTEGER UNSIGNED PRIMARY KEY,
												commodity_id INTEGER UNSIGNED COMMENT'商品id',
												full_cover LONGTEXT COMMENT'封面',
												sort INTEGER COMMENT'排序',
												is_deleted INT NOT NULL DEFAULT'0' COMMENT'是否删除',
												create_timestamp INTEGER COMMENT'创建时间',
CONSTRAINT fk_commodity_banner FOREIGN KEY (commodity_id) REFERENCES tb_commodity(id)
);

-- 创建一个tb_track足迹表
CREATE TABLE IF NOT EXISTS tb_track(
											id INTEGER UNSIGNED,
											commodity_id INTEGER UNSIGNED COMMENT'商品id',
											user_id INTEGER UNSIGNED COMMENT'用户id',
											join_timestamp INTEGER COMMENT'加入时间',
CONSTRAINT fk_commodity_track FOREIGN KEY (commodity_id) REFERENCES tb_commodity(id),
CONSTRAINT fk_user_track FOREIGN KEY (user_id) REFERENCES tb_user(id)
);
```





## 接口设计



### 客户端接口



#### 用户注册-申请验证短信

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户注册-验证验证短信

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户登陆-申请验证短信

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户登陆-申请验证短信

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户信息-修改昵称

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户信息-修改头像

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户信息-修改性别

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户地址-新增

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户地址-修改

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户地址-删除

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 横幅列表

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 分类列表

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 商品列表

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 商品详情

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 商品评论-查询

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 商品评论-新增

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 商品评论-删除

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 购物车-加入

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 购物车-修改

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 购物车-移除

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 收藏夹-加入

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 收藏夹-移除

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 优惠卷-查询

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户订单-查询

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户订单-新增

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户订单-付款

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 用户订单-删除

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---



### 管理端接口




#### 统计

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---



#### 用户-查询

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 用户-详情

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 商品分类-查询

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 商品分类-新增

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 商品分类-修改

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```json

```



---

#### 商品分类-删除

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 商品-查询

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 商品-新增

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 商品-修改

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 商品-删除

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 横幅-查询

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 横幅-新增

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 横幅-修改

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 横幅-删除

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 订单-查询

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---




#### 订单-修改

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---

#### 惠卷-查询

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 惠卷-新增

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 惠卷-删除

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 惠卷-发放

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```




---

#### 财务

> 

Path: ``````

Method: ``````

Request

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Response

| 参数名称 | 参数类型 | 参数简介 | 是否必传 |
| -------- | -------- | -------- | :------- |
|          |          |          |          |



Example

```

```



---



## 第三方库

[flask-sqlalchemy](http://www.pythondoc.com/flask-sqlalchemy/index.html)

[yagmail](https://github.com/kootenpv/yagmail)
