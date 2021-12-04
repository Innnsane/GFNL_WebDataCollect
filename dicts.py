ALGORITHM = {
    "1_1": {
        "name": "最小阈值",
        "inTurn": 2,
        "position": 3,
        "attribute": 1,
    },
    "1_2": {
        "name": "数据复原",
        "inTurn": 5,
        "position": 3,
        "attribute": 1,
    },
    "1_3": {
        "name": "异相回归",
        "inTurn": 5,
        "position": 3,
        "attribute": 1,
    },
    "1_4": {
        "name": "前馈",
        "inTurn": 2,
        "position": 2,
        "attribute": 1,
    },
    "1_5": {
        "name": "渐进",
        "inTurn": 3,
        "position": 2,
        "attribute": 1,
    },
    "1_6": {
        "name": "推演",
        "inTurn": 4,
        "position": 2,
        "attribute": 1,
    },
    "2_1": {
        "name": "代码封装",
        "inTurn": 1,
        "position": 3,
        "attribute": 2,
    },
    "2_2": {
        "name": "机器学习",
        "inTurn": 1,
        "position": 3,
        "attribute": 2,
    },
    "2_3": {
        "name": "补码溢出",
        "inTurn": 2,
        "position": 3,
        "attribute": 2,
    },
    "2_4": {
        "name": "感知",
        "inTurn": 1,
        "position": 2,
        "attribute": 2,
    },
    "2_5": {
        "name": "理性",
        "inTurn": 2,
        "position": 2,
        "attribute": 2,
    },
    "2_6": {
        "name": "连结",
        "inTurn": 3,
        "position": 2,
        "attribute": 2,
    },
    "3_1": {
        "name": "正向反馈",
        "inTurn": 3,
        "position": 3,
        "attribute": 3,
    },
    "3_2": {
        "name": "支持向量",
        "inTurn": 3,
        "position": 3,
        "attribute": 3,
    },
    "3_3": {
        "name": "矢量加速",
        "inTurn": 4,
        "position": 3,
        "attribute": 3,
    },
    "3_4": {
        "name": "矩阵结构",
        "inTurn": 4,
        "position": 3,
        "attribute": 3,
    },
    "3_5": {
        "name": "集束",
        "inTurn": 5,
        "position": 2,
        "attribute": 3,
    },
    "3_6": {
        "name": "启发",
        "inTurn": 1,
        "position": 2,
        "attribute": 3,
    },
    "3_7": {
        "name": "卷积",
        "inTurn": 4,
        "position": 2,
        "attribute": 3,
    },
    "3_8": {
        "name": "博弈",
        "inTurn": 5,
        "position": 2,
        "attribute": 3,
    },
    "4_1": {
        "name": "单件A区",
        "inTurn": 0,
        "position": 1,
        "attribute": 4,
    },
    "4_2": {
        "name": "单件B区",
        "inTurn": 0,
        "position": 1,
        "attribute": 5,
    },
    "4_3": {
        "name": "单件C区",
        "inTurn": 0,
        "position": 1,
        "attribute": 6,
    }
}

ATTRIBUTELIST = {
    1: [1, 2, 3, 4, 5, 6, 7, 8],
    2: [9, 10, 11, 12, 13, 14, 15],
    3: [11, 12, 13, 14, 16, 17, 18, 19],
    4: [20, 21, 22, 23, 24, 25, 26, 27],
    5: [28, 29, 30, 31, 32, 33, 34],
    6: [30, 31, 32, 33, 35, 36, 37, 38]
}

ATTRIBUTE = {
    1: "攻击力 12%",
    2: "攻击力 54",
    3: "算力 12%",
    4: "算力 54",
    5: "物理穿透 7.2%",
    6: "物理穿透 20",
    7: "算量穿透 7.2%",
    8: "算量穿透 20",

    9: "最大生命 12%",
    10: "最大生命 1800",
    11: "物理防御 7.2%",
    12: "物理防御 56",
    13: "算量防御 7.2%",
    14: "算量防御 56",
    15: "战后生命恢复 720",

    16: "暴击率 8%",
    17: "暴击伤害 16%",
    18: "治疗效果 4%",
    19: "技能急速 8%",

    20: "攻击力 6%",
    21: "攻击力 27",
    22: "算力 6%",
    23: "算力 27",
    24: "物理穿透 3.6%",
    25: "物理穿透 10",
    26: "算量穿透 3.6%",
    27: "算量穿透 10",

    28: "最大生命 6%",
    29: "最大生命 900",
    30: "物理防御 3.6%",
    31: "物理防御 28",
    32: "算量防御 3.6%",
    33: "算量防御 28",
    34: "战后生命恢复 360",

    35: "暴击率 4%",
    36: "暴击伤害 8%",
    37: "治疗效果 2%",
    38: "技能急速 4%",
}

WORK = {
    "1": "守卫",
    "2": "射手",
    "3": "战士",
    "4": "特种",
    "5": "医师",
}

DOLL = {
    "1001": {
        "name": "帕斯卡",
        "job": "5",
        "icon": "http://wiki.42lab.cloud/images/f/f8/ICON_Item_2001.png",
    },
    "1002": {
        "name": "安冬妮娜",
        "job": "4",
        "icon": "http://wiki.42lab.cloud/images/4/47/ICON_Item_2002.png",
    },
    "1003": {
        "name": "苏尔",
        "job": "3",
        "icon": "http://wiki.42lab.cloud/images/9/99/ICON_Item_2003.png",
    },
    "1004": {
        "name": "席摩",
        "job": "2",
        "icon": "http://wiki.42lab.cloud/images/4/4f/ICON_Item_2004.png",
    },
    "1005": {
        "name": "克罗琦",
        "job": "1",
        "icon": "http://wiki.42lab.cloud/images/9/97/ICON_Item_2005.png",
    },
    "1006": {
        "name": "菲涅尔",
        "job": "2",
        "icon": "http://wiki.42lab.cloud/images/f/f7/ICON_Item_2006.png",
    },
    "1007": {
        "name": "炽",
        "job": "3",
        "icon": "http://wiki.42lab.cloud/images/1/12/ICON_Item_2007.png",
    },
    "1008": {
        "name": "琴",
        "job": "5",
        "icon": "http://wiki.42lab.cloud/images/c/c5/ICON_Item_2008.png",
    },
    "1009": {
        "name": "迈迈",
        "job": "4",
        "icon": "http://wiki.42lab.cloud/images/3/34/ICON_Item_2009.png",
    },
    "1010": {
        "name": "伊芙琳",
        "job": "1",
        "icon": "http://wiki.42lab.cloud/images/4/46/ICON_Item_2010.png",
    },
    "1011": {
        "name": "薮春",
        "job": "1",
        "icon": "http://wiki.42lab.cloud/images/9/9b/ICON_Item_2011.png",
    },
    "1012": {
        "name": "麦克斯",
        "job": "2",
        "icon": "http://wiki.42lab.cloud/images/4/4e/ICON_Item_2012.png",
    },
    "1013": {
        "name": "贝蒂",
        "job": "3",
        "icon": "http://wiki.42lab.cloud/images/d/de/ICON_Item_2013.png",
    },
    "1014": {
        "name": "巧可",
        "job": "5",
        "icon": "http://wiki.42lab.cloud/images/e/e8/ICON_Item_2014.png",
    },
    "1015": {
        "name": "帕那刻亚",
        "job": "5",
        "icon": "http://wiki.42lab.cloud/images/f/fb/ICON_Item_2015.png",
    },
    "1016": {
        "name": "坂口希",
        "job": "4",
        "icon": "http://wiki.42lab.cloud/images/f/f9/ICON_Item_2016.png",
    },
    "1017": {
        "name": "安吉拉",
        "job": "4",
        "icon": "http://wiki.42lab.cloud/images/8/82/ICON_Item_2017.png",
    },
    "1018": {
        "name": "芙洛伦",
        "job": "5",
        "icon": "http://wiki.42lab.cloud/images/6/63/ICON_Item_2018.png",
    },
    "1019": {
        "name": "芬恩",
        "job": "3",
        "icon": "http://wiki.42lab.cloud/images/f/f9/ICON_Item_2019.png",
    },
    "1020": {
        "name": "扬尼",
        "job": "1",
        "icon": "http://wiki.42lab.cloud/images/0/00/ICON_Item_2020.png",
    },
    "1021": {
        "name": "音流",
        "job": "4",
        "icon": "http://wiki.42lab.cloud/images/5/57/ICON_Item_2021.png",
    },
    "1022": {
        "name": "秋",
        "job": "3",
        "icon": "http://wiki.42lab.cloud/images/1/11/ICON_Item_2022.png",
    },
    "1023": {
        "name": "波妮",
        "job": "1",
        "icon": "http://wiki.42lab.cloud/images/c/c8/ICON_Item_2023.png",
    },
    "1024": {
        "name": "埃尔赫",
        "job": "2",
        "icon": "http://wiki.42lab.cloud/images/b/be/ICON_Item_2024.png",
    },
    "1025": {
        "name": "缠枝",
        "job": "2",
        "icon": "http://wiki.42lab.cloud/images/8/8e/ICON_Item_2025.png",
    },
    "1026": {
        "name": "七花",
        "job": "5",
        "icon": "http://wiki.42lab.cloud/images/7/70/ICON_Item_2026.png",
    },
    "1027": {
        "name": "希安",
        "job": "1",
        "icon": "http://wiki.42lab.cloud/images/4/44/ICON_Item_2027.png",
    },
    "1028": {
        "name": "薇",
        "job": "3",
        "icon": "http://wiki.42lab.cloud/images/9/97/ICON_Item_2028.png",
    },
    "1029": {
        "name": "薇洛儿",
        "job": "4",
        "icon": "http://wiki.42lab.cloud/images/4/48/ICON_Item_2029.png",
    },
    "1030": {
        "name": "科谢尼娅",
        "job": "4",
        "icon": "http://wiki.42lab.cloud/images/3/3d/ICON_Item_2030.png",
    },
    "1031": {
        "name": "伊姆赫特",
        "job": "5",
        "icon": "http://wiki.42lab.cloud/images/0/0c/ICON_Item_2031.png",
    },
    "1032": {
        "name": "奥托金",
        "job": "2",
        "icon": "http://wiki.42lab.cloud/images/7/74/ICON_Item_2032.png",
    },
    "1033": {
        "name": "莉丝",
        "job": "4",
        "icon": "http://wiki.42lab.cloud/images/7/72/ICON_Item_2033.png",
    },
    "1034": {
        "name": "阿比盖尔",
        "job": "4",
        "icon": "http://wiki.42lab.cloud/images/b/b2/ICON_Item_2034.png",
    },
    "1035": {
        "name": "洁西",
        "job": "5",
        "icon": "http://wiki.42lab.cloud/images/5/57/ICON_Item_2035.png",
    },
    "1036": {
        "name": "拉姆",
        "job": "2",
        "icon": "http://wiki.42lab.cloud/images/3/32/ICON_Item_2036.png",
    },
    "1037": {
        "name": "赫波",
        "job": "2",
        "icon": "http://wiki.42lab.cloud/images/c/ce/ICON_Item_2037.png",
    },
    "1038": {
        "name": "咲耶",
        "job": "4",
        "icon": "http://wiki.42lab.cloud/images/3/38/ICON_Item_2038.png",
    },
    "1039": {
        "name": "桑朵莱希",
        "job": "3",
        "icon": "http://wiki.42lab.cloud/images/b/b6/ICON_Item_2039.png",
    },
    "1040": {
        "name": "杜莎妮",
        "job": "4",
        "icon": "http://wiki.42lab.cloud/images/d/d6/ICON_Item_2040.png",
    },
    "1041": {
        "name": "德菈赛",
        "job": "5",
        "icon": "http://wiki.42lab.cloud/images/6/65/ICON_Item_2041.png",
    },
    "1042": {
        "name": "初尘",
        "job": "3",
        "icon": "http://wiki.42lab.cloud/images/1/17/ICON_Item_2042.png",
    },
    "1043": {
        "name": "派森",
        "job": "1",
        "icon": "http://wiki.42lab.cloud/images/1/17/ICON_Item_2043.png",
    }
}

ITEM = {
    "doll": {
        "doll_1008": {
            "name": "琴",
            "rarity": "3",
            "card": "http://wiki.42lab.cloud/images/a/ab/Npic_gin.png",
        },
        "doll_1009": {
            "name": "迈迈",
            "rarity": "1",
            "card": "http://wiki.42lab.cloud/images/4/4f/Npic_mai.png",
        },
        "doll_1013": {
            "name": "贝蒂",
            "rarity": "2",
            "card": "http://wiki.42lab.cloud/images/9/9a/Npic_betty.png",
        },
        "doll_1016": {
            "name": "坂口希",
            "rarity": "3",
            "card": "http://wiki.42lab.cloud/images/4/40/Npic_banxsy.png",
        },
        "doll_1017": {
            "name": "安吉拉",
            "rarity": "2",
            "card": "http://wiki.42lab.cloud/images/f/f0/Npic_angela.png",
        },
        "doll_1023": {
            "name": "波妮",
            "rarity": "1",
            "card": "http://wiki.42lab.cloud/images/e/e8/Npic_bonee.png",
        },
        "doll_1024": {
            "name": "埃尔赫",
            "rarity": "2",
            "card": "http://wiki.42lab.cloud/images/1/1c/Npic_earhart.png",
        },
        "doll_1031": {
            "name": "伊姆赫特",
            "rarity": "2",
            "card": "http://wiki.42lab.cloud/images/6/6f/Npic_imhotep.png",
        },
        "doll_1035": {
            "name": "洁西",
            "rarity": "1",
            "card": "http://wiki.42lab.cloud/images/c/c6/Npic_jessie.png",
        }
    },
    "mindf": {
        "mindf_1001": {
            "name": "帕斯卡",
            "job": "5",
        },
        "mindf_1002": {
            "name": "安冬妮娜",
            "job": "4",
        },
        "mindf_1003": {
            "name": "苏尔",
            "job": "3",
        },
        "mindf_1004": {
            "name": "席摩",
            "job": "2",
        },
        "mindf_1005": {
            "name": "克罗琦",
            "job": "1",
        },
        "mindf_1006": {
            "name": "菲涅尔",
            "job": "2",
        },
        "mindf_1007": {
            "name": "炽",
            "job": "3",
        },
        "mindf_1008": {
            "name": "琴",
            "job": "5",
        },
        "mindf_1009": {
            "name": "迈迈",
            "job": "4",
        },
        "mindf_1010": {
            "name": "伊芙琳",
            "job": "1",
        },
        "mindf_1011": {
            "name": "薮春",
            "job": "1",
        },
        "mindf_1012": {
            "name": "麦克斯",
            "job": "2",
        },
        "mindf_1013": {
            "name": "贝蒂",
            "job": "3",
        },
        "mindf_1014": {
            "name": "巧可",
            "job": "5",
        },
        "mindf_1015": {
            "name": "帕那刻亚",
            "job": "5",
        },
        "mindf_1016": {
            "name": "坂口希",
            "job": "4",
        },
        "mindf_1017": {
            "name": "安吉拉",
            "job": "4",
        },
        "mindf_1018": {
            "name": "芙洛伦",
            "job": "5",
        },
        "mindf_1019": {
            "name": "芬恩",
            "job": "3",
        },
        "mindf_1020": {
            "name": "扬尼",
            "job": "1",
        },
        "mindf_1021": {
            "name": "音流",
            "job": "4",
        },
        "mindf_1022": {
            "name": "秋",
            "job": "3",
        },
        "mindf_1023": {
            "name": "波妮",
            "job": "1",
        },
        "mindf_1024": {
            "name": "埃尔赫",
            "job": "2",
        },
        "mindf_1025": {
            "name": "缠枝",
            "job": "2",
        },
        "mindf_1026": {
            "name": "七花",
            "job": "5",
        },
        "mindf_1027": {
            "name": "希安",
            "job": "1",
        },
        "mindf_1028": {
            "name": "薇",
            "job": "3",
        },
        "mindf_1029": {
            "name": "薇洛儿",
            "job": "4",
        },
        "mindf_1030": {
            "name": "科谢尼娅",
            "job": "4",
        },
        "mindf_1031": {
            "name": "伊姆赫特",
            "job": "5",
        },
        "mindf_1032": {
            "name": "奥托金",
            "job": "2",
        },
        "mindf_1033": {
            "name": "莉丝",
            "job": "4",
        },
        "mindf_1034": {
            "name": "阿比盖尔",
            "job": "4",
        },
        "mindf_1035": {
            "name": "洁西",
            "job": "5",
        },
        "mindf_1036": {
            "name": "拉姆",
            "job": "2",
        },
        "mindf_1037": {
            "name": "赫波",
            "job": "2",
        },
        "mindf_1038": {
            "name": "咲耶",
            "job": "4",
        },
        "mindf_1039": {
            "name": "桑朵莱希",
            "job": "3",
        },
        "mindf_1040": {
            "name": "杜莎妮",
            "job": "3",
        },
        "mindf_1041": {
            "name": "德菈赛",
            "job": "5",
        },
        "mindf_1042": {
            "name": "初尘",
            "job": "3",
        },
        "mindf_1043": {
            "name": "派森",
            "job": "1",
        }
    },
    "minds": {
        "minds_1": {
            "name": "心智构件",
            "number": "1",
        },
        "minds_2": {
            "name": "心智构件",
            "number": "2",
        },
        "minds_4": {
            "name": "心智构件",
            "number": "4",
        }
    },
    "factory": {
        "factory_1_1": {
            "name": "低模方形数据",
            "rarity": "2"
        },
        "factory_1_2": {
            "name": "低模三角数据",
            "rarity": "2"
        },
        "factory_1_3": {
            "name": "低模菱形数据",
            "rarity": "2"
        },
        "factory_2_1": {
            "name": "中模方形数据",
            "rarity": "3"
        },
        "factory_2_2": {
            "name": "中模三角数据",
            "rarity": "3"
        },
        "factory_2_3": {
            "name": "中模菱形数据",
            "rarity": "3"
        },
        "factory_3_1": {
            "name": "高模方形数据",
            "rarity": "4"
        },
        "factory_3_2": {
            "name": "高模三角数据",
            "rarity": "4"
        },
        "factory_3_3": {
            "name": "高模菱形数据",
            "rarity": "4"
        },
    },
    "xp": {
        "xp_1_1": {
            "name": "作战经验*100",
            "number": "1",
            "rarity": "3"
        },
        "xp_1_3": {
            "name": "作战经验*100",
            "number": "3",
            "rarity": "3"
        },
        "xp_2_1": {
            "name": "作战经验*600",
            "number": "1",
            "rarity": "4"
        },
        "xp_2_2": {
            "name": "作战经验*600",
            "number": "2",
            "rarity": "4"
        },
        "xp_2_3": {
            "name": "作战经验*600",
            "number": "3",
            "rarity": "4"
        },
        "xp_3_1": {
            "name": "作战经验*3600",
            "number": "1",
            "rarity": "5"
        },
    },
    "gift": {
        "gift_1_1": {
            "name": "包子",
            "rarity": "3"
        },
        "gift_1_2": {
            "name": "快餐",
            "rarity": "3"
        },
        "gift_1_3": {
            "name": "小块蛋糕",
            "rarity": "3"
        },
        "gift_1_4": {
            "name": "蜂蜜",
            "rarity": "3"
        },
        "gift_1_5": {
            "name": "关东煮",
            "rarity": "3"
        },
        "gift_1_6": {
            "name": "毛绒挂饰",
            "rarity": "3"
        },
        "gift_1_7": {
            "name": "数码积木",
            "rarity": "3"
        },
        "gift_1_8": {
            "name": "练习竹剑",
            "rarity": "3"
        },
        "gift_2_1": {
            "name": "一笼包子",
            "rarity": "4"
        },
        "gift_2_2": {
            "name": "工作套餐",
            "rarity": "4"
        },
        "gift_2_3": {
            "name": "加量蛋糕",
            "rarity": "4"
        },
        "gift_2_4": {
            "name": "巧克力圣代",
            "rarity": "4"
        },
        "gift_2_5": {
            "name": "草莓蛋糕",
            "rarity": "4"
        },
        "gift_2_6": {
            "name": "卡通玩偶",
            "rarity": "4"
        },
        "gift_2_7": {
            "name": "瓶中飞船",
            "rarity": "4"
        },
        "gift_2_8": {
            "name": "实用军刀",
            "rarity": "4"
        },
        "gift_3_1": {
            "name": "一屉包子",
            "rarity": "5"
        },
        "gift_3_2": {
            "name": "双人套餐",
            "rarity": "5"
        },
        "gift_3_3": {
            "name": "豪华蛋糕",
            "rarity": "5"
        },
        "gift_3_4": {
            "name": "咖啡",
            "rarity": "5"
        },
        "gift_3_5": {
            "name": "下午茶",
            "rarity": "5"
        },
        "gift_3_6": {
            "name": "玩具大熊",
            "rarity": "5"
        },
        "gift_3_7": {
            "name": "手办模型",
            "rarity": "5"
        },
        "gift_3_8": {
            "name": "典藏名刀",
            "rarity": "5"
        },
    },
    "ctrl": {
        "ctrl_1_1": {
            "name": "简化突破控件·守卫",
            "rarity": "1"
        },
        "ctrl_1_2": {
            "name": "简化突破控件·射手",
            "rarity": "1"
        },
        "ctrl_1_3": {
            "name": "简化突破控件·战士",
            "rarity": "1"
        },
        "ctrl_1_4": {
            "name": "简化突破控件·特种",
            "rarity": "1"
        },
        "ctrl_1_5": {
            "name": "简化突破控件·医师",
            "rarity": "1"
        },
        "ctrl_2_1": {
            "name": "标准突破控件·守卫",
            "rarity": "2"
        },
        "ctrl_2_2": {
            "name": "标准突破控件·射手",
            "rarity": "2"
        },
        "ctrl_2_3": {
            "name": "标准突破控件·战士",
            "rarity": "2"
        },
        "ctrl_2_4": {
            "name": "标准突破控件·特种",
            "rarity": "2"
        },
        "ctrl_2_5": {
            "name": "标准突破控件·医师",
            "rarity": "2"
        },
        "ctrl_3_1": {
            "name": "高级突破控件·守卫",
            "rarity": "3"
        },
        "ctrl_3_2": {
            "name": "高级突破控件·射手",
            "rarity": "3"
        },
        "ctrl_3_3": {
            "name": "高级突破控件·战士",
            "rarity": "3"
        },
        "ctrl_3_4": {
            "name": "高级突破控件·特种",
            "rarity": "3"
        },
        "ctrl_3_5": {
            "name": "高级突破控件·医师",
            "rarity": "3"
        },
        "ctrl_4_1": {
            "name": "特级突破控件·守卫",
            "rarity": "4"
        },
        "ctrl_4_2": {
            "name": "特级突破控件·射手",
            "rarity": "4"
        },
        "ctrl_4_3": {
            "name": "特级突破控件·战士",
            "rarity": "4"
        },
        "ctrl_4_4": {
            "name": "特级突破控件·特种",
            "rarity": "4"
        },
        "ctrl_4_5": {
            "name": "特级突破控件·医师",
            "rarity": "4"
        },
        "ctrl_5_1": {
            "name": "尖端突破控件·守卫",
            "rarity": "5"
        },
        "ctrl_5_2": {
            "name": "尖端突破控件·射手",
            "rarity": "5"
        },
        "ctrl_5_3": {
            "name": "尖端突破控件·战士",
            "rarity": "5"
        },
        "ctrl_5_4": {
            "name": "尖端突破控件·特种",
            "rarity": "5"
        },
        "ctrl_5_5": {
            "name": "尖端突破控件·医师",
            "rarity": "5"
        },
    }
}
