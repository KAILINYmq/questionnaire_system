/*
 Navicat Premium Data Transfer

 Source Server         : KAILIN1
 Source Server Type    : MongoDB
 Source Server Version : 40010
 Source Host           : localhost:27017
 Source Schema         : questionnaire_system

 Target Server Type    : MongoDB
 Target Server Version : 40010
 File Encoding         : 65001

 Date: 17/02/2020 18:50:36
*/


// ----------------------------
// Collection structure for excel_url
// ----------------------------
db.getCollection("excel_url").drop();
db.createCollection("excel_url");

// ----------------------------
// Documents of excel_url
// ----------------------------
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4290e0cb250000da0064d2"),
    "统一社会信用代码": "1",
    file: "aasd.xlsx",
    time: "1581477948"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e43cc5c4478c74667af420a"),
    "统一社会信用代码": "1",
    file: "15815015311style_sheet.xlsx",
    time: "1581501532"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e43cc654478c74667af420b"),
    "统一社会信用代码": "1",
    file: "15815015401style_sheet.xlsx",
    time: "1581501541"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a6485bb75075dcfd9aa67"),
    "统一社会信用代码": "1",
    file: "15819337011style_sheet.xlsx",
    time: "1581933701"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a64d6cdda769fed471fe9"),
    "统一社会信用代码": "1",
    file: "15819337821style_sheet.xlsx",
    time: "1581933782"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a64fcdb10d80882f3936a"),
    "统一社会信用代码": "1",
    file: "15819338201style_sheet.xlsx",
    time: "1581933820"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a65f14c34620429d7a0c5"),
    "统一社会信用代码": "1",
    file: "15819340651style_sheet.xlsx",
    time: "1581934065"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a65fc4c34620429d7a0c6"),
    "统一社会信用代码": "1",
    file: "15819340761style_sheet.xlsx",
    time: "1581934076"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a669bfec0cfe343f9e91c"),
    "统一社会信用代码": "1",
    file: "15819342351style_sheet.xlsx",
    time: "1581934235"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a66bf48815eda27734efd"),
    "统一社会信用代码": "1",
    file: "15819342711style_sheet.xlsx",
    time: "1581934271"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a670b85dbffe8edec3734"),
    "统一社会信用代码": "1",
    file: "15819343461style_sheet.xlsx",
    time: "1581934347"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a6a0b2dc7325045c23dbd"),
    "统一社会信用代码": "1",
    file: "15819351141style_sheet.xlsx",
    time: "1581935115"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a6ac718ced5470ad484e8"),
    "统一社会信用代码": "1",
    file: "15819353031style_sheet.xlsx",
    time: "1581935303"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a6b95788395174c49e8fe"),
    "统一社会信用代码": "1",
    file: "15819355081style_sheet.xlsx",
    time: "1581935509"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a6bea0b7f90dba96b9137"),
    "统一社会信用代码": "1",
    file: "15819355941style_sheet.xlsx",
    time: "1581935594"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a6e2ea3974573c7325b2b"),
    "统一社会信用代码": "1",
    file: "15819361731style_sheet.xlsx",
    time: "1581936174"
} ]);
db.getCollection("excel_url").insert([ {
    _id: ObjectId("5e4a6fc31db261ef4be7aaf0"),
    "统一社会信用代码": "1",
    file: "15819365791style_sheet.xlsx",
    time: "1581936579"
} ]);

// ----------------------------
// Collection structure for message
// ----------------------------
db.getCollection("message").drop();
db.createCollection("message");

// ----------------------------
// Documents of message
// ----------------------------
db.getCollection("message").insert([ {
    _id: ObjectId("5e415426ec1e00003e004a76"),
    "统一社会信用代码": "1",
    "组织机构代码": "125555555.0",
    "法人单位名称": "2.0",
    "法定代表人 （单位负责人）": "3.0",
    "联系方式": {
        "固话": "41231111.0",
        "手机": "17956492147.0"
    },
    "企业所在地行政区划代码": "常熟市",
    "单位隶属关系": "其他",
    "行业类别代码": "纺织、服装及日用品专门零售",
    "企业规模": "小型企业",
    "登记注册类型": "有限责任公司（含国有独资公司）",
    "企业从业人员平均人数": "38.0",
    "销售（营业）收入": 5718,
    "利润总额": "11.4",
    "固定资产折旧": "4.5",
    "主营业务税金及附加": "19.4",
    "成本费用总额": "931.5",
    "人工成本总计": "328.9",
    "从业人员工资总额": "266.0",
    "福利费用": "6.9",
    "劳务派遣人员工资总额": "1",
    "在岗职工工资总额": "266.0",
    "教育经费": "1",
    "保险费用": "56.0",
    "劳动保护费用": "1",
    "住房费用": "1",
    "其他人工成本": "1"
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e41669eec1e00003e004a77"),
    "统一社会信用代码": "2"
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e416899ec1e00003e004a78")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e41689bec1e00003e004a79")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e41689cec1e00003e004a7a")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e41689dec1e00003e004a7b")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e41689fec1e00003e004a7c")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e4168a0ec1e00003e004a7d")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e4168a1ec1e00003e004a7e")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e4168a2ec1e00003e004a7f")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e4168a3ec1e00003e004a80")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e4168a4ec1e00003e004a81")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e4168a5ec1e00003e004a82")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e4168bcec1e00003e004a83")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e4168beec1e00003e004a84")
} ]);
db.getCollection("message").insert([ {
    _id: ObjectId("5e4168bfec1e00003e004a85")
} ]);

// ----------------------------
// Collection structure for path
// ----------------------------
db.getCollection("path").drop();
db.createCollection("path");

// ----------------------------
// Documents of path
// ----------------------------
db.getCollection("path").insert([ {
    _id: ObjectId("5e436f8411c689ad73fbaa7f"),
    "统一社会信用代码": "1",
    path: "./upload_table/15814777631/"
} ]);

// ----------------------------
// Collection structure for users
// ----------------------------
db.getCollection("users").drop();
db.createCollection("users");

// ----------------------------
// Documents of users
// ----------------------------
db.getCollection("users").insert([ {
    _id: ObjectId("5e40e98fec1e00003e004a72"),
    username: "admin",
    password: "123456",
    admin: 1,
    "is_de": 0
} ]);
db.getCollection("users").insert([ {
    _id: ObjectId("5e40ff62ec1e00003e004a75"),
    username: "1",
    admin: 0,
    "is_de": 0,
    password: "123456"
} ]);
