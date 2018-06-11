# -*-coding:UTF-8-*-
# _author_= 'gao'
import random

import time
import selenium.webdriver.support.expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def login(driver, username, password):
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/input").clear()
    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[1]/input").send_keys(username)
    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/div[2]/input").send_keys(password)
    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div/a").click()
    return driver


def culture_creat(driver, title, label, position):
    url = "https://mp-test1.cpmap.com/culture/81326a0ed45946edb6f9a6f5ec98737d/create"
    driver.get(url)
    driver.implicitly_wait(30)

    try:
        WebDriverWait(driver, 5, 0.5).until(EC.visibility_of(
            driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/input")))
    finally:
        pass

    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/input").send_keys(
        title)
    driver.find_element_by_class_name("mpc-select").click()
    driver.implicitly_wait(30)
    list = driver.find_elements_by_class_name("mpc-select_panel-item")
    x = random.randint(0, len(list) - 1)

    list[x].click()
    y = driver.find_element_by_xpath(
        "//*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/div/span").text

    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[3]/input").send_keys(
        label)
    # print(driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div/img").text)
    driver.find_element_by_xpath(
        "//*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/input").send_keys(
        "C:\\Users\\gao\Desktop\\testimage\\1F52G20Z0-5.jpg")

    driver.find_element_by_class_name("map-search-input").send_keys(position)
    time.sleep(2)
    # driver.find_element_by_class_name("map-search-icon").click()
    driver.implicitly_wait(30)
    # position_ = driver.find_element_by_xpath("//*[@id=\"amap-sug0\"]/text()").text
    # position_ = driver.find_element_by_class_name("map-search-input").text
    driver.find_element_by_class_name("map-search-icon").click()
    time.sleep(2)
    print("<titile:>", title, '\t', "<label:>", label, '\t', "<类型:>", y)
    # C:\\Users\\Public\\Pictures\\Sample Pictures\\test1.jpg
    # time.sleep(3)
    try:
        WebDriverWait(driver, 5, 1).until(EC.visibility_of(driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div/img")))
    finally:
        pass

    # print(driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div/img").get_attribute("src"))
    if driver.find_element_by_xpath(
            # //*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div

            # //*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div/i
            "//*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[4]/div/div/img").get_attribute(
        "src") != "":
        driver.find_element_by_class_name("next-button").click()
    return driver


from AMS import Driver, ReadCSV

driver = Driver.driver("https://mp-test1.cpmap.com/login")
login(driver, "test121803", "123456")
# list = ReadCSV.parameter("C:\\Users\\gao\\Desktop\\test2.csv")
list = ["北京市", "上海市", "广州市", "深圳", "成都市", "杭州市", "武汉市", "重庆市", "南京市", "天津市", "苏州市", "西安市", "长沙市", "沈阳市", "青岛市", "郑州市",
        "大连市", "东莞市", "宁波市", "厦门市", "福州市", "无锡市", "合肥市", "昆明市", "哈尔滨市", "济南市", "佛山市", "长春市", "温州市", "石家庄市", "南宁市",
        "常州市", "泉州市", "南昌市", "贵阳市", "太原市", "烟台市", "嘉兴市", "南通市", "金华市", "珠海市", "惠州市", "徐州市", "海口市", "乌鲁木齐市", "绍兴市",
        "中山市", "台州市", "兰州市", "潍坊市", "保定市", "镇江市", "扬州市", "桂林市", "唐山市", "三亚市", "湖州市", "呼和浩特市", "廊坊市", "洛阳市", "威海市",
        "盐城市", "临沂市", "江门市", "汕头市", "泰州市", "漳州市", "邯郸市", "济宁市", "芜湖市", "淄博市", "银川市", "柳州市", "绵阳市", "湛江市", "鞍山市", "赣州市",
        "大庆市", "宜昌市", "包头市", "咸阳市", "秦皇岛市", "株洲市", "莆田市", "吉林市", "淮安市", "肇庆市", "宁德市", "衡阳市", "南平市", "连云港市", "丹东市",
        "丽江市", "揭阳市", "延边朝鲜族自治州", "舟山市", "九江市", "龙岩市", "沧州市", "抚顺市", "襄阳市", "上饶市", "营口市", "三明市", "蚌埠市", "丽水市", "岳阳市",
        "清远市", "荆州市", "泰安市", "衢州市", "盘锦市", "东营市", "南阳市", "马鞍山市", "南充市", "西宁市", "孝感市", "齐齐哈尔市", "乐山市", "湘潭市", "遵义市",
        "宿迁市", "新乡市", "信阳市", "滁州市", "锦州市", "潮州市", "黄冈市", "开封市", "德阳市", "德州市", "梅州市", "鄂尔多斯市", "邢台市", "茂名市", "大理白族自治州",
        "韶关市", "商丘市", "安庆市", "黄石市", "六安市", "玉林市", "宜春市", "北海市", "牡丹江市", "张家口市", "梧州市", "日照市", "咸宁市", "常德市", "佳木斯市",
        "红河哈尼族彝族自治州", "黔东南苗族侗族自治州", "阳江市", "晋中市", "渭南市", "呼伦贝尔市", "恩施土家族苗族自治州", "河源市", "郴州市", "阜阳市", "聊城市", "大同市",
        "宝鸡市", "许昌市", "赤峰市", "运城市", "安阳市", "临汾市", "宣城市", "曲靖市", "西双版纳傣族自治州", "邵阳市", "葫芦岛市", "平顶山市", "辽阳市", "菏泽市", "本溪市",
        "驻马店市", "汕尾市", "焦作市", "黄山市", "怀化市", "四平市", "榆林市", "十堰市", "宜宾市", "滨州市", "抚州市", "淮南市", "周口市", "黔南布依族苗族自治州", "泸州市",
        "玉溪市", "眉山市", "通化市", "宿州市", "枣庄市", "内江市", "遂宁市", "吉安市", "通辽市", "景德镇市", "阜新市", "雅安市", "铁岭市", "承德市", "娄底市",
        "克拉玛依市", "长治市", "永州市", "绥化市", "巴音郭楞蒙古自治州", "拉萨市", "云浮市", "益阳市", "百色市", "资阳市", "荆门市", "松原市", "凉山彝族自治州", "达州市",
        "伊犁哈萨克自治州", "广安市", "自贡市", "汉中市", "朝阳市", "漯河市", "钦州市", "贵港市", "安顺市", "鄂州市", "广元市", "河池市", "鹰潭市", "乌兰察布市", "铜陵市",
        "昌吉回族自治州", "衡水市", "黔西南布依族苗族自治州", "濮阳市", "锡林郭勒盟", "巴彦淖尔市", "鸡西市", "贺州市", "防城港市", "兴安盟", "白山市", "三门峡市", "忻州市",
        "双鸭山市", "楚雄彝族自治州", "新余市", "来宾市", "淮北市", "亳州市", "湘西土家族苗族自治州", "吕梁市", "攀枝花市", "晋城市", "延安市", "毕节市", "张家界市", "酒泉市",
        "崇左市", "萍乡市", "乌海市", "伊春市", "六盘水市", "随州市", "德宏傣族景颇族自治州", "池州市", "黑河市", "哈密市", "文山壮族苗族自治州", "阿坝藏族羌族自治州", "天水市",
        "辽源市", "张掖市", "铜仁市", "鹤壁市", "儋州市", "保山市", "安康市", "白城市", "巴中市", "普洱市", "鹤岗市", "莱芜市", "阳泉市", "甘孜藏族自治州", "嘉峪关市",
        "白银市", "临沧市", "商洛市", "阿克苏地区", "海西蒙古族藏族自治州", "大兴安岭地区", "七台河市", "朔州市", "铜川市", "定西市", "迪庆藏族自治州", "日喀则市", "庆阳市",
        "昭通市", "喀什地区", "怒江傈僳族自治州", "海东市", "阿勒泰地区", "平凉市", "石嘴山市", "武威市", "阿拉善盟", "塔城地区", "林芝市", "金昌市", "吴忠市", "中卫市",
        "陇南市", "山南市", "吐鲁番市", "博尔塔拉蒙古自治州", "临夏回族自治州", "固原市", "甘南藏族自治州", "昌都市", "阿里地区", "海南藏族自治州", "和田地区", "克孜勒苏柯尔克孜自治州",
        "海北藏族自治州", "那曲地区", "玉树藏族自治州", "黄南藏族自治州", "果洛藏族自治州", "三沙市"]

i = 1
for li in list:
    print(i, end='')
    i += 1
    title = "标题" + li
    label = "签名" + li
    try:
        culture_creat(driver, title, label, li)
        WebDriverWait(driver, 5, 0.5).until(EC.visibility_of(
            driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div[4]/div")))
        driver.find_element_by_class_name("ant-select-selection__placeholder").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div/div/div/ul/li[1]").click()
        time.sleep(1)
        driver.find_element_by_class_name("step-next-button-container").click()
        time.sleep(1)
        print(driver.find_element_by_class_name("hint").text)
    except Exception as e:
        print("捕获异常", e)
    finally:
        pass