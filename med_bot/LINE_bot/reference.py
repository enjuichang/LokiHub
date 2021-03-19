#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#FindDepartment科別查詢用字典
departmentDICT = {
    "身心科":["心情","睡眠", "瘋", "身心"],
    "耳鼻喉科": ["顎", "耳朵", "鼻子", "鼻", "咽喉", "鼻涕", "喉嚨", "脖子", "耳", "鼻樑", "鼻腔內", "耳鼻喉", "鼻炎", "打呼", "打鼾", "扁桃腺", "流鼻血", "過敏性鼻炎"],
    "家醫科": ["喉部", "頸椎", "嘴", "風池穴", "小腿", "臉頰", "屁股", "眉間", "頭", "頸部", "腹瀉", "家醫", "頭痛", "頭暈", "咳嗽", "噁心", "小拇指", "下背", "發燒", "疲勞", "疲倦", "暈眩", "背", "累","臂"],
    "肝膽腸胃科": ["肚子", "腸胃", "胃","腹脹","腹鳴","腹瀉","大便不規則","食慾不振","胃酸","胃潰瘍","黑便","吐血","膚色變黃","B型肝炎帶原者","C型肝炎帶原者","肝機能異常","肝膽結石", "肝膽腸胃"],
    "婦產科": ["陰部", "婦產", "乳房", "乳腺", "陰道","陰道","月經","不孕症","婦科腫瘤","避孕","優生","流產","女性結紮","婦科檢查","產前檢查","子宮頸","抹片","妊娠"],
    "一般內科": ["腹", "高血壓", "黃疸", "一般內科"],
    "心臟內科": ["心臟", "瓣膜", "心", "心導管手術", "心跳", "心臟內","心悸","心臟無力","高血壓","心絞痛","心律不整","先天性心臟病"],
    "胸腔外科": ["胸口", "胸"],
    "眼科": ["眼睛", "飛蚊症"],
    "泌尿科": ["泌尿", "小便", "尿","泌尿道腫瘤","前列腺肥大","腎結石","膀胱結石","血尿","頻尿","小便無力","尿道下裂","隱睪","陰囊腫痛","夜尿","尿失禁","不孕","男性性機能異常","包皮","性病","膀胱機能異常"],
    "內分泌科": ["賀爾蒙","甲狀腺疾病","糖尿病","肥胖","腦下垂體病變","腎上腺","甲狀腺","高尿酸","代謝異常"],
    "神經內科": ["神經內", "麻痺"],
    "胸腔內科": ["胸腔內","咳嗽","咳血","氣喘","肺結核","肺腫瘤","肺炎","胸悶","支氣管炎"],
    "牙科": ["牙齒"],
    "皮膚科":["掉頭髮","皮膚","脂肪瘤","痘痘", "禿"],
    "骨科":["骨", "骨頭","骨折","骨骼疼痛","脫臼","骨髓炎","關節退化","腰酸背痛","關節炎","骨畸形","骨腫瘤","脊椎病變","脊椎骨骨折","脊椎側彎","駝背","骨質疏鬆症","坐骨神經痛","運動傷害"],
    "外科" : ["外"],
    "感染科":["感染"],
    "消化內科":["消化內"],
    "老人醫學科":["老人醫學"],
    "整形外科" : ["整形外","顏面","手部外科","神經肌腱接合","頭頸部腫瘤","軀幹重建","美容","整形","皮膚腫瘤切除","疤痕"],
    "腎臟科":["腎臟炎","血尿","尿蛋白","水腫","尿毒","腎結石","尿路感染","電解質不平衡","中毒"],
    "新陳代謝":["疲倦或虛弱","容易流汗","夜汗","糖尿病","口渴","多尿","口乾","多尿","乳房分泌物","肢端肥大症","肥胖症","高血脂症","血糖過低","尿酸過高","身高異常","性別異常","體重","腦下腺","腎上腺"],
    "直腸外科":["大腸直腸癌","肛門","人工肛門","人工膀胱","大腸炎","大腸鏡","息肉","超音波","生理檢查","排便","疝氣","闌尾炎","腸胃道"],
    "神經外科":["頭部","脊髓","腦血管","腦瘤","水腦症","交感神經","周圍神經","疼痛","麻木","麻麻","顱顏","中風","動脈","內視鏡","三叉神經痛","顏面神經","脊椎","帕金森氏症","疼痛治療"],
    "復健科":["骨骼肌肉","腰酸背痛","關節","運動傷害","中風","脊椎","腦性麻痺","心肺復健","肩膀"],
    
    }


#FindDepartment危急情況字典
emergencyLIST = ["大量出血","昏迷","失去意識","沒有心跳","血流不止","停止呼吸", "暈倒","噴血","暈倒","中槍","中彈","不會動"]
otherLIST = ["狗", "貓", "鳥", "鼠","鵝"]