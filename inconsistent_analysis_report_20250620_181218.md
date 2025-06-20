# 音频场景预测不一致样本分析报告
生成时间: 2025-06-20 18:12:18
分析样本数量: 2161

## 分析统计

### 真实场景分布
| 场景 | 数量 |
| --- | --- |
| airport | 302 |
| bus | 146 |
| metro | 236 |
| metro_station | 280 |
| park | 54 |
| public_square | 201 |
| shopping_mall | 251 |
| street_pedestrian | 366 |
| street_traffic | 52 |
| tram | 273 |

### 预测不一致模式 (AE vs AS)
| 预测模式 | 数量 |
| --- | --- |
| street_pedestrian vs airport | 206 |
| public_square vs street_pedestrian | 186 |
| airport vs street_pedestrian | 165 |
| bus vs metro | 140 |
| tram vs metro | 140 |
| shopping_mall vs airport | 136 |
| airport vs shopping_mall | 135 |
| metro vs tram | 123 |
| airport vs metro_station | 96 |
| bus vs tram | 79 |
| shopping_mall vs metro_station | 72 |
| tram vs bus | 63 |
| metro vs metro_station | 57 |
| street_pedestrian vs public_square | 49 |
| metro_station vs metro | 45 |
| metro_station vs airport | 39 |
| metro vs bus | 34 |
| shopping_mall vs street_pedestrian | 33 |
| public_square vs street_traffic | 32 |
| park vs public_square | 31 |
| public_square vs park | 30 |
| street_pedestrian vs shopping_mall | 25 |
| street_pedestrian vs metro_station | 23 |
| metro_station vs street_pedestrian | 21 |
| metro_station vs shopping_mall | 19 |
| park vs street_traffic | 18 |
| airport vs public_square | 14 |
| street_traffic vs public_square | 14 |
| metro_station vs tram | 12 |
| metro_station vs public_square | 12 |
| metro_station vs street_traffic | 11 |
| bus vs street_traffic | 11 |
| public_square vs airport | 10 |
| tram vs metro_station | 9 |
| street_pedestrian vs park | 9 |
| metro vs street_traffic | 6 |
| street_traffic vs park | 6 |
| metro_station vs park | 5 |
| bus vs metro_station | 5 |
| metro vs airport | 3 |
| street_pedestrian vs street_traffic | 3 |
| airport vs tram | 3 |
| tram vs park | 3 |
| street_traffic vs bus | 2 |
| tram vs airport | 2 |
| tram vs public_square | 2 |
| public_square vs metro_station | 2 |
| park vs tram | 2 |
| metro_station vs bus | 2 |
| shopping_mall vs metro | 2 |
| park vs street_pedestrian | 2 |
| shopping_mall vs tram | 2 |
| tram vs street_pedestrian | 2 |
| airport vs street_traffic | 2 |
| public_square vs metro | 1 |
| public_square vs shopping_mall | 1 |
| street_traffic vs street_pedestrian | 1 |
| street_pedestrian vs metro | 1 |
| bus vs public_square | 1 |
| shopping_mall vs public_square | 1 |

## 详细样本分析

### 样本 1: street_pedestrian-paris-153-4646-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.594), Mouse(0.133)
- **音频特征**: RMS=0.0017, 频谱重心=1331Hz, 场景提示=quiet_indoor

### 样本 2: metro_station-milan-1187-44944-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.696), Music(0.384), Vehicle(0.102)
- **音频特征**: RMS=0.0069, 频谱重心=946Hz, 场景提示=quiet_indoor

### 样本 3: public_square-vienna-122-3614-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.897), Run(0.328), Animal(0.281)
- **音频特征**: RMS=0.0010, 频谱重心=1419Hz, 场景提示=quiet_indoor

### 样本 4: street_pedestrian-vienna-160-4872-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.716), Clip-clop(0.251), Animal(0.224)
- **音频特征**: RMS=0.0021, 频谱重心=1229Hz, 场景提示=quiet_indoor

### 样本 5: metro-barcelona-41-1253-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.186), Train(0.169)
- **音频特征**: RMS=0.0052, 频谱重心=1355Hz, 场景提示=quiet_indoor

### 样本 6: shopping_mall-lisbon-1176-45042-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.278), Music(0.267), Vehicle(0.153)
- **音频特征**: RMS=0.0055, 频谱重心=1018Hz, 场景提示=quiet_indoor

### 样本 7: airport-london-6-276-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.747), Clip-clop(0.358), Horse(0.278)
- **音频特征**: RMS=0.0020, 频谱重心=1255Hz, 场景提示=quiet_indoor

### 样本 8: street_pedestrian-london-150-4541-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.815), Animal(0.181), Run(0.171)
- **音频特征**: RMS=0.0038, 频谱重心=1372Hz, 场景提示=quiet_indoor

### 样本 9: shopping_mall-paris-134-4063-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **音频特征**: RMS=0.0017, 频谱重心=1095Hz, 场景提示=quiet_indoor

### 样本 10: metro_station-barcelona-62-1871-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Silence(0.185), Speech(0.151)
- **音频特征**: RMS=0.0009, 频谱重心=1369Hz, 场景提示=quiet_indoor

### 样本 11: airport-barcelona-1-40-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.660), Clip-clop(0.319), Animal(0.290)
- **音频特征**: RMS=0.0030, 频谱重心=1424Hz, 场景提示=quiet_indoor

### 样本 12: park-prague-1092-42204-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.223)
- **音频特征**: RMS=0.0034, 频谱重心=734Hz, 场景提示=quiet_indoor

### 样本 13: tram-prague-1184-44141-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.386), Field recording(0.113)
- **音频特征**: RMS=0.0225, 频谱重心=601Hz, 场景提示=mixed_environment

### 样本 14: tram-stockholm-283-8562-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.162), Music(0.101)
- **音频特征**: RMS=0.0275, 频谱重心=290Hz, 场景提示=mixed_environment

### 样本 15: metro_station-prague-1019-43305-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Silence(0.118)
- **音频特征**: RMS=0.0019, 频谱重心=1001Hz, 场景提示=quiet_indoor

### 样本 16: metro-barcelona-220-6635-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.859), Vehicle(0.612), Bus(0.218)
- **音频特征**: RMS=0.0211, 频谱重心=962Hz, 场景提示=mixed_environment

### 样本 17: tram-prague-1210-44352-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.519), Train(0.462), Rail transport(0.251)
- **音频特征**: RMS=0.0234, 频谱重心=548Hz, 场景提示=mixed_environment

### 样本 18: metro-barcelona-42-1289-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.168)
- **音频特征**: RMS=0.0106, 频谱重心=758Hz, 场景提示=mixed_environment

### 样本 19: metro_station-milan-1127-40753-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.719), Animal(0.110)
- **音频特征**: RMS=0.0044, 频谱重心=1418Hz, 场景提示=mixed_environment

### 样本 20: street_pedestrian-lisbon-1099-42250-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.887), Music(0.270), Outside, urban or manmade(0.155)
- **音频特征**: RMS=0.0040, 频谱重心=1370Hz, 场景提示=mixed_environment

### 样本 21: bus-vienna-219-6616-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.230), Animal(0.139), Bird(0.126)
- **音频特征**: RMS=0.0290, 频谱重心=298Hz, 场景提示=mixed_environment

### 样本 22: airport-paris-206-6268-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.618), Vehicle(0.262), Boat, Water vehicle(0.115)
- **音频特征**: RMS=0.0071, 频谱重心=1158Hz, 场景提示=quiet_indoor

### 样本 23: airport-stockholm-12-501-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.889), Clip-clop(0.224), Run(0.183)
- **音频特征**: RMS=0.0037, 频谱重心=854Hz, 场景提示=quiet_indoor

### 样本 24: airport-barcelona-203-6128-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.793), Run(0.242), Vehicle(0.194)
- **音频特征**: RMS=0.0021, 频谱重心=1363Hz, 场景提示=quiet_indoor

### 样本 25: shopping_mall-london-256-7755-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.661), Children playing(0.162), Animal(0.147)
- **音频特征**: RMS=0.0035, 频谱重心=1652Hz, 场景提示=mixed_environment

### 样本 26: public_square-vienna-124-3685-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.831), Animal(0.595), Bow-wow(0.579)
- **音频特征**: RMS=0.0017, 频谱重心=1262Hz, 场景提示=quiet_indoor

### 样本 27: metro-vienna-59-1768-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.822), Rail transport(0.659), Railroad car, train wagon(0.615)
- **音频特征**: RMS=0.0179, 频谱重心=429Hz, 场景提示=mixed_environment

### 样本 28: tram-lyon-1093-42804-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Train(0.503), Vehicle(0.490), Railroad car, train wagon(0.325)
- **音频特征**: RMS=0.0106, 频谱重心=771Hz, 场景提示=mixed_environment

### 样本 29: street_pedestrian-vienna-158-4819-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.306)
- **音频特征**: RMS=0.0018, 频谱重心=1054Hz, 场景提示=quiet_indoor

### 样本 30: metro-barcelona-220-6662-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.797), Vehicle(0.308)
- **音频特征**: RMS=0.0102, 频谱重心=979Hz, 场景提示=mixed_environment

### 样本 31: shopping_mall-vienna-139-4232-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.637)
- **音频特征**: RMS=0.0030, 频谱重心=1482Hz, 场景提示=mixed_environment

### 样本 32: street_pedestrian-lisbon-1004-42834-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.748), Vehicle(0.106), Animal(0.101)
- **音频特征**: RMS=0.0026, 频谱重心=1209Hz, 场景提示=quiet_indoor

### 样本 33: bus-milan-1115-40248-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.677), Vehicle(0.282)
- **音频特征**: RMS=0.0137, 频谱重心=1192Hz, 场景提示=mixed_environment

### 样本 34: public_square-stockholm-252-7555-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.179)
- **音频特征**: RMS=0.0024, 频谱重心=1084Hz, 场景提示=quiet_indoor

### 样本 35: tram-milan-1158-43737-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.797), Vehicle(0.340), Music(0.119)
- **音频特征**: RMS=0.0106, 频谱重心=939Hz, 场景提示=mixed_environment

### 样本 36: bus-stockholm-36-1065-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.917), Chatter(0.271), Outside, urban or manmade(0.149)
- **音频特征**: RMS=0.0102, 频谱重心=1181Hz, 场景提示=mixed_environment

### 样本 37: bus-stockholm-36-1086-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.813), Vehicle(0.411), Car(0.124)
- **音频特征**: RMS=0.0547, 频谱重心=388Hz, 场景提示=mixed_environment

### 样本 38: shopping_mall-lisbon-1176-44242-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.624), Vehicle(0.219)
- **音频特征**: RMS=0.0057, 频谱重心=1054Hz, 场景提示=quiet_indoor

### 样本 39: tram-prague-1184-44119-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.447), Train(0.399), Railroad car, train wagon(0.257)
- **音频特征**: RMS=0.0359, 频谱重心=413Hz, 场景提示=mixed_environment

### 样本 40: metro-vienna-59-1786-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.856), Rail transport(0.733), Railroad car, train wagon(0.701)
- **音频特征**: RMS=0.0153, 频谱重心=470Hz, 场景提示=mixed_environment

### 样本 41: shopping_mall-helsinki-129-3850-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.753), Animal(0.227), Mouse(0.163)
- **音频特征**: RMS=0.0027, 频谱重心=1458Hz, 场景提示=quiet_indoor

### 样本 42: tram-paris-192-5860-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.520)
- **音频特征**: RMS=0.0121, 频谱重心=529Hz, 场景提示=mixed_environment

### 样本 43: tram-vienna-285-8611-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.771), Music(0.329), Vehicle(0.182)
- **音频特征**: RMS=0.0166, 频谱重心=455Hz, 场景提示=mixed_environment

### 样本 44: public_square-lyon-1056-40449-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.780), Vehicle(0.152), Outside, urban or manmade(0.107)
- **音频特征**: RMS=0.0028, 频谱重心=1156Hz, 场景提示=quiet_indoor

### 样本 45: metro-stockholm-55-1624-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.711), Vehicle(0.153)
- **音频特征**: RMS=0.0142, 频谱重心=465Hz, 场景提示=mixed_environment

### 样本 46: airport-helsinki-4-201-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.479)
- **音频特征**: RMS=0.0016, 频谱重心=1144Hz, 场景提示=quiet_indoor

### 样本 47: airport-vienna-13-515-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Clip-clop(0.530), Horse(0.487), Animal(0.452)
- **音频特征**: RMS=0.0015, 频谱重心=1350Hz, 场景提示=quiet_indoor

### 样本 48: public_square-stockholm-119-3515-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.129), Mouse(0.108)
- **音频特征**: RMS=0.0044, 频谱重心=991Hz, 场景提示=quiet_indoor

### 样本 49: metro_station-paris-238-7063-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.662), Mouse(0.204), Animal(0.126)
- **音频特征**: RMS=0.0063, 频谱重心=2051Hz, 场景提示=mixed_environment

### 样本 50: shopping_mall-lyon-1196-45170-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.502), Music(0.186)
- **音频特征**: RMS=0.0021, 频谱重心=1193Hz, 场景提示=quiet_indoor

### 样本 51: shopping_mall-helsinki-255-7664-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.600), Music(0.148)
- **音频特征**: RMS=0.0037, 频谱重心=1238Hz, 场景提示=quiet_indoor

### 样本 52: public_square-paris-251-7520-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Church bell(0.710), Bell(0.356), Change ringing (campanology)(0.136)
- **音频特征**: RMS=0.0039, 频谱重心=1032Hz, 场景提示=quiet_indoor

### 样本 53: airport-london-205-6198-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.893), Outside, urban or manmade(0.222), Animal(0.203)
- **音频特征**: RMS=0.0018, 频谱重心=1705Hz, 场景提示=mixed_environment

### 样本 54: shopping_mall-stockholm-258-7829-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.797)
- **音频特征**: RMS=0.0025, 频谱重心=1049Hz, 场景提示=quiet_indoor

### 样本 55: metro-vienna-58-1728-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.610), Vehicle(0.236), Animal(0.112)
- **音频特征**: RMS=0.0080, 频谱重心=1014Hz, 场景提示=quiet_indoor

### 样本 56: airport-barcelona-1-64-a.wav
- **真实场景**: airport
- **AE预测**: metro
- **AS预测**: airport
- **检测到的事件**: Speech(0.925), Male speech, man speaking(0.436), Narration, monologue(0.296)
- **音频特征**: RMS=0.0095, 频谱重心=1275Hz, 场景提示=mixed_environment

### 样本 57: street_traffic-helsinki-166-5110-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_traffic
- **AS预测**: bus
- **检测到的事件**: Speech(0.657), Tick-tock(0.285), Vehicle(0.274)
- **音频特征**: RMS=0.0069, 频谱重心=783Hz, 场景提示=quiet_indoor

### 样本 58: metro-helsinki-222-6706-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.706), Animal(0.198), Vehicle(0.163)
- **音频特征**: RMS=0.0110, 频谱重心=1092Hz, 场景提示=mixed_environment

### 样本 59: airport-lisbon-1114-43732-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.709)
- **音频特征**: RMS=0.0045, 频谱重心=1589Hz, 场景提示=mixed_environment

### 样本 60: public_square-stockholm-120-3533-a.wav
- **真实场景**: public_square
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Speech(0.366), Vehicle(0.294), Animal(0.212)
- **音频特征**: RMS=0.0068, 频谱重心=828Hz, 场景提示=quiet_indoor

### 样本 61: public_square-stockholm-120-3551-a.wav
- **真实场景**: public_square
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Animal(0.207), Vehicle(0.189), Speech(0.151)
- **音频特征**: RMS=0.0084, 频谱重心=838Hz, 场景提示=quiet_indoor

### 样本 62: metro_station-lisbon-1221-45022-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.749)
- **音频特征**: RMS=0.0063, 频谱重心=1078Hz, 场景提示=quiet_indoor

### 样本 63: street_pedestrian-stockholm-155-4698-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.839), Animal(0.152), Clip-clop(0.152)
- **音频特征**: RMS=0.0054, 频谱重心=974Hz, 场景提示=quiet_indoor

### 样本 64: metro_station-lyon-1179-45234-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.771), Mouse(0.211), Music(0.134)
- **音频特征**: RMS=0.0034, 频谱重心=1362Hz, 场景提示=quiet_indoor

### 样本 65: street_traffic-lisbon-1076-43662-a.wav
- **真实场景**: street_traffic
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.254), Vehicle(0.124)
- **音频特征**: RMS=0.0023, 频谱重心=720Hz, 场景提示=quiet_indoor

### 样本 66: metro_station-prague-1019-41347-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.713), Clip-clop(0.131), Horse(0.117)
- **音频特征**: RMS=0.0036, 频谱重心=1191Hz, 场景提示=quiet_indoor

### 样本 67: tram-milan-1132-40320-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.484), Sliding door(0.392), Door(0.287)
- **音频特征**: RMS=0.0081, 频谱重心=965Hz, 场景提示=quiet_indoor

### 样本 68: shopping_mall-prague-1219-45209-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.799), Clip-clop(0.128), Basketball bounce(0.113)
- **音频特征**: RMS=0.0023, 频谱重心=1661Hz, 场景提示=mixed_environment

### 样本 69: metro_station-milan-1117-42816-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.441), Vehicle(0.141)
- **音频特征**: RMS=0.0078, 频谱重心=797Hz, 场景提示=quiet_indoor

### 样本 70: park-lyon-1144-41676-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.407), Animal(0.254), Mouse(0.187)
- **音频特征**: RMS=0.0008, 频谱重心=1061Hz, 场景提示=quiet_indoor

### 样本 71: metro-milan-1025-41648-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.752), Vehicle(0.245)
- **音频特征**: RMS=0.0088, 频谱重心=1291Hz, 场景提示=quiet_indoor

### 样本 72: metro_station-stockholm-84-2257-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.790), Animal(0.155), Clip-clop(0.123)
- **音频特征**: RMS=0.0044, 频谱重心=1383Hz, 场景提示=mixed_environment

### 样本 73: tram-lisbon-1100-41423-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.445), Car(0.122), Boat, Water vehicle(0.111)
- **音频特征**: RMS=0.0184, 频谱重心=1366Hz, 场景提示=mixed_environment

### 样本 74: metro-stockholm-227-6853-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.756), Bird(0.343), Pigeon, dove(0.238)
- **音频特征**: RMS=0.0155, 频谱重心=871Hz, 场景提示=mixed_environment

### 样本 75: airport-milan-1108-41690-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.855), Clip-clop(0.316), Horse(0.255)
- **音频特征**: RMS=0.0018, 频谱重心=1516Hz, 场景提示=mixed_environment

### 样本 76: shopping_mall-prague-1031-42692-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Silence(0.155)
- **音频特征**: RMS=0.0019, 频谱重心=1110Hz, 场景提示=quiet_indoor

### 样本 77: metro-stockholm-55-1639-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.691), Vehicle(0.380), Field recording(0.102)
- **音频特征**: RMS=0.0114, 频谱重心=493Hz, 场景提示=mixed_environment

### 样本 78: tram-lyon-1112-41121-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.661), Vehicle(0.252)
- **音频特征**: RMS=0.0085, 频谱重心=817Hz, 场景提示=quiet_indoor

### 样本 79: shopping_mall-london-256-7690-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.549)
- **音频特征**: RMS=0.0022, 频谱重心=1509Hz, 场景提示=mixed_environment

### 样本 80: bus-lyon-1129-43409-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.778), Vehicle(0.574), Car(0.227)
- **音频特征**: RMS=0.0171, 频谱重心=395Hz, 场景提示=mixed_environment

### 样本 81: street_pedestrian-london-149-4528-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.791)
- **音频特征**: RMS=0.0026, 频谱重心=1041Hz, 场景提示=quiet_indoor

### 样本 82: tram-milan-1182-44927-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Train(0.570), Vehicle(0.495), Rail transport(0.387)
- **音频特征**: RMS=0.0248, 频谱重心=1043Hz, 场景提示=mixed_environment

### 样本 83: metro_station-london-235-7025-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.844), Animal(0.162), Domestic animals, pets(0.105)
- **音频特征**: RMS=0.0047, 频谱重心=1462Hz, 场景提示=mixed_environment

### 样本 84: shopping_mall-barcelona-127-3780-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **音频特征**: RMS=0.0048, 频谱重心=1168Hz, 场景提示=quiet_indoor

### 样本 85: metro-paris-226-6817-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.720), Inside, small room(0.150)
- **音频特征**: RMS=0.0062, 频谱重心=959Hz, 场景提示=quiet_indoor

### 样本 86: tram-milan-1222-45592-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Speech(0.801), Vehicle(0.121), Animal(0.103)
- **音频特征**: RMS=0.0078, 频谱重心=1086Hz, 场景提示=quiet_indoor

### 样本 87: metro-milan-1218-44325-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.590), Sliding door(0.150), Music(0.129)
- **音频特征**: RMS=0.0098, 频谱重心=1044Hz, 场景提示=quiet_indoor

### 样本 88: metro_station-lisbon-1221-45759-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.793), Clip-clop(0.148), Vehicle(0.123)
- **音频特征**: RMS=0.0064, 频谱重心=856Hz, 场景提示=quiet_indoor

### 样本 89: street_pedestrian-london-263-7997-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Music(0.723), Speech(0.642), Clip-clop(0.378)
- **音频特征**: RMS=0.0032, 频谱重心=1260Hz, 场景提示=quiet_indoor

### 样本 90: metro_station-vienna-86-2344-a.wav
- **真实场景**: metro_station
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.498), Field recording(0.268), Speech(0.245)
- **音频特征**: RMS=0.0192, 频谱重心=395Hz, 场景提示=mixed_environment

### 样本 91: bus-milan-1180-44182-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.391), Vehicle(0.236)
- **音频特征**: RMS=0.0446, 频谱重心=658Hz, 场景提示=mixed_environment

### 样本 92: metro_station-paris-236-7043-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Music(0.785), Orchestra(0.331), Musical instrument(0.294)
- **音频特征**: RMS=0.0062, 频谱重心=1443Hz, 场景提示=mixed_environment

### 样本 93: shopping_mall-prague-1219-44728-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.326), Music(0.266)
- **音频特征**: RMS=0.0027, 频谱重心=1423Hz, 场景提示=mixed_environment

### 样本 94: metro-barcelona-41-1237-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Train(0.401), Vehicle(0.325), Railroad car, train wagon(0.280)
- **音频特征**: RMS=0.0153, 频谱重心=752Hz, 场景提示=mixed_environment

### 样本 95: shopping_mall-stockholm-136-4118-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.716)
- **音频特征**: RMS=0.0035, 频谱重心=950Hz, 场景提示=quiet_indoor

### 样本 96: tram-milan-1036-40090-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.545), Sliding door(0.226), Vehicle(0.201)
- **音频特征**: RMS=0.0088, 频谱重心=1010Hz, 场景提示=quiet_indoor

### 样本 97: metro-helsinki-222-6721-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.806), Vehicle(0.227), Animal(0.143)
- **音频特征**: RMS=0.0125, 频谱重心=947Hz, 场景提示=mixed_environment

### 样本 98: shopping_mall-barcelona-127-3776-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.446), Animal(0.132), Vehicle(0.109)
- **音频特征**: RMS=0.0023, 频谱重心=1436Hz, 场景提示=mixed_environment

### 样本 99: metro-london-48-1489-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.733), Vehicle(0.604), Train(0.189)
- **音频特征**: RMS=0.0161, 频谱重心=658Hz, 场景提示=mixed_environment

### 样本 100: shopping_mall-prague-1053-40075-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.835), Outside, urban or manmade(0.160), Clip-clop(0.145)
- **音频特征**: RMS=0.0037, 频谱重心=1282Hz, 场景提示=quiet_indoor

### 样本 101: shopping_mall-prague-1053-40935-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.328), Animal(0.208), Music(0.152)
- **音频特征**: RMS=0.0034, 频谱重心=1418Hz, 场景提示=quiet_indoor

### 样本 102: airport-barcelona-1-78-a.wav
- **真实场景**: airport
- **AE预测**: metro
- **AS预测**: airport
- **检测到的事件**: Speech(0.922), Male speech, man speaking(0.332), Clip-clop(0.217)
- **音频特征**: RMS=0.0088, 频谱重心=1298Hz, 场景提示=mixed_environment

### 样本 103: metro_station-milan-1187-44931-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.802), Music(0.173)
- **音频特征**: RMS=0.0055, 频谱重心=983Hz, 场景提示=quiet_indoor

### 样本 104: tram-stockholm-197-5938-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.748), Vehicle(0.372), Music(0.213)
- **音频特征**: RMS=0.0320, 频谱重心=531Hz, 场景提示=mixed_environment

### 样本 105: airport-stockholm-207-6306-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.705), Vehicle(0.218), Clip-clop(0.198)
- **音频特征**: RMS=0.0045, 频谱重心=1337Hz, 场景提示=quiet_indoor

### 样本 106: street_pedestrian-prague-1037-40957-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.861), Chatter(0.132), Animal(0.105)
- **音频特征**: RMS=0.0022, 频谱重心=1440Hz, 场景提示=mixed_environment

### 样本 107: tram-milan-1048-43830-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: park
- **检测到的事件**: Tick(0.196), Tick-tock(0.189), Silence(0.113)
- **音频特征**: RMS=0.0022, 频谱重心=1161Hz, 场景提示=quiet_indoor

### 样本 108: street_pedestrian-lisbon-1004-44015-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.552), Animal(0.104)
- **音频特征**: RMS=0.0023, 频谱重心=1177Hz, 场景提示=quiet_indoor

### 样本 109: shopping_mall-prague-1219-45542-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.744), Music(0.320), Chink, clink(0.138)
- **音频特征**: RMS=0.0024, 频谱重心=1556Hz, 场景提示=mixed_environment

### 样本 110: bus-lyon-1159-43767-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.844), Vehicle(0.204)
- **音频特征**: RMS=0.0157, 频谱重心=732Hz, 场景提示=mixed_environment

### 样本 111: street_pedestrian-stockholm-155-4708-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.732), Animal(0.222), Clip-clop(0.192)
- **音频特征**: RMS=0.0056, 频谱重心=929Hz, 场景提示=quiet_indoor

### 样本 112: park-prague-1185-45741-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Rain(0.271), Rain on surface(0.263), Raindrop(0.242)
- **音频特征**: RMS=0.0056, 频谱重心=2410Hz, 场景提示=mixed_environment

### 样本 113: park-prague-1185-44690-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Vehicle(0.369), Speech(0.143)
- **音频特征**: RMS=0.0060, 频谱重心=567Hz, 场景提示=quiet_indoor

### 样本 114: shopping_mall-helsinki-255-7655-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.819), Animal(0.169), Clip-clop(0.159)
- **音频特征**: RMS=0.0072, 频谱重心=1369Hz, 场景提示=mixed_environment

### 样本 115: tram-milan-1036-42743-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.644), Train(0.463), Vehicle(0.452)
- **音频特征**: RMS=0.0230, 频谱重心=640Hz, 场景提示=mixed_environment

### 样本 116: metro_station-london-72-2057-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.808)
- **音频特征**: RMS=0.0022, 频谱重心=1840Hz, 场景提示=mixed_environment

### 样本 117: public_square-prague-1152-42445-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.684), Vehicle(0.254), Boat, Water vehicle(0.161)
- **音频特征**: RMS=0.0023, 频谱重心=1327Hz, 场景提示=mixed_environment

### 样本 118: street_pedestrian-vienna-160-4881-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.774), Animal(0.240), Clip-clop(0.218)
- **音频特征**: RMS=0.0027, 频谱重心=1245Hz, 场景提示=quiet_indoor

### 样本 119: street_pedestrian-barcelona-142-4321-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.846), Clip-clop(0.122), Animal(0.115)
- **音频特征**: RMS=0.0027, 频谱重心=1771Hz, 场景提示=mixed_environment

### 样本 120: bus-lisbon-1156-40685-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.729), Vehicle(0.484), Car(0.109)
- **音频特征**: RMS=0.0161, 频谱重心=877Hz, 场景提示=mixed_environment

### 样本 121: street_pedestrian-milan-1205-44980-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.621)
- **音频特征**: RMS=0.0014, 频谱重心=1417Hz, 场景提示=quiet_indoor

### 样本 122: shopping_mall-vienna-259-7879-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.828), Animal(0.264), Clip-clop(0.249)
- **音频特征**: RMS=0.0034, 频谱重心=1226Hz, 场景提示=quiet_indoor

### 样本 123: metro-lyon-1126-43441-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.621)
- **音频特征**: RMS=0.0130, 频谱重心=720Hz, 场景提示=mixed_environment

### 样本 124: airport-vienna-13-525-a.wav
- **真实场景**: airport
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.871), Male speech, man speaking(0.277), Narration, monologue(0.175)
- **音频特征**: RMS=0.0042, 频谱重心=1172Hz, 场景提示=quiet_indoor

### 样本 125: metro_station-lisbon-1021-42689-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.436), Vehicle(0.287)
- **音频特征**: RMS=0.0046, 频谱重心=844Hz, 场景提示=quiet_indoor

### 样本 126: public_square-paris-118-3448-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.415), Animal(0.207), Walk, footsteps(0.146)
- **音频特征**: RMS=0.0024, 频谱重心=1270Hz, 场景提示=quiet_indoor

### 样本 127: public_square-milan-1074-40820-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.757), Music(0.332), Animal(0.209)
- **音频特征**: RMS=0.0043, 频谱重心=1146Hz, 场景提示=quiet_indoor

### 样本 128: metro_station-london-73-2076-a.wav
- **真实场景**: metro_station
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.289), White noise(0.108)
- **音频特征**: RMS=0.0205, 频谱重心=1287Hz, 场景提示=mixed_environment

### 样本 129: street_pedestrian-milan-1096-40172-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.808), Clip-clop(0.333), Horse(0.277)
- **音频特征**: RMS=0.0038, 频谱重心=1135Hz, 场景提示=quiet_indoor

### 样本 130: shopping_mall-helsinki-130-3905-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.859), Chatter(0.132), Outside, urban or manmade(0.124)
- **音频特征**: RMS=0.0028, 频谱重心=1471Hz, 场景提示=mixed_environment

### 样本 131: airport-barcelona-1-32-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.761), Run(0.158), Vehicle(0.127)
- **音频特征**: RMS=0.0031, 频谱重心=1291Hz, 场景提示=quiet_indoor

### 样本 132: metro-barcelona-220-6638-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.702), Vehicle(0.417), Bus(0.109)
- **音频特征**: RMS=0.0153, 频谱重心=912Hz, 场景提示=mixed_environment

### 样本 133: shopping_mall-paris-134-4043-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Animal(0.185), Mouse(0.109)
- **音频特征**: RMS=0.0017, 频谱重心=1094Hz, 场景提示=quiet_indoor

### 样本 134: airport-vienna-13-558-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.242)
- **音频特征**: RMS=0.0011, 频谱重心=1498Hz, 场景提示=mixed_environment

### 样本 135: airport-paris-206-6272-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.276), Train(0.170), Vehicle(0.106)
- **音频特征**: RMS=0.0060, 频谱重心=775Hz, 场景提示=quiet_indoor

### 样本 136: metro_station-lyon-1179-44301-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.628), Music(0.550)
- **音频特征**: RMS=0.0033, 频谱重心=1414Hz, 场景提示=quiet_indoor

### 样本 137: street_pedestrian-lisbon-1098-41288-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.760), Chink, clink(0.208)
- **音频特征**: RMS=0.0028, 频谱重心=1460Hz, 场景提示=mixed_environment

### 样本 138: tram-barcelona-179-5534-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.327), Vehicle(0.312), Train(0.226)
- **音频特征**: RMS=0.0128, 频谱重心=602Hz, 场景提示=mixed_environment

### 样本 139: airport-london-205-6180-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.787), Clip-clop(0.327), Horse(0.264)
- **音频特征**: RMS=0.0015, 频谱重心=1605Hz, 场景提示=mixed_environment

### 样本 140: shopping_mall-paris-134-4062-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.460), Animal(0.152)
- **音频特征**: RMS=0.0019, 频谱重心=1115Hz, 场景提示=quiet_indoor

### 样本 141: airport-lyon-1101-41603-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.150)
- **音频特征**: RMS=0.0017, 频谱重心=1377Hz, 场景提示=quiet_indoor

### 样本 142: airport-lyon-1169-44279-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.713), Clip-clop(0.163), Animal(0.116)
- **音频特征**: RMS=0.0035, 频谱重心=1455Hz, 场景提示=mixed_environment

### 样本 143: metro-lyon-1126-42110-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.532), Speech(0.472), Vehicle(0.345)
- **音频特征**: RMS=0.0166, 频谱重心=864Hz, 场景提示=mixed_environment

### 样本 144: shopping_mall-lyon-1196-45202-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.687), Music(0.288)
- **音频特征**: RMS=0.0022, 频谱重心=1424Hz, 场景提示=quiet_indoor

### 样本 145: public_square-vienna-124-3686-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.754), Vehicle(0.146), Animal(0.115)
- **音频特征**: RMS=0.0021, 频谱重心=1164Hz, 场景提示=quiet_indoor

### 样本 146: airport-milan-1061-40921-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.781), Clip-clop(0.160), Animal(0.156)
- **音频特征**: RMS=0.0027, 频谱重心=2033Hz, 场景提示=mixed_environment

### 样本 147: bus-paris-214-6519-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.634)
- **音频特征**: RMS=0.0096, 频谱重心=961Hz, 场景提示=quiet_indoor

### 样本 148: street_pedestrian-vienna-158-4818-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.514)
- **音频特征**: RMS=0.0012, 频谱重心=1312Hz, 场景提示=quiet_indoor

### 样本 149: street_pedestrian-helsinki-146-4412-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.338), Music(0.224)
- **音频特征**: RMS=0.0038, 频谱重心=1089Hz, 场景提示=quiet_indoor

### 样本 150: metro_station-vienna-88-2428-a.wav
- **真实场景**: metro_station
- **AE预测**: public_square
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.135), Silence(0.106)
- **音频特征**: RMS=0.0076, 频谱重心=740Hz, 场景提示=quiet_indoor

### 样本 151: airport-milan-1172-44819-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.848), Run(0.338), Outside, urban or manmade(0.182)
- **音频特征**: RMS=0.0032, 频谱重心=1371Hz, 场景提示=mixed_environment

### 样本 152: airport-lyon-1095-42617-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.667), Clip-clop(0.275), Horse(0.217)
- **音频特征**: RMS=0.0016, 频谱重心=1305Hz, 场景提示=quiet_indoor

### 样本 153: shopping_mall-london-131-3927-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.371), Chink, clink(0.235), Music(0.139)
- **音频特征**: RMS=0.0021, 频谱重心=1269Hz, 场景提示=quiet_indoor

### 样本 154: shopping_mall-helsinki-128-3818-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.650)
- **音频特征**: RMS=0.0025, 频谱重心=1100Hz, 场景提示=mixed_environment

### 样本 155: shopping_mall-prague-1219-45378-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.781), Clip-clop(0.197), Horse(0.179)
- **音频特征**: RMS=0.0021, 频谱重心=1723Hz, 场景提示=mixed_environment

### 样本 156: shopping_mall-vienna-259-7874-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.860), Clip-clop(0.164), Animal(0.131)
- **音频特征**: RMS=0.0036, 频谱重心=1242Hz, 场景提示=quiet_indoor

### 样本 157: shopping_mall-vienna-139-4235-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Bow-wow(0.594), Animal(0.495), Dog(0.471)
- **音频特征**: RMS=0.0032, 频谱重心=1356Hz, 场景提示=mixed_environment

### 样本 158: shopping_mall-london-256-7736-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.399), Animal(0.306), Emergency vehicle(0.293)
- **音频特征**: RMS=0.0029, 频谱重心=1539Hz, 场景提示=mixed_environment

### 样本 159: street_pedestrian-milan-1205-44656-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.477), Music(0.170), Animal(0.115)
- **音频特征**: RMS=0.0015, 频谱重心=1352Hz, 场景提示=quiet_indoor

### 样本 160: street_traffic-milan-1202-44428-a.wav
- **真实场景**: street_traffic
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Silence(0.184)
- **音频特征**: RMS=0.0021, 频谱重心=1063Hz, 场景提示=quiet_indoor

### 样本 161: metro_station-milan-1127-42367-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.830), Clip-clop(0.112), Animal(0.109)
- **音频特征**: RMS=0.0034, 频谱重心=1367Hz, 场景提示=mixed_environment

### 样本 162: public_square-paris-117-3419-a.wav
- **真实场景**: public_square
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Speech(0.532), Vehicle(0.358), Boat, Water vehicle(0.170)
- **音频特征**: RMS=0.0053, 频谱重心=1006Hz, 场景提示=quiet_indoor

### 样本 163: street_pedestrian-paris-265-8035-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Animal(0.221), Walk, footsteps(0.154), Patter(0.152)
- **音频特征**: RMS=0.0010, 频谱重心=1674Hz, 场景提示=quiet_indoor

### 样本 164: street_pedestrian-paris-265-8052-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.715)
- **音频特征**: RMS=0.0014, 频谱重心=1664Hz, 场景提示=quiet_indoor

### 样本 165: metro_station-barcelona-61-1824-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.598), Speech(0.180), Car(0.147)
- **音频特征**: RMS=0.0135, 频谱重心=618Hz, 场景提示=mixed_environment

### 样本 166: shopping_mall-london-256-7749-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.283), Vehicle(0.134)
- **音频特征**: RMS=0.0024, 频谱重心=1447Hz, 场景提示=mixed_environment

### 样本 167: metro-paris-54-1568-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.420), Speech(0.386), Train(0.135)
- **音频特征**: RMS=0.0121, 频谱重心=619Hz, 场景提示=mixed_environment

### 样本 168: metro_station-paris-82-2207-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.741), Clip-clop(0.312), Animal(0.244)
- **音频特征**: RMS=0.0049, 频谱重心=1696Hz, 场景提示=mixed_environment

### 样本 169: metro-milan-1197-45069-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.831), Rail transport(0.719), Subway, metro, underground(0.672)
- **音频特征**: RMS=0.0582, 频谱重心=1186Hz, 场景提示=mixed_environment

### 样本 170: metro-milan-1197-45256-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.808), Vehicle(0.654), Aircraft(0.356)
- **音频特征**: RMS=0.0728, 频谱重心=722Hz, 场景提示=mixed_environment

### 样本 171: tram-vienna-200-6031-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.656), Music(0.440), Vehicle(0.141)
- **音频特征**: RMS=0.0133, 频谱重心=663Hz, 场景提示=mixed_environment

### 样本 172: metro_station-prague-1170-44909-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: public_square
- **检测到的事件**: Train(0.589), Vehicle(0.497), Railroad car, train wagon(0.411)
- **音频特征**: RMS=0.0177, 频谱重心=490Hz, 场景提示=mixed_environment

### 样本 173: metro-helsinki-222-6737-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro_station
- **检测到的事件**: Cupboard open or close(0.272), Sliding door(0.272), Vehicle(0.202)
- **音频特征**: RMS=0.0147, 频谱重心=681Hz, 场景提示=mixed_environment

### 样本 174: metro-london-48-1493-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.725), Rail transport(0.584), Railroad car, train wagon(0.544)
- **音频特征**: RMS=0.0355, 频谱重心=605Hz, 场景提示=mixed_environment

### 样本 175: shopping_mall-vienna-138-4195-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.857), Vehicle(0.119), Animal(0.110)
- **音频特征**: RMS=0.0042, 频谱重心=1450Hz, 场景提示=mixed_environment

### 样本 176: metro_station-paris-238-7064-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.815)
- **音频特征**: RMS=0.0038, 频谱重心=1324Hz, 场景提示=quiet_indoor

### 样本 177: metro-paris-226-6816-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.477), Train(0.470), Rail transport(0.301)
- **音频特征**: RMS=0.0080, 频谱重心=708Hz, 场景提示=quiet_indoor

### 样本 178: bus-vienna-39-1180-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.744), Children playing(0.160), Child speech, kid speaking(0.148)
- **音频特征**: RMS=0.0073, 频谱重心=1183Hz, 场景提示=quiet_indoor

### 样本 179: metro_station-milan-1187-45143-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Music(0.652), Speech(0.591), Vehicle(0.172)
- **音频特征**: RMS=0.0138, 频谱重心=754Hz, 场景提示=mixed_environment

### 样本 180: street_traffic-paris-172-5278-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.167), Animal(0.129), Honk(0.121)
- **音频特征**: RMS=0.0027, 频谱重心=1351Hz, 场景提示=quiet_indoor

### 样本 181: metro_station-london-72-2064-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.415), Vehicle(0.130), Music(0.109)
- **音频特征**: RMS=0.0032, 频谱重心=1491Hz, 场景提示=mixed_environment

### 样本 182: shopping_mall-barcelona-254-7624-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.614)
- **音频特征**: RMS=0.0029, 频谱重心=1292Hz, 场景提示=mixed_environment

### 样本 183: metro_station-london-233-6997-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.662), Music(0.145)
- **音频特征**: RMS=0.0029, 频谱重心=1720Hz, 场景提示=mixed_environment

### 样本 184: park-barcelona-241-7162-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.154)
- **音频特征**: RMS=0.0019, 频谱重心=856Hz, 场景提示=quiet_indoor

### 样本 185: park-lisbon-1104-41022-a.wav
- **真实场景**: park
- **AE预测**: street_pedestrian
- **AS预测**: park
- **检测到的事件**: Animal(0.120), Silence(0.118)
- **音频特征**: RMS=0.0013, 频谱重心=1178Hz, 场景提示=quiet_indoor

### 样本 186: metro_station-barcelona-63-1895-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.189)
- **音频特征**: RMS=0.0198, 频谱重心=1174Hz, 场景提示=mixed_environment

### 样本 187: tram-milan-1132-41888-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.715), Speech(0.580), Rail transport(0.540)
- **音频特征**: RMS=0.0221, 频谱重心=578Hz, 场景提示=mixed_environment

### 样本 188: public_square-prague-1192-45104-a.wav
- **真实场景**: public_square
- **AE预测**: metro_station
- **AS预测**: public_square
- **检测到的事件**: Speech(0.823), Vehicle(0.259), Clip-clop(0.132)
- **音频特征**: RMS=0.0132, 频谱重心=562Hz, 场景提示=mixed_environment

### 样本 189: airport-paris-7-307-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.393)
- **音频特征**: RMS=0.0022, 频谱重心=1294Hz, 场景提示=quiet_indoor

### 样本 190: airport-london-6-275-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.278), Vehicle(0.155)
- **音频特征**: RMS=0.0019, 频谱重心=1214Hz, 场景提示=quiet_indoor

### 样本 191: metro_station-milan-1187-44755-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.717), Mouse(0.107), Animal(0.104)
- **音频特征**: RMS=0.0057, 频谱重心=973Hz, 场景提示=quiet_indoor

### 样本 192: street_pedestrian-paris-154-4668-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Clip-clop(0.272), Animal(0.258), Horse(0.248)
- **音频特征**: RMS=0.0013, 频谱重心=1521Hz, 场景提示=mixed_environment

### 样本 193: metro_station-stockholm-85-2315-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Animal(0.437), Speech(0.399), Horse(0.353)
- **音频特征**: RMS=0.0119, 频谱重心=1436Hz, 场景提示=mixed_environment

### 样本 194: metro_station-london-76-2110-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.870), Children playing(0.541), Child speech, kid speaking(0.452)
- **音频特征**: RMS=0.0046, 频谱重心=1455Hz, 场景提示=mixed_environment

### 样本 195: street_pedestrian-london-150-4553-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.854), Run(0.228), Animal(0.188)
- **音频特征**: RMS=0.0039, 频谱重心=1416Hz, 场景提示=quiet_indoor

### 样本 196: metro_station-stockholm-239-7086-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.840)
- **音频特征**: RMS=0.0047, 频谱重心=1108Hz, 场景提示=quiet_indoor

### 样本 197: shopping_mall-prague-1219-45375-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.778)
- **音频特征**: RMS=0.0025, 频谱重心=1468Hz, 场景提示=mixed_environment

### 样本 198: bus-lyon-1129-40641-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.632), Vehicle(0.280), Bus(0.120)
- **音频特征**: RMS=0.0186, 频谱重心=667Hz, 场景提示=mixed_environment

### 样本 199: metro-barcelona-220-6636-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.784), Music(0.169), Vehicle(0.106)
- **音频特征**: RMS=0.0107, 频谱重心=1354Hz, 场景提示=mixed_environment

### 样本 200: bus-milan-1115-41857-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.633), Vehicle(0.209)
- **音频特征**: RMS=0.0136, 频谱重心=1196Hz, 场景提示=mixed_environment

### 样本 201: street_traffic-stockholm-273-8322-a.wav
- **真实场景**: street_traffic
- **AE预测**: bus
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.786), Vehicle(0.505), Car(0.146)
- **音频特征**: RMS=0.0171, 频谱重心=1032Hz, 场景提示=mixed_environment

### 样本 202: metro-helsinki-222-6702-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.726), Vehicle(0.340), Music(0.225)
- **音频特征**: RMS=0.0203, 频谱重心=699Hz, 场景提示=mixed_environment

### 样本 203: metro-barcelona-220-6659-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.768), Vehicle(0.332), Train(0.100)
- **音频特征**: RMS=0.0267, 频谱重心=762Hz, 场景提示=mixed_environment

### 样本 204: metro_station-prague-1019-42788-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Silence(0.130)
- **音频特征**: RMS=0.0019, 频谱重心=1001Hz, 场景提示=quiet_indoor

### 样本 205: street_pedestrian-barcelona-261-7923-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: metro_station
- **AS预测**: park
- **检测到的事件**: Speech(0.532), Animal(0.225)
- **音频特征**: RMS=0.0033, 频谱重心=1126Hz, 场景提示=quiet_indoor

### 样本 206: public_square-stockholm-119-3484-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Bicycle(0.380), Vehicle(0.280), Speech(0.194)
- **音频特征**: RMS=0.0046, 频谱重心=1515Hz, 场景提示=quiet_indoor

### 样本 207: metro_station-prague-1170-44911-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.166)
- **音频特征**: RMS=0.0059, 频谱重心=899Hz, 场景提示=quiet_indoor

### 样本 208: street_traffic-paris-272-8291-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.640), Clip-clop(0.406), Horse(0.365)
- **音频特征**: RMS=0.0028, 频谱重心=1286Hz, 场景提示=quiet_indoor

### 样本 209: airport-lyon-1041-42920-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.550)
- **音频特征**: RMS=0.0022, 频谱重心=1078Hz, 场景提示=quiet_indoor

### 样本 210: street_traffic-london-270-8213-a.wav
- **真实场景**: street_traffic
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.756), Vehicle(0.264)
- **音频特征**: RMS=0.0079, 频谱重心=1222Hz, 场景提示=quiet_indoor

### 样本 211: metro-helsinki-43-1320-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.626), Vehicle(0.500), Train(0.367)
- **音频特征**: RMS=0.0087, 频谱重心=920Hz, 场景提示=quiet_indoor

### 样本 212: airport-lisbon-1000-40073-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: airport
- **检测到的事件**: Speech(0.846)
- **音频特征**: RMS=0.0048, 频谱重心=1541Hz, 场景提示=mixed_environment

### 样本 213: street_pedestrian-helsinki-148-4494-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Silence(0.138), Inside, small room(0.103)
- **音频特征**: RMS=0.0015, 频谱重心=1257Hz, 场景提示=quiet_indoor

### 样本 214: tram-lyon-1225-44849-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.715), Bird(0.268), Vehicle(0.267)
- **音频特征**: RMS=0.0105, 频谱重心=937Hz, 场景提示=mixed_environment

### 样本 215: street_pedestrian-milan-1080-43498-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Silence(0.218), Speech(0.152)
- **音频特征**: RMS=0.0016, 频谱重心=1017Hz, 场景提示=quiet_indoor

### 样本 216: shopping_mall-prague-1219-45744-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.812), Basketball bounce(0.122), Animal(0.110)
- **音频特征**: RMS=0.0024, 频谱重心=1621Hz, 场景提示=mixed_environment

### 样本 217: metro_station-stockholm-239-7096-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.358), Animal(0.308), Clip-clop(0.293)
- **音频特征**: RMS=0.0031, 频谱重心=1158Hz, 场景提示=quiet_indoor

### 样本 218: shopping_mall-prague-1053-42630-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Animal(0.183), Speech(0.150), Music(0.133)
- **音频特征**: RMS=0.0035, 频谱重心=1560Hz, 场景提示=mixed_environment

### 样本 219: airport-london-6-289-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.762), Clip-clop(0.266), Animal(0.237)
- **音频特征**: RMS=0.0026, 频谱重心=1203Hz, 场景提示=quiet_indoor

### 样本 220: airport-lisbon-1122-41837-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Speech(0.479), Vehicle(0.341), Boat, Water vehicle(0.119)
- **音频特征**: RMS=0.0040, 频谱重心=1379Hz, 场景提示=mixed_environment

### 样本 221: street_traffic-stockholm-173-5303-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Clip-clop(0.292), Horse(0.256), Animal(0.241)
- **音频特征**: RMS=0.0089, 频谱重心=870Hz, 场景提示=quiet_indoor

### 样本 222: airport-stockholm-12-498-a.wav
- **真实场景**: airport
- **AE预测**: tram
- **AS预测**: airport
- **检测到的事件**: Speech(0.872), Chatter(0.117), Animal(0.107)
- **音频特征**: RMS=0.0040, 频谱重心=968Hz, 场景提示=quiet_indoor

### 样本 223: metro_station-stockholm-239-7107-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.214), Inside, small room(0.168), Animal(0.162)
- **音频特征**: RMS=0.0036, 频谱重心=1198Hz, 场景提示=quiet_indoor

### 样本 224: metro-milan-1062-41974-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.282), Train(0.163), Rail transport(0.104)
- **音频特征**: RMS=0.0078, 频谱重心=903Hz, 场景提示=quiet_indoor

### 样本 225: metro_station-prague-1118-41592-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.403), Speech(0.293), Train(0.165)
- **音频特征**: RMS=0.0174, 频谱重心=833Hz, 场景提示=mixed_environment

### 样本 226: tram-barcelona-181-5627-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.844), Vehicle(0.256)
- **音频特征**: RMS=0.0108, 频谱重心=1284Hz, 场景提示=mixed_environment

### 样本 227: street_pedestrian-vienna-267-8110-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Vehicle(0.134), Sliding door(0.121)
- **音频特征**: RMS=0.0042, 频谱重心=879Hz, 场景提示=quiet_indoor

### 样本 228: airport-stockholm-11-465-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.369)
- **音频特征**: RMS=0.0038, 频谱重心=1176Hz, 场景提示=quiet_indoor

### 样本 229: shopping_mall-helsinki-130-3904-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.849), Clip-clop(0.150), Animal(0.107)
- **音频特征**: RMS=0.0041, 频谱重心=1287Hz, 场景提示=mixed_environment

### 样本 230: metro-stockholm-57-1715-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.657), Vehicle(0.431), Train(0.185)
- **音频特征**: RMS=0.0139, 频谱重心=546Hz, 场景提示=mixed_environment

### 样本 231: public_square-paris-117-3421-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.270), Rain(0.146), Rain on surface(0.119)
- **音频特征**: RMS=0.0040, 频谱重心=924Hz, 场景提示=quiet_indoor

### 样本 232: metro-vienna-228-6868-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.693), Vehicle(0.198)
- **音频特征**: RMS=0.0086, 频谱重心=630Hz, 场景提示=quiet_indoor

### 样本 233: metro-stockholm-55-1636-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.727), Vehicle(0.191)
- **音频特征**: RMS=0.0135, 频谱重心=971Hz, 场景提示=mixed_environment

### 样本 234: tram-vienna-285-8628-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.643), Crow(0.127), Bird(0.122)
- **音频特征**: RMS=0.0123, 频谱重心=788Hz, 场景提示=mixed_environment

### 样本 235: shopping_mall-prague-1031-40056-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Music(0.105)
- **音频特征**: RMS=0.0047, 频谱重心=691Hz, 场景提示=quiet_indoor

### 样本 236: metro_station-london-76-2114-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.871), Children playing(0.225), Child speech, kid speaking(0.222)
- **音频特征**: RMS=0.0023, 频谱重心=1377Hz, 场景提示=quiet_indoor

### 样本 237: metro-stockholm-56-1650-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.750), Vehicle(0.298), Car(0.105)
- **音频特征**: RMS=0.0050, 频谱重心=729Hz, 场景提示=quiet_indoor

### 样本 238: metro_station-helsinki-232-6978-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.825), Clip-clop(0.277), Horse(0.209)
- **音频特征**: RMS=0.0050, 频谱重心=1166Hz, 场景提示=quiet_indoor

### 样本 239: bus-barcelona-16-649-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.355), Speech(0.180), Bird(0.151)
- **音频特征**: RMS=0.0109, 频谱重心=732Hz, 场景提示=mixed_environment

### 样本 240: airport-paris-206-6262-a.wav
- **真实场景**: airport
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.781), Narration, monologue(0.106)
- **音频特征**: RMS=0.0060, 频谱重心=1052Hz, 场景提示=quiet_indoor

### 样本 241: shopping_mall-stockholm-136-4129-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.283)
- **音频特征**: RMS=0.0033, 频谱重心=1090Hz, 场景提示=quiet_indoor

### 样本 242: metro-prague-1026-43278-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Train(0.771), Speech(0.636), Vehicle(0.592)
- **音频特征**: RMS=0.0451, 频谱重心=684Hz, 场景提示=mixed_environment

### 样本 243: tram-london-277-8438-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.612), Vehicle(0.543), Train(0.443)
- **音频特征**: RMS=0.0145, 频谱重心=868Hz, 场景提示=mixed_environment

### 样本 244: metro_station-barcelona-63-1883-a.wav
- **真实场景**: metro_station
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.286), White noise(0.140)
- **音频特征**: RMS=0.0389, 频谱重心=1020Hz, 场景提示=mixed_environment

### 样本 245: shopping_mall-paris-133-4019-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.713), Clip-clop(0.293), Animal(0.242)
- **音频特征**: RMS=0.0035, 频谱重心=1220Hz, 场景提示=quiet_indoor

### 样本 246: public_square-london-113-3293-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.706), Clip-clop(0.230), Animal(0.216)
- **音频特征**: RMS=0.0027, 频谱重心=1191Hz, 场景提示=quiet_indoor

### 样本 247: metro-barcelona-42-1288-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.216), Speech(0.192), Rail transport(0.145)
- **音频特征**: RMS=0.0110, 频谱重心=713Hz, 场景提示=mixed_environment

### 样本 248: street_pedestrian-barcelona-141-4295-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Speech(0.784), Vehicle(0.487), Outside, urban or manmade(0.128)
- **音频特征**: RMS=0.0092, 频谱重心=1420Hz, 场景提示=quiet_indoor

### 样本 249: tram-paris-195-5893-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.740), Vehicle(0.548), Music(0.262)
- **音频特征**: RMS=0.0410, 频谱重心=476Hz, 场景提示=mixed_environment

### 样本 250: bus-stockholm-218-6588-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.806), Vehicle(0.514), Car(0.206)
- **音频特征**: RMS=0.0402, 频谱重心=448Hz, 场景提示=mixed_environment

### 样本 251: street_pedestrian-stockholm-266-8072-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **音频特征**: RMS=0.0038, 频谱重心=1051Hz, 场景提示=quiet_indoor

### 样本 252: public_square-prague-1152-40734-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.669), Animal(0.214), Run(0.177)
- **音频特征**: RMS=0.0022, 频谱重心=1373Hz, 场景提示=mixed_environment

### 样本 253: metro_station-barcelona-63-1888-a.wav
- **真实场景**: metro_station
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: White noise(0.202), Vehicle(0.192)
- **音频特征**: RMS=0.0212, 频谱重心=1203Hz, 场景提示=mixed_environment

### 样本 254: tram-prague-1210-44576-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.617), Vehicle(0.552), Rail transport(0.426)
- **音频特征**: RMS=0.0260, 频谱重心=565Hz, 场景提示=mixed_environment

### 样本 255: bus-milan-1180-45238-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.783), Vehicle(0.357)
- **音频特征**: RMS=0.0135, 频谱重心=645Hz, 场景提示=mixed_environment

### 样本 256: tram-paris-195-5892-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.829), Vehicle(0.444), Car(0.122)
- **音频特征**: RMS=0.0079, 频谱重心=1055Hz, 场景提示=quiet_indoor

### 样本 257: street_pedestrian-london-263-7973-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.715), Animal(0.199)
- **音频特征**: RMS=0.0017, 频谱重心=1485Hz, 场景提示=quiet_indoor

### 样本 258: street_pedestrian-prague-1085-42175-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.717), Clip-clop(0.473), Horse(0.406)
- **音频特征**: RMS=0.0018, 频谱重心=1262Hz, 场景提示=quiet_indoor

### 样本 259: street_pedestrian-milan-1205-45228-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.737)
- **音频特征**: RMS=0.0014, 频谱重心=1383Hz, 场景提示=quiet_indoor

### 样本 260: airport-barcelona-1-63-a.wav
- **真实场景**: airport
- **AE预测**: metro
- **AS预测**: airport
- **检测到的事件**: Speech(0.936), Male speech, man speaking(0.254), Narration, monologue(0.111)
- **音频特征**: RMS=0.0081, 频谱重心=1389Hz, 场景提示=mixed_environment

### 样本 261: metro-paris-226-6814-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.454), Music(0.186), Door(0.174)
- **音频特征**: RMS=0.0090, 频谱重心=1148Hz, 场景提示=quiet_indoor

### 样本 262: metro_station-helsinki-64-1930-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.552), Vehicle(0.315)
- **音频特征**: RMS=0.0152, 频谱重心=828Hz, 场景提示=mixed_environment

### 样本 263: airport-london-6-294-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.289), Vehicle(0.121)
- **音频特征**: RMS=0.0021, 频谱重心=1158Hz, 场景提示=quiet_indoor

### 样本 264: metro-barcelona-41-1266-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Music(0.312), Singing bowl(0.117)
- **音频特征**: RMS=0.0133, 频谱重心=1208Hz, 场景提示=mixed_environment

### 样本 265: shopping_mall-helsinki-129-3868-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.783), Clip-clop(0.134), Animal(0.122)
- **音频特征**: RMS=0.0040, 频谱重心=1045Hz, 场景提示=quiet_indoor

### 样本 266: metro-lisbon-1148-42474-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.656), Train(0.354), Railroad car, train wagon(0.262)
- **音频特征**: RMS=0.0413, 频谱重心=975Hz, 场景提示=mixed_environment

### 样本 267: metro-paris-50-1519-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Music(0.184), Train(0.176), Vehicle(0.155)
- **音频特征**: RMS=0.0074, 频谱重心=1169Hz, 场景提示=quiet_indoor

### 样本 268: metro-london-223-6779-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.732), Vehicle(0.466), Music(0.410)
- **音频特征**: RMS=0.0117, 频谱重心=826Hz, 场景提示=mixed_environment

### 样本 269: metro-paris-52-1542-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.282), Train(0.274), Rail transport(0.178)
- **音频特征**: RMS=0.0158, 频谱重心=1189Hz, 场景提示=mixed_environment

### 样本 270: street_pedestrian-stockholm-156-4735-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.575), Animal(0.470), Clip-clop(0.458)
- **音频特征**: RMS=0.0083, 频谱重心=1014Hz, 场景提示=quiet_indoor

### 样本 271: metro-london-46-1381-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.702), Rail transport(0.544), Railroad car, train wagon(0.516)
- **音频特征**: RMS=0.0248, 频谱重心=1036Hz, 场景提示=mixed_environment

### 样本 272: tram-lyon-1112-41181-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.825), Vehicle(0.242)
- **音频特征**: RMS=0.0136, 频谱重心=492Hz, 场景提示=mixed_environment

### 样本 273: street_pedestrian-milan-1205-44672-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.803), Male speech, man speaking(0.111)
- **音频特征**: RMS=0.0010, 频谱重心=1216Hz, 场景提示=quiet_indoor

### 样本 274: public_square-stockholm-121-3590-a.wav
- **真实场景**: public_square
- **AE预测**: metro_station
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.277), Siren(0.257), Emergency vehicle(0.199)
- **音频特征**: RMS=0.0062, 频谱重心=877Hz, 场景提示=quiet_indoor

### 样本 275: public_square-vienna-122-3607-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.827), Animal(0.228), Run(0.221)
- **音频特征**: RMS=0.0009, 频谱重心=1264Hz, 场景提示=quiet_indoor

### 样本 276: airport-london-205-6233-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.825), Clip-clop(0.140), Animal(0.137)
- **音频特征**: RMS=0.0017, 频谱重心=1584Hz, 场景提示=mixed_environment

### 样本 277: public_square-lyon-1178-45576-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.787), Music(0.235), Animal(0.101)
- **音频特征**: RMS=0.0013, 频谱重心=1110Hz, 场景提示=quiet_indoor

### 样本 278: metro_station-london-235-7021-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.145), Speech(0.121), Train(0.118)
- **音频特征**: RMS=0.0032, 频谱重心=1389Hz, 场景提示=quiet_indoor

### 样本 279: tram-prague-1109-41241-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.482), Vehicle(0.180)
- **音频特征**: RMS=0.0058, 频谱重心=1124Hz, 场景提示=quiet_indoor

### 样本 280: metro-barcelona-220-6652-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.718), Vehicle(0.237), Music(0.131)
- **音频特征**: RMS=0.0089, 频谱重心=1088Hz, 场景提示=quiet_indoor

### 样本 281: shopping_mall-lisbon-1002-43065-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Vehicle(0.145)
- **音频特征**: RMS=0.0022, 频谱重心=1234Hz, 场景提示=mixed_environment

### 样本 282: metro_station-prague-1130-41020-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.513)
- **音频特征**: RMS=0.0045, 频谱重心=864Hz, 场景提示=quiet_indoor

### 样本 283: street_pedestrian-lisbon-1174-45739-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.871), Outside, urban or manmade(0.133)
- **音频特征**: RMS=0.0039, 频谱重心=1240Hz, 场景提示=quiet_indoor

### 样本 284: metro_station-prague-1019-41356-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.592), Animal(0.238), Vehicle(0.198)
- **音频特征**: RMS=0.0073, 频谱重心=961Hz, 场景提示=quiet_indoor

### 样本 285: public_square-prague-1192-44436-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.607), Animal(0.178), Clip-clop(0.169)
- **音频特征**: RMS=0.0029, 频谱重心=979Hz, 场景提示=quiet_indoor

### 样本 286: park-helsinki-242-7214-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.645), Animal(0.356), Bow-wow(0.165)
- **音频特征**: RMS=0.0024, 频谱重心=1041Hz, 场景提示=quiet_indoor

### 样本 287: street_pedestrian-milan-1005-41749-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.777), Animal(0.118), Clip-clop(0.103)
- **音频特征**: RMS=0.0021, 频谱重心=1182Hz, 场景提示=quiet_indoor

### 样本 288: public_square-milan-1074-43921-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.778), Run(0.193), Outside, urban or manmade(0.178)
- **音频特征**: RMS=0.0045, 频谱重心=969Hz, 场景提示=quiet_indoor

### 样本 289: tram-vienna-201-6075-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.619), Animal(0.120)
- **音频特征**: RMS=0.0040, 频谱重心=2623Hz, 场景提示=mixed_environment

### 样本 290: tram-lyon-1103-42890-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.820), Vehicle(0.312)
- **音频特征**: RMS=0.0074, 频谱重心=980Hz, 场景提示=quiet_indoor

### 样本 291: tram-london-277-8447-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.396), Speech(0.188), Train(0.185)
- **音频特征**: RMS=0.0063, 频谱重心=679Hz, 场景提示=quiet_indoor

### 样本 292: tram-paris-196-5924-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.722), Vehicle(0.275)
- **音频特征**: RMS=0.0069, 频谱重心=886Hz, 场景提示=quiet_indoor

### 样本 293: shopping_mall-lyon-1066-40452-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.184), Clip-clop(0.181), Horse(0.160)
- **音频特征**: RMS=0.0017, 频谱重心=1534Hz, 场景提示=mixed_environment

### 样本 294: metro_station-helsinki-66-1980-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Animal(0.208)
- **音频特征**: RMS=0.0013, 频谱重心=1521Hz, 场景提示=quiet_indoor

### 样本 295: bus-helsinki-211-6423-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Cupboard open or close(0.267), Sliding door(0.151), Vehicle(0.123)
- **音频特征**: RMS=0.0164, 频谱重心=873Hz, 场景提示=mixed_environment

### 样本 296: street_pedestrian-lyon-1047-42521-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.352), Animal(0.256), Domestic animals, pets(0.124)
- **音频特征**: RMS=0.0015, 频谱重心=1362Hz, 场景提示=quiet_indoor

### 样本 297: metro_station-paris-81-2185-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Animal(0.373), Clip-clop(0.232), Horse(0.223)
- **音频特征**: RMS=0.0030, 频谱重心=1547Hz, 场景提示=quiet_indoor

### 样本 298: street_traffic-vienna-176-5423-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_pedestrian
- **AS预测**: park
- **检测到的事件**: Silence(0.157)
- **音频特征**: RMS=0.0019, 频谱重心=840Hz, 场景提示=quiet_indoor

### 样本 299: metro-milan-1218-44775-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.710), Music(0.380), Vehicle(0.184)
- **音频特征**: RMS=0.0176, 频谱重心=803Hz, 场景提示=mixed_environment

### 样本 300: tram-barcelona-179-5523-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.633), Vehicle(0.315)
- **音频特征**: RMS=0.0092, 频谱重心=655Hz, 场景提示=quiet_indoor

### 样本 301: airport-stockholm-11-475-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.849), Outside, urban or manmade(0.113), Vehicle(0.106)
- **音频特征**: RMS=0.0051, 频谱重心=1245Hz, 场景提示=mixed_environment

### 样本 302: airport-stockholm-208-6346-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.703)
- **音频特征**: RMS=0.0058, 频谱重心=1123Hz, 场景提示=quiet_indoor

### 样本 303: metro_station-lisbon-1007-43992-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.809), Vehicle(0.190), Music(0.139)
- **音频特征**: RMS=0.0078, 频谱重心=873Hz, 场景提示=quiet_indoor

### 样本 304: metro_station-milan-1050-43057-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.792), Music(0.220), Vehicle(0.163)
- **音频特征**: RMS=0.0082, 频谱重心=777Hz, 场景提示=quiet_indoor

### 样本 305: public_square-vienna-122-3600-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.801), Clip-clop(0.282), Animal(0.233)
- **音频特征**: RMS=0.0012, 频谱重心=876Hz, 场景提示=quiet_indoor

### 样本 306: airport-milan-1108-43228-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.749), Clip-clop(0.146), Animal(0.145)
- **音频特征**: RMS=0.0018, 频谱重心=1401Hz, 场景提示=quiet_indoor

### 样本 307: metro_station-vienna-87-2369-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.734)
- **音频特征**: RMS=0.0037, 频谱重心=1064Hz, 场景提示=quiet_indoor

### 样本 308: airport-london-5-241-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.830), Clip-clop(0.200), Animal(0.182)
- **音频特征**: RMS=0.0011, 频谱重心=1406Hz, 场景提示=quiet_indoor

### 样本 309: bus-milan-1115-40220-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.612), Vehicle(0.373)
- **音频特征**: RMS=0.0137, 频谱重心=1155Hz, 场景提示=mixed_environment

### 样本 310: street_pedestrian-vienna-160-4882-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.836), Vehicle(0.165), Outside, urban or manmade(0.138)
- **音频特征**: RMS=0.0021, 频谱重心=1188Hz, 场景提示=quiet_indoor

### 样本 311: airport-london-5-223-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.735), Outside, urban or manmade(0.136), Run(0.113)
- **音频特征**: RMS=0.0013, 频谱重心=1572Hz, 场景提示=mixed_environment

### 样本 312: street_pedestrian-lyon-1047-41939-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.839), Clip-clop(0.159), Animal(0.158)
- **音频特征**: RMS=0.0022, 频谱重心=1453Hz, 场景提示=quiet_indoor

### 样本 313: tram-lisbon-1100-40171-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.310), Speech(0.213)
- **音频特征**: RMS=0.0183, 频谱重心=933Hz, 场景提示=mixed_environment

### 样本 314: bus-milan-1190-44132-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.764), Vehicle(0.331), Music(0.294)
- **音频特征**: RMS=0.0190, 频谱重心=689Hz, 场景提示=mixed_environment

### 样本 315: tram-london-279-8486-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.637), Vehicle(0.244), Music(0.217)
- **音频特征**: RMS=0.0140, 频谱重心=745Hz, 场景提示=mixed_environment

### 样本 316: metro_station-milan-1117-43730-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.564), Vehicle(0.160), Clip-clop(0.152)
- **音频特征**: RMS=0.0068, 频谱重心=943Hz, 场景提示=quiet_indoor

### 样本 317: bus-stockholm-35-1043-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.689), Vehicle(0.532), Bus(0.286)
- **音频特征**: RMS=0.0265, 频谱重心=584Hz, 场景提示=mixed_environment

### 样本 318: park-paris-99-2804-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.543), Run(0.192), Animal(0.179)
- **音频特征**: RMS=0.0020, 频谱重心=1369Hz, 场景提示=quiet_indoor

### 样本 319: public_square-prague-1152-43826-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.843), Animal(0.124), Outside, urban or manmade(0.111)
- **音频特征**: RMS=0.0030, 频谱重心=1223Hz, 场景提示=quiet_indoor

### 样本 320: street_pedestrian-vienna-160-4898-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.689), Animal(0.158), Single-lens reflex camera(0.152)
- **音频特征**: RMS=0.0018, 频谱重心=1343Hz, 场景提示=quiet_indoor

### 样本 321: shopping_mall-stockholm-258-7819-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.801), Chatter(0.140)
- **音频特征**: RMS=0.0030, 频谱重心=1239Hz, 场景提示=quiet_indoor

### 样本 322: tram-lyon-1150-41055-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.802), Music(0.411), Vehicle(0.360)
- **音频特征**: RMS=0.0050, 频谱重心=1332Hz, 场景提示=quiet_indoor

### 样本 323: tram-barcelona-180-5586-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.610), Music(0.240)
- **音频特征**: RMS=0.0133, 频谱重心=1254Hz, 场景提示=mixed_environment

### 样本 324: shopping_mall-london-256-7718-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.710), Clip-clop(0.372), Horse(0.292)
- **音频特征**: RMS=0.0022, 频谱重心=1411Hz, 场景提示=mixed_environment

### 样本 325: shopping_mall-helsinki-129-3858-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.459), Animal(0.251)
- **音频特征**: RMS=0.0048, 频谱重心=1007Hz, 场景提示=quiet_indoor

### 样本 326: airport-paris-9-396-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.365), Clip-clop(0.174), Horse(0.141)
- **音频特征**: RMS=0.0032, 频谱重心=1168Hz, 场景提示=quiet_indoor

### 样本 327: metro-stockholm-227-6839-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.883), Vehicle(0.248), Male speech, man speaking(0.113)
- **音频特征**: RMS=0.0118, 频谱重心=758Hz, 场景提示=mixed_environment

### 样本 328: metro_station-milan-1117-43162-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.435), Vehicle(0.223)
- **音频特征**: RMS=0.0073, 频谱重心=1016Hz, 场景提示=quiet_indoor

### 样本 329: bus-lyon-1129-43108-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.698), Vehicle(0.640), Car(0.193)
- **音频特征**: RMS=0.0084, 频谱重心=477Hz, 场景提示=quiet_indoor

### 样本 330: street_pedestrian-milan-1205-44244-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.265), Silence(0.148), Music(0.100)
- **音频特征**: RMS=0.0012, 频谱重心=1078Hz, 场景提示=quiet_indoor

### 样本 331: public_square-london-115-3345-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.857), Outside, urban or manmade(0.145), Vehicle(0.114)
- **音频特征**: RMS=0.0027, 频谱重心=1299Hz, 场景提示=quiet_indoor

### 样本 332: tram-vienna-285-8605-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.131)
- **音频特征**: RMS=0.0053, 频谱重心=764Hz, 场景提示=quiet_indoor

### 样本 333: public_square-paris-118-3470-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.532), Animal(0.428), Clip-clop(0.197)
- **音频特征**: RMS=0.0014, 频谱重心=1464Hz, 场景提示=quiet_indoor

### 样本 334: shopping_mall-lyon-1066-43777-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.365), Music(0.158)
- **音频特征**: RMS=0.0015, 频谱重心=1484Hz, 场景提示=mixed_environment

### 样本 335: tram-stockholm-199-5994-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.837), Vehicle(0.594), Car(0.290)
- **音频特征**: RMS=0.0228, 频谱重心=388Hz, 场景提示=mixed_environment

### 样本 336: metro_station-prague-1118-41156-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.282), Silence(0.144)
- **音频特征**: RMS=0.0015, 频谱重心=1224Hz, 场景提示=quiet_indoor

### 样本 337: tram-vienna-201-6084-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Tick-tock(0.206), Tick(0.176)
- **音频特征**: RMS=0.0057, 频谱重心=1648Hz, 场景提示=quiet_indoor

### 样本 338: bus-lisbon-1212-44366-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.500), Vehicle(0.468), Car(0.173)
- **音频特征**: RMS=0.0196, 频谱重心=965Hz, 场景提示=mixed_environment

### 样本 339: tram-vienna-200-6027-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.680), Vehicle(0.474)
- **音频特征**: RMS=0.0299, 频谱重心=349Hz, 场景提示=mixed_environment

### 样本 340: metro_station-barcelona-230-6920-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.335), Vehicle(0.107)
- **音频特征**: RMS=0.0039, 频谱重心=955Hz, 场景提示=quiet_indoor

### 样本 341: public_square-paris-251-7526-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Animal(0.193), Clip-clop(0.120), Horse(0.106)
- **音频特征**: RMS=0.0031, 频谱重心=892Hz, 场景提示=quiet_indoor

### 样本 342: shopping_mall-prague-1009-41691-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.730), Music(0.125), Vehicle(0.117)
- **音频特征**: RMS=0.0073, 频谱重心=1326Hz, 场景提示=quiet_indoor

### 样本 343: tram-barcelona-275-8401-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.411), Silence(0.151)
- **音频特征**: RMS=0.0132, 频谱重心=649Hz, 场景提示=mixed_environment

### 样本 344: airport-lisbon-1122-41270-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.183)
- **音频特征**: RMS=0.0039, 频谱重心=1239Hz, 场景提示=mixed_environment

### 样本 345: street_pedestrian-paris-264-8029-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.612), Animal(0.241), Horse(0.118)
- **音频特征**: RMS=0.0028, 频谱重心=1162Hz, 场景提示=quiet_indoor

### 样本 346: street_pedestrian-vienna-159-4862-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Music(0.808), Speech(0.537), Clip-clop(0.403)
- **音频特征**: RMS=0.0011, 频谱重心=1369Hz, 场景提示=quiet_indoor

### 样本 347: tram-helsinki-184-5711-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.511), Speech(0.494), Aircraft(0.190)
- **音频特征**: RMS=0.0138, 频谱重心=625Hz, 场景提示=mixed_environment

### 样本 348: tram-barcelona-275-8395-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.252), Train(0.172), Vehicle(0.171)
- **音频特征**: RMS=0.0334, 频谱重心=607Hz, 场景提示=mixed_environment

### 样本 349: airport-barcelona-203-6134-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.806), Clip-clop(0.603), Animal(0.553)
- **音频特征**: RMS=0.0021, 频谱重心=1264Hz, 场景提示=quiet_indoor

### 样本 350: tram-helsinki-184-5722-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.673), Vehicle(0.209)
- **音频特征**: RMS=0.0079, 频谱重心=723Hz, 场景提示=quiet_indoor

### 样本 351: bus-lyon-1159-42272-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.845), Vehicle(0.231), Outside, urban or manmade(0.105)
- **音频特征**: RMS=0.0125, 频谱重心=758Hz, 场景提示=mixed_environment

### 样本 352: tram-lisbon-1191-44241-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.744), Vehicle(0.489), Music(0.265)
- **音频特征**: RMS=0.0721, 频谱重心=690Hz, 场景提示=mixed_environment

### 样本 353: public_square-prague-1111-43361-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Silence(0.163)
- **音频特征**: RMS=0.0044, 频谱重心=1522Hz, 场景提示=quiet_indoor

### 样本 354: public_square-prague-1214-45077-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.870), Clip-clop(0.163), Animal(0.146)
- **音频特征**: RMS=0.0024, 频谱重心=1138Hz, 场景提示=quiet_indoor

### 样本 355: public_square-lyon-1178-45424-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.416), Animal(0.252), Clip-clop(0.183)
- **音频特征**: RMS=0.0016, 频谱重心=1182Hz, 场景提示=quiet_indoor

### 样本 356: street_pedestrian-lyon-1162-44579-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.542), Animal(0.267), Clip-clop(0.255)
- **音频特征**: RMS=0.0017, 频谱重心=1230Hz, 场景提示=quiet_indoor

### 样本 357: street_pedestrian-stockholm-157-4766-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.782), Clip-clop(0.244), Animal(0.202)
- **音频特征**: RMS=0.0042, 频谱重心=1123Hz, 场景提示=quiet_indoor

### 样本 358: public_square-prague-1111-42693-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.259), Vehicle(0.147)
- **音频特征**: RMS=0.0058, 频谱重心=1366Hz, 场景提示=quiet_indoor

### 样本 359: street_pedestrian-prague-1085-43483-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.830), Clip-clop(0.153), Horse(0.123)
- **音频特征**: RMS=0.0020, 频谱重心=1217Hz, 场景提示=quiet_indoor

### 样本 360: public_square-london-113-3276-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.841), Run(0.329), Animal(0.216)
- **音频特征**: RMS=0.0027, 频谱重心=1271Hz, 场景提示=quiet_indoor

### 样本 361: street_pedestrian-london-151-4576-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Animal(0.139)
- **音频特征**: RMS=0.0015, 频谱重心=1089Hz, 场景提示=quiet_indoor

### 样本 362: street_pedestrian-london-151-4592-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: tram
- **AS预测**: public_square
- **检测到的事件**: Alarm(0.425), Speech(0.226), Car alarm(0.218)
- **音频特征**: RMS=0.0032, 频谱重心=1752Hz, 场景提示=mixed_environment

### 样本 363: metro_station-lyon-1077-41563-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.403)
- **音频特征**: RMS=0.0070, 频谱重心=1354Hz, 场景提示=mixed_environment

### 样本 364: airport-prague-1173-44705-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.794), Music(0.614), Clip-clop(0.465)
- **音频特征**: RMS=0.0030, 频谱重心=1505Hz, 场景提示=mixed_environment

### 样本 365: metro-lyon-1149-41287-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.851), Vehicle(0.243)
- **音频特征**: RMS=0.0066, 频谱重心=1039Hz, 场景提示=quiet_indoor

### 样本 366: public_square-london-114-3324-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: airport
- **检测到的事件**: Speech(0.900), Male speech, man speaking(0.527), Narration, monologue(0.331)
- **音频特征**: RMS=0.0030, 频谱重心=1111Hz, 场景提示=quiet_indoor

### 样本 367: shopping_mall-prague-1219-44935-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.792), Inside, public space(0.111), Animal(0.103)
- **音频特征**: RMS=0.0028, 频谱重心=1429Hz, 场景提示=mixed_environment

### 样本 368: tram-milan-1222-44359-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.644), Vehicle(0.196)
- **音频特征**: RMS=0.0063, 频谱重心=947Hz, 场景提示=quiet_indoor

### 样本 369: metro-stockholm-57-1713-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.715), Vehicle(0.138), Zipper (clothing)(0.105)
- **音频特征**: RMS=0.0091, 频谱重心=935Hz, 场景提示=quiet_indoor

### 样本 370: tram-prague-1151-42944-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.523), Speech(0.368), Train(0.273)
- **音频特征**: RMS=0.0290, 频谱重心=730Hz, 场景提示=mixed_environment

### 样本 371: street_traffic-stockholm-175-5385-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.403), Speech(0.395), Wind noise (microphone)(0.238)
- **音频特征**: RMS=0.0302, 频谱重心=555Hz, 场景提示=mixed_environment

### 样本 372: airport-milan-1108-43786-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.779)
- **音频特征**: RMS=0.0020, 频谱重心=1610Hz, 场景提示=mixed_environment

### 样本 373: street_pedestrian-barcelona-260-7904-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.436), Animal(0.176), Clip-clop(0.110)
- **音频特征**: RMS=0.0025, 频谱重心=1908Hz, 场景提示=mixed_environment

### 样本 374: street_pedestrian-prague-1227-45094-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.911), Run(0.694), Clip-clop(0.478)
- **音频特征**: RMS=0.0023, 频谱重心=1597Hz, 场景提示=mixed_environment

### 样本 375: metro-vienna-59-1758-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Silence(0.179)
- **音频特征**: RMS=0.0031, 频谱重心=712Hz, 场景提示=quiet_indoor

### 样本 376: shopping_mall-stockholm-137-4160-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.768), Clip-clop(0.334), Horse(0.237)
- **音频特征**: RMS=0.0038, 频谱重心=1371Hz, 场景提示=quiet_indoor

### 样本 377: airport-helsinki-4-172-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.198), Scissors(0.130)
- **音频特征**: RMS=0.0016, 频谱重心=1278Hz, 场景提示=quiet_indoor

### 样本 378: street_pedestrian-milan-1096-43942-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.830), Outside, urban or manmade(0.146), Clip-clop(0.102)
- **音频特征**: RMS=0.0033, 频谱重心=1396Hz, 场景提示=mixed_environment

### 样本 379: metro_station-barcelona-229-6906-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.125), Train(0.108)
- **音频特征**: RMS=0.0106, 频谱重心=1297Hz, 场景提示=mixed_environment

### 样本 380: metro_station-prague-1118-41688-a.wav
- **真实场景**: metro_station
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.253), Vehicle(0.140)
- **音频特征**: RMS=0.0059, 频谱重心=571Hz, 场景提示=quiet_indoor

### 样本 381: street_pedestrian-milan-1165-44591-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.847), Music(0.364), Vehicle(0.105)
- **音频特征**: RMS=0.0020, 频谱重心=1551Hz, 场景提示=mixed_environment

### 样本 382: street_pedestrian-paris-152-4611-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.511), Music(0.115)
- **音频特征**: RMS=0.0017, 频谱重心=1712Hz, 场景提示=mixed_environment

### 样本 383: metro_station-prague-1130-42569-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.779), Clip-clop(0.119), Animal(0.104)
- **音频特征**: RMS=0.0035, 频谱重心=1107Hz, 场景提示=quiet_indoor

### 样本 384: shopping_mall-london-256-7686-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.787), Animal(0.129), Chatter(0.118)
- **音频特征**: RMS=0.0031, 频谱重心=1341Hz, 场景提示=mixed_environment

### 样本 385: bus-stockholm-217-6557-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.603), Car(0.262), Rumble(0.177)
- **音频特征**: RMS=0.1136, 频谱重心=251Hz, 场景提示=mixed_environment

### 样本 386: airport-lisbon-1114-41736-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.733)
- **音频特征**: RMS=0.0071, 频谱重心=1222Hz, 场景提示=quiet_indoor

### 样本 387: tram-milan-1182-44596-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.487), Rumble(0.361), Car(0.253)
- **音频特征**: RMS=0.0182, 频谱重心=618Hz, 场景提示=mixed_environment

### 样本 388: street_pedestrian-lyon-1162-44468-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.745), Clip-clop(0.246), Boat, Water vehicle(0.238)
- **音频特征**: RMS=0.0016, 频谱重心=1324Hz, 场景提示=quiet_indoor

### 样本 389: street_pedestrian-stockholm-157-4779-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.771), Animal(0.232), Bird(0.197)
- **音频特征**: RMS=0.0042, 频谱重心=1167Hz, 场景提示=quiet_indoor

### 样本 390: metro-london-48-1448-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.751), Rail transport(0.592), Railroad car, train wagon(0.576)
- **音频特征**: RMS=0.0194, 频谱重心=636Hz, 场景提示=mixed_environment

### 样本 391: metro_station-lisbon-1020-40325-a.wav
- **真实场景**: metro_station
- **AE预测**: bus
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.624), Speech(0.479), Car(0.137)
- **音频特征**: RMS=0.0333, 频谱重心=1108Hz, 场景提示=mixed_environment

### 样本 392: shopping_mall-vienna-259-7864-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.772), Clip-clop(0.249), Horse(0.168)
- **音频特征**: RMS=0.0033, 频谱重心=1292Hz, 场景提示=quiet_indoor

### 样本 393: metro_station-lisbon-1221-44416-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.721), Animal(0.119)
- **音频特征**: RMS=0.0040, 频谱重心=1124Hz, 场景提示=quiet_indoor

### 样本 394: metro_station-milan-1127-40878-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.350), Vehicle(0.309)
- **音频特征**: RMS=0.0066, 频谱重心=1252Hz, 场景提示=quiet_indoor

### 样本 395: street_pedestrian-lyon-1072-40691-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.829), Clip-clop(0.440), Horse(0.339)
- **音频特征**: RMS=0.0012, 频谱重心=1747Hz, 场景提示=mixed_environment

### 样本 396: park-helsinki-92-2541-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.654), Animal(0.232)
- **音频特征**: RMS=0.0033, 频谱重心=1014Hz, 场景提示=quiet_indoor

### 样本 397: park-lyon-1012-43874-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.606), Animal(0.204), Clip-clop(0.181)
- **音频特征**: RMS=0.0014, 频谱重心=1064Hz, 场景提示=quiet_indoor

### 样本 398: airport-barcelona-203-6136-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.783), Animal(0.360), Clip-clop(0.318)
- **音频特征**: RMS=0.0019, 频谱重心=1355Hz, 场景提示=quiet_indoor

### 样本 399: tram-stockholm-198-5976-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.777), Vehicle(0.386), Bus(0.237)
- **音频特征**: RMS=0.0410, 频谱重心=413Hz, 场景提示=mixed_environment

### 样本 400: shopping_mall-helsinki-130-3884-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.627), Mouse(0.150), Animal(0.108)
- **音频特征**: RMS=0.0025, 频谱重心=1259Hz, 场景提示=quiet_indoor

### 样本 401: airport-barcelona-1-38-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.825), Run(0.252), Animal(0.194)
- **音频特征**: RMS=0.0033, 频谱重心=1281Hz, 场景提示=quiet_indoor

### 样本 402: airport-vienna-209-6368-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.317), Typing(0.183), Clip-clop(0.174)
- **音频特征**: RMS=0.0013, 频谱重心=1735Hz, 场景提示=mixed_environment

### 样本 403: shopping_mall-barcelona-127-3804-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.708)
- **音频特征**: RMS=0.0040, 频谱重心=1283Hz, 场景提示=quiet_indoor

### 样本 404: bus-milan-1115-42877-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.650), Vehicle(0.276)
- **音频特征**: RMS=0.0180, 频谱重心=1041Hz, 场景提示=mixed_environment

### 样本 405: metro-lisbon-1217-44266-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.773), Vehicle(0.481), Field recording(0.165)
- **音频特征**: RMS=0.0152, 频谱重心=590Hz, 场景提示=mixed_environment

### 样本 406: metro_station-vienna-86-2345-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.549), Silence(0.143)
- **音频特征**: RMS=0.0023, 频谱重心=870Hz, 场景提示=quiet_indoor

### 样本 407: tram-barcelona-179-5556-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.397), Vehicle(0.366), Music(0.126)
- **音频特征**: RMS=0.0102, 频谱重心=579Hz, 场景提示=mixed_environment

### 样本 408: tram-stockholm-198-5959-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.801), Vehicle(0.537), Car(0.205)
- **音频特征**: RMS=0.0571, 频谱重心=318Hz, 场景提示=mixed_environment

### 样本 409: street_pedestrian-milan-1205-44920-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.777)
- **音频特征**: RMS=0.0015, 频谱重心=1314Hz, 场景提示=quiet_indoor

### 样本 410: shopping_mall-paris-134-4050-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.606), Cough(0.270), Music(0.252)
- **音频特征**: RMS=0.0030, 频谱重心=1291Hz, 场景提示=quiet_indoor

### 样本 411: bus-lisbon-1106-43861-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.827), Vehicle(0.248)
- **音频特征**: RMS=0.0231, 频谱重心=519Hz, 场景提示=mixed_environment

### 样本 412: public_square-lyon-1208-45737-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.108)
- **音频特征**: RMS=0.0033, 频谱重心=1589Hz, 场景提示=mixed_environment

### 样本 413: metro-stockholm-57-1708-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.638), Vehicle(0.447), Train(0.121)
- **音频特征**: RMS=0.0146, 频谱重心=489Hz, 场景提示=mixed_environment

### 样本 414: public_square-london-115-3342-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.823), Outside, urban or manmade(0.154), Run(0.103)
- **音频特征**: RMS=0.0022, 频谱重心=1241Hz, 场景提示=quiet_indoor

### 样本 415: metro-paris-52-1541-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.247), Cough(0.217), Breathing(0.129)
- **音频特征**: RMS=0.0020, 频谱重心=1360Hz, 场景提示=quiet_indoor

### 样本 416: public_square-paris-118-3463-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.753), Animal(0.174), Vehicle(0.168)
- **音频特征**: RMS=0.0018, 频谱重心=1624Hz, 场景提示=mixed_environment

### 样本 417: street_pedestrian-lyon-1162-44399-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.292), Animal(0.115), Silence(0.105)
- **音频特征**: RMS=0.0018, 频谱重心=1012Hz, 场景提示=quiet_indoor

### 样本 418: tram-london-186-5770-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.631), Vehicle(0.193)
- **音频特征**: RMS=0.0053, 频谱重心=809Hz, 场景提示=quiet_indoor

### 样本 419: shopping_mall-helsinki-130-3907-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.695)
- **音频特征**: RMS=0.0023, 频谱重心=1279Hz, 场景提示=mixed_environment

### 样本 420: shopping_mall-london-256-7719-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.849), Clip-clop(0.161), Animal(0.154)
- **音频特征**: RMS=0.0027, 频谱重心=1611Hz, 场景提示=mixed_environment

### 样本 421: street_pedestrian-vienna-267-8114-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.413)
- **音频特征**: RMS=0.0029, 频谱重心=1118Hz, 场景提示=quiet_indoor

### 样本 422: airport-paris-9-397-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.668), Clip-clop(0.282), Horse(0.226)
- **音频特征**: RMS=0.0035, 频谱重心=1236Hz, 场景提示=quiet_indoor

### 样本 423: street_pedestrian-lisbon-1174-45131-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.859), Animal(0.159), Outside, urban or manmade(0.133)
- **音频特征**: RMS=0.0042, 频谱重心=1067Hz, 场景提示=quiet_indoor

### 样本 424: public_square-london-115-3366-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.793), Outside, urban or manmade(0.119)
- **音频特征**: RMS=0.0017, 频谱重心=1189Hz, 场景提示=quiet_indoor

### 样本 425: public_square-lyon-1056-40210-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.821), Clip-clop(0.191), Outside, urban or manmade(0.170)
- **音频特征**: RMS=0.0026, 频谱重心=1193Hz, 场景提示=quiet_indoor

### 样本 426: tram-lisbon-1100-43401-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.467), Boat, Water vehicle(0.341), Wind(0.227)
- **音频特征**: RMS=0.0307, 频谱重心=1193Hz, 场景提示=mixed_environment

### 样本 427: bus-lyon-1177-45521-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.844), Vehicle(0.379), Car(0.108)
- **音频特征**: RMS=0.0196, 频谱重心=648Hz, 场景提示=mixed_environment

### 样本 428: bus-lyon-1159-42892-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.816), Music(0.120)
- **音频特征**: RMS=0.0076, 频谱重心=813Hz, 场景提示=quiet_indoor

### 样本 429: shopping_mall-helsinki-129-3847-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.481), Music(0.214)
- **音频特征**: RMS=0.0025, 频谱重心=1198Hz, 场景提示=quiet_indoor

### 样本 430: street_pedestrian-prague-1085-42638-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.398), Run(0.137), Vehicle(0.126)
- **音频特征**: RMS=0.0022, 频谱重心=1105Hz, 场景提示=quiet_indoor

### 样本 431: street_pedestrian-paris-264-8011-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.787), Animal(0.193), Clip-clop(0.174)
- **音频特征**: RMS=0.0028, 频谱重心=1224Hz, 场景提示=quiet_indoor

### 样本 432: metro_station-london-234-7005-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Silence(0.124)
- **音频特征**: RMS=0.0038, 频谱重心=1332Hz, 场景提示=quiet_indoor

### 样本 433: shopping_mall-london-131-3955-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.644)
- **音频特征**: RMS=0.0021, 频谱重心=1146Hz, 场景提示=quiet_indoor

### 样本 434: tram-helsinki-184-5738-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.672), Vehicle(0.449), Train(0.131)
- **音频特征**: RMS=0.0111, 频谱重心=477Hz, 场景提示=mixed_environment

### 样本 435: metro-stockholm-57-1702-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.652), Pigeon, dove(0.287), Bird(0.281)
- **音频特征**: RMS=0.0099, 频谱重心=999Hz, 场景提示=quiet_indoor

### 样本 436: metro-london-46-1419-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.521), Vehicle(0.403), Train(0.109)
- **音频特征**: RMS=0.0058, 频谱重心=1044Hz, 场景提示=quiet_indoor

### 样本 437: shopping_mall-lisbon-1002-42636-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.409)
- **音频特征**: RMS=0.0024, 频谱重心=1203Hz, 场景提示=quiet_indoor

### 样本 438: shopping_mall-lisbon-1002-42623-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.741), Vehicle(0.100)
- **音频特征**: RMS=0.0025, 频谱重心=1120Hz, 场景提示=quiet_indoor

### 样本 439: airport-stockholm-10-430-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.809), Clip-clop(0.315), Horse(0.222)
- **音频特征**: RMS=0.0022, 频谱重心=1190Hz, 场景提示=quiet_indoor

### 样本 440: street_pedestrian-barcelona-145-4372-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.784), Vehicle(0.148), Animal(0.127)
- **音频特征**: RMS=0.0039, 频谱重心=1483Hz, 场景提示=mixed_environment

### 样本 441: metro_station-stockholm-239-7083-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.606), Train(0.524), Subway, metro, underground(0.386)
- **音频特征**: RMS=0.0142, 频谱重心=1331Hz, 场景提示=mixed_environment

### 样本 442: metro-stockholm-56-1645-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.569), Vehicle(0.232)
- **音频特征**: RMS=0.0050, 频谱重心=642Hz, 场景提示=quiet_indoor

### 样本 443: metro_station-stockholm-239-7082-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.745), Vehicle(0.117)
- **音频特征**: RMS=0.0137, 频谱重心=943Hz, 场景提示=mixed_environment

### 样本 444: public_square-stockholm-119-3508-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: street_traffic
- **检测到的事件**: Bicycle(0.423), Vehicle(0.283), Ratchet, pawl(0.177)
- **音频特征**: RMS=0.0048, 频谱重心=1809Hz, 场景提示=quiet_indoor

### 样本 445: metro_station-paris-236-7042-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.200)
- **音频特征**: RMS=0.0027, 频谱重心=971Hz, 场景提示=quiet_indoor

### 样本 446: metro_station-vienna-86-2328-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Silence(0.271)
- **音频特征**: RMS=0.0030, 频谱重心=727Hz, 场景提示=quiet_indoor

### 样本 447: bus-lisbon-1226-44601-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.769), Vehicle(0.185), Hubbub, speech noise, speech babble(0.125)
- **音频特征**: RMS=0.0722, 频谱重心=753Hz, 场景提示=mixed_environment

### 样本 448: airport-barcelona-1-51-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.783), Vehicle(0.126)
- **音频特征**: RMS=0.0038, 频谱重心=1074Hz, 场景提示=quiet_indoor

### 样本 449: street_pedestrian-london-149-4517-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.899), Run(0.349), Outside, urban or manmade(0.210)
- **音频特征**: RMS=0.0036, 频谱重心=959Hz, 场景提示=quiet_indoor

### 样本 450: metro-vienna-58-1746-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.330), Bird(0.189), Sliding door(0.174)
- **音频特征**: RMS=0.0070, 频谱重心=1141Hz, 场景提示=quiet_indoor

### 样本 451: airport-london-6-267-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.691), Animal(0.127), Clip-clop(0.115)
- **音频特征**: RMS=0.0020, 频谱重心=1427Hz, 场景提示=quiet_indoor

### 样本 452: metro-prague-1026-40088-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.726), Music(0.641), Animal(0.111)
- **音频特征**: RMS=0.0069, 频谱重心=1283Hz, 场景提示=quiet_indoor

### 样本 453: tram-helsinki-182-5659-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.587), Vehicle(0.500), Field recording(0.224)
- **音频特征**: RMS=0.0185, 频谱重心=405Hz, 场景提示=mixed_environment

### 样本 454: metro_station-vienna-240-7147-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.131)
- **音频特征**: RMS=0.0026, 频谱重心=989Hz, 场景提示=quiet_indoor

### 样本 455: airport-barcelona-2-99-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.835), Clip-clop(0.550), Horse(0.486)
- **音频特征**: RMS=0.0023, 频谱重心=1334Hz, 场景提示=quiet_indoor

### 样本 456: metro_station-helsinki-232-6977-a.wav
- **真实场景**: metro_station
- **AE预测**: bus
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.236), White noise(0.112)
- **音频特征**: RMS=0.0151, 频谱重心=865Hz, 场景提示=mixed_environment

### 样本 457: shopping_mall-vienna-139-4240-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.719), Animal(0.207)
- **音频特征**: RMS=0.0021, 频谱重心=1666Hz, 场景提示=mixed_environment

### 样本 458: public_square-paris-116-3387-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.755), Clip-clop(0.305), Animal(0.293)
- **音频特征**: RMS=0.0020, 频谱重心=1210Hz, 场景提示=quiet_indoor

### 样本 459: metro-milan-1142-41516-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.556), Train(0.506), Rail transport(0.316)
- **音频特征**: RMS=0.0247, 频谱重心=705Hz, 场景提示=mixed_environment

### 样本 460: metro_station-prague-1019-43831-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.211), Animal(0.146), Mouse(0.103)
- **音频特征**: RMS=0.0030, 频谱重心=1161Hz, 场景提示=quiet_indoor

### 样本 461: metro_station-prague-1118-42429-a.wav
- **真实场景**: metro_station
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.330), Speech(0.212)
- **音频特征**: RMS=0.0089, 频谱重心=924Hz, 场景提示=quiet_indoor

### 样本 462: street_pedestrian-paris-265-8050-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.721), Animal(0.214)
- **音频特征**: RMS=0.0014, 频谱重心=1786Hz, 场景提示=mixed_environment

### 样本 463: bus-paris-29-959-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.650), Vehicle(0.112)
- **音频特征**: RMS=0.0047, 频谱重心=1033Hz, 场景提示=quiet_indoor

### 样本 464: street_traffic-stockholm-273-8313-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.611), Vehicle(0.371), Car(0.135)
- **音频特征**: RMS=0.0198, 频谱重心=1061Hz, 场景提示=mixed_environment

### 样本 465: street_pedestrian-lisbon-1098-43711-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.809)
- **音频特征**: RMS=0.0027, 频谱重心=1400Hz, 场景提示=quiet_indoor

### 样本 466: metro-london-223-6771-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.708), Vehicle(0.410)
- **音频特征**: RMS=0.0107, 频谱重心=858Hz, 场景提示=mixed_environment

### 样本 467: shopping_mall-stockholm-136-4106-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.692), Clip-clop(0.136), Animal(0.115)
- **音频特征**: RMS=0.0048, 频谱重心=942Hz, 场景提示=quiet_indoor

### 样本 468: metro-barcelona-42-1276-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Train(0.667), Railroad car, train wagon(0.541), Rail transport(0.531)
- **音频特征**: RMS=0.0187, 频谱重心=435Hz, 场景提示=mixed_environment

### 样本 469: metro_station-lisbon-1020-42713-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.589), Vehicle(0.134)
- **音频特征**: RMS=0.0050, 频谱重心=990Hz, 场景提示=quiet_indoor

### 样本 470: airport-london-6-306-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Vehicle(0.118), Animal(0.114)
- **音频特征**: RMS=0.0018, 频谱重心=1179Hz, 场景提示=quiet_indoor

### 样本 471: street_pedestrian-barcelona-261-7912-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.814), Vehicle(0.141), Music(0.121)
- **音频特征**: RMS=0.0048, 频谱重心=1352Hz, 场景提示=quiet_indoor

### 样本 472: airport-helsinki-3-150-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.797)
- **音频特征**: RMS=0.0023, 频谱重心=1176Hz, 场景提示=quiet_indoor

### 样本 473: street_pedestrian-london-263-7967-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.861), Clip-clop(0.220), Animal(0.185)
- **音频特征**: RMS=0.0018, 频谱重心=1575Hz, 场景提示=mixed_environment

### 样本 474: metro-lyon-1082-42282-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.731), Vehicle(0.583), Car(0.189)
- **音频特征**: RMS=0.0118, 频谱重心=1429Hz, 场景提示=mixed_environment

### 样本 475: airport-lyon-1041-41216-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.814)
- **音频特征**: RMS=0.0029, 频谱重心=1129Hz, 场景提示=quiet_indoor

### 样本 476: tram-milan-1065-40094-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Sliding door(0.463), Door(0.331), Vehicle(0.136)
- **音频特征**: RMS=0.0097, 频谱重心=1052Hz, 场景提示=quiet_indoor

### 样本 477: shopping_mall-paris-134-4036-a.wav
- **真实场景**: shopping_mall
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.672), Animal(0.297), Clip-clop(0.263)
- **音频特征**: RMS=0.0015, 频谱重心=1357Hz, 场景提示=quiet_indoor

### 样本 478: public_square-lyon-1024-43540-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.242), Silence(0.185), Vehicle(0.158)
- **音频特征**: RMS=0.0033, 频谱重心=1050Hz, 场景提示=quiet_indoor

### 样本 479: shopping_mall-milan-1183-45567-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.406), Animal(0.135), Clip-clop(0.112)
- **音频特征**: RMS=0.0061, 频谱重心=1762Hz, 场景提示=mixed_environment

### 样本 480: shopping_mall-vienna-259-7870-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.841), Clip-clop(0.371), Horse(0.284)
- **音频特征**: RMS=0.0032, 频谱重心=1345Hz, 场景提示=quiet_indoor

### 样本 481: public_square-stockholm-119-3483-a.wav
- **真实场景**: public_square
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Patter(0.189), Animal(0.134)
- **音频特征**: RMS=0.0048, 频谱重心=1028Hz, 场景提示=quiet_indoor

### 样本 482: metro_station-vienna-88-2421-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Animal(0.135)
- **音频特征**: RMS=0.0028, 频谱重心=785Hz, 场景提示=quiet_indoor

### 样本 483: metro-lyon-1064-42173-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.699), Pigeon, dove(0.359), Bird(0.320)
- **音频特征**: RMS=0.0041, 频谱重心=1261Hz, 场景提示=quiet_indoor

### 样本 484: street_pedestrian-prague-1037-42740-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.878), Outside, urban or manmade(0.153)
- **音频特征**: RMS=0.0119, 频谱重心=1460Hz, 场景提示=mixed_environment

### 样本 485: public_square-paris-118-3475-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.500), Animal(0.407), Clip-clop(0.210)
- **音频特征**: RMS=0.0016, 频谱重心=1458Hz, 场景提示=quiet_indoor

### 样本 486: tram-lyon-1103-41495-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.754), Vehicle(0.290)
- **音频特征**: RMS=0.0074, 频谱重心=1086Hz, 场景提示=quiet_indoor

### 样本 487: metro_station-lisbon-1007-42145-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.809), Vehicle(0.187)
- **音频特征**: RMS=0.0029, 频谱重心=1123Hz, 场景提示=quiet_indoor

### 样本 488: metro-vienna-58-1718-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.675), Power windows, electric windows(0.392), Vehicle(0.196)
- **音频特征**: RMS=0.0100, 频谱重心=1105Hz, 场景提示=quiet_indoor

### 样本 489: airport-paris-206-6259-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.193)
- **音频特征**: RMS=0.0075, 频谱重心=987Hz, 场景提示=quiet_indoor

### 样本 490: street_traffic-paris-272-8279-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Speech(0.741), Animal(0.194), Clip-clop(0.140)
- **音频特征**: RMS=0.0027, 频谱重心=1288Hz, 场景提示=quiet_indoor

### 样本 491: public_square-milan-1074-40688-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.853), Clip-clop(0.389), Horse(0.321)
- **音频特征**: RMS=0.0039, 频谱重心=1102Hz, 场景提示=quiet_indoor

### 样本 492: shopping_mall-prague-1031-40304-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **音频特征**: RMS=0.0019, 频谱重心=1129Hz, 场景提示=quiet_indoor

### 样本 493: street_pedestrian-lyon-1047-42052-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.780), Run(0.261), Animal(0.202)
- **音频特征**: RMS=0.0025, 频谱重心=1288Hz, 场景提示=quiet_indoor

### 样本 494: metro_station-milan-1117-43104-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.758), Clip-clop(0.240), Animal(0.222)
- **音频特征**: RMS=0.0052, 频谱重心=983Hz, 场景提示=quiet_indoor

### 样本 495: shopping_mall-vienna-139-4221-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.546), Clip-clop(0.122), Horse(0.119)
- **音频特征**: RMS=0.0022, 频谱重心=1619Hz, 场景提示=mixed_environment

### 样本 496: metro_station-lyon-1010-41728-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.652), Music(0.369)
- **音频特征**: RMS=0.0036, 频谱重心=1164Hz, 场景提示=quiet_indoor

### 样本 497: metro-helsinki-222-6703-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.743), Vehicle(0.362), Music(0.283)
- **音频特征**: RMS=0.0131, 频谱重心=836Hz, 场景提示=mixed_environment

### 样本 498: metro-paris-52-1552-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Train(0.242), Vehicle(0.213), Railroad car, train wagon(0.156)
- **音频特征**: RMS=0.0144, 频谱重心=1041Hz, 场景提示=mixed_environment

### 样本 499: park-prague-1038-40071-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.753), Vehicle(0.201), Run(0.140)
- **音频特征**: RMS=0.0024, 频谱重心=758Hz, 场景提示=quiet_indoor

### 样本 500: metro-stockholm-56-1655-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.480), Sliding door(0.399), Door(0.204)
- **音频特征**: RMS=0.0107, 频谱重心=614Hz, 场景提示=mixed_environment

### 样本 501: tram-milan-1158-43588-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.745), Vehicle(0.288)
- **音频特征**: RMS=0.0048, 频谱重心=1084Hz, 场景提示=quiet_indoor

### 样本 502: public_square-vienna-122-3611-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.849), Outside, urban or manmade(0.155), Clip-clop(0.148)
- **音频特征**: RMS=0.0011, 频谱重心=1171Hz, 场景提示=quiet_indoor

### 样本 503: street_pedestrian-stockholm-157-4775-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.790), Animal(0.318), Clip-clop(0.187)
- **音频特征**: RMS=0.0026, 频谱重心=1530Hz, 场景提示=mixed_environment

### 样本 504: bus-stockholm-218-6573-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.802), Vehicle(0.496), Bus(0.177)
- **音频特征**: RMS=0.0355, 频谱重心=876Hz, 场景提示=mixed_environment

### 样本 505: tram-stockholm-199-5993-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.824), Vehicle(0.587), Car(0.256)
- **音频特征**: RMS=0.0519, 频谱重心=357Hz, 场景提示=mixed_environment

### 样本 506: metro-paris-54-1595-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.793), Music(0.462), Vehicle(0.102)
- **音频特征**: RMS=0.0044, 频谱重心=942Hz, 场景提示=quiet_indoor

### 样本 507: metro_station-lisbon-1007-43165-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.682), Vehicle(0.534), Railroad car, train wagon(0.532)
- **音频特征**: RMS=0.0624, 频谱重心=769Hz, 场景提示=mixed_environment

### 样本 508: metro_station-vienna-86-2322-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.863), Children playing(0.422), Chatter(0.184)
- **音频特征**: RMS=0.0019, 频谱重心=1603Hz, 场景提示=mixed_environment

### 样本 509: street_pedestrian-barcelona-142-4307-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.852), Inside, public space(0.102)
- **音频特征**: RMS=0.0047, 频谱重心=1472Hz, 场景提示=mixed_environment

### 样本 510: street_pedestrian-barcelona-261-7907-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.569), Animal(0.131)
- **音频特征**: RMS=0.0067, 频谱重心=875Hz, 场景提示=quiet_indoor

### 样本 511: bus-london-22-843-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.605), Vehicle(0.300), Music(0.145)
- **音频特征**: RMS=0.0106, 频谱重心=1064Hz, 场景提示=mixed_environment

### 样本 512: tram-lisbon-1200-45287-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.832), Music(0.705), Vehicle(0.293)
- **音频特征**: RMS=0.0176, 频谱重心=936Hz, 场景提示=mixed_environment

### 样本 513: public_square-stockholm-252-7543-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.265), Walk, footsteps(0.109)
- **音频特征**: RMS=0.0030, 频谱重心=1193Hz, 场景提示=quiet_indoor

### 样本 514: airport-london-205-6203-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.819), Clip-clop(0.252), Horse(0.180)
- **音频特征**: RMS=0.0014, 频谱重心=1589Hz, 场景提示=mixed_environment

### 样本 515: metro-lisbon-1121-42987-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.306)
- **音频特征**: RMS=0.0099, 频谱重心=1181Hz, 场景提示=quiet_indoor

### 样本 516: metro_station-milan-1187-45508-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.412), Rumble(0.125), Field recording(0.124)
- **音频特征**: RMS=0.1638, 频谱重心=431Hz, 场景提示=mixed_environment

### 样本 517: street_pedestrian-milan-1096-42039-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.817), Outside, urban or manmade(0.154), Run(0.117)
- **音频特征**: RMS=0.0031, 频谱重心=1347Hz, 场景提示=mixed_environment

### 样本 518: metro-barcelona-41-1259-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.658), Vehicle(0.492), Train(0.205)
- **音频特征**: RMS=0.0146, 频谱重心=702Hz, 场景提示=mixed_environment

### 样本 519: street_pedestrian-helsinki-147-4430-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.740), Animal(0.380), Run(0.216)
- **音频特征**: RMS=0.0038, 频谱重心=1212Hz, 场景提示=quiet_indoor

### 样本 520: airport-paris-7-348-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.686), Mouse(0.128)
- **音频特征**: RMS=0.0023, 频谱重心=1339Hz, 场景提示=quiet_indoor

### 样本 521: tram-lisbon-1100-42237-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.300)
- **音频特征**: RMS=0.0071, 频谱重心=927Hz, 场景提示=quiet_indoor

### 样本 522: shopping_mall-stockholm-258-7838-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.815)
- **音频特征**: RMS=0.0052, 频谱重心=1348Hz, 场景提示=quiet_indoor

### 样本 523: public_square-london-114-3312-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.791), Music(0.110)
- **音频特征**: RMS=0.0021, 频谱重心=1399Hz, 场景提示=mixed_environment

### 样本 524: street_traffic-stockholm-173-5326-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Speech(0.644), Vehicle(0.494), Boat, Water vehicle(0.282)
- **音频特征**: RMS=0.0110, 频谱重心=958Hz, 场景提示=mixed_environment

### 样本 525: bus-prague-1120-43520-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.711), Vehicle(0.433), Train(0.128)
- **音频特征**: RMS=0.0194, 频谱重心=818Hz, 场景提示=mixed_environment

### 样本 526: bus-lyon-1124-43137-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.271), Sliding door(0.229), Music(0.172)
- **音频特征**: RMS=0.0161, 频谱重心=908Hz, 场景提示=mixed_environment

### 样本 527: tram-vienna-200-6021-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.798), Vehicle(0.300)
- **音频特征**: RMS=0.0143, 频谱重心=677Hz, 场景提示=mixed_environment

### 样本 528: street_pedestrian-barcelona-260-7886-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.792), Animal(0.363), Clip-clop(0.310)
- **音频特征**: RMS=0.0021, 频谱重心=1526Hz, 场景提示=mixed_environment

### 样本 529: metro_station-vienna-240-7128-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.721), Subway, metro, underground(0.542), Rail transport(0.526)
- **音频特征**: RMS=0.0217, 频谱重心=1041Hz, 场景提示=mixed_environment

### 样本 530: metro-london-48-1494-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.729), Music(0.285), Vehicle(0.242)
- **音频特征**: RMS=0.0133, 频谱重心=904Hz, 场景提示=mixed_environment

### 样本 531: public_square-lyon-1056-43077-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.813), Outside, urban or manmade(0.156), Chatter(0.106)
- **音频特征**: RMS=0.0025, 频谱重心=1138Hz, 场景提示=quiet_indoor

### 样本 532: street_pedestrian-helsinki-148-4476-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.656), Animal(0.111)
- **音频特征**: RMS=0.0016, 频谱重心=1249Hz, 场景提示=quiet_indoor

### 样本 533: tram-stockholm-283-8557-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.373), Car(0.163), Rumble(0.151)
- **音频特征**: RMS=0.0182, 频谱重心=270Hz, 场景提示=mixed_environment

### 样本 534: tram-prague-1161-41755-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.723), Music(0.356), Vehicle(0.340)
- **音频特征**: RMS=0.0122, 频谱重心=923Hz, 场景提示=mixed_environment

### 样本 535: street_pedestrian-lisbon-1098-43300-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.717), Vehicle(0.195)
- **音频特征**: RMS=0.0031, 频谱重心=1145Hz, 场景提示=quiet_indoor

### 样本 536: street_pedestrian-lyon-1047-43224-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.702), Animal(0.178), Clip-clop(0.177)
- **音频特征**: RMS=0.0022, 频谱重心=1383Hz, 场景提示=quiet_indoor

### 样本 537: street_pedestrian-milan-1005-41239-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.797), Horse(0.537), Clip-clop(0.504)
- **音频特征**: RMS=0.0036, 频谱重心=973Hz, 场景提示=quiet_indoor

### 样本 538: public_square-milan-1074-41678-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.791), Vehicle(0.154), Outside, urban or manmade(0.124)
- **音频特征**: RMS=0.0044, 频谱重心=897Hz, 场景提示=quiet_indoor

### 样本 539: metro-vienna-60-1817-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Sliding door(0.317), Cupboard open or close(0.309), Door(0.214)
- **音频特征**: RMS=0.0292, 频谱重心=531Hz, 场景提示=mixed_environment

### 样本 540: tram-lisbon-1131-40493-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.687), Car(0.360), Speech(0.193)
- **音频特征**: RMS=0.1126, 频谱重心=469Hz, 场景提示=mixed_environment

### 样本 541: street_pedestrian-helsinki-147-4461-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Music(0.140), Vehicle(0.101)
- **音频特征**: RMS=0.0058, 频谱重心=838Hz, 场景提示=quiet_indoor

### 样本 542: metro_station-prague-1170-44500-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.201), Speech(0.108)
- **音频特征**: RMS=0.0046, 频谱重心=875Hz, 场景提示=quiet_indoor

### 样本 543: metro_station-stockholm-84-2265-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.647), Animal(0.246), Clip-clop(0.138)
- **音频特征**: RMS=0.0069, 频谱重心=1297Hz, 场景提示=quiet_indoor

### 样本 544: street_pedestrian-london-150-4565-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.817), Clip-clop(0.219), Run(0.179)
- **音频特征**: RMS=0.0036, 频谱重心=1038Hz, 场景提示=quiet_indoor

### 样本 545: street_traffic-paris-171-5242-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.253), Vehicle(0.245), Silence(0.101)
- **音频特征**: RMS=0.0046, 频谱重心=960Hz, 场景提示=quiet_indoor

### 样本 546: airport-lyon-1169-44283-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.627), Run(0.549), Animal(0.216)
- **音频特征**: RMS=0.0034, 频谱重心=1476Hz, 场景提示=mixed_environment

### 样本 547: metro_station-vienna-86-2332-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.840), Children playing(0.628), Child speech, kid speaking(0.213)
- **音频特征**: RMS=0.0088, 频谱重心=956Hz, 场景提示=quiet_indoor

### 样本 548: tram-london-279-8472-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.874), Vehicle(0.168)
- **音频特征**: RMS=0.0030, 频谱重心=1821Hz, 场景提示=mixed_environment

### 样本 549: public_square-prague-1152-40549-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.699), Vehicle(0.269), Boat, Water vehicle(0.203)
- **音频特征**: RMS=0.0022, 频谱重心=1360Hz, 场景提示=mixed_environment

### 样本 550: street_traffic-london-270-8216-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Speech(0.711), Vehicle(0.354), Boat, Water vehicle(0.132)
- **音频特征**: RMS=0.0090, 频谱重心=1514Hz, 场景提示=quiet_indoor

### 样本 551: bus-lisbon-1123-42544-a.wav
- **真实场景**: bus
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.710), Vehicle(0.303)
- **音频特征**: RMS=0.0095, 频谱重心=1357Hz, 场景提示=quiet_indoor

### 样本 552: airport-milan-1172-44126-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.410)
- **音频特征**: RMS=0.0026, 频谱重心=1697Hz, 场景提示=mixed_environment

### 样本 553: metro-helsinki-222-6764-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.821), Music(0.479), Vehicle(0.364)
- **音频特征**: RMS=0.0123, 频谱重心=749Hz, 场景提示=mixed_environment

### 样本 554: airport-helsinki-204-6138-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.311), Animal(0.201)
- **音频特征**: RMS=0.0024, 频谱重心=1467Hz, 场景提示=quiet_indoor

### 样本 555: public_square-prague-1027-43344-a.wav
- **真实场景**: public_square
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.608), Fire(0.180), Vehicle(0.148)
- **音频特征**: RMS=0.0070, 频谱重心=1435Hz, 场景提示=quiet_indoor

### 样本 556: airport-lisbon-1114-40411-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.838), Clip-clop(0.270), Animal(0.212)
- **音频特征**: RMS=0.0049, 频谱重心=1379Hz, 场景提示=quiet_indoor

### 样本 557: street_traffic-prague-1006-44030-a.wav
- **真实场景**: street_traffic
- **AE预测**: bus
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.135)
- **音频特征**: RMS=0.0047, 频谱重心=1144Hz, 场景提示=quiet_indoor

### 样本 558: metro_station-london-76-2106-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.725), Music(0.178), Children playing(0.155)
- **音频特征**: RMS=0.0078, 频谱重心=1214Hz, 场景提示=quiet_indoor

### 样本 559: tram-milan-1222-44558-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.632), Rail transport(0.477), Railroad car, train wagon(0.448)
- **音频特征**: RMS=0.0224, 频谱重心=807Hz, 场景提示=mixed_environment

### 样本 560: airport-prague-1015-40787-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.752), Clip-clop(0.290), Horse(0.211)
- **音频特征**: RMS=0.0031, 频谱重心=1129Hz, 场景提示=quiet_indoor

### 样本 561: street_pedestrian-stockholm-157-4759-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.649), Run(0.150), Animal(0.118)
- **音频特征**: RMS=0.0026, 频谱重心=1830Hz, 场景提示=mixed_environment

### 样本 562: shopping_mall-vienna-259-7882-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.826), Clip-clop(0.169), Horse(0.120)
- **音频特征**: RMS=0.0035, 频谱重心=1356Hz, 场景提示=quiet_indoor

### 样本 563: shopping_mall-lyon-1196-45205-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Music(0.611), Speech(0.301), Silence(0.103)
- **音频特征**: RMS=0.0020, 频谱重心=1390Hz, 场景提示=quiet_indoor

### 样本 564: park-london-243-7227-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.794), Animal(0.397), Clip-clop(0.239)
- **音频特征**: RMS=0.0027, 频谱重心=801Hz, 场景提示=quiet_indoor

### 样本 565: bus-milan-1190-44511-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.819), Music(0.427), Vehicle(0.114)
- **音频特征**: RMS=0.0102, 频谱重心=1013Hz, 场景提示=mixed_environment

### 样本 566: metro_station-london-73-2067-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.865), Female speech, woman speaking(0.170), Narration, monologue(0.154)
- **音频特征**: RMS=0.0053, 频谱重心=1177Hz, 场景提示=quiet_indoor

### 样本 567: shopping_mall-paris-257-7805-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Animal(0.238), Speech(0.237), Clip-clop(0.197)
- **音频特征**: RMS=0.0019, 频谱重心=1547Hz, 场景提示=mixed_environment

### 样本 568: tram-stockholm-284-8585-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.700), Vehicle(0.697), Car(0.387)
- **音频特征**: RMS=0.1081, 频谱重心=341Hz, 场景提示=mixed_environment

### 样本 569: airport-paris-9-377-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.343), Mouse(0.152)
- **音频特征**: RMS=0.0019, 频谱重心=1299Hz, 场景提示=quiet_indoor

### 样本 570: metro-helsinki-221-6683-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.750), Sliding door(0.415), Door(0.307)
- **音频特征**: RMS=0.0109, 频谱重心=843Hz, 场景提示=mixed_environment

### 样本 571: metro_station-london-76-2105-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.344), Silence(0.131)
- **音频特征**: RMS=0.0028, 频谱重心=1079Hz, 场景提示=quiet_indoor

### 样本 572: shopping_mall-london-131-3920-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.841), Clip-clop(0.449), Animal(0.394)
- **音频特征**: RMS=0.0017, 频谱重心=1645Hz, 场景提示=mixed_environment

### 样本 573: tram-vienna-200-6035-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Mouse(0.429), Rodents, rats, mice(0.164)
- **音频特征**: RMS=0.0054, 频谱重心=726Hz, 场景提示=quiet_indoor

### 样本 574: metro-milan-1062-41981-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.527), Vehicle(0.200), Train(0.128)
- **音频特征**: RMS=0.0180, 频谱重心=723Hz, 场景提示=mixed_environment

### 样本 575: metro-lyon-1064-42345-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.822), Vehicle(0.217)
- **音频特征**: RMS=0.0059, 频谱重心=1422Hz, 场景提示=quiet_indoor

### 样本 576: shopping_mall-lisbon-1176-44811-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.149), Speech(0.129)
- **音频特征**: RMS=0.0057, 频谱重心=958Hz, 场景提示=quiet_indoor

### 样本 577: street_pedestrian-paris-152-4608-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.820)
- **音频特征**: RMS=0.0017, 频谱重心=1526Hz, 场景提示=quiet_indoor

### 样本 578: shopping_mall-vienna-138-4177-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.826), Animal(0.157), Children playing(0.138)
- **音频特征**: RMS=0.0034, 频谱重心=1482Hz, 场景提示=mixed_environment

### 样本 579: airport-helsinki-4-182-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.650)
- **音频特征**: RMS=0.0021, 频谱重心=1174Hz, 场景提示=quiet_indoor

### 样本 580: tram-helsinki-184-5736-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.144), Vehicle(0.141), Silence(0.120)
- **音频特征**: RMS=0.0052, 频谱重心=582Hz, 场景提示=quiet_indoor

### 样本 581: public_square-stockholm-121-3573-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.680), Typing(0.115), Vehicle(0.107)
- **音频特征**: RMS=0.0052, 频谱重心=1492Hz, 场景提示=quiet_indoor

### 样本 582: metro-lisbon-1145-42741-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.341), Speech(0.212), Bird(0.167)
- **音频特征**: RMS=0.0084, 频谱重心=928Hz, 场景提示=quiet_indoor

### 样本 583: bus-lyon-1073-42169-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.759), Vehicle(0.295), Music(0.282)
- **音频特征**: RMS=0.0154, 频谱重心=535Hz, 场景提示=mixed_environment

### 样本 584: metro_station-helsinki-66-1971-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Silence(0.198)
- **音频特征**: RMS=0.0012, 频谱重心=925Hz, 场景提示=quiet_indoor

### 样本 585: airport-stockholm-11-451-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.845), Animal(0.163), Clip-clop(0.156)
- **音频特征**: RMS=0.0046, 频谱重心=1129Hz, 场景提示=quiet_indoor

### 样本 586: airport-stockholm-10-440-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.709), Vehicle(0.212), Fire(0.141)
- **音频特征**: RMS=0.0043, 频谱重心=1191Hz, 场景提示=quiet_indoor

### 样本 587: airport-lisbon-1000-42611-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.802), Animal(0.209), Clip-clop(0.113)
- **音频特征**: RMS=0.0047, 频谱重心=1422Hz, 场景提示=mixed_environment

### 样本 588: public_square-milan-1044-41890-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.812), Animal(0.141), Outside, urban or manmade(0.112)
- **音频特征**: RMS=0.0034, 频谱重心=1134Hz, 场景提示=quiet_indoor

### 样本 589: tram-helsinki-183-5691-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: public_square
- **检测到的事件**: Speech(0.731), Vehicle(0.146)
- **音频特征**: RMS=0.0051, 频谱重心=696Hz, 场景提示=quiet_indoor

### 样本 590: tram-lisbon-1191-44967-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.617), Vehicle(0.445), Bus(0.155)
- **音频特征**: RMS=0.0675, 频谱重心=749Hz, 场景提示=mixed_environment

### 样本 591: street_pedestrian-lisbon-1004-40636-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.866), Clip-clop(0.156), Animal(0.141)
- **音频特征**: RMS=0.0023, 频谱重心=1246Hz, 场景提示=quiet_indoor

### 样本 592: street_pedestrian-lyon-1003-40207-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.824), Chatter(0.111)
- **音频特征**: RMS=0.0019, 频谱重心=1328Hz, 场景提示=quiet_indoor

### 样本 593: tram-prague-1088-41430-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.373), Train(0.202), Railroad car, train wagon(0.114)
- **音频特征**: RMS=0.0181, 频谱重心=592Hz, 场景提示=mixed_environment

### 样本 594: tram-milan-1158-42258-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.654), Vehicle(0.401), Train(0.108)
- **音频特征**: RMS=0.0054, 频谱重心=962Hz, 场景提示=quiet_indoor

### 样本 595: metro-stockholm-227-6829-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.713), Vehicle(0.412), Train(0.118)
- **音频特征**: RMS=0.0205, 频谱重心=553Hz, 场景提示=mixed_environment

### 样本 596: airport-lisbon-1175-45707-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.759), Animal(0.123), Clip-clop(0.121)
- **音频特征**: RMS=0.0035, 频谱重心=1465Hz, 场景提示=mixed_environment

### 样本 597: street_pedestrian-stockholm-157-4763-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.328), Animal(0.225), Clip-clop(0.122)
- **音频特征**: RMS=0.0048, 频谱重心=1248Hz, 场景提示=quiet_indoor

### 样本 598: tram-london-277-8444-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Mouse(0.129)
- **音频特征**: RMS=0.0052, 频谱重心=688Hz, 场景提示=quiet_indoor

### 样本 599: metro-lyon-1201-44668-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.730), Vehicle(0.463)
- **音频特征**: RMS=0.0110, 频谱重心=899Hz, 场景提示=mixed_environment

### 样本 600: metro-helsinki-222-6752-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.723), Vehicle(0.459), Music(0.181)
- **音频特征**: RMS=0.0199, 频谱重心=708Hz, 场景提示=mixed_environment

### 样本 601: metro_station-stockholm-85-2294-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.638), Music(0.338), Clip-clop(0.181)
- **音频特征**: RMS=0.0067, 频谱重心=1268Hz, 场景提示=quiet_indoor

### 样本 602: shopping_mall-helsinki-130-3891-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.534), Vehicle(0.210), Clip-clop(0.119)
- **音频特征**: RMS=0.0048, 频谱重心=1011Hz, 场景提示=quiet_indoor

### 样本 603: street_pedestrian-milan-1096-40534-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.836), Clip-clop(0.268), Horse(0.223)
- **音频特征**: RMS=0.0032, 频谱重心=1418Hz, 场景提示=mixed_environment

### 样本 604: metro-barcelona-42-1299-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.213), Music(0.210), Rail transport(0.119)
- **音频特征**: RMS=0.0097, 频谱重心=548Hz, 场景提示=quiet_indoor

### 样本 605: metro_station-helsinki-64-1914-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.148), Vehicle(0.143)
- **音频特征**: RMS=0.0057, 频谱重心=843Hz, 场景提示=quiet_indoor

### 样本 606: street_pedestrian-prague-1203-44222-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.760), Clip-clop(0.223), Music(0.142)
- **音频特征**: RMS=0.0019, 频谱重心=1522Hz, 场景提示=mixed_environment

### 样本 607: shopping_mall-lisbon-1137-43432-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.506), Basketball bounce(0.130)
- **音频特征**: RMS=0.0027, 频谱重心=1427Hz, 场景提示=mixed_environment

### 样本 608: street_pedestrian-vienna-267-8106-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Vehicle(0.323)
- **音频特征**: RMS=0.0036, 频谱重心=885Hz, 场景提示=quiet_indoor

### 样本 609: street_pedestrian-prague-1051-43615-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.859), Run(0.213), Outside, urban or manmade(0.212)
- **音频特征**: RMS=0.0048, 频谱重心=1398Hz, 场景提示=mixed_environment

### 样本 610: airport-prague-1069-40257-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.775), Music(0.129), Vehicle(0.104)
- **音频特征**: RMS=0.0033, 频谱重心=1326Hz, 场景提示=quiet_indoor

### 样本 611: airport-stockholm-207-6296-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.795), Clip-clop(0.174), Animal(0.165)
- **音频特征**: RMS=0.0030, 频谱重心=1441Hz, 场景提示=mixed_environment

### 样本 612: airport-lisbon-1000-40463-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.818), Chatter(0.130)
- **音频特征**: RMS=0.0048, 频谱重心=1593Hz, 场景提示=mixed_environment

### 样本 613: metro_station-lisbon-1020-42493-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.689), Music(0.150)
- **音频特征**: RMS=0.0035, 频谱重心=1119Hz, 场景提示=quiet_indoor

### 样本 614: tram-lisbon-1191-45571-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.723), Vehicle(0.574), Train(0.224)
- **音频特征**: RMS=0.0724, 频谱重心=634Hz, 场景提示=mixed_environment

### 样本 615: metro-lyon-1064-43472-a.wav
- **真实场景**: metro
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.714), Music(0.183)
- **音频特征**: RMS=0.0038, 频谱重心=1341Hz, 场景提示=quiet_indoor

### 样本 616: airport-vienna-13-544-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.833), Clip-clop(0.182), Vehicle(0.145)
- **音频特征**: RMS=0.0019, 频谱重心=1384Hz, 场景提示=mixed_environment

### 样本 617: street_pedestrian-lyon-1072-43072-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: tram
- **检测到的事件**: Speech(0.805), Male speech, man speaking(0.130)
- **音频特征**: RMS=0.0009, 频谱重心=1502Hz, 场景提示=mixed_environment

### 样本 618: metro_station-prague-1170-44263-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Train(0.267), Vehicle(0.259), Railroad car, train wagon(0.164)
- **音频特征**: RMS=0.0065, 频谱重心=898Hz, 场景提示=quiet_indoor

### 样本 619: tram-helsinki-184-5726-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.675), Vehicle(0.128)
- **音频特征**: RMS=0.0033, 频谱重心=730Hz, 场景提示=quiet_indoor

### 样本 620: bus-paris-29-965-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.474)
- **音频特征**: RMS=0.0058, 频谱重心=1064Hz, 场景提示=quiet_indoor

### 样本 621: bus-lisbon-1123-42725-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.773), Vehicle(0.262)
- **音频特征**: RMS=0.0109, 频谱重心=981Hz, 场景提示=mixed_environment

### 样本 622: tram-lyon-1091-43153-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.745), Vehicle(0.361)
- **音频特征**: RMS=0.0132, 频谱重心=791Hz, 场景提示=mixed_environment

### 样本 623: park-prague-1185-45724-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.581), Music(0.254), Animal(0.254)
- **音频特征**: RMS=0.0065, 频谱重心=871Hz, 场景提示=quiet_indoor

### 样本 624: airport-vienna-14-597-a.wav
- **真实场景**: airport
- **AE预测**: tram
- **AS预测**: airport
- **检测到的事件**: Speech(0.864), Female speech, woman speaking(0.525), Narration, monologue(0.375)
- **音频特征**: RMS=0.0066, 频谱重心=2238Hz, 场景提示=mixed_environment

### 样本 625: metro_station-stockholm-85-2317-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.794), Clip-clop(0.114), Animal(0.103)
- **音频特征**: RMS=0.0074, 频谱重心=867Hz, 场景提示=quiet_indoor

### 样本 626: shopping_mall-prague-1009-43699-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.632), Music(0.121)
- **音频特征**: RMS=0.0053, 频谱重心=1323Hz, 场景提示=quiet_indoor

### 样本 627: tram-milan-1134-40341-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.218), Train(0.167), Rail transport(0.115)
- **音频特征**: RMS=0.0370, 频谱重心=835Hz, 场景提示=mixed_environment

### 样本 628: metro-barcelona-42-1290-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Mouse(0.127), Vehicle(0.107)
- **音频特征**: RMS=0.0098, 频谱重心=777Hz, 场景提示=quiet_indoor

### 样本 629: bus-prague-1147-41496-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.410), White noise(0.119), Car(0.110)
- **音频特征**: RMS=0.0195, 频谱重心=1411Hz, 场景提示=mixed_environment

### 样本 630: airport-prague-1173-45158-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.430), Tick-tock(0.160), Music(0.159)
- **音频特征**: RMS=0.0015, 频谱重心=1618Hz, 场景提示=mixed_environment

### 样本 631: metro-helsinki-44-1324-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.353), Train(0.325), Railroad car, train wagon(0.233)
- **音频特征**: RMS=0.0384, 频谱重心=634Hz, 场景提示=mixed_environment

### 样本 632: park-lyon-1144-42494-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.791), Animal(0.451), Clip-clop(0.400)
- **音频特征**: RMS=0.0007, 频谱重心=1336Hz, 场景提示=quiet_indoor

### 样本 633: airport-lisbon-1114-43635-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.803), Clip-clop(0.170), Animal(0.151)
- **音频特征**: RMS=0.0072, 频谱重心=1293Hz, 场景提示=quiet_indoor

### 样本 634: shopping_mall-paris-132-3986-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.745), Clip-clop(0.236), Animal(0.228)
- **音频特征**: RMS=0.0035, 频谱重心=1478Hz, 场景提示=quiet_indoor

### 样本 635: street_pedestrian-lyon-1047-42214-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.410), Animal(0.169), Clip-clop(0.135)
- **音频特征**: RMS=0.0015, 频谱重心=1337Hz, 场景提示=quiet_indoor

### 样本 636: street_traffic-helsinki-269-8200-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.500), Vehicle(0.362), Boat, Water vehicle(0.253)
- **音频特征**: RMS=0.0063, 频谱重心=806Hz, 场景提示=quiet_indoor

### 样本 637: airport-barcelona-1-53-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.800), Clip-clop(0.156), Animal(0.142)
- **音频特征**: RMS=0.0036, 频谱重心=1143Hz, 场景提示=quiet_indoor

### 样本 638: shopping_mall-paris-257-7798-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.811), Clip-clop(0.134), Animal(0.127)
- **音频特征**: RMS=0.0026, 频谱重心=1610Hz, 场景提示=mixed_environment

### 样本 639: airport-paris-7-324-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.477)
- **音频特征**: RMS=0.0024, 频谱重心=1295Hz, 场景提示=quiet_indoor

### 样本 640: street_pedestrian-milan-1165-44526-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.747), Clip-clop(0.264), Animal(0.246)
- **音频特征**: RMS=0.0012, 频谱重心=1505Hz, 场景提示=mixed_environment

### 样本 641: shopping_mall-lisbon-1137-42585-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.621)
- **音频特征**: RMS=0.0029, 频谱重心=1485Hz, 场景提示=mixed_environment

### 样本 642: shopping_mall-paris-257-7782-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.728), Animal(0.334), Clip-clop(0.277)
- **音频特征**: RMS=0.0022, 频谱重心=1641Hz, 场景提示=mixed_environment

### 样本 643: metro_station-barcelona-62-1873-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.796), Male speech, man speaking(0.148)
- **音频特征**: RMS=0.0016, 频谱重心=1138Hz, 场景提示=quiet_indoor

### 样本 644: street_pedestrian-stockholm-266-8083-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.267)
- **音频特征**: RMS=0.0046, 频谱重心=1349Hz, 场景提示=mixed_environment

### 样本 645: shopping_mall-paris-132-3970-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.443), Music(0.197)
- **音频特征**: RMS=0.0022, 频谱重心=1360Hz, 场景提示=quiet_indoor

### 样本 646: metro_station-lisbon-1221-44560-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Music(0.159), Speech(0.120)
- **音频特征**: RMS=0.0075, 频谱重心=776Hz, 场景提示=quiet_indoor

### 样本 647: airport-vienna-14-585-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.539), Animal(0.253), Bird(0.147)
- **音频特征**: RMS=0.0010, 频谱重心=1479Hz, 场景提示=quiet_indoor

### 样本 648: public_square-paris-251-7519-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.502), Animal(0.491), Domestic animals, pets(0.426)
- **音频特征**: RMS=0.0058, 频谱重心=912Hz, 场景提示=quiet_indoor

### 样本 649: street_pedestrian-lyon-1003-40803-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.587)
- **音频特征**: RMS=0.0018, 频谱重心=1166Hz, 场景提示=quiet_indoor

### 样本 650: tram-barcelona-180-5563-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.718), Door(0.311), Sliding door(0.259)
- **音频特征**: RMS=0.0091, 频谱重心=1250Hz, 场景提示=quiet_indoor

### 样本 651: bus-lisbon-1123-43119-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.715), Vehicle(0.299)
- **音频特征**: RMS=0.0102, 频谱重心=1006Hz, 场景提示=mixed_environment

### 样本 652: public_square-vienna-253-7571-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.862), Outside, urban or manmade(0.189), Hubbub, speech noise, speech babble(0.121)
- **音频特征**: RMS=0.0025, 频谱重心=1191Hz, 场景提示=quiet_indoor

### 样本 653: metro-barcelona-41-1224-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.803), Vehicle(0.442), Bus(0.106)
- **音频特征**: RMS=0.0095, 频谱重心=799Hz, 场景提示=quiet_indoor

### 样本 654: street_traffic-helsinki-166-5114-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.425), Boat, Water vehicle(0.354), Wind(0.167)
- **音频特征**: RMS=0.0058, 频谱重心=995Hz, 场景提示=quiet_indoor

### 样本 655: bus-milan-1154-40556-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.655), Speech(0.570), Car(0.443)
- **音频特征**: RMS=0.0250, 频谱重心=1211Hz, 场景提示=mixed_environment

### 样本 656: bus-paris-27-925-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.577), Vehicle(0.515), Car(0.170)
- **音频特征**: RMS=0.0197, 频谱重心=562Hz, 场景提示=mixed_environment

### 样本 657: street_pedestrian-lisbon-1004-43105-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.723)
- **音频特征**: RMS=0.0024, 频谱重心=1163Hz, 场景提示=quiet_indoor

### 样本 658: tram-milan-1036-43582-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.335), Bus(0.145), Sliding door(0.105)
- **音频特征**: RMS=0.0056, 频谱重心=1293Hz, 场景提示=mixed_environment

### 样本 659: metro_station-lisbon-1007-42527-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.743), Vehicle(0.429), Train(0.107)
- **音频特征**: RMS=0.0206, 频谱重心=1060Hz, 场景提示=mixed_environment

### 样本 660: metro_station-paris-79-2153-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.204), Walk, footsteps(0.161), Animal(0.150)
- **音频特征**: RMS=0.0020, 频谱重心=1511Hz, 场景提示=quiet_indoor

### 样本 661: airport-lyon-1095-43600-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.792), Clip-clop(0.192), Animal(0.157)
- **音频特征**: RMS=0.0021, 频谱重心=1509Hz, 场景提示=mixed_environment

### 样本 662: metro-lyon-1201-45023-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.460), Ship(0.144), Car(0.125)
- **音频特征**: RMS=0.0127, 频谱重心=1365Hz, 场景提示=mixed_environment

### 样本 663: metro-helsinki-222-6756-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.652), Vehicle(0.409), Train(0.209)
- **音频特征**: RMS=0.0146, 频谱重心=851Hz, 场景提示=mixed_environment

### 样本 664: shopping_mall-london-256-7693-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.689), Clip-clop(0.336), Horse(0.256)
- **音频特征**: RMS=0.0026, 频谱重心=1657Hz, 场景提示=mixed_environment

### 样本 665: tram-lyon-1225-45456-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Sliding door(0.512), Door(0.340), Cupboard open or close(0.172)
- **音频特征**: RMS=0.0090, 频谱重心=838Hz, 场景提示=quiet_indoor

### 样本 666: tram-vienna-285-8625-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.862), Vehicle(0.310), Female speech, woman speaking(0.181)
- **音频特征**: RMS=0.0158, 频谱重心=584Hz, 场景提示=mixed_environment

### 样本 667: shopping_mall-stockholm-136-4112-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.669)
- **音频特征**: RMS=0.0036, 频谱重心=998Hz, 场景提示=quiet_indoor

### 样本 668: bus-milan-1190-44598-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.679), Vehicle(0.537), Bus(0.187)
- **音频特征**: RMS=0.0181, 频谱重心=747Hz, 场景提示=mixed_environment

### 样本 669: public_square-milan-1014-44082-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.300), Vehicle(0.212), Animal(0.133)
- **音频特征**: RMS=0.0054, 频谱重心=1157Hz, 场景提示=quiet_indoor

### 样本 670: public_square-milan-1168-44912-a.wav
- **真实场景**: public_square
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.561), Vehicle(0.160)
- **音频特征**: RMS=0.0029, 频谱重心=2286Hz, 场景提示=mixed_environment

### 样本 671: street_traffic-milan-1097-41108-a.wav
- **真实场景**: street_traffic
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.205)
- **音频特征**: RMS=0.0014, 频谱重心=1153Hz, 场景提示=quiet_indoor

### 样本 672: tram-vienna-285-8615-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Bird(0.539), Pigeon, dove(0.527), Coo(0.325)
- **音频特征**: RMS=0.0147, 频谱重心=527Hz, 场景提示=mixed_environment

### 样本 673: shopping_mall-london-256-7772-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.796), Clip-clop(0.286), Horse(0.217)
- **音频特征**: RMS=0.0024, 频谱重心=1573Hz, 场景提示=mixed_environment

### 样本 674: tram-stockholm-197-5931-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.796), Music(0.462), Vehicle(0.293)
- **音频特征**: RMS=0.0171, 频谱重心=568Hz, 场景提示=mixed_environment

### 样本 675: park-london-243-7259-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.588), Animal(0.138), Vehicle(0.130)
- **音频特征**: RMS=0.0011, 频谱重心=913Hz, 场景提示=quiet_indoor

### 样本 676: street_pedestrian-milan-1096-41707-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.832), Animal(0.156), Clip-clop(0.145)
- **音频特征**: RMS=0.0035, 频谱重心=1513Hz, 场景提示=mixed_environment

### 样本 677: airport-prague-1023-42332-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.478)
- **音频特征**: RMS=0.0055, 频谱重心=1283Hz, 场景提示=mixed_environment

### 样本 678: tram-stockholm-197-5932-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.766), Microwave oven(0.180), Vehicle(0.165)
- **音频特征**: RMS=0.0103, 频谱重心=783Hz, 场景提示=mixed_environment

### 样本 679: street_pedestrian-vienna-158-4790-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.387)
- **音频特征**: RMS=0.0012, 频谱重心=1261Hz, 场景提示=quiet_indoor

### 样本 680: shopping_mall-london-256-7756-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.558), Animal(0.103)
- **音频特征**: RMS=0.0028, 频谱重心=1401Hz, 场景提示=mixed_environment

### 样本 681: metro-lyon-1126-43905-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.567), Sliding door(0.355), Door(0.199)
- **音频特征**: RMS=0.0105, 频谱重心=957Hz, 场景提示=mixed_environment

### 样本 682: metro-stockholm-57-1699-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Train(0.578), Vehicle(0.458), Rail transport(0.413)
- **音频特征**: RMS=0.0185, 频谱重心=393Hz, 场景提示=mixed_environment

### 样本 683: tram-paris-280-8507-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.649), Vehicle(0.421), Car(0.190)
- **音频特征**: RMS=0.0096, 频谱重心=738Hz, 场景提示=quiet_indoor

### 样本 684: public_square-london-113-3302-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.647), Animal(0.214), Clip-clop(0.136)
- **音频特征**: RMS=0.0029, 频谱重心=1142Hz, 场景提示=quiet_indoor

### 样本 685: airport-lyon-1101-41267-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.264), Vehicle(0.234)
- **音频特征**: RMS=0.0024, 频谱重心=1916Hz, 场景提示=mixed_environment

### 样本 686: metro_station-barcelona-62-1862-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.696)
- **音频特征**: RMS=0.0014, 频谱重心=1204Hz, 场景提示=quiet_indoor

### 样本 687: street_pedestrian-paris-153-4648-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Inside, small room(0.102)
- **音频特征**: RMS=0.0020, 频谱重心=1295Hz, 场景提示=quiet_indoor

### 样本 688: metro_station-helsinki-65-1947-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.439), Animal(0.111)
- **音频特征**: RMS=0.0022, 频谱重心=989Hz, 场景提示=quiet_indoor

### 样本 689: street_pedestrian-vienna-267-8124-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: metro_station
- **检测到的事件**: Patter(0.155), Mouse(0.134)
- **音频特征**: RMS=0.0039, 频谱重心=898Hz, 场景提示=quiet_indoor

### 样本 690: tram-vienna-200-6049-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.740), Vehicle(0.418), Power windows, electric windows(0.163)
- **音频特征**: RMS=0.0047, 频谱重心=1132Hz, 场景提示=quiet_indoor

### 样本 691: airport-london-205-6197-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.442), Animal(0.253), Horse(0.212)
- **音频特征**: RMS=0.0017, 频谱重心=1628Hz, 场景提示=mixed_environment

### 样本 692: shopping_mall-lyon-1196-44886-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.328)
- **音频特征**: RMS=0.0014, 频谱重心=1471Hz, 场景提示=mixed_environment

### 样本 693: airport-milan-1061-41750-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.803), Animal(0.176)
- **音频特征**: RMS=0.0022, 频谱重心=1506Hz, 场景提示=mixed_environment

### 样本 694: park-london-96-2676-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.830), Animal(0.347), Crow(0.221)
- **音频特征**: RMS=0.0008, 频谱重心=1814Hz, 场景提示=mixed_environment

### 样本 695: airport-helsinki-204-6146-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.754), Vehicle(0.135), Animal(0.119)
- **音频特征**: RMS=0.0030, 频谱重心=1400Hz, 场景提示=quiet_indoor

### 样本 696: tram-paris-196-5912-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.337), Vehicle(0.331), Train(0.130)
- **音频特征**: RMS=0.0076, 频谱重心=698Hz, 场景提示=quiet_indoor

### 样本 697: tram-milan-1134-42209-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.305), Train(0.233), Rail transport(0.173)
- **音频特征**: RMS=0.0144, 频谱重心=863Hz, 场景提示=mixed_environment

### 样本 698: tram-barcelona-181-5607-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.756), Vehicle(0.500), Train(0.118)
- **音频特征**: RMS=0.0183, 频谱重心=714Hz, 场景提示=mixed_environment

### 样本 699: street_pedestrian-london-263-7976-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.741), Music(0.634)
- **音频特征**: RMS=0.0031, 频谱重心=1269Hz, 场景提示=quiet_indoor

### 样本 700: tram-lyon-1216-44958-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.713), Vehicle(0.174)
- **音频特征**: RMS=0.0052, 频谱重心=981Hz, 场景提示=quiet_indoor

### 样本 701: shopping_mall-paris-134-4039-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.413), Animal(0.359), Clip-clop(0.303)
- **音频特征**: RMS=0.0018, 频谱重心=1187Hz, 场景提示=quiet_indoor

### 样本 702: shopping_mall-prague-1219-45370-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.868), Animal(0.128), Horse(0.114)
- **音频特征**: RMS=0.0024, 频谱重心=1438Hz, 场景提示=mixed_environment

### 样本 703: shopping_mall-london-256-7733-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.808), Animal(0.254), Clip-clop(0.185)
- **音频特征**: RMS=0.0039, 频谱重心=1174Hz, 场景提示=quiet_indoor

### 样本 704: tram-vienna-201-6054-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.715), Animal(0.166), Vehicle(0.121)
- **音频特征**: RMS=0.0071, 频谱重心=2287Hz, 场景提示=mixed_environment

### 样本 705: bus-milan-1078-40500-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.578), Train(0.185), Field recording(0.108)
- **音频特征**: RMS=0.0118, 频谱重心=977Hz, 场景提示=mixed_environment

### 样本 706: public_square-london-114-3309-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: airport
- **检测到的事件**: Speech(0.860), Male speech, man speaking(0.354), Narration, monologue(0.255)
- **音频特征**: RMS=0.0026, 频谱重心=1050Hz, 场景提示=quiet_indoor

### 样本 707: metro-vienna-60-1808-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.479), Train(0.156)
- **音频特征**: RMS=0.0257, 频谱重心=313Hz, 场景提示=mixed_environment

### 样本 708: metro_station-milan-1127-41248-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.539)
- **音频特征**: RMS=0.0033, 频谱重心=1358Hz, 场景提示=quiet_indoor

### 样本 709: street_pedestrian-milan-1080-40536-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Vehicle(0.226), Boat, Water vehicle(0.163), Rain(0.125)
- **音频特征**: RMS=0.0015, 频谱重心=2387Hz, 场景提示=mixed_environment

### 样本 710: street_pedestrian-paris-154-4678-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.803), Clip-clop(0.252), Horse(0.192)
- **音频特征**: RMS=0.0013, 频谱重心=1703Hz, 场景提示=mixed_environment

### 样本 711: street_pedestrian-lisbon-1098-40905-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.798), Music(0.290), Clip-clop(0.235)
- **音频特征**: RMS=0.0029, 频谱重心=1497Hz, 场景提示=mixed_environment

### 样本 712: metro_station-paris-82-2209-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Music(0.339)
- **音频特征**: RMS=0.0048, 频谱重心=1738Hz, 场景提示=quiet_indoor

### 样本 713: shopping_mall-london-256-7750-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.697), Clip-clop(0.370), Animal(0.347)
- **音频特征**: RMS=0.0025, 频谱重心=1369Hz, 场景提示=mixed_environment

### 样本 714: park-london-243-7229-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.563), Honk(0.115), Animal(0.104)
- **音频特征**: RMS=0.0011, 频谱重心=955Hz, 场景提示=quiet_indoor

### 样本 715: airport-paris-206-6261-a.wav
- **真实场景**: airport
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **音频特征**: RMS=0.0068, 频谱重心=984Hz, 场景提示=quiet_indoor

### 样本 716: metro_station-vienna-240-7130-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.837)
- **音频特征**: RMS=0.0030, 频谱重心=963Hz, 场景提示=quiet_indoor

### 样本 717: shopping_mall-paris-134-4051-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.744), Animal(0.153), Vehicle(0.110)
- **音频特征**: RMS=0.0016, 频谱重心=1284Hz, 场景提示=quiet_indoor

### 样本 718: metro-milan-1143-41720-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.490), Vehicle(0.153)
- **音频特征**: RMS=0.0118, 频谱重心=819Hz, 场景提示=mixed_environment

### 样本 719: tram-london-186-5772-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.570), Music(0.231), Television(0.117)
- **音频特征**: RMS=0.0053, 频谱重心=1027Hz, 场景提示=quiet_indoor

### 样本 720: public_square-prague-1075-42744-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.828), Clip-clop(0.394), Animal(0.386)
- **音频特征**: RMS=0.0020, 频谱重心=1232Hz, 场景提示=quiet_indoor

### 样本 721: street_pedestrian-london-149-4506-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.856), Run(0.363), Outside, urban or manmade(0.239)
- **音频特征**: RMS=0.0023, 频谱重心=1186Hz, 场景提示=quiet_indoor

### 样本 722: tram-helsinki-183-5677-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.221)
- **音频特征**: RMS=0.0037, 频谱重心=883Hz, 场景提示=quiet_indoor

### 样本 723: tram-prague-1042-42265-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.561), Animal(0.508), Horse(0.424)
- **音频特征**: RMS=0.0645, 频谱重心=409Hz, 场景提示=mixed_environment

### 样本 724: bus-lyon-1177-44264-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.797), Vehicle(0.220), Animal(0.160)
- **音频特征**: RMS=0.0171, 频谱重心=736Hz, 场景提示=mixed_environment

### 样本 725: tram-london-187-5789-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Train(0.781), Rail transport(0.637), Railroad car, train wagon(0.614)
- **音频特征**: RMS=0.0103, 频谱重心=859Hz, 场景提示=mixed_environment

### 样本 726: street_pedestrian-paris-152-4616-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Mouse(0.427), Speech(0.269), Animal(0.157)
- **音频特征**: RMS=0.0018, 频谱重心=1575Hz, 场景提示=quiet_indoor

### 样本 727: street_traffic-london-270-8221-a.wav
- **真实场景**: street_traffic
- **AE预测**: bus
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.732), Truck(0.258), Air brake(0.255)
- **音频特征**: RMS=0.0136, 频谱重心=1223Hz, 场景提示=mixed_environment

### 样本 728: shopping_mall-lyon-1043-41875-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.753), Animal(0.259)
- **音频特征**: RMS=0.0046, 频谱重心=1345Hz, 场景提示=mixed_environment

### 样本 729: airport-prague-1023-41418-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.779), Clip-clop(0.146), Animal(0.138)
- **音频特征**: RMS=0.0076, 频谱重心=1209Hz, 场景提示=mixed_environment

### 样本 730: metro-helsinki-222-6745-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.820), Vehicle(0.726), Car(0.202)
- **音频特征**: RMS=0.0314, 频谱重心=814Hz, 场景提示=mixed_environment

### 样本 731: metro-lisbon-1224-45583-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.638), Vehicle(0.408)
- **音频特征**: RMS=0.0101, 频谱重心=809Hz, 场景提示=mixed_environment

### 样本 732: airport-stockholm-208-6328-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.790), Clip-clop(0.281), Horse(0.241)
- **音频特征**: RMS=0.0052, 频谱重心=1155Hz, 场景提示=quiet_indoor

### 样本 733: street_pedestrian-prague-1051-43087-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.815), Animal(0.127), Vehicle(0.114)
- **音频特征**: RMS=0.0044, 频谱重心=1167Hz, 场景提示=quiet_indoor

### 样本 734: public_square-lyon-1208-45647-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.705), Animal(0.159), Vehicle(0.137)
- **音频特征**: RMS=0.0037, 频谱重心=1716Hz, 场景提示=mixed_environment

### 样本 735: street_pedestrian-paris-153-4638-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.640), Animal(0.146)
- **音频特征**: RMS=0.0020, 频谱重心=1195Hz, 场景提示=quiet_indoor

### 样本 736: airport-paris-9-413-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.689)
- **音频特征**: RMS=0.0021, 频谱重心=1499Hz, 场景提示=mixed_environment

### 样本 737: public_square-milan-1014-40695-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.328), Animal(0.138)
- **音频特征**: RMS=0.0023, 频谱重心=1353Hz, 场景提示=quiet_indoor

### 样本 738: metro-helsinki-222-6762-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.604), Vehicle(0.332), Sliding door(0.142)
- **音频特征**: RMS=0.0133, 频谱重心=768Hz, 场景提示=mixed_environment

### 样本 739: tram-london-279-8476-a.wav
- **真实场景**: tram
- **AE预测**: airport
- **AS预测**: tram
- **检测到的事件**: Speech(0.693), Vehicle(0.151)
- **音频特征**: RMS=0.0023, 频谱重心=1218Hz, 场景提示=quiet_indoor

### 样本 740: airport-paris-206-6265-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Clip-clop(0.150), Animal(0.140), Horse(0.112)
- **音频特征**: RMS=0.0105, 频谱重心=1064Hz, 场景提示=mixed_environment

### 样本 741: airport-milan-1089-41269-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.723), Animal(0.272), Clip-clop(0.258)
- **音频特征**: RMS=0.0015, 频谱重心=1441Hz, 场景提示=mixed_environment

### 样本 742: shopping_mall-vienna-140-4283-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.698), Clip-clop(0.159), Animal(0.157)
- **音频特征**: RMS=0.0015, 频谱重心=1238Hz, 场景提示=mixed_environment

### 样本 743: shopping_mall-vienna-259-7875-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.880), Clip-clop(0.249), Horse(0.174)
- **音频特征**: RMS=0.0038, 频谱重心=1279Hz, 场景提示=quiet_indoor

### 样本 744: street_pedestrian-stockholm-157-4777-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.541), Fire(0.168), Rain on surface(0.114)
- **音频特征**: RMS=0.0043, 频谱重心=1812Hz, 场景提示=quiet_indoor

### 样本 745: airport-lisbon-1122-40992-a.wav
- **真实场景**: airport
- **AE预测**: metro_station
- **AS预测**: street_traffic
- **检测到的事件**: Animal(0.226), Vehicle(0.185), Horse(0.174)
- **音频特征**: RMS=0.0041, 频谱重心=1466Hz, 场景提示=mixed_environment

### 样本 746: park-london-97-2724-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.742), Vehicle(0.413), Bicycle(0.224)
- **音频特征**: RMS=0.0027, 频谱重心=963Hz, 场景提示=quiet_indoor

### 样本 747: street_pedestrian-lyon-1072-42716-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.744)
- **音频特征**: RMS=0.0010, 频谱重心=1598Hz, 场景提示=mixed_environment

### 样本 748: tram-milan-1134-42351-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.493), Rail transport(0.386), Vehicle(0.380)
- **音频特征**: RMS=0.0163, 频谱重心=941Hz, 场景提示=mixed_environment

### 样本 749: airport-lyon-1095-40245-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.845), Animal(0.140), Clip-clop(0.127)
- **音频特征**: RMS=0.0014, 频谱重心=1337Hz, 场景提示=quiet_indoor

### 样本 750: metro-lyon-1079-40316-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.744), Vehicle(0.290), Animal(0.175)
- **音频特征**: RMS=0.0062, 频谱重心=1124Hz, 场景提示=quiet_indoor

### 样本 751: metro-stockholm-227-6822-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.886), Music(0.688), Vehicle(0.127)
- **音频特征**: RMS=0.0126, 频谱重心=846Hz, 场景提示=mixed_environment

### 样本 752: street_pedestrian-lisbon-1099-41223-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.848), Vehicle(0.130), Animal(0.112)
- **音频特征**: RMS=0.0035, 频谱重心=1159Hz, 场景提示=quiet_indoor

### 样本 753: metro-milan-1062-43335-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.640), Vehicle(0.579), Bus(0.157)
- **音频特征**: RMS=0.0176, 频谱重心=522Hz, 场景提示=mixed_environment

### 样本 754: street_pedestrian-stockholm-156-4745-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.891), Run(0.331), Outside, urban or manmade(0.231)
- **音频特征**: RMS=0.0065, 频谱重心=1328Hz, 场景提示=mixed_environment

### 样本 755: shopping_mall-milan-1084-42326-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.622), Music(0.108)
- **音频特征**: RMS=0.0024, 频谱重心=1594Hz, 场景提示=mixed_environment

### 样本 756: airport-lyon-1095-42753-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.656), Music(0.112)
- **音频特征**: RMS=0.0020, 频谱重心=1370Hz, 场景提示=quiet_indoor

### 样本 757: public_square-prague-1152-42858-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.572), Church bell(0.366), Bell(0.228)
- **音频特征**: RMS=0.0030, 频谱重心=1294Hz, 场景提示=mixed_environment

### 样本 758: tram-london-190-5830-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.651), Vehicle(0.337), Train(0.309)
- **音频特征**: RMS=0.0110, 频谱重心=661Hz, 场景提示=mixed_environment

### 样本 759: street_pedestrian-prague-1051-43235-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.875), Clip-clop(0.214), Animal(0.175)
- **音频特征**: RMS=0.0056, 频谱重心=1143Hz, 场景提示=quiet_indoor

### 样本 760: street_pedestrian-stockholm-156-4723-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.825), Outside, urban or manmade(0.137), Animal(0.116)
- **音频特征**: RMS=0.0092, 频谱重心=998Hz, 场景提示=quiet_indoor

### 样本 761: street_pedestrian-helsinki-148-4468-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.261)
- **音频特征**: RMS=0.0022, 频谱重心=674Hz, 场景提示=quiet_indoor

### 样本 762: metro-stockholm-227-6841-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.800), Music(0.239), Pigeon, dove(0.236)
- **音频特征**: RMS=0.0112, 频谱重心=870Hz, 场景提示=mixed_environment

### 样本 763: airport-lisbon-1122-43249-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.737), Vehicle(0.154), Animal(0.119)
- **音频特征**: RMS=0.0038, 频谱重心=1236Hz, 场景提示=quiet_indoor

### 样本 764: shopping_mall-helsinki-255-7643-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.838), Clip-clop(0.222), Animal(0.153)
- **音频特征**: RMS=0.0072, 频谱重心=1349Hz, 场景提示=mixed_environment

### 样本 765: street_traffic-stockholm-175-5402-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Speech(0.370), Vehicle(0.228), Animal(0.128)
- **音频特征**: RMS=0.0141, 频谱重心=720Hz, 场景提示=mixed_environment

### 样本 766: airport-london-5-230-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.663), Music(0.363), Animal(0.228)
- **音频特征**: RMS=0.0014, 频谱重心=1713Hz, 场景提示=mixed_environment

### 样本 767: public_square-paris-251-7507-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.159), Vehicle(0.132)
- **音频特征**: RMS=0.0050, 频谱重心=736Hz, 场景提示=quiet_indoor

### 样本 768: public_square-milan-1044-42475-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.550), Animal(0.220), Bird(0.143)
- **音频特征**: RMS=0.0036, 频谱重心=1328Hz, 场景提示=quiet_indoor

### 样本 769: street_pedestrian-lyon-1003-42712-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.734)
- **音频特征**: RMS=0.0015, 频谱重心=1236Hz, 场景提示=quiet_indoor

### 样本 770: street_pedestrian-milan-1205-44602-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.426), Mouse(0.339), Animal(0.158)
- **音频特征**: RMS=0.0024, 频谱重心=1203Hz, 场景提示=quiet_indoor

### 样本 771: airport-vienna-209-6373-a.wav
- **真实场景**: airport
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.732), Silence(0.185)
- **音频特征**: RMS=0.0013, 频谱重心=999Hz, 场景提示=quiet_indoor

### 样本 772: bus-paris-29-963-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.664), Vehicle(0.326), Bus(0.102)
- **音频特征**: RMS=0.0060, 频谱重心=1036Hz, 场景提示=quiet_indoor

### 样本 773: airport-milan-1108-43191-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.766), Bleat(0.572), Sheep(0.534)
- **音频特征**: RMS=0.0017, 频谱重心=1397Hz, 场景提示=quiet_indoor

### 样本 774: tram-barcelona-275-8386-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.383), Speech(0.247), Train(0.108)
- **音频特征**: RMS=0.0116, 频谱重心=536Hz, 场景提示=mixed_environment

### 样本 775: metro_station-milan-1127-40584-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.645), Animal(0.130), Vehicle(0.107)
- **音频特征**: RMS=0.0052, 频谱重心=1375Hz, 场景提示=mixed_environment

### 样本 776: metro_station-paris-237-7055-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.876), Outside, urban or manmade(0.140), Animal(0.116)
- **音频特征**: RMS=0.0095, 频谱重心=1301Hz, 场景提示=quiet_indoor

### 样本 777: shopping_mall-lisbon-1176-44166-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Music(0.171), Speech(0.151)
- **音频特征**: RMS=0.0060, 频谱重心=1049Hz, 场景提示=quiet_indoor

### 样本 778: airport-london-6-290-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Silence(0.117), Mouse(0.106)
- **音频特征**: RMS=0.0017, 频谱重心=1248Hz, 场景提示=quiet_indoor

### 样本 779: metro_station-paris-238-7074-a.wav
- **真实场景**: metro_station
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.605), Narration, monologue(0.113), Music(0.113)
- **音频特征**: RMS=0.0049, 频谱重心=849Hz, 场景提示=quiet_indoor

### 样本 780: airport-prague-1023-42171-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Clip-clop(0.350), Horse(0.319), Animal(0.273)
- **音频特征**: RMS=0.0060, 频谱重心=1131Hz, 场景提示=quiet_indoor

### 样本 781: street_traffic-lyon-1110-43164-a.wav
- **真实场景**: street_traffic
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.244)
- **音频特征**: RMS=0.0030, 频谱重心=849Hz, 场景提示=quiet_indoor

### 样本 782: tram-milan-1048-43480-a.wav
- **真实场景**: tram
- **AE预测**: park
- **AS预测**: tram
- **检测到的事件**: Tick(0.281), Tick-tock(0.273), Silence(0.128)
- **音频特征**: RMS=0.0015, 频谱重心=1390Hz, 场景提示=quiet_indoor

### 样本 783: metro_station-vienna-86-2325-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.836), Children playing(0.530), Child speech, kid speaking(0.192)
- **音频特征**: RMS=0.0171, 频谱重心=744Hz, 场景提示=mixed_environment

### 样本 784: street_pedestrian-barcelona-145-4376-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.830), Vehicle(0.103)
- **音频特征**: RMS=0.0029, 频谱重心=1606Hz, 场景提示=mixed_environment

### 样本 785: street_pedestrian-london-151-4596-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Sigh(0.309), Speech(0.301), Inside, small room(0.118)
- **音频特征**: RMS=0.0009, 频谱重心=1185Hz, 场景提示=quiet_indoor

### 样本 786: public_square-paris-251-7521-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.278), Animal(0.227), Vehicle(0.130)
- **音频特征**: RMS=0.0039, 频谱重心=963Hz, 场景提示=quiet_indoor

### 样本 787: street_pedestrian-paris-154-4661-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.468), Vehicle(0.189)
- **音频特征**: RMS=0.0020, 频谱重心=1319Hz, 场景提示=quiet_indoor

### 样本 788: metro_station-helsinki-67-1984-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: park
- **检测到的事件**: Vehicle(0.142)
- **音频特征**: RMS=0.0009, 频谱重心=875Hz, 场景提示=quiet_indoor

### 样本 789: metro_station-prague-1170-44837-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.666), Vehicle(0.157), Animal(0.117)
- **音频特征**: RMS=0.0162, 频谱重心=808Hz, 场景提示=mixed_environment

### 样本 790: park-paris-99-2797-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.442), Animal(0.215), Run(0.178)
- **音频特征**: RMS=0.0031, 频谱重心=1136Hz, 场景提示=quiet_indoor

### 样本 791: park-prague-1185-44295-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.628), Vehicle(0.302), Animal(0.125)
- **音频特征**: RMS=0.0087, 频谱重心=483Hz, 场景提示=quiet_indoor

### 样本 792: street_pedestrian-london-149-4533-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.630)
- **音频特征**: RMS=0.0017, 频谱重心=711Hz, 场景提示=quiet_indoor

### 样本 793: tram-prague-1109-40196-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.373), Vehicle(0.255), Train(0.210)
- **音频特征**: RMS=0.0161, 频谱重心=678Hz, 场景提示=mixed_environment

### 样本 794: street_pedestrian-lyon-1162-44621-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.747), Clip-clop(0.389), Animal(0.318)
- **音频特征**: RMS=0.0019, 频谱重心=1143Hz, 场景提示=quiet_indoor

### 样本 795: public_square-lyon-1208-45198-a.wav
- **真实场景**: public_square
- **AE预测**: metro_station
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.273), White noise(0.151)
- **音频特征**: RMS=0.0048, 频谱重心=2195Hz, 场景提示=mixed_environment

### 样本 796: public_square-milan-1074-42786-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.669), Animal(0.195), Clip-clop(0.177)
- **音频特征**: RMS=0.0040, 频谱重心=969Hz, 场景提示=quiet_indoor

### 样本 797: park-prague-1185-44120-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.341)
- **音频特征**: RMS=0.0054, 频谱重心=559Hz, 场景提示=quiet_indoor

### 样本 798: metro_station-paris-78-2134-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.809), Animal(0.355), Clip-clop(0.331)
- **音频特征**: RMS=0.0083, 频谱重心=1012Hz, 场景提示=quiet_indoor

### 样本 799: airport-milan-1108-41447-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Arrow(0.687), Speech(0.659), Chop(0.158)
- **音频特征**: RMS=0.0020, 频谱重心=1425Hz, 场景提示=quiet_indoor

### 样本 800: shopping_mall-prague-1031-40390-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.269), White noise(0.101)
- **音频特征**: RMS=0.0088, 频谱重心=1067Hz, 场景提示=quiet_indoor

### 样本 801: tram-milan-1058-42871-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Silence(0.119), Cupboard open or close(0.115)
- **音频特征**: RMS=0.0033, 频谱重心=1371Hz, 场景提示=quiet_indoor

### 样本 802: tram-barcelona-180-5580-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.361), Music(0.168)
- **音频特征**: RMS=0.0108, 频谱重心=797Hz, 场景提示=mixed_environment

### 样本 803: airport-prague-1069-44057-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.756)
- **音频特征**: RMS=0.0022, 频谱重心=1451Hz, 场景提示=quiet_indoor

### 样本 804: park-helsinki-92-2539-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.600), Animal(0.198), Bird(0.197)
- **音频特征**: RMS=0.0012, 频谱重心=1362Hz, 场景提示=quiet_indoor

### 样本 805: airport-lisbon-1114-40796-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.773), Clip-clop(0.190), Horse(0.139)
- **音频特征**: RMS=0.0056, 频谱重心=1271Hz, 场景提示=quiet_indoor

### 样本 806: metro_station-london-74-2079-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Train(0.776), Railroad car, train wagon(0.660), Rail transport(0.656)
- **音频特征**: RMS=0.0241, 频谱重心=1172Hz, 场景提示=mixed_environment

### 样本 807: metro_station-london-69-2027-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.767), Music(0.149)
- **音频特征**: RMS=0.0026, 频谱重心=1542Hz, 场景提示=mixed_environment

### 样本 808: tram-barcelona-179-5550-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.613), Rail transport(0.423), Railroad car, train wagon(0.384)
- **音频特征**: RMS=0.0091, 频谱重心=568Hz, 场景提示=quiet_indoor

### 样本 809: tram-milan-1182-45217-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.469), Vehicle(0.241), Music(0.229)
- **音频特征**: RMS=0.0179, 频谱重心=666Hz, 场景提示=mixed_environment

### 样本 810: metro-milan-1218-44353-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.643), Music(0.497), Vehicle(0.132)
- **音频特征**: RMS=0.0448, 频谱重心=546Hz, 场景提示=mixed_environment

### 样本 811: airport-milan-1172-45327-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.717), Vehicle(0.253)
- **音频特征**: RMS=0.0034, 频谱重心=1475Hz, 场景提示=mixed_environment

### 样本 812: street_pedestrian-lisbon-1099-43338-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.881), Clip-clop(0.164), Animal(0.160)
- **音频特征**: RMS=0.0038, 频谱重心=1335Hz, 场景提示=mixed_environment

### 样本 813: tram-stockholm-198-5967-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.827), Vehicle(0.732), Car(0.415)
- **音频特征**: RMS=0.0736, 频谱重心=280Hz, 场景提示=mixed_environment

### 样本 814: street_pedestrian-lisbon-1098-43801-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.767), Music(0.124)
- **音频特征**: RMS=0.0029, 频谱重心=1380Hz, 场景提示=quiet_indoor

### 样本 815: airport-paris-206-6244-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.353), Animal(0.151), Vehicle(0.112)
- **音频特征**: RMS=0.0069, 频谱重心=1121Hz, 场景提示=quiet_indoor

### 样本 816: street_pedestrian-stockholm-266-8084-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.738)
- **音频特征**: RMS=0.0043, 频谱重心=1106Hz, 场景提示=quiet_indoor

### 样本 817: metro-barcelona-42-1308-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.183), Mouse(0.182)
- **音频特征**: RMS=0.0073, 频谱重心=999Hz, 场景提示=quiet_indoor

### 样本 818: street_pedestrian-barcelona-144-4368-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.788), Animal(0.168), Clip-clop(0.145)
- **音频特征**: RMS=0.0020, 频谱重心=1343Hz, 场景提示=quiet_indoor

### 样本 819: bus-milan-1078-43270-a.wav
- **真实场景**: bus
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.650), Speech(0.577), Train(0.277)
- **音频特征**: RMS=0.0167, 频谱重心=1087Hz, 场景提示=mixed_environment

### 样本 820: street_pedestrian-stockholm-155-4697-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.762), Clip-clop(0.218), Horse(0.157)
- **音频特征**: RMS=0.0043, 频谱重心=1029Hz, 场景提示=quiet_indoor

### 样本 821: metro-helsinki-222-6717-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.428), Music(0.305), Vehicle(0.218)
- **音频特征**: RMS=0.0120, 频谱重心=805Hz, 场景提示=mixed_environment

### 样本 822: airport-milan-1172-44687-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.750), Bird(0.108), Outside, urban or manmade(0.107)
- **音频特征**: RMS=0.0030, 频谱重心=1519Hz, 场景提示=mixed_environment

### 样本 823: airport-helsinki-3-147-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.581)
- **音频特征**: RMS=0.0018, 频谱重心=1423Hz, 场景提示=quiet_indoor

### 样本 824: public_square-lyon-1056-41462-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.539), Outside, urban or manmade(0.112)
- **音频特征**: RMS=0.0025, 频谱重心=1112Hz, 场景提示=quiet_indoor

### 样本 825: street_pedestrian-lyon-1047-40853-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.853), Clip-clop(0.199), Run(0.170)
- **音频特征**: RMS=0.0024, 频谱重心=1392Hz, 场景提示=quiet_indoor

### 样本 826: street_pedestrian-london-149-4512-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.784), Run(0.173)
- **音频特征**: RMS=0.0022, 频谱重心=959Hz, 场景提示=quiet_indoor

### 样本 827: street_pedestrian-lyon-1047-44078-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.647), Clip-clop(0.275), Animal(0.246)
- **音频特征**: RMS=0.0018, 频谱重心=1275Hz, 场景提示=quiet_indoor

### 样本 828: metro-prague-1022-40890-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.411), Train(0.251), Vehicle(0.251)
- **音频特征**: RMS=0.0213, 频谱重心=655Hz, 场景提示=mixed_environment

### 样本 829: metro_station-prague-1118-43240-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Mouse(0.100)
- **音频特征**: RMS=0.0030, 频谱重心=1264Hz, 场景提示=quiet_indoor

### 样本 830: airport-lyon-1041-43521-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.672), Animal(0.160), Clip-clop(0.122)
- **音频特征**: RMS=0.0021, 频谱重心=972Hz, 场景提示=quiet_indoor

### 样本 831: metro_station-lyon-1179-45709-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.831), Music(0.149)
- **音频特征**: RMS=0.0031, 频谱重心=1295Hz, 场景提示=mixed_environment

### 样本 832: bus-prague-1102-41226-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.620), Vehicle(0.466), Train(0.190)
- **音频特征**: RMS=0.0347, 频谱重心=987Hz, 场景提示=mixed_environment

### 样本 833: park-barcelona-91-2518-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.747), Animal(0.312), Vehicle(0.151)
- **音频特征**: RMS=0.0020, 频谱重心=1270Hz, 场景提示=quiet_indoor

### 样本 834: bus-vienna-219-6595-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.167), Music(0.108)
- **音频特征**: RMS=0.0074, 频谱重心=484Hz, 场景提示=quiet_indoor

### 样本 835: airport-milan-1061-42883-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.641), Bicycle(0.196), Animal(0.170)
- **音频特征**: RMS=0.0023, 频谱重心=1872Hz, 场景提示=mixed_environment

### 样本 836: airport-helsinki-3-138-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.708), Animal(0.106)
- **音频特征**: RMS=0.0014, 频谱重心=1337Hz, 场景提示=quiet_indoor

### 样本 837: metro-barcelona-42-1279-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.654), Vehicle(0.337), Mouse(0.166)
- **音频特征**: RMS=0.0124, 频谱重心=862Hz, 场景提示=mixed_environment

### 样本 838: metro_station-barcelona-63-1881-a.wav
- **真实场景**: metro_station
- **AE预测**: bus
- **AS预测**: metro_station
- **检测到的事件**: Music(0.184), Vehicle(0.115)
- **音频特征**: RMS=0.0224, 频谱重心=903Hz, 场景提示=mixed_environment

### 样本 839: tram-barcelona-180-5568-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.736), Vehicle(0.306), Sliding door(0.292)
- **音频特征**: RMS=0.0060, 频谱重心=984Hz, 场景提示=quiet_indoor

### 样本 840: airport-barcelona-1-20-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.822), Clip-clop(0.413), Horse(0.314)
- **音频特征**: RMS=0.0034, 频谱重心=1168Hz, 场景提示=quiet_indoor

### 样本 841: street_pedestrian-milan-1005-43399-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.789), Clip-clop(0.157), Horse(0.122)
- **音频特征**: RMS=0.0023, 频谱重心=1194Hz, 场景提示=quiet_indoor

### 样本 842: tram-vienna-200-6028-a.wav
- **真实场景**: tram
- **AE预测**: park
- **AS预测**: tram
- **检测到的事件**: Tick(0.210), Tick-tock(0.203)
- **音频特征**: RMS=0.0067, 频谱重心=675Hz, 场景提示=quiet_indoor

### 样本 843: metro_station-barcelona-62-1854-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.124), White noise(0.102)
- **音频特征**: RMS=0.0076, 频谱重心=985Hz, 场景提示=quiet_indoor

### 样本 844: airport-helsinki-204-6144-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.332)
- **音频特征**: RMS=0.0022, 频谱重心=1316Hz, 场景提示=quiet_indoor

### 样本 845: street_pedestrian-stockholm-266-8099-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: airport
- **检测到的事件**: Speech(0.561), Vehicle(0.270)
- **音频特征**: RMS=0.0065, 频谱重心=1658Hz, 场景提示=mixed_environment

### 样本 846: street_pedestrian-barcelona-142-4322-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.845), Chatter(0.432), Music(0.216)
- **音频特征**: RMS=0.0025, 频谱重心=1610Hz, 场景提示=mixed_environment

### 样本 847: metro-vienna-59-1767-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.226)
- **音频特征**: RMS=0.0064, 频谱重心=561Hz, 场景提示=quiet_indoor

### 样本 848: shopping_mall-prague-1053-40771-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.254), Vehicle(0.123)
- **音频特征**: RMS=0.0037, 频谱重心=1306Hz, 场景提示=quiet_indoor

### 样本 849: airport-helsinki-3-145-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.502), Animal(0.118)
- **音频特征**: RMS=0.0016, 频谱重心=1398Hz, 场景提示=quiet_indoor

### 样本 850: street_pedestrian-milan-1096-43064-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.754), Animal(0.105), Vehicle(0.104)
- **音频特征**: RMS=0.0032, 频谱重心=1390Hz, 场景提示=mixed_environment

### 样本 851: metro-prague-1016-42430-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.796), Meow(0.361), Cat(0.337)
- **音频特征**: RMS=0.0147, 频谱重心=842Hz, 场景提示=mixed_environment

### 样本 852: street_pedestrian-lyon-1072-40261-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.753), Clip-clop(0.148), Animal(0.138)
- **音频特征**: RMS=0.0017, 频谱重心=1734Hz, 场景提示=mixed_environment

### 样本 853: public_square-milan-1168-44573-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.467), Animal(0.177)
- **音频特征**: RMS=0.0031, 频谱重心=2210Hz, 场景提示=mixed_environment

### 样本 854: public_square-prague-1027-42279-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.672), Vehicle(0.138), Boat, Water vehicle(0.113)
- **音频特征**: RMS=0.0068, 频谱重心=1233Hz, 场景提示=quiet_indoor

### 样本 855: street_pedestrian-paris-264-8030-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.664), Clip-clop(0.289), Horse(0.270)
- **音频特征**: RMS=0.0027, 频谱重心=1362Hz, 场景提示=quiet_indoor

### 样本 856: street_pedestrian-stockholm-155-4683-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.685), Animal(0.269), Run(0.262)
- **音频特征**: RMS=0.0055, 频谱重心=1003Hz, 场景提示=quiet_indoor

### 样本 857: airport-helsinki-3-165-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.560), Vehicle(0.102)
- **音频特征**: RMS=0.0020, 频谱重心=1302Hz, 场景提示=quiet_indoor

### 样本 858: tram-london-278-8453-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.329), Vehicle(0.264), Train(0.185)
- **音频特征**: RMS=0.0126, 频谱重心=693Hz, 场景提示=mixed_environment

### 样本 859: airport-paris-9-412-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.568), Animal(0.101)
- **音频特征**: RMS=0.0022, 频谱重心=1329Hz, 场景提示=mixed_environment

### 样本 860: metro_station-prague-1019-41604-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.788)
- **音频特征**: RMS=0.0022, 频谱重心=1162Hz, 场景提示=quiet_indoor

### 样本 861: shopping_mall-lisbon-1002-42418-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.721)
- **音频特征**: RMS=0.0024, 频谱重心=1119Hz, 场景提示=quiet_indoor

### 样本 862: metro-stockholm-57-1683-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.371), Animal(0.124)
- **音频特征**: RMS=0.0135, 频谱重心=689Hz, 场景提示=mixed_environment

### 样本 863: bus-helsinki-211-6439-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.573), Car(0.228), Rumble(0.131)
- **音频特征**: RMS=0.0300, 频谱重心=419Hz, 场景提示=mixed_environment

### 样本 864: street_pedestrian-stockholm-156-4721-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.793), Vehicle(0.208), Animal(0.133)
- **音频特征**: RMS=0.0126, 频谱重心=835Hz, 场景提示=mixed_environment

### 样本 865: shopping_mall-lisbon-1176-45140-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.591), Silence(0.143)
- **音频特征**: RMS=0.0019, 频谱重心=1515Hz, 场景提示=quiet_indoor

### 样本 866: street_pedestrian-vienna-267-8112-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.373), Vehicle(0.223), Patter(0.121)
- **音频特征**: RMS=0.0035, 频谱重心=966Hz, 场景提示=quiet_indoor

### 样本 867: tram-lyon-1216-45629-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.716), Vehicle(0.290)
- **音频特征**: RMS=0.0141, 频谱重心=550Hz, 场景提示=mixed_environment

### 样本 868: tram-paris-193-5870-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Power windows, electric windows(0.158), Sliding door(0.135), Vehicle(0.132)
- **音频特征**: RMS=0.0096, 频谱重心=987Hz, 场景提示=quiet_indoor

### 样本 869: public_square-milan-1014-41882-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.572), Vehicle(0.137), Animal(0.109)
- **音频特征**: RMS=0.0039, 频谱重心=1174Hz, 场景提示=quiet_indoor

### 样本 870: public_square-prague-1152-42311-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.773), Vehicle(0.257), Outside, urban or manmade(0.143)
- **音频特征**: RMS=0.0023, 频谱重心=1388Hz, 场景提示=mixed_environment

### 样本 871: public_square-paris-117-3431-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.296), Animal(0.207), Vehicle(0.118)
- **音频特征**: RMS=0.0034, 频谱重心=948Hz, 场景提示=quiet_indoor

### 样本 872: bus-paris-31-987-a.wav
- **真实场景**: bus
- **AE预测**: metro_station
- **AS预测**: bus
- **检测到的事件**: Speech(0.642), Vehicle(0.431)
- **音频特征**: RMS=0.0099, 频谱重心=1046Hz, 场景提示=quiet_indoor

### 样本 873: street_pedestrian-stockholm-157-4776-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.599), Animal(0.168)
- **音频特征**: RMS=0.0041, 频谱重心=1354Hz, 场景提示=quiet_indoor

### 样本 874: shopping_mall-prague-1031-41856-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.444)
- **音频特征**: RMS=0.0114, 频谱重心=997Hz, 场景提示=mixed_environment

### 样本 875: airport-london-5-232-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.781), Vehicle(0.133), Clip-clop(0.130)
- **音频特征**: RMS=0.0014, 频谱重心=1626Hz, 场景提示=mixed_environment

### 样本 876: metro-barcelona-220-6680-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.819), Vehicle(0.665), Car(0.218)
- **音频特征**: RMS=0.0294, 频谱重心=671Hz, 场景提示=mixed_environment

### 样本 877: shopping_mall-stockholm-136-4133-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.231)
- **音频特征**: RMS=0.0030, 频谱重心=949Hz, 场景提示=quiet_indoor

### 样本 878: public_square-paris-117-3415-a.wav
- **真实场景**: public_square
- **AE预测**: street_traffic
- **AS预测**: park
- **检测到的事件**: Vehicle(0.362)
- **音频特征**: RMS=0.0062, 频谱重心=1020Hz, 场景提示=quiet_indoor

### 样本 879: street_pedestrian-milan-1080-43264-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.433), Rain(0.140), Rain on surface(0.134)
- **音频特征**: RMS=0.0025, 频谱重心=2124Hz, 场景提示=mixed_environment

### 样本 880: park-helsinki-242-7204-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Animal(0.628), Speech(0.602), Horse(0.540)
- **音频特征**: RMS=0.0024, 频谱重心=863Hz, 场景提示=quiet_indoor

### 样本 881: street_pedestrian-london-151-4582-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **音频特征**: RMS=0.0011, 频谱重心=1181Hz, 场景提示=quiet_indoor

### 样本 882: shopping_mall-lisbon-1176-44890-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.718)
- **音频特征**: RMS=0.0023, 频谱重心=1737Hz, 场景提示=mixed_environment

### 样本 883: tram-barcelona-180-5567-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.618), Music(0.178), Vehicle(0.105)
- **音频特征**: RMS=0.0067, 频谱重心=601Hz, 场景提示=quiet_indoor

### 样本 884: street_pedestrian-stockholm-266-8098-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Music(0.375), Speech(0.285)
- **音频特征**: RMS=0.0040, 频谱重心=993Hz, 场景提示=quiet_indoor

### 样本 885: street_pedestrian-milan-1080-43313-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Boat, Water vehicle(0.230), Vehicle(0.197)
- **音频特征**: RMS=0.0016, 频谱重心=2414Hz, 场景提示=mixed_environment

### 样本 886: street_pedestrian-vienna-160-4895-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.633), Vehicle(0.196)
- **音频特征**: RMS=0.0020, 频谱重心=1408Hz, 场景提示=mixed_environment

### 样本 887: bus-prague-1030-44021-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.761), Vehicle(0.704), Car(0.204)
- **音频特征**: RMS=0.0489, 频谱重心=736Hz, 场景提示=mixed_environment

### 样本 888: metro_station-barcelona-61-1830-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.221), Train(0.186), Vehicle(0.157)
- **音频特征**: RMS=0.0054, 频谱重心=957Hz, 场景提示=quiet_indoor

### 样本 889: airport-london-205-6214-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.843), Outside, urban or manmade(0.122), Chatter(0.115)
- **音频特征**: RMS=0.0015, 频谱重心=1608Hz, 场景提示=mixed_environment

### 样本 890: bus-paris-29-961-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.667)
- **音频特征**: RMS=0.0047, 频谱重心=1076Hz, 场景提示=quiet_indoor

### 样本 891: airport-lisbon-1114-42707-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.681)
- **音频特征**: RMS=0.0068, 频谱重心=1218Hz, 场景提示=quiet_indoor

### 样本 892: street_pedestrian-stockholm-156-4718-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.513), Animal(0.319), Bow-wow(0.214)
- **音频特征**: RMS=0.0112, 频谱重心=1474Hz, 场景提示=mixed_environment

### 样本 893: metro-barcelona-42-1304-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.228)
- **音频特征**: RMS=0.0099, 频谱重心=763Hz, 场景提示=quiet_indoor

### 样本 894: metro_station-lyon-1028-42480-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Music(0.420), Train(0.325), Rail transport(0.186)
- **音频特征**: RMS=0.0047, 频谱重心=1358Hz, 场景提示=mixed_environment

### 样本 895: street_pedestrian-helsinki-147-4440-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: metro_station
- **AS预测**: public_square
- **检测到的事件**: Music(0.246), Vehicle(0.116)
- **音频特征**: RMS=0.0043, 频谱重心=993Hz, 场景提示=quiet_indoor

### 样本 896: street_pedestrian-milan-1080-40936-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Rain(0.268), Rain on surface(0.217), Raindrop(0.164)
- **音频特征**: RMS=0.0021, 频谱重心=2157Hz, 场景提示=mixed_environment

### 样本 897: bus-milan-1115-42999-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.577), Vehicle(0.268)
- **音频特征**: RMS=0.0200, 频谱重心=949Hz, 场景提示=mixed_environment

### 样本 898: shopping_mall-prague-1031-41010-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Vehicle(0.133), Music(0.113)
- **音频特征**: RMS=0.0049, 频谱重心=697Hz, 场景提示=quiet_indoor

### 样本 899: street_pedestrian-helsinki-148-4469-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: park
- **AS预测**: street_pedestrian
- **检测到的事件**: Silence(0.195)
- **音频特征**: RMS=0.0021, 频谱重心=752Hz, 场景提示=quiet_indoor

### 样本 900: tram-stockholm-199-6001-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.683), Vehicle(0.587), Car(0.202)
- **音频特征**: RMS=0.0241, 频谱重心=428Hz, 场景提示=mixed_environment

### 样本 901: metro_station-london-73-2069-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.188)
- **音频特征**: RMS=0.0234, 频谱重心=1194Hz, 场景提示=mixed_environment

### 样本 902: bus-milan-1190-44209-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.656), Vehicle(0.395), Bird(0.138)
- **音频特征**: RMS=0.0126, 频谱重心=815Hz, 场景提示=mixed_environment

### 样本 903: tram-paris-191-5848-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.752), Music(0.656), Vehicle(0.146)
- **音频特征**: RMS=0.0094, 频谱重心=623Hz, 场景提示=quiet_indoor

### 样本 904: metro_station-lyon-1179-45570-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.742), Music(0.289), Chicken, rooster(0.130)
- **音频特征**: RMS=0.0049, 频谱重心=1502Hz, 场景提示=mixed_environment

### 样本 905: tram-milan-1182-45488-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.290), Bus(0.141), Rodents, rats, mice(0.125)
- **音频特征**: RMS=0.0239, 频谱重心=1110Hz, 场景提示=mixed_environment

### 样本 906: shopping_mall-vienna-138-4181-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.784), Animal(0.201)
- **音频特征**: RMS=0.0032, 频谱重心=1510Hz, 场景提示=mixed_environment

### 样本 907: metro_station-stockholm-83-2235-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.495), Vehicle(0.409), Train(0.349)
- **音频特征**: RMS=0.0103, 频谱重心=1042Hz, 场景提示=mixed_environment

### 样本 908: metro-vienna-228-6877-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.718), Door(0.318), Sliding door(0.290)
- **音频特征**: RMS=0.0079, 频谱重心=915Hz, 场景提示=quiet_indoor

### 样本 909: shopping_mall-barcelona-127-3806-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.486), Animal(0.339), Horse(0.241)
- **音频特征**: RMS=0.0023, 频谱重心=1487Hz, 场景提示=mixed_environment

### 样本 910: airport-barcelona-1-70-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.880), Outside, urban or manmade(0.191), Vehicle(0.179)
- **音频特征**: RMS=0.0042, 频谱重心=1229Hz, 场景提示=quiet_indoor

### 样本 911: tram-milan-1158-41382-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.773), Vehicle(0.355)
- **音频特征**: RMS=0.0085, 频谱重心=1008Hz, 场景提示=quiet_indoor

### 样本 912: street_pedestrian-prague-1203-45623-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.250), Animal(0.162), Horse(0.111)
- **音频特征**: RMS=0.0014, 频谱重心=1222Hz, 场景提示=quiet_indoor

### 样本 913: public_square-lyon-1017-41596-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **音频特征**: RMS=0.0037, 频谱重心=1320Hz, 场景提示=quiet_indoor

### 样本 914: airport-barcelona-1-48-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.870), Run(0.367), Outside, urban or manmade(0.255)
- **音频特征**: RMS=0.0057, 频谱重心=1006Hz, 场景提示=quiet_indoor

### 样本 915: public_square-lyon-1017-40367-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.645), Vehicle(0.232)
- **音频特征**: RMS=0.0049, 频谱重心=1182Hz, 场景提示=quiet_indoor

### 样本 916: street_pedestrian-helsinki-146-4392-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.689), Music(0.561), Vehicle(0.185)
- **音频特征**: RMS=0.0041, 频谱重心=1146Hz, 场景提示=quiet_indoor

### 样本 917: shopping_mall-milan-1084-40312-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.816), Clip-clop(0.231), Horse(0.180)
- **音频特征**: RMS=0.0025, 频谱重心=1570Hz, 场景提示=mixed_environment

### 样本 918: bus-london-22-844-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.653), Music(0.188), Vehicle(0.136)
- **音频特征**: RMS=0.0137, 频谱重心=922Hz, 场景提示=mixed_environment

### 样本 919: metro_station-barcelona-62-1857-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.671)
- **音频特征**: RMS=0.0016, 频谱重心=1335Hz, 场景提示=quiet_indoor

### 样本 920: metro-barcelona-41-1240-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Cupboard open or close(0.178), Sliding door(0.175), Vehicle(0.119)
- **音频特征**: RMS=0.0060, 频谱重心=1313Hz, 场景提示=quiet_indoor

### 样本 921: shopping_mall-vienna-139-4213-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.323), Basketball bounce(0.107)
- **音频特征**: RMS=0.0032, 频谱重心=1332Hz, 场景提示=mixed_environment

### 样本 922: bus-milan-1190-45176-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.348), Speech(0.237), Train(0.189)
- **音频特征**: RMS=0.0139, 频谱重心=567Hz, 场景提示=mixed_environment

### 样本 923: airport-lisbon-1122-43307-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.877), Run(0.357), Outside, urban or manmade(0.262)
- **音频特征**: RMS=0.0044, 频谱重心=1462Hz, 场景提示=mixed_environment

### 样本 924: metro_station-helsinki-67-2009-a.wav
- **真实场景**: metro_station
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Music(0.286), Vehicle(0.183), Speech(0.152)
- **音频特征**: RMS=0.0028, 频谱重心=829Hz, 场景提示=quiet_indoor

### 样本 925: public_square-lyon-1056-43668-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.705), Chatter(0.135), Outside, urban or manmade(0.119)
- **音频特征**: RMS=0.0020, 频谱重心=1195Hz, 场景提示=quiet_indoor

### 样本 926: metro-barcelona-42-1287-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.654), Vehicle(0.291)
- **音频特征**: RMS=0.0107, 频谱重心=792Hz, 场景提示=mixed_environment

### 样本 927: metro_station-vienna-86-2353-a.wav
- **真实场景**: metro_station
- **AE预测**: tram
- **AS预测**: park
- **检测到的事件**: Speech(0.697), Vehicle(0.446), Field recording(0.154)
- **音频特征**: RMS=0.0120, 频谱重心=363Hz, 场景提示=mixed_environment

### 样本 928: park-prague-1185-44749-a.wav
- **真实场景**: park
- **AE预测**: street_traffic
- **AS预测**: park
- **检测到的事件**: Vehicle(0.171), Rain(0.157), Rain on surface(0.135)
- **音频特征**: RMS=0.0067, 频谱重心=1502Hz, 场景提示=quiet_indoor

### 样本 929: metro_station-barcelona-63-1892-a.wav
- **真实场景**: metro_station
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.325), White noise(0.155)
- **音频特征**: RMS=0.0381, 频谱重心=823Hz, 场景提示=mixed_environment

### 样本 930: metro-lyon-1149-42148-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.825), Vehicle(0.337), Door(0.100)
- **音频特征**: RMS=0.0076, 频谱重心=1034Hz, 场景提示=quiet_indoor

### 样本 931: street_traffic-stockholm-175-5383-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.360), Animal(0.214), Vehicle(0.210)
- **音频特征**: RMS=0.0198, 频谱重心=666Hz, 场景提示=mixed_environment

### 样本 932: tram-lisbon-1191-44557-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.743), Music(0.459), Vehicle(0.244)
- **音频特征**: RMS=0.0091, 频谱重心=1230Hz, 场景提示=quiet_indoor

### 样本 933: tram-london-278-8458-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.670), Music(0.339), Vehicle(0.163)
- **音频特征**: RMS=0.0097, 频谱重心=943Hz, 场景提示=quiet_indoor

### 样本 934: bus-prague-1032-41203-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.770), Vehicle(0.663), Car(0.251)
- **音频特征**: RMS=0.0407, 频谱重心=750Hz, 场景提示=mixed_environment

### 样本 935: metro-paris-52-1543-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.150)
- **音频特征**: RMS=0.0078, 频谱重心=1376Hz, 场景提示=quiet_indoor

### 样本 936: shopping_mall-london-131-3946-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.880), Chatter(0.267)
- **音频特征**: RMS=0.0034, 频谱重心=1739Hz, 场景提示=mixed_environment

### 样本 937: bus-lisbon-1123-40788-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.723), Vehicle(0.381)
- **音频特征**: RMS=0.0173, 频谱重心=800Hz, 场景提示=mixed_environment

### 样本 938: shopping_mall-barcelona-126-3763-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.839), Female speech, woman speaking(0.173), Narration, monologue(0.156)
- **音频特征**: RMS=0.0051, 频谱重心=1633Hz, 场景提示=mixed_environment

### 样本 939: airport-milan-1061-40507-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.718), Animal(0.275), Clip-clop(0.218)
- **音频特征**: RMS=0.0021, 频谱重心=1411Hz, 场景提示=mixed_environment

### 样本 940: street_pedestrian-vienna-158-4805-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.620), Animal(0.111)
- **音频特征**: RMS=0.0010, 频谱重心=1405Hz, 场景提示=quiet_indoor

### 样本 941: metro-stockholm-55-1608-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.448), Train(0.185)
- **音频特征**: RMS=0.0152, 频谱重心=508Hz, 场景提示=mixed_environment

### 样本 942: airport-milan-1089-40548-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.822), Clip-clop(0.363), Horse(0.341)
- **音频特征**: RMS=0.0028, 频谱重心=1582Hz, 场景提示=mixed_environment

### 样本 943: metro_station-london-70-2040-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.481)
- **音频特征**: RMS=0.0026, 频谱重心=807Hz, 场景提示=quiet_indoor

### 样本 944: street_pedestrian-prague-1051-42230-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.842), Animal(0.108), Outside, urban or manmade(0.102)
- **音频特征**: RMS=0.0045, 频谱重心=1169Hz, 场景提示=quiet_indoor

### 样本 945: bus-lisbon-1123-41222-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.732), Vehicle(0.418), Car(0.102)
- **音频特征**: RMS=0.0151, 频谱重心=831Hz, 场景提示=mixed_environment

### 样本 946: metro-london-223-6769-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.777), Vehicle(0.489), Music(0.417)
- **音频特征**: RMS=0.0170, 频谱重心=682Hz, 场景提示=mixed_environment

### 样本 947: bus-prague-1138-43184-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.591), Vehicle(0.237), Mouse(0.191)
- **音频特征**: RMS=0.0288, 频谱重心=691Hz, 场景提示=mixed_environment

### 样本 948: tram-lisbon-1046-43807-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.723), Speech(0.651), Train(0.287)
- **音频特征**: RMS=0.0868, 频谱重心=590Hz, 场景提示=mixed_environment

### 样本 949: bus-stockholm-36-1087-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.793), Vehicle(0.347)
- **音频特征**: RMS=0.0208, 频谱重心=639Hz, 场景提示=mixed_environment

### 样本 950: tram-london-279-8484-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Train(0.466), Rail transport(0.379), Railroad car, train wagon(0.342)
- **音频特征**: RMS=0.0111, 频谱重心=906Hz, 场景提示=mixed_environment

### 样本 951: airport-london-5-256-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.490), Music(0.158), Fowl(0.137)
- **音频特征**: RMS=0.0012, 频谱重心=1775Hz, 场景提示=mixed_environment

### 样本 952: bus-milan-1083-40287-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.751), Vehicle(0.479), Field recording(0.129)
- **音频特征**: RMS=0.0235, 频谱重心=715Hz, 场景提示=mixed_environment

### 样本 953: shopping_mall-london-131-3951-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.566)
- **音频特征**: RMS=0.0021, 频谱重心=1139Hz, 场景提示=quiet_indoor

### 样本 954: metro_station-vienna-88-2399-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.589), Field recording(0.222), Aircraft(0.134)
- **音频特征**: RMS=0.0252, 频谱重心=448Hz, 场景提示=mixed_environment

### 样本 955: bus-helsinki-211-6428-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.342), Car(0.113)
- **音频特征**: RMS=0.0117, 频谱重心=621Hz, 场景提示=mixed_environment

### 样本 956: metro_station-barcelona-63-1882-a.wav
- **真实场景**: metro_station
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: White noise(0.197), Vehicle(0.173)
- **音频特征**: RMS=0.0219, 频谱重心=1184Hz, 场景提示=mixed_environment

### 样本 957: airport-lisbon-1000-40242-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.803)
- **音频特征**: RMS=0.0046, 频谱重心=1390Hz, 场景提示=mixed_environment

### 样本 958: airport-prague-1069-41725-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.763), Vehicle(0.125)
- **音频特征**: RMS=0.0027, 频谱重心=1340Hz, 场景提示=quiet_indoor

### 样本 959: tram-london-185-5756-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Train(0.767), Vehicle(0.571), Railroad car, train wagon(0.563)
- **音频特征**: RMS=0.0137, 频谱重心=925Hz, 场景提示=mixed_environment

### 样本 960: bus-barcelona-210-6392-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.604), Vehicle(0.590), Rumble(0.262)
- **音频特征**: RMS=0.0499, 频谱重心=269Hz, 场景提示=mixed_environment

### 样本 961: street_pedestrian-barcelona-145-4369-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.876), Outside, urban or manmade(0.174), Run(0.112)
- **音频特征**: RMS=0.0035, 频谱重心=1514Hz, 场景提示=mixed_environment

### 样本 962: metro_station-vienna-86-2342-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Silence(0.262)
- **音频特征**: RMS=0.0012, 频谱重心=1232Hz, 场景提示=quiet_indoor

### 样本 963: shopping_mall-helsinki-255-7674-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.790), Clip-clop(0.202), Horse(0.132)
- **音频特征**: RMS=0.0047, 频谱重心=1413Hz, 场景提示=quiet_indoor

### 样本 964: tram-lyon-1150-41115-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.716), Music(0.382), Vehicle(0.165)
- **音频特征**: RMS=0.0070, 频谱重心=1295Hz, 场景提示=quiet_indoor

### 样本 965: public_square-milan-1074-42680-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.825), Animal(0.165), Outside, urban or manmade(0.145)
- **音频特征**: RMS=0.0031, 频谱重心=1214Hz, 场景提示=quiet_indoor

### 样本 966: airport-milan-1108-43755-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.805), Children playing(0.283), Child speech, kid speaking(0.148)
- **音频特征**: RMS=0.0023, 频谱重心=1711Hz, 场景提示=mixed_environment

### 样本 967: airport-helsinki-3-139-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.792), Animal(0.131)
- **音频特征**: RMS=0.0027, 频谱重心=1173Hz, 场景提示=quiet_indoor

### 样本 968: tram-paris-196-5916-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.777), Vehicle(0.318), Sliding door(0.166)
- **音频特征**: RMS=0.0061, 频谱重心=1225Hz, 场景提示=quiet_indoor

### 样本 969: metro_station-paris-237-7057-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.856), Children playing(0.292), Music(0.169)
- **音频特征**: RMS=0.0033, 频谱重心=1945Hz, 场景提示=mixed_environment

### 样本 970: public_square-stockholm-119-3518-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Speech(0.801), Clip-clop(0.238), Animal(0.185)
- **音频特征**: RMS=0.0046, 频谱重心=858Hz, 场景提示=quiet_indoor

### 样本 971: public_square-vienna-122-3622-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.565), Animal(0.246), Crow(0.160)
- **音频特征**: RMS=0.0012, 频谱重心=1120Hz, 场景提示=quiet_indoor

### 样本 972: street_pedestrian-lisbon-1098-41925-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.712), Horse(0.209), Animal(0.192)
- **音频特征**: RMS=0.0031, 频谱重心=1469Hz, 场景提示=mixed_environment

### 样本 973: metro_station-helsinki-66-1979-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.626), Vehicle(0.108)
- **音频特征**: RMS=0.0056, 频谱重心=1143Hz, 场景提示=quiet_indoor

### 样本 974: street_pedestrian-stockholm-156-4743-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.839), Vehicle(0.136), Outside, urban or manmade(0.117)
- **音频特征**: RMS=0.0132, 频谱重心=979Hz, 场景提示=mixed_environment

### 样本 975: street_traffic-helsinki-164-5010-a.wav
- **真实场景**: street_traffic
- **AE预测**: bus
- **AS预测**: street_traffic
- **检测到的事件**: Tick-tock(0.198), Tick(0.194), Vehicle(0.180)
- **音频特征**: RMS=0.0016, 频谱重心=1493Hz, 场景提示=quiet_indoor

### 样本 976: metro_station-lyon-1167-44748-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.862), Music(0.166), Clip-clop(0.143)
- **音频特征**: RMS=0.0044, 频谱重心=1022Hz, 场景提示=quiet_indoor

### 样本 977: street_pedestrian-barcelona-145-4374-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.747), Animal(0.108)
- **音频特征**: RMS=0.0028, 频谱重心=1546Hz, 场景提示=mixed_environment

### 样本 978: metro-paris-49-1511-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.467), Vehicle(0.252), Music(0.236)
- **音频特征**: RMS=0.0076, 频谱重心=1431Hz, 场景提示=quiet_indoor

### 样本 979: street_pedestrian-paris-153-4632-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.520), Animal(0.102)
- **音频特征**: RMS=0.0019, 频谱重心=875Hz, 场景提示=quiet_indoor

### 样本 980: street_pedestrian-lyon-1047-40533-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.541), Animal(0.179), Clip-clop(0.152)
- **音频特征**: RMS=0.0016, 频谱重心=1427Hz, 场景提示=mixed_environment

### 样本 981: bus-paris-30-974-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.416), Vehicle(0.129)
- **音频特征**: RMS=0.0075, 频谱重心=1111Hz, 场景提示=quiet_indoor

### 样本 982: bus-lisbon-1059-42410-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.489), Vehicle(0.196), Animal(0.165)
- **音频特征**: RMS=0.0249, 频谱重心=455Hz, 场景提示=mixed_environment

### 样本 983: shopping_mall-london-256-7698-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.652), Arrow(0.118)
- **音频特征**: RMS=0.0024, 频谱重心=1729Hz, 场景提示=mixed_environment

### 样本 984: metro_station-vienna-240-7138-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.652), Vehicle(0.265), Train(0.165)
- **音频特征**: RMS=0.0079, 频谱重心=821Hz, 场景提示=quiet_indoor

### 样本 985: public_square-prague-1111-43983-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.546), Vehicle(0.169)
- **音频特征**: RMS=0.0058, 频谱重心=1297Hz, 场景提示=quiet_indoor

### 样本 986: airport-vienna-13-527-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: airport
- **检测到的事件**: Speech(0.784), Clip-clop(0.114)
- **音频特征**: RMS=0.0014, 频谱重心=1367Hz, 场景提示=mixed_environment

### 样本 987: airport-helsinki-4-170-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **音频特征**: RMS=0.0022, 频谱重心=1561Hz, 场景提示=mixed_environment

### 样本 988: airport-paris-206-6276-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.573), Mouse(0.215)
- **音频特征**: RMS=0.0071, 频谱重心=1052Hz, 场景提示=quiet_indoor

### 样本 989: street_pedestrian-milan-1205-44377-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.761)
- **音频特征**: RMS=0.0016, 频谱重心=1390Hz, 场景提示=quiet_indoor

### 样本 990: park-milan-1133-42097-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Rain on surface(0.269), Rain(0.219), Raindrop(0.146)
- **音频特征**: RMS=0.0012, 频谱重心=2816Hz, 场景提示=mixed_environment

### 样本 991: airport-stockholm-207-6301-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.729), Animal(0.446), Goat(0.443)
- **音频特征**: RMS=0.0033, 频谱重心=1721Hz, 场景提示=mixed_environment

### 样本 992: metro-milan-1062-40086-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.392), Sliding door(0.260), Door(0.147)
- **音频特征**: RMS=0.0094, 频谱重心=919Hz, 场景提示=quiet_indoor

### 样本 993: tram-helsinki-276-8426-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.646), Vehicle(0.472), Boat, Water vehicle(0.140)
- **音频特征**: RMS=0.0226, 频谱重心=632Hz, 场景提示=mixed_environment

### 样本 994: street_pedestrian-helsinki-148-4486-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Clip-clop(0.162), Animal(0.146), Horse(0.137)
- **音频特征**: RMS=0.0012, 频谱重心=1260Hz, 场景提示=quiet_indoor

### 样本 995: metro_station-london-235-7016-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.197), Train(0.184), Railroad car, train wagon(0.111)
- **音频特征**: RMS=0.0066, 频谱重心=930Hz, 场景提示=quiet_indoor

### 样本 996: street_pedestrian-barcelona-260-7889-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.794), Music(0.152)
- **音频特征**: RMS=0.0023, 频谱重心=1555Hz, 场景提示=mixed_environment

### 样本 997: tram-lisbon-1100-40923-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.605), Car(0.180), Bus(0.111)
- **音频特征**: RMS=0.0109, 频谱重心=1158Hz, 场景提示=mixed_environment

### 样本 998: street_traffic-helsinki-166-5087-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: park
- **音频特征**: RMS=0.0029, 频谱重心=967Hz, 场景提示=quiet_indoor

### 样本 999: airport-barcelona-203-6137-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.891), Clip-clop(0.370), Horse(0.314)
- **音频特征**: RMS=0.0021, 频谱重心=1256Hz, 场景提示=quiet_indoor

### 样本 1000: street_pedestrian-milan-1005-41969-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.831), Outside, urban or manmade(0.134), Animal(0.128)
- **音频特征**: RMS=0.0027, 频谱重心=1646Hz, 场景提示=mixed_environment

### 样本 1001: public_square-prague-1075-42194-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.837), Vehicle(0.108), Clip-clop(0.105)
- **音频特征**: RMS=0.0023, 频谱重心=1083Hz, 场景提示=quiet_indoor

### 样本 1002: shopping_mall-stockholm-136-4124-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.638), Vehicle(0.153), Music(0.101)
- **音频特征**: RMS=0.0031, 频谱重心=1096Hz, 场景提示=quiet_indoor

### 样本 1003: metro_station-helsinki-67-1996-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **音频特征**: RMS=0.0009, 频谱重心=924Hz, 场景提示=quiet_indoor

### 样本 1004: tram-barcelona-180-5593-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.842), Vehicle(0.427), Car(0.107)
- **音频特征**: RMS=0.0146, 频谱重心=868Hz, 场景提示=mixed_environment

### 样本 1005: shopping_mall-london-256-7776-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.862), Clip-clop(0.233), Horse(0.181)
- **音频特征**: RMS=0.0036, 频谱重心=1445Hz, 场景提示=mixed_environment

### 样本 1006: metro_station-barcelona-230-6929-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.785), Vehicle(0.118)
- **音频特征**: RMS=0.0077, 频谱重心=1358Hz, 场景提示=mixed_environment

### 样本 1007: tram-lisbon-1035-42208-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Microwave oven(0.237), Vehicle(0.151)
- **音频特征**: RMS=0.0150, 频谱重心=808Hz, 场景提示=mixed_environment

### 样本 1008: metro_station-lyon-1179-44778-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.719), Vehicle(0.120)
- **音频特征**: RMS=0.0048, 频谱重心=1542Hz, 场景提示=mixed_environment

### 样本 1009: shopping_mall-helsinki-255-7659-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.681), Music(0.306)
- **音频特征**: RMS=0.0037, 频谱重心=1228Hz, 场景提示=quiet_indoor

### 样本 1010: metro_station-lisbon-1221-44789-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Speech(0.613), Vehicle(0.349), Train(0.278)
- **音频特征**: RMS=0.0156, 频谱重心=1118Hz, 场景提示=mixed_environment

### 样本 1011: metro_station-milan-1127-41928-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.745), Vehicle(0.206), Animal(0.120)
- **音频特征**: RMS=0.0134, 频谱重心=1532Hz, 场景提示=mixed_environment

### 样本 1012: airport-london-6-257-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Speech(0.719), Vehicle(0.183), Clip-clop(0.173)
- **音频特征**: RMS=0.0021, 频谱重心=1162Hz, 场景提示=quiet_indoor

### 样本 1013: bus-helsinki-211-6447-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.737), Car(0.472), Field recording(0.201)
- **音频特征**: RMS=0.0328, 频谱重心=608Hz, 场景提示=mixed_environment

### 样本 1014: street_pedestrian-paris-264-8032-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **音频特征**: RMS=0.0028, 频谱重心=1206Hz, 场景提示=quiet_indoor

### 样本 1015: bus-london-22-833-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.681), Vehicle(0.169), Sliding door(0.169)
- **音频特征**: RMS=0.0102, 频谱重心=1130Hz, 场景提示=mixed_environment

### 样本 1016: metro_station-lyon-1167-45555-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.800), Music(0.182)
- **音频特征**: RMS=0.0050, 频谱重心=1563Hz, 场景提示=quiet_indoor

### 样本 1017: airport-stockholm-12-508-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.594), Clip-clop(0.433), Horse(0.319)
- **音频特征**: RMS=0.0028, 频谱重心=1008Hz, 场景提示=quiet_indoor

### 样本 1018: tram-helsinki-184-5732-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Bird(0.146), Mouse(0.142), Rodents, rats, mice(0.105)
- **音频特征**: RMS=0.0039, 频谱重心=1544Hz, 场景提示=quiet_indoor

### 样本 1019: airport-stockholm-11-464-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.855), Clip-clop(0.260), Animal(0.192)
- **音频特征**: RMS=0.0048, 频谱重心=1052Hz, 场景提示=quiet_indoor

### 样本 1020: metro-paris-53-1567-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.759)
- **音频特征**: RMS=0.0069, 频谱重心=756Hz, 场景提示=quiet_indoor

### 样本 1021: airport-stockholm-12-500-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.837), Clip-clop(0.721), Horse(0.650)
- **音频特征**: RMS=0.0023, 频谱重心=1098Hz, 场景提示=quiet_indoor

### 样本 1022: street_pedestrian-paris-154-4670-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.532), Animal(0.125)
- **音频特征**: RMS=0.0014, 频谱重心=1665Hz, 场景提示=mixed_environment

### 样本 1023: airport-lisbon-1122-42956-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.753), Outside, urban or manmade(0.159), Run(0.140)
- **音频特征**: RMS=0.0049, 频谱重心=1364Hz, 场景提示=mixed_environment

### 样本 1024: metro_station-milan-1117-42729-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.717), Vehicle(0.171)
- **音频特征**: RMS=0.0070, 频谱重心=804Hz, 场景提示=quiet_indoor

### 样本 1025: metro_station-milan-1117-40964-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.688), Vehicle(0.237)
- **音频特征**: RMS=0.0071, 频谱重心=971Hz, 场景提示=quiet_indoor

### 样本 1026: airport-barcelona-1-82-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.860), Clip-clop(0.313), Horse(0.223)
- **音频特征**: RMS=0.0038, 频谱重心=1055Hz, 场景提示=quiet_indoor

### 样本 1027: metro-barcelona-42-1269-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.107), Speech(0.100)
- **音频特征**: RMS=0.0114, 频谱重心=823Hz, 场景提示=mixed_environment

### 样本 1028: bus-paris-29-954-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.624), Vehicle(0.162), Mouse(0.139)
- **音频特征**: RMS=0.0082, 频谱重心=888Hz, 场景提示=quiet_indoor

### 样本 1029: street_pedestrian-paris-264-8033-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.356)
- **音频特征**: RMS=0.0029, 频谱重心=1777Hz, 场景提示=quiet_indoor

### 样本 1030: street_pedestrian-london-151-4587-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Animal(0.174)
- **音频特征**: RMS=0.0024, 频谱重心=866Hz, 场景提示=quiet_indoor

### 样本 1031: public_square-london-115-3363-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.746)
- **音频特征**: RMS=0.0021, 频谱重心=1068Hz, 场景提示=quiet_indoor

### 样本 1032: airport-milan-1089-42955-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.713), Animal(0.261), Clip-clop(0.166)
- **音频特征**: RMS=0.0013, 频谱重心=1674Hz, 场景提示=mixed_environment

### 样本 1033: shopping_mall-lisbon-1137-40472-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.657), Clip-clop(0.129), Animal(0.125)
- **音频特征**: RMS=0.0017, 频谱重心=1493Hz, 场景提示=mixed_environment

### 样本 1034: public_square-lyon-1208-45446-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.154), Silence(0.117)
- **音频特征**: RMS=0.0055, 频谱重心=1381Hz, 场景提示=quiet_indoor

### 样本 1035: tram-london-278-8455-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.736), Vehicle(0.563), Bus(0.146)
- **音频特征**: RMS=0.0172, 频谱重心=668Hz, 场景提示=mixed_environment

### 样本 1036: tram-helsinki-183-5692-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.679), Vehicle(0.116)
- **音频特征**: RMS=0.0028, 频谱重心=1146Hz, 场景提示=quiet_indoor

### 样本 1037: shopping_mall-london-256-7717-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.782), Clip-clop(0.340), Horse(0.260)
- **音频特征**: RMS=0.0036, 频谱重心=1502Hz, 场景提示=mixed_environment

### 样本 1038: metro-vienna-58-1720-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.754), Music(0.542), Vehicle(0.506)
- **音频特征**: RMS=0.0154, 频谱重心=731Hz, 场景提示=mixed_environment

### 样本 1039: bus-milan-1180-45390-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.413), Ship(0.148), Boat, Water vehicle(0.144)
- **音频特征**: RMS=0.0402, 频谱重心=621Hz, 场景提示=mixed_environment

### 样本 1040: airport-stockholm-11-466-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.797), Animal(0.105)
- **音频特征**: RMS=0.0051, 频谱重心=1116Hz, 场景提示=quiet_indoor

### 样本 1041: metro-prague-1163-44734-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.613), Vehicle(0.499), Rail transport(0.376)
- **音频特征**: RMS=0.0366, 频谱重心=692Hz, 场景提示=mixed_environment

### 样本 1042: bus-vienna-40-1191-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.739), Animal(0.134), Buzzer(0.118)
- **音频特征**: RMS=0.0056, 频谱重心=1338Hz, 场景提示=quiet_indoor

### 样本 1043: street_pedestrian-vienna-158-4803-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.737), Clip-clop(0.216), Horse(0.191)
- **音频特征**: RMS=0.0014, 频谱重心=1359Hz, 场景提示=quiet_indoor

### 样本 1044: street_pedestrian-paris-265-8041-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.496), Animal(0.165), Music(0.131)
- **音频特征**: RMS=0.0014, 频谱重心=1660Hz, 场景提示=quiet_indoor

### 样本 1045: street_pedestrian-lyon-1162-44682-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.761), Animal(0.369), Clip-clop(0.329)
- **音频特征**: RMS=0.0014, 频谱重心=1388Hz, 场景提示=mixed_environment

### 样本 1046: metro-barcelona-42-1281-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.308), Train(0.208), Railroad car, train wagon(0.115)
- **音频特征**: RMS=0.0111, 频谱重心=892Hz, 场景提示=mixed_environment

### 样本 1047: airport-london-6-299-a.wav
- **真实场景**: airport
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.783), Narration, monologue(0.146), Male speech, man speaking(0.104)
- **音频特征**: RMS=0.0020, 频谱重心=1285Hz, 场景提示=quiet_indoor

### 样本 1048: tram-prague-1042-42454-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.778), Music(0.496), Ice cream truck, ice cream van(0.480)
- **音频特征**: RMS=0.0128, 频谱重心=634Hz, 场景提示=mixed_environment

### 样本 1049: bus-paris-215-6524-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.546), Train(0.400), Vehicle(0.399)
- **音频特征**: RMS=0.0160, 频谱重心=616Hz, 场景提示=mixed_environment

### 样本 1050: public_square-milan-1074-43009-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.776), Animal(0.161), Vehicle(0.153)
- **音频特征**: RMS=0.0050, 频谱重心=939Hz, 场景提示=quiet_indoor

### 样本 1051: airport-stockholm-10-432-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.723), Walk, footsteps(0.115), Animal(0.106)
- **音频特征**: RMS=0.0015, 频谱重心=1402Hz, 场景提示=quiet_indoor

### 样本 1052: street_pedestrian-milan-1005-41363-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.730), Clip-clop(0.444), Horse(0.357)
- **音频特征**: RMS=0.0032, 频谱重心=1045Hz, 场景提示=quiet_indoor

### 样本 1053: shopping_mall-london-131-3958-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Vehicle(0.146), Speech(0.137)
- **音频特征**: RMS=0.0021, 频谱重心=1420Hz, 场景提示=mixed_environment

### 样本 1054: airport-prague-1173-44397-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.780), Chatter(0.118)
- **音频特征**: RMS=0.0015, 频谱重心=1620Hz, 场景提示=mixed_environment

### 样本 1055: street_pedestrian-prague-1203-45268-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.741), Animal(0.138)
- **音频特征**: RMS=0.0022, 频谱重心=1202Hz, 场景提示=quiet_indoor

### 样本 1056: airport-paris-9-374-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.775)
- **音频特征**: RMS=0.0021, 频谱重心=1372Hz, 场景提示=mixed_environment

### 样本 1057: street_pedestrian-barcelona-142-4308-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.847), Hubbub, speech noise, speech babble(0.152), Chatter(0.143)
- **音频特征**: RMS=0.0037, 频谱重心=1458Hz, 场景提示=mixed_environment

### 样本 1058: shopping_mall-lyon-1066-41099-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.660)
- **音频特征**: RMS=0.0016, 频谱重心=1611Hz, 场景提示=mixed_environment

### 样本 1059: street_pedestrian-lyon-1047-43996-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.740), Vehicle(0.161), Animal(0.107)
- **音频特征**: RMS=0.0022, 频谱重心=1302Hz, 场景提示=quiet_indoor

### 样本 1060: street_pedestrian-paris-152-4614-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.134)
- **音频特征**: RMS=0.0014, 频谱重心=1443Hz, 场景提示=quiet_indoor

### 样本 1061: shopping_mall-london-256-7740-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Mouse(0.120), Speech(0.108)
- **音频特征**: RMS=0.0021, 频谱重心=1273Hz, 场景提示=quiet_indoor

### 样本 1062: metro_station-lisbon-1020-40275-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Horse(0.545), Neigh, whinny(0.521), Animal(0.332)
- **音频特征**: RMS=0.0086, 频谱重心=961Hz, 场景提示=quiet_indoor

### 样本 1063: public_square-vienna-123-3629-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.662), Animal(0.265), Clip-clop(0.195)
- **音频特征**: RMS=0.0016, 频谱重心=1373Hz, 场景提示=quiet_indoor

### 样本 1064: airport-helsinki-3-117-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Animal(0.233), Clip-clop(0.152), Horse(0.134)
- **音频特征**: RMS=0.0023, 频谱重心=1146Hz, 场景提示=quiet_indoor

### 样本 1065: airport-prague-1069-40919-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.863), Clip-clop(0.210), Horse(0.152)
- **音频特征**: RMS=0.0024, 频谱重心=1391Hz, 场景提示=quiet_indoor

### 样本 1066: public_square-prague-1152-41128-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.705), Vehicle(0.224)
- **音频特征**: RMS=0.0037, 频谱重心=1048Hz, 场景提示=quiet_indoor

### 样本 1067: metro-vienna-59-1761-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Sliding door(0.294), Door(0.182), Vehicle(0.154)
- **音频特征**: RMS=0.0041, 频谱重心=1026Hz, 场景提示=quiet_indoor

### 样本 1068: public_square-prague-1152-43002-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.776), Vehicle(0.314), Outside, urban or manmade(0.132)
- **音频特征**: RMS=0.0043, 频谱重心=1004Hz, 场景提示=quiet_indoor

### 样本 1069: airport-barcelona-1-83-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.673), Animal(0.391), Clip-clop(0.289)
- **音频特征**: RMS=0.0027, 频谱重心=1308Hz, 场景提示=quiet_indoor

### 样本 1070: street_pedestrian-london-151-4586-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.502), Silence(0.212)
- **音频特征**: RMS=0.0009, 频谱重心=1167Hz, 场景提示=quiet_indoor

### 样本 1071: metro_station-prague-1170-45125-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.562), Vehicle(0.157), Animal(0.135)
- **音频特征**: RMS=0.0034, 频谱重心=1004Hz, 场景提示=quiet_indoor

### 样本 1072: airport-paris-9-410-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.835), Music(0.246), Children playing(0.194)
- **音频特征**: RMS=0.0033, 频谱重心=1197Hz, 场景提示=quiet_indoor

### 样本 1073: shopping_mall-helsinki-130-3903-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.812), Music(0.101)
- **音频特征**: RMS=0.0028, 频谱重心=1443Hz, 场景提示=mixed_environment

### 样本 1074: park-helsinki-92-2573-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.705), Animal(0.332), Clip-clop(0.187)
- **音频特征**: RMS=0.0051, 频谱重心=617Hz, 场景提示=quiet_indoor

### 样本 1075: airport-milan-1172-45190-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.829), Clip-clop(0.511), Horse(0.407)
- **音频特征**: RMS=0.0030, 频谱重心=1634Hz, 场景提示=mixed_environment

### 样本 1076: shopping_mall-stockholm-137-4162-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.892), Chatter(0.139), Outside, urban or manmade(0.137)
- **音频特征**: RMS=0.0042, 频谱重心=1142Hz, 场景提示=quiet_indoor

### 样本 1077: street_pedestrian-stockholm-155-4699-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.760), Clip-clop(0.212), Animal(0.190)
- **音频特征**: RMS=0.0045, 频谱重心=1015Hz, 场景提示=quiet_indoor

### 样本 1078: airport-stockholm-11-458-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.690), Animal(0.535), Clip-clop(0.404)
- **音频特征**: RMS=0.0032, 频谱重心=1219Hz, 场景提示=quiet_indoor

### 样本 1079: street_pedestrian-barcelona-142-4315-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.837), Chatter(0.198), Outside, urban or manmade(0.104)
- **音频特征**: RMS=0.0024, 频谱重心=1661Hz, 场景提示=mixed_environment

### 样本 1080: street_pedestrian-helsinki-148-4483-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Silence(0.251)
- **音频特征**: RMS=0.0019, 频谱重心=813Hz, 场景提示=quiet_indoor

### 样本 1081: park-lyon-1144-43200-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.583), Silence(0.170)
- **音频特征**: RMS=0.0007, 频谱重心=1136Hz, 场景提示=quiet_indoor

### 样本 1082: tram-barcelona-180-5562-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Siren(0.449), Civil defense siren(0.279), Vehicle(0.172)
- **音频特征**: RMS=0.0132, 频谱重心=582Hz, 场景提示=mixed_environment

### 样本 1083: shopping_mall-paris-132-3969-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.762), Animal(0.156)
- **音频特征**: RMS=0.0036, 频谱重心=1442Hz, 场景提示=quiet_indoor

### 样本 1084: public_square-stockholm-121-3558-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.602), Animal(0.354), Clip-clop(0.207)
- **音频特征**: RMS=0.0064, 频谱重心=1028Hz, 场景提示=quiet_indoor

### 样本 1085: metro-london-47-1444-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Music(0.295), Speech(0.268), Vehicle(0.244)
- **音频特征**: RMS=0.0050, 频谱重心=986Hz, 场景提示=quiet_indoor

### 样本 1086: shopping_mall-london-256-7758-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.795), Animal(0.124), Clip-clop(0.106)
- **音频特征**: RMS=0.0030, 频谱重心=1462Hz, 场景提示=mixed_environment

### 样本 1087: metro-paris-224-6786-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.506), Train(0.399), Railroad car, train wagon(0.241)
- **音频特征**: RMS=0.0186, 频谱重心=790Hz, 场景提示=mixed_environment

### 样本 1088: street_traffic-vienna-274-8370-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.722), Bicycle(0.174), Vehicle(0.173)
- **音频特征**: RMS=0.0045, 频谱重心=1590Hz, 场景提示=quiet_indoor

### 样本 1089: shopping_mall-paris-134-4057-a.wav
- **真实场景**: shopping_mall
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.784), Clip-clop(0.501), Horse(0.432)
- **音频特征**: RMS=0.0017, 频谱重心=1350Hz, 场景提示=mixed_environment

### 样本 1090: metro_station-lyon-1167-45161-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.799), Vehicle(0.362), Train(0.102)
- **音频特征**: RMS=0.0078, 频谱重心=1424Hz, 场景提示=mixed_environment

### 样本 1091: street_pedestrian-prague-1227-45356-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.356), Music(0.287), Pigeon, dove(0.245)
- **音频特征**: RMS=0.0015, 频谱重心=1760Hz, 场景提示=mixed_environment

### 样本 1092: metro_station-helsinki-231-6952-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.831), Clip-clop(0.158), Animal(0.134)
- **音频特征**: RMS=0.0030, 频谱重心=1291Hz, 场景提示=quiet_indoor

### 样本 1093: tram-stockholm-284-8583-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.770), Vehicle(0.165)
- **音频特征**: RMS=0.0082, 频谱重心=1040Hz, 场景提示=quiet_indoor

### 样本 1094: street_pedestrian-lisbon-1099-40654-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.755), Music(0.258)
- **音频特征**: RMS=0.0033, 频谱重心=1088Hz, 场景提示=quiet_indoor

### 样本 1095: park-barcelona-91-2524-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.727), Vehicle(0.171), Animal(0.144)
- **音频特征**: RMS=0.0018, 频谱重心=1840Hz, 场景提示=mixed_environment

### 样本 1096: bus-helsinki-211-6456-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.174), Cupboard open or close(0.167)
- **音频特征**: RMS=0.0203, 频谱重心=810Hz, 场景提示=mixed_environment

### 样本 1097: tram-prague-1161-43974-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.660), Vehicle(0.560), Train(0.254)
- **音频特征**: RMS=0.0426, 频谱重心=469Hz, 场景提示=mixed_environment

### 样本 1098: metro-milan-1197-44802-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.765), Vehicle(0.234), Train(0.121)
- **音频特征**: RMS=0.0252, 频谱重心=662Hz, 场景提示=mixed_environment

### 样本 1099: street_pedestrian-barcelona-260-7887-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.790), Clip-clop(0.331), Music(0.252)
- **音频特征**: RMS=0.0019, 频谱重心=1689Hz, 场景提示=mixed_environment

### 样本 1100: street_pedestrian-milan-1096-43912-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.877), Clip-clop(0.375), Animal(0.318)
- **音频特征**: RMS=0.0032, 频谱重心=1353Hz, 场景提示=mixed_environment

### 样本 1101: shopping_mall-paris-134-4056-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Animal(0.527), Horse(0.465), Speech(0.413)
- **音频特征**: RMS=0.0017, 频谱重心=1228Hz, 场景提示=quiet_indoor

### 样本 1102: tram-lyon-1091-42255-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.826), Vehicle(0.436), Car(0.101)
- **音频特征**: RMS=0.0110, 频谱重心=701Hz, 场景提示=mixed_environment

### 样本 1103: street_pedestrian-milan-1080-42107-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.433), Chink, clink(0.166)
- **音频特征**: RMS=0.0023, 频谱重心=1329Hz, 场景提示=quiet_indoor

### 样本 1104: tram-helsinki-184-5717-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Animal(0.533), Domestic animals, pets(0.497), Dog(0.228)
- **音频特征**: RMS=0.0032, 频谱重心=1550Hz, 场景提示=quiet_indoor

### 样本 1105: tram-lyon-1225-45006-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.550), Vehicle(0.387)
- **音频特征**: RMS=0.0101, 频谱重心=933Hz, 场景提示=mixed_environment

### 样本 1106: bus-vienna-38-1129-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.580), Speech(0.197), Car(0.193)
- **音频特征**: RMS=0.0301, 频谱重心=334Hz, 场景提示=mixed_environment

### 样本 1107: metro_station-lyon-1179-44167-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Vehicle(0.146)
- **音频特征**: RMS=0.0034, 频谱重心=1206Hz, 场景提示=quiet_indoor

### 样本 1108: airport-milan-1061-41111-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.777), Clip-clop(0.222), Horse(0.172)
- **音频特征**: RMS=0.0018, 频谱重心=1294Hz, 场景提示=quiet_indoor

### 样本 1109: airport-milan-1061-42752-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.705), Clip-clop(0.295), Horse(0.264)
- **音频特征**: RMS=0.0016, 频谱重心=1571Hz, 场景提示=mixed_environment

### 样本 1110: metro_station-london-68-2014-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.780), Vehicle(0.116)
- **音频特征**: RMS=0.0026, 频谱重心=1184Hz, 场景提示=quiet_indoor

### 样本 1111: metro-paris-54-1581-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.729), Vehicle(0.366)
- **音频特征**: RMS=0.0209, 频谱重心=515Hz, 场景提示=mixed_environment

### 样本 1112: metro_station-lyon-1179-44683-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.804), Vehicle(0.155)
- **音频特征**: RMS=0.0064, 频谱重心=1620Hz, 场景提示=mixed_environment

### 样本 1113: metro-barcelona-42-1277-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.633), Music(0.597), Vehicle(0.286)
- **音频特征**: RMS=0.0142, 频谱重心=639Hz, 场景提示=mixed_environment

### 样本 1114: airport-lisbon-1000-43865-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.867), Animal(0.108)
- **音频特征**: RMS=0.0045, 频谱重心=1476Hz, 场景提示=mixed_environment

### 样本 1115: shopping_mall-stockholm-136-4109-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.247), Animal(0.103)
- **音频特征**: RMS=0.0046, 频谱重心=1058Hz, 场景提示=quiet_indoor

### 样本 1116: street_pedestrian-milan-1165-44151-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.663), Horse(0.505), Clip-clop(0.489)
- **音频特征**: RMS=0.0031, 频谱重心=1085Hz, 场景提示=quiet_indoor

### 样本 1117: metro-barcelona-42-1267-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.225), White noise(0.144)
- **音频特征**: RMS=0.0123, 频谱重心=727Hz, 场景提示=mixed_environment

### 样本 1118: airport-vienna-13-517-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Animal(0.206), Speech(0.128), Clip-clop(0.116)
- **音频特征**: RMS=0.0015, 频谱重心=1343Hz, 场景提示=quiet_indoor

### 样本 1119: metro_station-london-72-2061-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.799), Clip-clop(0.254), Horse(0.182)
- **音频特征**: RMS=0.0024, 频谱重心=1552Hz, 场景提示=mixed_environment

### 样本 1120: public_square-london-115-3343-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.849), Outside, urban or manmade(0.225), Run(0.206)
- **音频特征**: RMS=0.0021, 频谱重心=1058Hz, 场景提示=quiet_indoor

### 样本 1121: street_pedestrian-milan-1205-44767-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.686)
- **音频特征**: RMS=0.0015, 频谱重心=1220Hz, 场景提示=quiet_indoor

### 样本 1122: bus-lisbon-1123-40729-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.672), Vehicle(0.193)
- **音频特征**: RMS=0.0112, 频谱重心=1124Hz, 场景提示=mixed_environment

### 样本 1123: airport-stockholm-11-450-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.677), Animal(0.319), Horse(0.129)
- **音频特征**: RMS=0.0041, 频谱重心=1105Hz, 场景提示=quiet_indoor

### 样本 1124: tram-paris-195-5903-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.708), Vehicle(0.292)
- **音频特征**: RMS=0.0061, 频谱重心=1129Hz, 场景提示=quiet_indoor

### 样本 1125: tram-milan-1146-43572-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.530), Vehicle(0.469), Train(0.369)
- **音频特征**: RMS=0.0225, 频谱重心=578Hz, 场景提示=mixed_environment

### 样本 1126: street_pedestrian-lisbon-1098-40973-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.739), Vehicle(0.194), Animal(0.124)
- **音频特征**: RMS=0.0029, 频谱重心=986Hz, 场景提示=quiet_indoor

### 样本 1127: metro-paris-53-1559-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.754), Vehicle(0.173)
- **音频特征**: RMS=0.0114, 频谱重心=656Hz, 场景提示=mixed_environment

### 样本 1128: metro_station-stockholm-83-2234-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.832), Vehicle(0.358), Clip-clop(0.152)
- **音频特征**: RMS=0.0065, 频谱重心=1334Hz, 场景提示=mixed_environment

### 样本 1129: shopping_mall-lisbon-1176-44404-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.703)
- **音频特征**: RMS=0.0022, 频谱重心=1504Hz, 场景提示=quiet_indoor

### 样本 1130: metro_station-lyon-1167-44872-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.605), Vehicle(0.319)
- **音频特征**: RMS=0.0060, 频谱重心=921Hz, 场景提示=quiet_indoor

### 样本 1131: shopping_mall-barcelona-127-3798-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.286), Animal(0.121)
- **音频特征**: RMS=0.0023, 频谱重心=1446Hz, 场景提示=mixed_environment

### 样本 1132: metro-barcelona-41-1241-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.694), Railroad car, train wagon(0.548), Rail transport(0.535)
- **音频特征**: RMS=0.0205, 频谱重心=561Hz, 场景提示=mixed_environment

### 样本 1133: tram-helsinki-276-8403-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.440), Car(0.153)
- **音频特征**: RMS=0.0147, 频谱重心=691Hz, 场景提示=mixed_environment

### 样本 1134: metro-prague-1016-42469-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.739), Cat(0.633), Domestic animals, pets(0.608)
- **音频特征**: RMS=0.0128, 频谱重心=882Hz, 场景提示=mixed_environment

### 样本 1135: airport-london-5-242-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.752)
- **音频特征**: RMS=0.0014, 频谱重心=1734Hz, 场景提示=mixed_environment

### 样本 1136: tram-lisbon-1131-43459-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.770), Vehicle(0.641), Car(0.277)
- **音频特征**: RMS=0.0686, 频谱重心=613Hz, 场景提示=mixed_environment

### 样本 1137: metro-vienna-228-6878-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.758), Vehicle(0.267)
- **音频特征**: RMS=0.0040, 频谱重心=933Hz, 场景提示=quiet_indoor

### 样本 1138: airport-lisbon-1122-41037-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Speech(0.487), Vehicle(0.214)
- **音频特征**: RMS=0.0037, 频谱重心=1230Hz, 场景提示=mixed_environment

### 样本 1139: tram-stockholm-197-5943-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.735), Music(0.402), Vehicle(0.251)
- **音频特征**: RMS=0.0446, 频谱重心=385Hz, 场景提示=mixed_environment

### 样本 1140: airport-london-5-240-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.798), Clip-clop(0.358), Horse(0.323)
- **音频特征**: RMS=0.0016, 频谱重心=1552Hz, 场景提示=mixed_environment

### 样本 1141: metro-helsinki-221-6692-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.598), Vehicle(0.568), Train(0.238)
- **音频特征**: RMS=0.0540, 频谱重心=454Hz, 场景提示=mixed_environment

### 样本 1142: public_square-lyon-1017-41371-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.717), Vehicle(0.218), Animal(0.147)
- **音频特征**: RMS=0.0038, 频谱重心=1651Hz, 场景提示=quiet_indoor

### 样本 1143: public_square-lyon-1056-40903-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.737), Laughter(0.127), Chatter(0.116)
- **音频特征**: RMS=0.0024, 频谱重心=1486Hz, 场景提示=mixed_environment

### 样本 1144: metro-stockholm-57-1685-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.776), Vehicle(0.205), Animal(0.155)
- **音频特征**: RMS=0.0122, 频谱重心=559Hz, 场景提示=mixed_environment

### 样本 1145: street_pedestrian-lisbon-1098-40264-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.709)
- **音频特征**: RMS=0.0030, 频谱重心=1377Hz, 场景提示=quiet_indoor

### 样本 1146: tram-london-189-5817-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.751), Smoke detector, smoke alarm(0.171), Inside, small room(0.139)
- **音频特征**: RMS=0.0044, 频谱重心=1282Hz, 场景提示=quiet_indoor

### 样本 1147: bus-lisbon-1128-43660-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.751), Vehicle(0.589), Car(0.173)
- **音频特征**: RMS=0.0410, 频谱重心=528Hz, 场景提示=mixed_environment

### 样本 1148: tram-helsinki-276-8427-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.546), Vehicle(0.437), Car(0.113)
- **音频特征**: RMS=0.0185, 频谱重心=657Hz, 场景提示=mixed_environment

### 样本 1149: bus-milan-1180-44625-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.763), Vehicle(0.415), Music(0.124)
- **音频特征**: RMS=0.0123, 频谱重心=819Hz, 场景提示=mixed_environment

### 样本 1150: tram-stockholm-198-5962-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.827), Vehicle(0.459), Music(0.277)
- **音频特征**: RMS=0.0549, 频谱重心=422Hz, 场景提示=mixed_environment

### 样本 1151: airport-milan-1172-45028-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Neigh, whinny(0.845), Horse(0.780), Speech(0.732)
- **音频特征**: RMS=0.0032, 频谱重心=1480Hz, 场景提示=mixed_environment

### 样本 1152: shopping_mall-lisbon-1002-40391-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.794), Music(0.188), Vehicle(0.111)
- **音频特征**: RMS=0.0025, 频谱重心=1113Hz, 场景提示=quiet_indoor

### 样本 1153: public_square-lyon-1178-45608-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.877), Clip-clop(0.150), Outside, urban or manmade(0.138)
- **音频特征**: RMS=0.0023, 频谱重心=1218Hz, 场景提示=quiet_indoor

### 样本 1154: street_pedestrian-milan-1096-41141-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.772), Outside, urban or manmade(0.126), Animal(0.108)
- **音频特征**: RMS=0.0033, 频谱重心=1427Hz, 场景提示=mixed_environment

### 样本 1155: metro_station-stockholm-84-2258-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.783), Animal(0.101)
- **音频特征**: RMS=0.0038, 频谱重心=1252Hz, 场景提示=quiet_indoor

### 样本 1156: shopping_mall-paris-257-7779-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.809), Clip-clop(0.193), Animal(0.146)
- **音频特征**: RMS=0.0037, 频谱重心=1308Hz, 场景提示=mixed_environment

### 样本 1157: metro_station-barcelona-229-6916-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.600), Snort(0.126), Gasp(0.102)
- **音频特征**: RMS=0.0022, 频谱重心=1052Hz, 场景提示=quiet_indoor

### 样本 1158: metro_station-london-72-2062-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.793), Female speech, woman speaking(0.103)
- **音频特征**: RMS=0.0023, 频谱重心=1674Hz, 场景提示=mixed_environment

### 样本 1159: street_pedestrian-london-150-4535-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.741), Animal(0.283), Clip-clop(0.266)
- **音频特征**: RMS=0.0033, 频谱重心=1388Hz, 场景提示=quiet_indoor

### 样本 1160: metro-vienna-228-6884-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **音频特征**: RMS=0.0055, 频谱重心=765Hz, 场景提示=quiet_indoor

### 样本 1161: airport-milan-1089-42174-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.740), Music(0.151), Vehicle(0.147)
- **音频特征**: RMS=0.0024, 频谱重心=1627Hz, 场景提示=mixed_environment

### 样本 1162: tram-milan-1048-40817-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.602), Train(0.556), Railroad car, train wagon(0.416)
- **音频特征**: RMS=0.0134, 频谱重心=1207Hz, 场景提示=mixed_environment

### 样本 1163: street_pedestrian-helsinki-147-4429-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Animal(0.352), Quack(0.262), Duck(0.249)
- **音频特征**: RMS=0.0037, 频谱重心=702Hz, 场景提示=quiet_indoor

### 样本 1164: shopping_mall-lisbon-1002-40707-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Mouse(0.105)
- **音频特征**: RMS=0.0022, 频谱重心=1209Hz, 场景提示=quiet_indoor

### 样本 1165: tram-stockholm-198-5960-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.895), Vehicle(0.251), Hubbub, speech noise, speech babble(0.196)
- **音频特征**: RMS=0.0118, 频谱重心=1056Hz, 场景提示=mixed_environment

### 样本 1166: bus-lyon-1001-42349-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Bird(0.435), Speech(0.407), Pigeon, dove(0.299)
- **音频特征**: RMS=0.0193, 频谱重心=602Hz, 场景提示=mixed_environment

### 样本 1167: airport-milan-1172-44205-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.359), Animal(0.335), Horse(0.224)
- **音频特征**: RMS=0.0030, 频谱重心=1347Hz, 场景提示=mixed_environment

### 样本 1168: tram-vienna-201-6064-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Animal(0.415), Speech(0.390), Domestic animals, pets(0.141)
- **音频特征**: RMS=0.0058, 频谱重心=2516Hz, 场景提示=mixed_environment

### 样本 1169: street_pedestrian-lyon-1003-41906-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.706), Arrow(0.213)
- **音频特征**: RMS=0.0022, 频谱重心=1354Hz, 场景提示=quiet_indoor

### 样本 1170: metro-helsinki-43-1315-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.739), Vehicle(0.390)
- **音频特征**: RMS=0.0080, 频谱重心=854Hz, 场景提示=quiet_indoor

### 样本 1171: bus-vienna-39-1165-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.825), Cat(0.775), Domestic animals, pets(0.698)
- **音频特征**: RMS=0.0057, 频谱重心=785Hz, 场景提示=quiet_indoor

### 样本 1172: tram-london-185-5750-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.783), Vehicle(0.507), Field recording(0.151)
- **音频特征**: RMS=0.0158, 频谱重心=514Hz, 场景提示=mixed_environment

### 样本 1173: airport-vienna-14-568-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.716)
- **音频特征**: RMS=0.0011, 频谱重心=1971Hz, 场景提示=mixed_environment

### 样本 1174: public_square-stockholm-119-3494-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Bicycle(0.458), Speech(0.446), Vehicle(0.315)
- **音频特征**: RMS=0.0044, 频谱重心=1674Hz, 场景提示=quiet_indoor

### 样本 1175: airport-paris-7-347-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.816), Music(0.560), Clip-clop(0.130)
- **音频特征**: RMS=0.0027, 频谱重心=1391Hz, 场景提示=mixed_environment

### 样本 1176: airport-london-5-222-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.909), Clip-clop(0.366), Horse(0.290)
- **音频特征**: RMS=0.0014, 频谱重心=1555Hz, 场景提示=mixed_environment

### 样本 1177: airport-barcelona-1-37-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.852), Outside, urban or manmade(0.132), Run(0.118)
- **音频特征**: RMS=0.0032, 频谱重心=1232Hz, 场景提示=quiet_indoor

### 样本 1178: airport-stockholm-11-460-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.604), Clip-clop(0.451), Horse(0.403)
- **音频特征**: RMS=0.0037, 频谱重心=1131Hz, 场景提示=quiet_indoor

### 样本 1179: bus-stockholm-218-6585-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.748), Vehicle(0.500), Bus(0.191)
- **音频特征**: RMS=0.0607, 频谱重心=440Hz, 场景提示=mixed_environment

### 样本 1180: metro_station-vienna-88-2425-a.wav
- **真实场景**: metro_station
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.171)
- **音频特征**: RMS=0.0074, 频谱重心=762Hz, 场景提示=quiet_indoor

### 样本 1181: public_square-london-115-3372-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.815), Outside, urban or manmade(0.128), Vehicle(0.109)
- **音频特征**: RMS=0.0018, 频谱重心=1120Hz, 场景提示=quiet_indoor

### 样本 1182: airport-paris-206-6237-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Animal(0.128), Speech(0.113)
- **音频特征**: RMS=0.0061, 频谱重心=937Hz, 场景提示=quiet_indoor

### 样本 1183: shopping_mall-helsinki-128-3809-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.767), Animal(0.160), Bird(0.144)
- **音频特征**: RMS=0.0020, 频谱重心=1245Hz, 场景提示=quiet_indoor

### 样本 1184: airport-stockholm-11-476-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.757), Animal(0.166), Vehicle(0.129)
- **音频特征**: RMS=0.0044, 频谱重心=1103Hz, 场景提示=quiet_indoor

### 样本 1185: shopping_mall-prague-1031-43722-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **音频特征**: RMS=0.0019, 频谱重心=1088Hz, 场景提示=quiet_indoor

### 样本 1186: airport-london-6-272-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **音频特征**: RMS=0.0021, 频谱重心=1194Hz, 场景提示=quiet_indoor

### 样本 1187: bus-vienna-39-1163-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.743), Vehicle(0.119), Throat clearing(0.113)
- **音频特征**: RMS=0.0073, 频谱重心=1023Hz, 场景提示=quiet_indoor

### 样本 1188: public_square-london-113-3296-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.811), Clip-clop(0.272), Animal(0.242)
- **音频特征**: RMS=0.0027, 频谱重心=1352Hz, 场景提示=quiet_indoor

### 样本 1189: airport-vienna-14-566-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.610), Music(0.364), Clip-clop(0.207)
- **音频特征**: RMS=0.0013, 频谱重心=1685Hz, 场景提示=mixed_environment

### 样本 1190: street_traffic-prague-1006-43449-a.wav
- **真实场景**: street_traffic
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.353), Train(0.213), Railroad car, train wagon(0.124)
- **音频特征**: RMS=0.0017, 频谱重心=848Hz, 场景提示=quiet_indoor

### 样本 1191: metro-lisbon-1121-43256-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Cupboard open or close(0.487), Vehicle(0.184), Arrow(0.168)
- **音频特征**: RMS=0.0113, 频谱重心=1006Hz, 场景提示=mixed_environment

### 样本 1192: shopping_mall-paris-133-4030-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.753), Clip-clop(0.314), Horse(0.233)
- **音频特征**: RMS=0.0035, 频谱重心=1294Hz, 场景提示=quiet_indoor

### 样本 1193: metro_station-helsinki-65-1951-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.509), Car(0.127), Field recording(0.121)
- **音频特征**: RMS=0.0100, 频谱重心=816Hz, 场景提示=quiet_indoor

### 样本 1194: street_pedestrian-stockholm-157-4772-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.767), Animal(0.155), Clip-clop(0.149)
- **音频特征**: RMS=0.0024, 频谱重心=1322Hz, 场景提示=quiet_indoor

### 样本 1195: airport-stockholm-12-484-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.766), Clip-clop(0.505), Horse(0.425)
- **音频特征**: RMS=0.0028, 频谱重心=967Hz, 场景提示=quiet_indoor

### 样本 1196: airport-milan-1172-45165-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.424)
- **音频特征**: RMS=0.0028, 频谱重心=1986Hz, 场景提示=mixed_environment

### 样本 1197: tram-helsinki-183-5703-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.672), Vehicle(0.257), Train(0.209)
- **音频特征**: RMS=0.0082, 频谱重心=795Hz, 场景提示=quiet_indoor

### 样本 1198: shopping_mall-lyon-1043-40503-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.788), Clip-clop(0.321), Animal(0.271)
- **音频特征**: RMS=0.0037, 频谱重心=1527Hz, 场景提示=mixed_environment

### 样本 1199: metro-lisbon-1224-45308-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.399), Vehicle(0.386), Rail transport(0.232)
- **音频特征**: RMS=0.0467, 频谱重心=755Hz, 场景提示=mixed_environment

### 样本 1200: metro_station-prague-1118-40997-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **音频特征**: RMS=0.0116, 频谱重心=1103Hz, 场景提示=mixed_environment

### 样本 1201: shopping_mall-vienna-139-4229-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.804), Run(0.222), Animal(0.220)
- **音频特征**: RMS=0.0024, 频谱重心=1694Hz, 场景提示=mixed_environment

### 样本 1202: shopping_mall-helsinki-128-3839-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.663)
- **音频特征**: RMS=0.0019, 频谱重心=1326Hz, 场景提示=mixed_environment

### 样本 1203: metro_station-helsinki-66-1977-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.807), Vehicle(0.138), Music(0.101)
- **音频特征**: RMS=0.0062, 频谱重心=1196Hz, 场景提示=quiet_indoor

### 样本 1204: street_pedestrian-vienna-158-4810-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.607), Church bell(0.212), Music(0.173)
- **音频特征**: RMS=0.0017, 频谱重心=1124Hz, 场景提示=quiet_indoor

### 样本 1205: tram-lisbon-1035-40049-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.813), Vehicle(0.337), Music(0.154)
- **音频特征**: RMS=0.0208, 频谱重心=906Hz, 场景提示=mixed_environment

### 样本 1206: metro-paris-226-6811-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Sliding door(0.421), Door(0.414), Speech(0.166)
- **音频特征**: RMS=0.0096, 频谱重心=1064Hz, 场景提示=quiet_indoor

### 样本 1207: bus-barcelona-16-667-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.786), Vehicle(0.418), Mouse(0.144)
- **音频特征**: RMS=0.0055, 频谱重心=606Hz, 场景提示=quiet_indoor

### 样本 1208: bus-prague-1215-45666-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.520), Car(0.173)
- **音频特征**: RMS=0.0264, 频谱重心=451Hz, 场景提示=mixed_environment

### 样本 1209: tram-lyon-1093-42568-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.797), Vehicle(0.233), Music(0.106)
- **音频特征**: RMS=0.0083, 频谱重心=680Hz, 场景提示=quiet_indoor

### 样本 1210: metro_station-lyon-1167-45500-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.352), Vehicle(0.255)
- **音频特征**: RMS=0.0081, 频谱重心=1708Hz, 场景提示=mixed_environment

### 样本 1211: tram-helsinki-184-5737-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.498), Chink, clink(0.123), Vehicle(0.109)
- **音频特征**: RMS=0.0169, 频谱重心=430Hz, 场景提示=mixed_environment

### 样本 1212: airport-vienna-14-578-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.760)
- **音频特征**: RMS=0.0011, 频谱重心=1582Hz, 场景提示=mixed_environment

### 样本 1213: metro_station-paris-238-7070-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: tram
- **音频特征**: RMS=0.0054, 频谱重心=1086Hz, 场景提示=quiet_indoor

### 样本 1214: metro_station-lisbon-1020-41101-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Music(0.474), Speech(0.129)
- **音频特征**: RMS=0.0034, 频谱重心=1137Hz, 场景提示=quiet_indoor

### 样本 1215: metro-stockholm-227-6821-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.701), Bird(0.209), Pigeon, dove(0.148)
- **音频特征**: RMS=0.0106, 频谱重心=1219Hz, 场景提示=mixed_environment

### 样本 1216: airport-stockholm-10-441-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.625), Clip-clop(0.210), Horse(0.184)
- **音频特征**: RMS=0.0015, 频谱重心=1361Hz, 场景提示=quiet_indoor

### 样本 1217: street_pedestrian-prague-1037-42972-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.811), Vehicle(0.160)
- **音频特征**: RMS=0.0141, 频谱重心=1443Hz, 场景提示=mixed_environment

### 样本 1218: street_pedestrian-stockholm-266-8073-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.424), Animal(0.208), Clip-clop(0.141)
- **音频特征**: RMS=0.0047, 频谱重心=1089Hz, 场景提示=quiet_indoor

### 样本 1219: tram-london-278-8469-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.773), Vehicle(0.392), Train(0.179)
- **音频特征**: RMS=0.0153, 频谱重心=731Hz, 场景提示=mixed_environment

### 样本 1220: street_pedestrian-milan-1080-43411-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.285), Silence(0.122)
- **音频特征**: RMS=0.0013, 频谱重心=1611Hz, 场景提示=mixed_environment

### 样本 1221: airport-prague-1195-45749-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.762), Clip-clop(0.257), Horse(0.217)
- **音频特征**: RMS=0.0012, 频谱重心=1412Hz, 场景提示=quiet_indoor

### 样本 1222: airport-milan-1172-44409-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.778), Vehicle(0.126)
- **音频特征**: RMS=0.0032, 频谱重心=1281Hz, 场景提示=mixed_environment

### 样本 1223: airport-london-205-6230-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.612)
- **音频特征**: RMS=0.0028, 频谱重心=1444Hz, 场景提示=quiet_indoor

### 样本 1224: street_pedestrian-helsinki-262-7945-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.853), Outside, urban or manmade(0.117), Vehicle(0.110)
- **音频特征**: RMS=0.0037, 频谱重心=1153Hz, 场景提示=quiet_indoor

### 样本 1225: metro-paris-50-1515-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.724), Rail transport(0.553), Railroad car, train wagon(0.493)
- **音频特征**: RMS=0.0123, 频谱重心=727Hz, 场景提示=mixed_environment

### 样本 1226: street_pedestrian-milan-1096-43079-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.694), Animal(0.165), Children playing(0.130)
- **音频特征**: RMS=0.0038, 频谱重心=1343Hz, 场景提示=mixed_environment

### 样本 1227: park-helsinki-92-2558-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.665), Crow(0.353), Caw(0.326)
- **音频特征**: RMS=0.0033, 频谱重心=807Hz, 场景提示=quiet_indoor

### 样本 1228: metro_station-lyon-1077-43951-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Music(0.451), Speech(0.336), Vehicle(0.122)
- **音频特征**: RMS=0.0032, 频谱重心=1018Hz, 场景提示=quiet_indoor

### 样本 1229: tram-lyon-1216-44845-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.717), Vehicle(0.382), Sliding door(0.123)
- **音频特征**: RMS=0.0073, 频谱重心=943Hz, 场景提示=quiet_indoor

### 样本 1230: public_square-milan-1074-43378-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.814), Clip-clop(0.185), Outside, urban or manmade(0.184)
- **音频特征**: RMS=0.0026, 频谱重心=1140Hz, 场景提示=quiet_indoor

### 样本 1231: tram-vienna-200-6048-a.wav
- **真实场景**: tram
- **AE预测**: street_traffic
- **AS预测**: park
- **检测到的事件**: Vehicle(0.141), Silence(0.112)
- **音频特征**: RMS=0.0048, 频谱重心=633Hz, 场景提示=quiet_indoor

### 样本 1232: tram-vienna-201-6068-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.690), Vehicle(0.154), Animal(0.111)
- **音频特征**: RMS=0.0040, 频谱重心=1607Hz, 场景提示=quiet_indoor

### 样本 1233: tram-barcelona-179-5553-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Siren(0.285), Vehicle(0.263), Civil defense siren(0.246)
- **音频特征**: RMS=0.0107, 频谱重心=673Hz, 场景提示=mixed_environment

### 样本 1234: street_pedestrian-london-149-4531-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.843), Clip-clop(0.205), Horse(0.162)
- **音频特征**: RMS=0.0036, 频谱重心=1040Hz, 场景提示=quiet_indoor

### 样本 1235: street_pedestrian-stockholm-157-4781-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.853), Clip-clop(0.252), Animal(0.215)
- **音频特征**: RMS=0.0033, 频谱重心=1365Hz, 场景提示=quiet_indoor

### 样本 1236: airport-milan-1108-43082-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.863), Run(0.290), Outside, urban or manmade(0.221)
- **音频特征**: RMS=0.0019, 频谱重心=1526Hz, 场景提示=quiet_indoor

### 样本 1237: shopping_mall-lyon-1066-42164-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.463), Clip-clop(0.203), Horse(0.169)
- **音频特征**: RMS=0.0014, 频谱重心=1398Hz, 场景提示=mixed_environment

### 样本 1238: tram-vienna-201-6060-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.721), Vehicle(0.187)
- **音频特征**: RMS=0.0039, 频谱重心=1462Hz, 场景提示=quiet_indoor

### 样本 1239: street_pedestrian-london-151-4598-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.343), Clicking(0.117)
- **音频特征**: RMS=0.0013, 频谱重心=1224Hz, 场景提示=quiet_indoor

### 样本 1240: street_pedestrian-helsinki-146-4421-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.806), Clip-clop(0.234), Horse(0.197)
- **音频特征**: RMS=0.0041, 频谱重心=1087Hz, 场景提示=quiet_indoor

### 样本 1241: public_square-prague-1075-42778-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.789), Run(0.181), Outside, urban or manmade(0.136)
- **音频特征**: RMS=0.0019, 频谱重心=1327Hz, 场景提示=quiet_indoor

### 样本 1242: tram-paris-282-8539-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.814), Music(0.566), Vehicle(0.290)
- **音频特征**: RMS=0.0072, 频谱重心=878Hz, 场景提示=quiet_indoor

### 样本 1243: airport-stockholm-208-6324-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.820), Clip-clop(0.330), Animal(0.236)
- **音频特征**: RMS=0.0049, 频谱重心=1315Hz, 场景提示=quiet_indoor

### 样本 1244: public_square-prague-1192-44139-a.wav
- **真实场景**: public_square
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.752), Vehicle(0.133), Animal(0.101)
- **音频特征**: RMS=0.0072, 频谱重心=736Hz, 场景提示=quiet_indoor

### 样本 1245: public_square-london-115-3360-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.881), Clip-clop(0.453), Horse(0.343)
- **音频特征**: RMS=0.0021, 频谱重心=1323Hz, 场景提示=quiet_indoor

### 样本 1246: tram-vienna-201-6083-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: park
- **检测到的事件**: Speech(0.648)
- **音频特征**: RMS=0.0031, 频谱重心=2863Hz, 场景提示=mixed_environment

### 样本 1247: street_pedestrian-vienna-158-4798-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.779), Animal(0.187), Clip-clop(0.160)
- **音频特征**: RMS=0.0015, 频谱重心=1348Hz, 场景提示=quiet_indoor

### 样本 1248: metro_station-paris-77-2129-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Snort(0.102)
- **音频特征**: RMS=0.0036, 频谱重心=1207Hz, 场景提示=quiet_indoor

### 样本 1249: tram-milan-1158-43750-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.729), Vehicle(0.472), Train(0.148)
- **音频特征**: RMS=0.0061, 频谱重心=1063Hz, 场景提示=quiet_indoor

### 样本 1250: tram-paris-192-5863-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.673), Music(0.483), Vehicle(0.359)
- **音频特征**: RMS=0.0076, 频谱重心=807Hz, 场景提示=quiet_indoor

### 样本 1251: public_square-stockholm-119-3491-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.309), Speech(0.140), Boat, Water vehicle(0.109)
- **音频特征**: RMS=0.0055, 频谱重心=914Hz, 场景提示=quiet_indoor

### 样本 1252: metro_station-vienna-240-7129-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.768), Animal(0.329), Horse(0.226)
- **音频特征**: RMS=0.0056, 频谱重心=754Hz, 场景提示=quiet_indoor

### 样本 1253: airport-milan-1061-44026-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.694), Mouse(0.315), Animal(0.121)
- **音频特征**: RMS=0.0017, 频谱重心=1409Hz, 场景提示=mixed_environment

### 样本 1254: tram-helsinki-184-5720-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.649), Vehicle(0.558), Field recording(0.285)
- **音频特征**: RMS=0.0351, 频谱重心=376Hz, 场景提示=mixed_environment

### 样本 1255: metro-london-46-1400-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.479), Vehicle(0.449), Music(0.297)
- **音频特征**: RMS=0.0102, 频谱重心=874Hz, 场景提示=mixed_environment

### 样本 1256: shopping_mall-vienna-138-4209-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.823), Outside, urban or manmade(0.108), Clip-clop(0.103)
- **音频特征**: RMS=0.0036, 频谱重心=1415Hz, 场景提示=mixed_environment

### 样本 1257: metro-prague-1054-43216-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.785), Rail transport(0.627), Railroad car, train wagon(0.617)
- **音频特征**: RMS=0.0319, 频谱重心=1012Hz, 场景提示=mixed_environment

### 样本 1258: park-lyon-1144-41816-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.705), Animal(0.341), Horse(0.180)
- **音频特征**: RMS=0.0008, 频谱重心=1080Hz, 场景提示=quiet_indoor

### 样本 1259: public_square-stockholm-120-3544-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.491), Animal(0.115), Vehicle(0.101)
- **音频特征**: RMS=0.0064, 频谱重心=1045Hz, 场景提示=quiet_indoor

### 样本 1260: street_pedestrian-vienna-158-4788-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.731), Clip-clop(0.227), Horse(0.174)
- **音频特征**: RMS=0.0014, 频谱重心=1313Hz, 场景提示=quiet_indoor

### 样本 1261: tram-milan-1134-43517-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.670), Train(0.544), Rail transport(0.385)
- **音频特征**: RMS=0.0191, 频谱重心=811Hz, 场景提示=mixed_environment

### 样本 1262: tram-vienna-201-6072-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **音频特征**: RMS=0.0126, 频谱重心=1270Hz, 场景提示=mixed_environment

### 样本 1263: public_square-lyon-1024-40059-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.476), Silence(0.224), Vehicle(0.132)
- **音频特征**: RMS=0.0018, 频谱重心=828Hz, 场景提示=quiet_indoor

### 样本 1264: public_square-prague-1152-41860-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.821), Animal(0.114)
- **音频特征**: RMS=0.0028, 频谱重心=1119Hz, 场景提示=quiet_indoor

### 样本 1265: tram-helsinki-276-8412-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.204)
- **音频特征**: RMS=0.0311, 频谱重心=408Hz, 场景提示=mixed_environment

### 样本 1266: bus-london-22-835-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.796), Music(0.136), Vehicle(0.129)
- **音频特征**: RMS=0.0041, 频谱重心=1990Hz, 场景提示=mixed_environment

### 样本 1267: metro_station-lyon-1077-43296-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.752), Music(0.297)
- **音频特征**: RMS=0.0037, 频谱重心=1017Hz, 场景提示=quiet_indoor

### 样本 1268: airport-paris-7-308-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.851), Clip-clop(0.234), Horse(0.192)
- **音频特征**: RMS=0.0025, 频谱重心=1418Hz, 场景提示=mixed_environment

### 样本 1269: street_pedestrian-lisbon-1098-41624-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.728), Chink, clink(0.175)
- **音频特征**: RMS=0.0026, 频谱重心=1456Hz, 场景提示=mixed_environment

### 样本 1270: airport-prague-1015-43103-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.903), Clip-clop(0.828), Horse(0.750)
- **音频特征**: RMS=0.0041, 频谱重心=1136Hz, 场景提示=quiet_indoor

### 样本 1271: public_square-prague-1111-40293-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.452), Vehicle(0.122), Silence(0.101)
- **音频特征**: RMS=0.0054, 频谱重心=1362Hz, 场景提示=quiet_indoor

### 样本 1272: metro_station-vienna-240-7123-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: airport
- **音频特征**: RMS=0.0035, 频谱重心=1133Hz, 场景提示=quiet_indoor

### 样本 1273: street_pedestrian-london-150-4536-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.775), Clip-clop(0.238), Horse(0.175)
- **音频特征**: RMS=0.0022, 频谱重心=1264Hz, 场景提示=quiet_indoor

### 样本 1274: tram-stockholm-199-6008-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.677), Vehicle(0.511), Train(0.196)
- **音频特征**: RMS=0.0183, 频谱重心=542Hz, 场景提示=mixed_environment

### 样本 1275: metro-stockholm-57-1698-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.370), Train(0.104)
- **音频特征**: RMS=0.0150, 频谱重心=328Hz, 场景提示=mixed_environment

### 样本 1276: metro_station-helsinki-64-1910-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: park
- **检测到的事件**: Silence(0.160), Inside, small room(0.136)
- **音频特征**: RMS=0.0008, 频谱重心=1138Hz, 场景提示=quiet_indoor

### 样本 1277: street_pedestrian-barcelona-144-4353-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.842), Chatter(0.181), Music(0.110)
- **音频特征**: RMS=0.0023, 频谱重心=1420Hz, 场景提示=mixed_environment

### 样本 1278: shopping_mall-lisbon-1002-42125-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.698), Animal(0.111), Music(0.106)
- **音频特征**: RMS=0.0024, 频谱重心=1237Hz, 场景提示=quiet_indoor

### 样本 1279: tram-paris-191-5853-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.780), Music(0.436), Vehicle(0.128)
- **音频特征**: RMS=0.0090, 频谱重心=635Hz, 场景提示=quiet_indoor

### 样本 1280: street_pedestrian-paris-153-4639-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.797), Male speech, man speaking(0.101)
- **音频特征**: RMS=0.0020, 频谱重心=1327Hz, 场景提示=quiet_indoor

### 样本 1281: street_pedestrian-vienna-160-4888-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.429), Animal(0.106)
- **音频特征**: RMS=0.0020, 频谱重心=1284Hz, 场景提示=mixed_environment

### 样本 1282: street_pedestrian-lyon-1047-43198-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.465), Vehicle(0.412), Music(0.165)
- **音频特征**: RMS=0.0020, 频谱重心=1664Hz, 场景提示=mixed_environment

### 样本 1283: public_square-prague-1075-43336-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.865), Clip-clop(0.251), Run(0.179)
- **音频特征**: RMS=0.0022, 频谱重心=1112Hz, 场景提示=quiet_indoor

### 样本 1284: metro-vienna-228-6882-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.825), Vehicle(0.273)
- **音频特征**: RMS=0.0115, 频谱重心=637Hz, 场景提示=mixed_environment

### 样本 1285: shopping_mall-stockholm-136-4113-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.523), Vehicle(0.145)
- **音频特征**: RMS=0.0044, 频谱重心=858Hz, 场景提示=quiet_indoor

### 样本 1286: public_square-vienna-122-3621-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.549), Animal(0.259), Clip-clop(0.161)
- **音频特征**: RMS=0.0010, 频谱重心=948Hz, 场景提示=quiet_indoor

### 样本 1287: street_pedestrian-london-149-4525-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.846), Clip-clop(0.235), Animal(0.218)
- **音频特征**: RMS=0.0017, 频谱重心=929Hz, 场景提示=quiet_indoor

### 样本 1288: tram-prague-1088-40937-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.149), Silence(0.118), White noise(0.110)
- **音频特征**: RMS=0.0038, 频谱重心=1075Hz, 场景提示=quiet_indoor

### 样本 1289: airport-barcelona-203-6135-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.785), Animal(0.352), Clip-clop(0.324)
- **音频特征**: RMS=0.0020, 频谱重心=1262Hz, 场景提示=quiet_indoor

### 样本 1290: street_traffic-london-167-5123-a.wav
- **真实场景**: street_traffic
- **AE预测**: metro_station
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.743), Vehicle(0.381), Fire(0.139)
- **音频特征**: RMS=0.0102, 频谱重心=1313Hz, 场景提示=mixed_environment

### 样本 1291: airport-stockholm-11-474-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Clip-clop(0.220), Horse(0.183), Animal(0.152)
- **音频特征**: RMS=0.0036, 频谱重心=1139Hz, 场景提示=quiet_indoor

### 样本 1292: public_square-london-114-3311-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: airport
- **检测到的事件**: Speech(0.706), Slam(0.201), Arrow(0.153)
- **音频特征**: RMS=0.0044, 频谱重心=1150Hz, 场景提示=mixed_environment

### 样本 1293: street_pedestrian-paris-265-8043-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Animal(0.368), Clip-clop(0.323), Horse(0.307)
- **音频特征**: RMS=0.0024, 频谱重心=1176Hz, 场景提示=quiet_indoor

### 样本 1294: bus-lisbon-1212-45534-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.426), Train(0.232), Rail transport(0.133)
- **音频特征**: RMS=0.0228, 频谱重心=1038Hz, 场景提示=mixed_environment

### 样本 1295: shopping_mall-lisbon-1176-45025-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.778), Music(0.230), Female speech, woman speaking(0.102)
- **音频特征**: RMS=0.0019, 频谱重心=1440Hz, 场景提示=quiet_indoor

### 样本 1296: airport-barcelona-1-86-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.738), Animal(0.108)
- **音频特征**: RMS=0.0039, 频谱重心=1132Hz, 场景提示=quiet_indoor

### 样本 1297: metro_station-lisbon-1021-42993-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.367), Train(0.139), Mouse(0.113)
- **音频特征**: RMS=0.0071, 频谱重心=935Hz, 场景提示=quiet_indoor

### 样本 1298: shopping_mall-prague-1031-43971-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Music(0.379), Opera(0.119), Orchestra(0.102)
- **音频特征**: RMS=0.0020, 频谱重心=1027Hz, 场景提示=quiet_indoor

### 样本 1299: street_pedestrian-lyon-1003-40446-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.715)
- **音频特征**: RMS=0.0016, 频谱重心=1510Hz, 场景提示=quiet_indoor

### 样本 1300: metro-lyon-1139-41087-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.768), Music(0.759), Vehicle(0.177)
- **音频特征**: RMS=0.0121, 频谱重心=1044Hz, 场景提示=mixed_environment

### 样本 1301: public_square-lyon-1056-43132-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.588), Vehicle(0.113), Silence(0.104)
- **音频特征**: RMS=0.0019, 频谱重心=1153Hz, 场景提示=quiet_indoor

### 样本 1302: street_pedestrian-london-150-4558-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.821), Run(0.461), Outside, urban or manmade(0.242)
- **音频特征**: RMS=0.0029, 频谱重心=1134Hz, 场景提示=quiet_indoor

### 样本 1303: metro_station-milan-1127-43513-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Camera(0.345), Single-lens reflex camera(0.270), Speech(0.168)
- **音频特征**: RMS=0.0038, 频谱重心=1339Hz, 场景提示=quiet_indoor

### 样本 1304: public_square-stockholm-121-3578-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.568), Animal(0.259), Duck(0.210)
- **音频特征**: RMS=0.0060, 频谱重心=1193Hz, 场景提示=quiet_indoor

### 样本 1305: street_traffic-milan-1202-44780-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_traffic
- **AS预测**: park
- **检测到的事件**: Silence(0.149), Vehicle(0.117)
- **音频特征**: RMS=0.0027, 频谱重心=1081Hz, 场景提示=quiet_indoor

### 样本 1306: airport-london-6-297-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.659), Animal(0.307), Clip-clop(0.220)
- **音频特征**: RMS=0.0019, 频谱重心=1162Hz, 场景提示=quiet_indoor

### 样本 1307: public_square-lyon-1178-44197-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Music(0.436), Horse(0.165), Clip-clop(0.159)
- **音频特征**: RMS=0.0014, 频谱重心=1231Hz, 场景提示=quiet_indoor

### 样本 1308: metro-barcelona-42-1268-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.487), Train(0.140)
- **音频特征**: RMS=0.0117, 频谱重心=750Hz, 场景提示=mixed_environment

### 样本 1309: tram-lyon-1216-44986-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.805), Vehicle(0.416), Car(0.140)
- **音频特征**: RMS=0.0132, 频谱重心=513Hz, 场景提示=mixed_environment

### 样本 1310: tram-prague-1210-44236-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.614), Vehicle(0.578), Train(0.204)
- **音频特征**: RMS=0.0516, 频谱重心=540Hz, 场景提示=mixed_environment

### 样本 1311: tram-barcelona-181-5600-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.853), Hubbub, speech noise, speech babble(0.210), Vehicle(0.150)
- **音频特征**: RMS=0.0131, 频谱重心=1426Hz, 场景提示=mixed_environment

### 样本 1312: street_traffic-barcelona-161-4917-a.wav
- **真实场景**: street_traffic
- **AE预测**: metro_station
- **AS预测**: public_square
- **检测到的事件**: Speech(0.656), Vehicle(0.444), Car(0.121)
- **音频特征**: RMS=0.0082, 频谱重心=1098Hz, 场景提示=quiet_indoor

### 样本 1313: street_pedestrian-helsinki-146-4422-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.623), Vehicle(0.120)
- **音频特征**: RMS=0.0042, 频谱重心=879Hz, 场景提示=quiet_indoor

### 样本 1314: shopping_mall-paris-132-3987-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.370), Music(0.340), Chink, clink(0.105)
- **音频特征**: RMS=0.0034, 频谱重心=1383Hz, 场景提示=quiet_indoor

### 样本 1315: public_square-prague-1152-41395-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.816), Chatter(0.136), Outside, urban or manmade(0.108)
- **音频特征**: RMS=0.0030, 频谱重心=1134Hz, 场景提示=mixed_environment

### 样本 1316: street_pedestrian-helsinki-146-4420-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.756), Animal(0.371), Clip-clop(0.313)
- **音频特征**: RMS=0.0037, 频谱重心=1149Hz, 场景提示=quiet_indoor

### 样本 1317: airport-prague-1034-43893-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.641), Animal(0.156), Vehicle(0.111)
- **音频特征**: RMS=0.0082, 频谱重心=1830Hz, 场景提示=mixed_environment

### 样本 1318: street_pedestrian-london-149-4508-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.787), Clip-clop(0.180), Animal(0.159)
- **音频特征**: RMS=0.0024, 频谱重心=1032Hz, 场景提示=quiet_indoor

### 样本 1319: airport-stockholm-208-6316-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.816), Animal(0.117), Clip-clop(0.105)
- **音频特征**: RMS=0.0055, 频谱重心=1204Hz, 场景提示=quiet_indoor

### 样本 1320: shopping_mall-london-131-3952-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.770), Animal(0.118)
- **音频特征**: RMS=0.0022, 频谱重心=1703Hz, 场景提示=mixed_environment

### 样本 1321: airport-lyon-1095-43177-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.493)
- **音频特征**: RMS=0.0011, 频谱重心=1161Hz, 场景提示=quiet_indoor

### 样本 1322: street_pedestrian-stockholm-155-4713-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.734), Animal(0.297), Chewing, mastication(0.134)
- **音频特征**: RMS=0.0063, 频谱重心=965Hz, 场景提示=quiet_indoor

### 样本 1323: shopping_mall-barcelona-126-3770-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.691), Snort(0.170), Basketball bounce(0.122)
- **音频特征**: RMS=0.0018, 频谱重心=2060Hz, 场景提示=mixed_environment

### 样本 1324: shopping_mall-barcelona-254-7610-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.855), Horse(0.355), Clip-clop(0.316)
- **音频特征**: RMS=0.0034, 频谱重心=1476Hz, 场景提示=mixed_environment

### 样本 1325: public_square-milan-1168-45167-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: airport
- **检测到的事件**: Speech(0.594)
- **音频特征**: RMS=0.0030, 频谱重心=2366Hz, 场景提示=mixed_environment

### 样本 1326: airport-helsinki-4-181-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Clicking(0.162), Inside, small room(0.126)
- **音频特征**: RMS=0.0014, 频谱重心=1303Hz, 场景提示=quiet_indoor

### 样本 1327: metro_station-stockholm-83-2242-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.788), Clip-clop(0.375), Horse(0.279)
- **音频特征**: RMS=0.0055, 频谱重心=1049Hz, 场景提示=quiet_indoor

### 样本 1328: tram-paris-280-8495-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.669), Music(0.143), Vehicle(0.115)
- **音频特征**: RMS=0.0068, 频谱重心=995Hz, 场景提示=quiet_indoor

### 样本 1329: metro_station-vienna-87-2384-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.279), Speech(0.187)
- **音频特征**: RMS=0.0056, 频谱重心=602Hz, 场景提示=quiet_indoor

### 样本 1330: metro-milan-1197-44145-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro_station
- **检测到的事件**: Music(0.451), Speech(0.441), Vehicle(0.166)
- **音频特征**: RMS=0.0407, 频谱重心=869Hz, 场景提示=mixed_environment

### 样本 1331: shopping_mall-prague-1219-45503-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.823), Basketball bounce(0.190)
- **音频特征**: RMS=0.0036, 频谱重心=1647Hz, 场景提示=mixed_environment

### 样本 1332: street_pedestrian-stockholm-266-8076-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.599), Animal(0.233), Clip-clop(0.190)
- **音频特征**: RMS=0.0038, 频谱重心=1097Hz, 场景提示=quiet_indoor

### 样本 1333: shopping_mall-helsinki-129-3853-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.794), Music(0.161), Inside, public space(0.105)
- **音频特征**: RMS=0.0074, 频谱重心=1120Hz, 场景提示=quiet_indoor

### 样本 1334: street_pedestrian-barcelona-141-4298-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: metro_station
- **AS预测**: public_square
- **检测到的事件**: Speech(0.785), Vehicle(0.574), Car(0.254)
- **音频特征**: RMS=0.0117, 频谱重心=1629Hz, 场景提示=mixed_environment

### 样本 1335: street_pedestrian-paris-153-4651-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.860), Run(0.542), Outside, urban or manmade(0.330)
- **音频特征**: RMS=0.0019, 频谱重心=1377Hz, 场景提示=quiet_indoor

### 样本 1336: airport-lyon-1169-44528-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.722), Music(0.578), Run(0.183)
- **音频特征**: RMS=0.0044, 频谱重心=1462Hz, 场景提示=mixed_environment

### 样本 1337: airport-paris-206-6253-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.323), Vehicle(0.115)
- **音频特征**: RMS=0.0066, 频谱重心=1039Hz, 场景提示=quiet_indoor

### 样本 1338: public_square-stockholm-119-3498-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Clip-clop(0.317), Horse(0.268), Animal(0.252)
- **音频特征**: RMS=0.0058, 频谱重心=1096Hz, 场景提示=quiet_indoor

### 样本 1339: metro-barcelona-41-1246-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.599), Vehicle(0.439), Train(0.380)
- **音频特征**: RMS=0.0101, 频谱重心=701Hz, 场景提示=mixed_environment

### 样本 1340: airport-barcelona-2-102-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.830), Animal(0.209), Clip-clop(0.191)
- **音频特征**: RMS=0.0026, 频谱重心=1258Hz, 场景提示=quiet_indoor

### 样本 1341: shopping_mall-lyon-1043-42837-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.809), Clip-clop(0.266), Horse(0.189)
- **音频特征**: RMS=0.0037, 频谱重心=1553Hz, 场景提示=mixed_environment

### 样本 1342: street_pedestrian-paris-153-4618-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: park
- **检测到的事件**: Speech(0.274), Animal(0.101)
- **音频特征**: RMS=0.0039, 频谱重心=901Hz, 场景提示=quiet_indoor

### 样本 1343: park-paris-244-7292-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.781), Animal(0.273), Clip-clop(0.257)
- **音频特征**: RMS=0.0025, 频谱重心=743Hz, 场景提示=quiet_indoor

### 样本 1344: park-london-96-2679-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.870), Animal(0.315), Horse(0.201)
- **音频特征**: RMS=0.0015, 频谱重心=1621Hz, 场景提示=mixed_environment

### 样本 1345: shopping_mall-barcelona-127-3805-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.697), Animal(0.192), Clip-clop(0.180)
- **音频特征**: RMS=0.0025, 频谱重心=1501Hz, 场景提示=mixed_environment

### 样本 1346: tram-helsinki-276-8408-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.768), Vehicle(0.396)
- **音频特征**: RMS=0.0144, 频谱重心=618Hz, 场景提示=mixed_environment

### 样本 1347: metro-lisbon-1121-42924-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.636), Field recording(0.295), Train(0.222)
- **音频特征**: RMS=0.0499, 频谱重心=547Hz, 场景提示=mixed_environment

### 样本 1348: airport-barcelona-1-96-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.856), Outside, urban or manmade(0.205), Run(0.182)
- **音频特征**: RMS=0.0039, 频谱重心=1132Hz, 场景提示=quiet_indoor

### 样本 1349: metro-london-46-1368-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.698), Vehicle(0.615), Car(0.327)
- **音频特征**: RMS=0.0079, 频谱重心=1074Hz, 场景提示=quiet_indoor

### 样本 1350: street_traffic-prague-1006-41700-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.262)
- **音频特征**: RMS=0.0078, 频谱重心=754Hz, 场景提示=quiet_indoor

### 样本 1351: metro_station-helsinki-67-1993-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: park
- **检测到的事件**: Silence(0.292), Inside, small room(0.133)
- **音频特征**: RMS=0.0009, 频谱重心=1059Hz, 场景提示=quiet_indoor

### 样本 1352: tram-milan-1209-45314-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Sliding door(0.300), Speech(0.278), Vehicle(0.266)
- **音频特征**: RMS=0.0071, 频谱重心=1320Hz, 场景提示=quiet_indoor

### 样本 1353: metro-lisbon-1217-44642-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.719), Vehicle(0.539), Train(0.221)
- **音频特征**: RMS=0.0261, 频谱重心=653Hz, 场景提示=mixed_environment

### 样本 1354: street_pedestrian-barcelona-261-7918-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.506), Vehicle(0.201), Music(0.108)
- **音频特征**: RMS=0.0038, 频谱重心=1233Hz, 场景提示=quiet_indoor

### 样本 1355: metro_station-lisbon-1020-41598-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.464), Train(0.199), Vehicle(0.182)
- **音频特征**: RMS=0.0056, 频谱重心=982Hz, 场景提示=quiet_indoor

### 样本 1356: public_square-vienna-122-3626-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.763), Animal(0.210), Clip-clop(0.182)
- **音频特征**: RMS=0.0010, 频谱重心=1070Hz, 场景提示=quiet_indoor

### 样本 1357: metro_station-lisbon-1221-44386-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.819), Clip-clop(0.436), Horse(0.377)
- **音频特征**: RMS=0.0040, 频谱重心=1328Hz, 场景提示=quiet_indoor

### 样本 1358: metro-stockholm-227-6843-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.684), Animal(0.150), Vehicle(0.125)
- **音频特征**: RMS=0.0087, 频谱重心=1281Hz, 场景提示=quiet_indoor

### 样本 1359: park-milan-1018-42284-a.wav
- **真实场景**: park
- **AE预测**: street_pedestrian
- **AS预测**: park
- **检测到的事件**: Speech(0.722), Vehicle(0.205), Bicycle(0.177)
- **音频特征**: RMS=0.0013, 频谱重心=1973Hz, 场景提示=mixed_environment

### 样本 1360: tram-vienna-200-6016-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.708), Pigeon, dove(0.197), Vehicle(0.195)
- **音频特征**: RMS=0.0054, 频谱重心=1101Hz, 场景提示=quiet_indoor

### 样本 1361: shopping_mall-helsinki-255-7648-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.859), Outside, urban or manmade(0.138), Clip-clop(0.137)
- **音频特征**: RMS=0.0071, 频谱重心=1152Hz, 场景提示=quiet_indoor

### 样本 1362: bus-stockholm-217-6548-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.296), Rumble(0.179), Music(0.107)
- **音频特征**: RMS=0.0469, 频谱重心=390Hz, 场景提示=mixed_environment

### 样本 1363: tram-lyon-1216-44380-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.763), Vehicle(0.331)
- **音频特征**: RMS=0.0091, 频谱重心=871Hz, 场景提示=quiet_indoor

### 样本 1364: public_square-vienna-123-3643-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.816), Outside, urban or manmade(0.139), Vehicle(0.113)
- **音频特征**: RMS=0.0036, 频谱重心=1238Hz, 场景提示=quiet_indoor

### 样本 1365: street_pedestrian-prague-1037-40046-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.837), Outside, urban or manmade(0.133), Clip-clop(0.132)
- **音频特征**: RMS=0.0022, 频谱重心=1395Hz, 场景提示=mixed_environment

### 样本 1366: park-barcelona-90-2489-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.271)
- **音频特征**: RMS=0.0056, 频谱重心=658Hz, 场景提示=quiet_indoor

### 样本 1367: metro_station-prague-1170-44553-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.738)
- **音频特征**: RMS=0.0095, 频谱重心=971Hz, 场景提示=quiet_indoor

### 样本 1368: street_pedestrian-lisbon-1098-41806-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.769)
- **音频特征**: RMS=0.0029, 频谱重心=1357Hz, 场景提示=mixed_environment

### 样本 1369: airport-prague-1023-40436-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.668), Clip-clop(0.124), Music(0.116)
- **音频特征**: RMS=0.0048, 频谱重心=1253Hz, 场景提示=quiet_indoor

### 样本 1370: tram-stockholm-199-5996-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.769), Vehicle(0.525), Rumble(0.391)
- **音频特征**: RMS=0.1214, 频谱重心=237Hz, 场景提示=mixed_environment

### 样本 1371: street_pedestrian-prague-1085-40779-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: park
- **检测到的事件**: Speech(0.294), Vehicle(0.150)
- **音频特征**: RMS=0.0028, 频谱重心=867Hz, 场景提示=quiet_indoor

### 样本 1372: tram-milan-1065-41654-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.696), Vehicle(0.415), Train(0.267)
- **音频特征**: RMS=0.0142, 频谱重心=722Hz, 场景提示=mixed_environment

### 样本 1373: street_pedestrian-stockholm-157-4752-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.269), Ratchet, pawl(0.195), Mechanisms(0.189)
- **音频特征**: RMS=0.0059, 频谱重心=1523Hz, 场景提示=mixed_environment

### 样本 1374: metro-barcelona-42-1305-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.422), Train(0.307), Railroad car, train wagon(0.165)
- **音频特征**: RMS=0.0118, 频谱重心=679Hz, 场景提示=mixed_environment

### 样本 1375: airport-stockholm-207-6287-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.790), Clip-clop(0.265), Animal(0.193)
- **音频特征**: RMS=0.0033, 频谱重心=1492Hz, 场景提示=mixed_environment

### 样本 1376: shopping_mall-helsinki-130-3900-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.772), Clip-clop(0.111), Tick(0.110)
- **音频特征**: RMS=0.0051, 频谱重心=1152Hz, 场景提示=quiet_indoor

### 样本 1377: street_traffic-london-168-5159-a.wav
- **真实场景**: street_traffic
- **AE预测**: bus
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.538), Car(0.136), Truck(0.110)
- **音频特征**: RMS=0.0108, 频谱重心=1221Hz, 场景提示=mixed_environment

### 样本 1378: metro_station-vienna-86-2346-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.777), Vehicle(0.264)
- **音频特征**: RMS=0.0063, 频谱重心=1223Hz, 场景提示=quiet_indoor

### 样本 1379: metro-paris-54-1597-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.799), Children playing(0.185), Music(0.171)
- **音频特征**: RMS=0.0062, 频谱重心=1253Hz, 场景提示=quiet_indoor

### 样本 1380: street_pedestrian-milan-1080-41328-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.812), Clip-clop(0.184), Horse(0.146)
- **音频特征**: RMS=0.0021, 频谱重心=1478Hz, 场景提示=quiet_indoor

### 样本 1381: shopping_mall-helsinki-255-7647-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.766), Mouse(0.114)
- **音频特征**: RMS=0.0055, 频谱重心=1273Hz, 场景提示=quiet_indoor

### 样本 1382: metro_station-lisbon-1221-45207-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: public_square
- **检测到的事件**: Speech(0.612), Train(0.460), Vehicle(0.389)
- **音频特征**: RMS=0.0144, 频谱重心=1056Hz, 场景提示=mixed_environment

### 样本 1383: metro-vienna-228-6875-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.685), Vehicle(0.156), Animal(0.117)
- **音频特征**: RMS=0.0056, 频谱重心=1016Hz, 场景提示=quiet_indoor

### 样本 1384: tram-lisbon-1035-43353-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.821), Vehicle(0.431), Car(0.125)
- **音频特征**: RMS=0.0338, 频谱重心=524Hz, 场景提示=mixed_environment

### 样本 1385: metro-lyon-1201-45026-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.206), Sliding door(0.160), Train(0.144)
- **音频特征**: RMS=0.0105, 频谱重心=876Hz, 场景提示=mixed_environment

### 样本 1386: public_square-london-113-3298-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Animal(0.264), Clip-clop(0.190), Horse(0.176)
- **音频特征**: RMS=0.0029, 频谱重心=1038Hz, 场景提示=quiet_indoor

### 样本 1387: airport-helsinki-204-6172-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.718), Clip-clop(0.108), Animal(0.107)
- **音频特征**: RMS=0.0020, 频谱重心=1723Hz, 场景提示=mixed_environment

### 样本 1388: street_pedestrian-london-263-7979-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.886), Animal(0.196), Outside, urban or manmade(0.176)
- **音频特征**: RMS=0.0017, 频谱重心=1561Hz, 场景提示=mixed_environment

### 样本 1389: metro-milan-1141-40656-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.557), Vehicle(0.180), Insect(0.117)
- **音频特征**: RMS=0.0112, 频谱重心=720Hz, 场景提示=mixed_environment

### 样本 1390: metro_station-vienna-86-2355-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.857), Children playing(0.556), Child speech, kid speaking(0.176)
- **音频特征**: RMS=0.0053, 频谱重心=1075Hz, 场景提示=quiet_indoor

### 样本 1391: street_traffic-paris-272-8274-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.805), Animal(0.150), Outside, urban or manmade(0.123)
- **音频特征**: RMS=0.0038, 频谱重心=1124Hz, 场景提示=quiet_indoor

### 样本 1392: bus-milan-1078-40258-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.632), Train(0.173), Car(0.154)
- **音频特征**: RMS=0.0128, 频谱重心=990Hz, 场景提示=mixed_environment

### 样本 1393: street_pedestrian-barcelona-141-4287-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.571), Vehicle(0.234)
- **音频特征**: RMS=0.0050, 频谱重心=1791Hz, 场景提示=mixed_environment

### 样本 1394: bus-milan-1155-43531-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.531), Vehicle(0.462)
- **音频特征**: RMS=0.0350, 频谱重心=489Hz, 场景提示=mixed_environment

### 样本 1395: tram-barcelona-179-5542-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.780), Sliding door(0.534), Door(0.369)
- **音频特征**: RMS=0.0114, 频谱重心=891Hz, 场景提示=mixed_environment

### 样本 1396: shopping_mall-helsinki-129-3866-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.750), Animal(0.132)
- **音频特征**: RMS=0.0065, 频谱重心=1000Hz, 场景提示=quiet_indoor

### 样本 1397: tram-prague-1210-45507-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.506), Train(0.367), Rail transport(0.219)
- **音频特征**: RMS=0.0291, 频谱重心=594Hz, 场景提示=mixed_environment

### 样本 1398: tram-london-279-8473-a.wav
- **真实场景**: tram
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.773), Vehicle(0.276)
- **音频特征**: RMS=0.0022, 频谱重心=1059Hz, 场景提示=quiet_indoor

### 样本 1399: public_square-lyon-1024-43928-a.wav
- **真实场景**: public_square
- **AE预测**: street_traffic
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.657), Vehicle(0.209)
- **音频特征**: RMS=0.0030, 频谱重心=987Hz, 场景提示=quiet_indoor

### 样本 1400: metro_station-stockholm-85-2285-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.719), Clip-clop(0.402), Horse(0.320)
- **音频特征**: RMS=0.0065, 频谱重心=1036Hz, 场景提示=quiet_indoor

### 样本 1401: airport-barcelona-0-1-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.793), Run(0.296), Outside, urban or manmade(0.185)
- **音频特征**: RMS=0.0028, 频谱重心=1319Hz, 场景提示=quiet_indoor

### 样本 1402: metro_station-vienna-86-2333-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.645)
- **音频特征**: RMS=0.0016, 频谱重心=1064Hz, 场景提示=quiet_indoor

### 样本 1403: public_square-paris-118-3447-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.850), Run(0.459), Animal(0.250)
- **音频特征**: RMS=0.0020, 频谱重心=1556Hz, 场景提示=quiet_indoor

### 样本 1404: street_pedestrian-helsinki-147-4427-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.753), Clip-clop(0.205), Animal(0.202)
- **音频特征**: RMS=0.0045, 频谱重心=978Hz, 场景提示=quiet_indoor

### 样本 1405: metro_station-helsinki-232-6974-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.390), Clip-clop(0.323), Horse(0.251)
- **音频特征**: RMS=0.0046, 频谱重心=1022Hz, 场景提示=quiet_indoor

### 样本 1406: metro-stockholm-227-6847-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.772), Vehicle(0.379)
- **音频特征**: RMS=0.0119, 频谱重心=577Hz, 场景提示=mixed_environment

### 样本 1407: public_square-london-113-3277-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.762), Clip-clop(0.220), Animal(0.198)
- **音频特征**: RMS=0.0029, 频谱重心=1189Hz, 场景提示=quiet_indoor

### 样本 1408: street_pedestrian-london-149-4501-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.900), Clip-clop(0.557), Horse(0.442)
- **音频特征**: RMS=0.0024, 频谱重心=1377Hz, 场景提示=quiet_indoor

### 样本 1409: street_pedestrian-vienna-158-4794-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.725), Music(0.449), Clip-clop(0.258)
- **音频特征**: RMS=0.0019, 频谱重心=1331Hz, 场景提示=quiet_indoor

### 样本 1410: shopping_mall-helsinki-255-7671-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.741)
- **音频特征**: RMS=0.0037, 频谱重心=1211Hz, 场景提示=quiet_indoor

### 样本 1411: bus-stockholm-36-1067-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.739), Vehicle(0.281)
- **音频特征**: RMS=0.0085, 频谱重心=1164Hz, 场景提示=quiet_indoor

### 样本 1412: street_pedestrian-stockholm-155-4711-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.785), Vehicle(0.164), Animal(0.150)
- **音频特征**: RMS=0.0063, 频谱重心=865Hz, 场景提示=quiet_indoor

### 样本 1413: metro_station-barcelona-230-6931-a.wav
- **真实场景**: metro_station
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.165), Rumble(0.132), Music(0.100)
- **音频特征**: RMS=0.0194, 频谱重心=422Hz, 场景提示=mixed_environment

### 样本 1414: airport-vienna-209-6377-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Mechanisms(0.164), Typewriter(0.160), Ratchet, pawl(0.102)
- **音频特征**: RMS=0.0029, 频谱重心=1707Hz, 场景提示=mixed_environment

### 样本 1415: bus-vienna-40-1216-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.817), Vehicle(0.417), Outside, urban or manmade(0.103)
- **音频特征**: RMS=0.0111, 频谱重心=697Hz, 场景提示=mixed_environment

### 样本 1416: metro-paris-54-1599-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.653), Chicken, rooster(0.177), Door(0.124)
- **音频特征**: RMS=0.0077, 频谱重心=1082Hz, 场景提示=quiet_indoor

### 样本 1417: shopping_mall-lyon-1043-43686-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.560), Music(0.237), Animal(0.104)
- **音频特征**: RMS=0.0040, 频谱重心=1325Hz, 场景提示=mixed_environment

### 样本 1418: street_pedestrian-vienna-159-4842-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.223), Music(0.174), Fowl(0.122)
- **音频特征**: RMS=0.0011, 频谱重心=1302Hz, 场景提示=quiet_indoor

### 样本 1419: shopping_mall-helsinki-129-3846-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.740), Animal(0.107), Vehicle(0.105)
- **音频特征**: RMS=0.0043, 频谱重心=1009Hz, 场景提示=quiet_indoor

### 样本 1420: shopping_mall-helsinki-255-7673-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.860), Clip-clop(0.160), Animal(0.125)
- **音频特征**: RMS=0.0079, 频谱重心=1294Hz, 场景提示=mixed_environment

### 样本 1421: public_square-paris-118-3461-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.503), Animal(0.371), Clip-clop(0.295)
- **音频特征**: RMS=0.0015, 频谱重心=1512Hz, 场景提示=quiet_indoor

### 样本 1422: metro_station-lisbon-1221-45262-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.730), Vehicle(0.428), Train(0.248)
- **音频特征**: RMS=0.0176, 频谱重心=1137Hz, 场景提示=mixed_environment

### 样本 1423: shopping_mall-stockholm-136-4131-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.703)
- **音频特征**: RMS=0.0036, 频谱重心=1129Hz, 场景提示=quiet_indoor

### 样本 1424: street_pedestrian-paris-153-4643-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.563), Music(0.278), Mouse(0.137)
- **音频特征**: RMS=0.0019, 频谱重心=1148Hz, 场景提示=quiet_indoor

### 样本 1425: metro-paris-225-6798-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.795), Rail transport(0.685), Railroad car, train wagon(0.618)
- **音频特征**: RMS=0.0076, 频谱重心=1561Hz, 场景提示=quiet_indoor

### 样本 1426: public_square-paris-251-7516-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.152)
- **音频特征**: RMS=0.0043, 频谱重心=960Hz, 场景提示=quiet_indoor

### 样本 1427: shopping_mall-lyon-1043-42657-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.560), Clip-clop(0.325), Horse(0.323)
- **音频特征**: RMS=0.0046, 频谱重心=1498Hz, 场景提示=mixed_environment

### 样本 1428: street_pedestrian-helsinki-262-7948-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.282)
- **音频特征**: RMS=0.0062, 频谱重心=853Hz, 场景提示=quiet_indoor

### 样本 1429: bus-paris-33-1015-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.493), Speech(0.486), Field recording(0.120)
- **音频特征**: RMS=0.0290, 频谱重心=536Hz, 场景提示=mixed_environment

### 样本 1430: metro_station-lyon-1010-40838-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.722), Music(0.391)
- **音频特征**: RMS=0.0028, 频谱重心=1198Hz, 场景提示=quiet_indoor

### 样本 1431: shopping_mall-lisbon-1002-42988-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.136)
- **音频特征**: RMS=0.0022, 频谱重心=1233Hz, 场景提示=quiet_indoor

### 样本 1432: public_square-prague-1214-44552-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.620), Vehicle(0.418), Car(0.151)
- **音频特征**: RMS=0.0045, 频谱重心=999Hz, 场景提示=quiet_indoor

### 样本 1433: airport-london-5-224-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.578), Animal(0.108)
- **音频特征**: RMS=0.0016, 频谱重心=1383Hz, 场景提示=mixed_environment

### 样本 1434: metro-milan-1025-41558-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.728), Vehicle(0.313)
- **音频特征**: RMS=0.0091, 频谱重心=1219Hz, 场景提示=quiet_indoor

### 样本 1435: street_pedestrian-paris-265-8045-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Horse(0.557), Clip-clop(0.555), Animal(0.535)
- **音频特征**: RMS=0.0025, 频谱重心=1102Hz, 场景提示=quiet_indoor

### 样本 1436: bus-lyon-1073-43978-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.217), Music(0.127)
- **音频特征**: RMS=0.0107, 频谱重心=519Hz, 场景提示=mixed_environment

### 样本 1437: street_pedestrian-lyon-1072-44088-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.725), Basketball bounce(0.161), Thump, thud(0.116)
- **音频特征**: RMS=0.0017, 频谱重心=1359Hz, 场景提示=quiet_indoor

### 样本 1438: bus-lyon-1159-41089-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.811), Animal(0.190), Bird(0.171)
- **音频特征**: RMS=0.0062, 频谱重心=1488Hz, 场景提示=quiet_indoor

### 样本 1439: metro_station-barcelona-61-1835-a.wav
- **真实场景**: metro_station
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.137)
- **音频特征**: RMS=0.0022, 频谱重心=1629Hz, 场景提示=quiet_indoor

### 样本 1440: public_square-vienna-123-3654-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.344), Animal(0.260), Patter(0.181)
- **音频特征**: RMS=0.0012, 频谱重心=1481Hz, 场景提示=quiet_indoor

### 样本 1441: bus-stockholm-36-1083-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.868), Hubbub, speech noise, speech babble(0.213), Chatter(0.213)
- **音频特征**: RMS=0.0126, 频谱重心=1086Hz, 场景提示=mixed_environment

### 样本 1442: street_pedestrian-helsinki-147-4432-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.320), Vehicle(0.169)
- **音频特征**: RMS=0.0039, 频谱重心=689Hz, 场景提示=quiet_indoor

### 样本 1443: public_square-prague-1075-42472-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.844), Animal(0.224), Clip-clop(0.142)
- **音频特征**: RMS=0.0015, 频谱重心=1363Hz, 场景提示=quiet_indoor

### 样本 1444: metro_station-milan-1187-44677-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.775)
- **音频特征**: RMS=0.0059, 频谱重心=994Hz, 场景提示=quiet_indoor

### 样本 1445: public_square-prague-1027-42405-a.wav
- **真实场景**: public_square
- **AE预测**: metro
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.232)
- **音频特征**: RMS=0.0133, 频谱重心=761Hz, 场景提示=mixed_environment

### 样本 1446: metro-lisbon-1055-43172-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.819), Vehicle(0.317), Train(0.128)
- **音频特征**: RMS=0.0170, 频谱重心=824Hz, 场景提示=mixed_environment

### 样本 1447: public_square-paris-251-7522-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.225)
- **音频特征**: RMS=0.0031, 频谱重心=894Hz, 场景提示=quiet_indoor

### 样本 1448: metro_station-prague-1019-40540-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.778), Music(0.139), Clip-clop(0.124)
- **音频特征**: RMS=0.0024, 频谱重心=1205Hz, 场景提示=quiet_indoor

### 样本 1449: shopping_mall-milan-1183-44759-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Music(0.568), Speech(0.286), Clip-clop(0.218)
- **音频特征**: RMS=0.0038, 频谱重心=1352Hz, 场景提示=quiet_indoor

### 样本 1450: public_square-paris-117-3425-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.407), Vehicle(0.287), Animal(0.165)
- **音频特征**: RMS=0.0052, 频谱重心=1036Hz, 场景提示=quiet_indoor

### 样本 1451: shopping_mall-stockholm-137-4154-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.651), Clip-clop(0.128), Horse(0.101)
- **音频特征**: RMS=0.0037, 频谱重心=1152Hz, 场景提示=quiet_indoor

### 样本 1452: airport-lisbon-1175-44210-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Animal(0.181), Clip-clop(0.160), Speech(0.153)
- **音频特征**: RMS=0.0040, 频谱重心=1709Hz, 场景提示=mixed_environment

### 样本 1453: shopping_mall-paris-132-3968-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.549), Animal(0.178), Clip-clop(0.128)
- **音频特征**: RMS=0.0023, 频谱重心=1242Hz, 场景提示=quiet_indoor

### 样本 1454: street_pedestrian-stockholm-155-4695-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.815), Vehicle(0.179), Run(0.147)
- **音频特征**: RMS=0.0061, 频谱重心=885Hz, 场景提示=quiet_indoor

### 样本 1455: street_pedestrian-barcelona-260-7894-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.736), Vehicle(0.129)
- **音频特征**: RMS=0.0045, 频谱重心=1954Hz, 场景提示=mixed_environment

### 样本 1456: metro_station-prague-1170-44983-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.808), Animal(0.129)
- **音频特征**: RMS=0.0097, 频谱重心=903Hz, 场景提示=quiet_indoor

### 样本 1457: metro_station-barcelona-229-6891-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.415), Train(0.225), Railroad car, train wagon(0.151)
- **音频特征**: RMS=0.0195, 频谱重心=926Hz, 场景提示=mixed_environment

### 样本 1458: metro-stockholm-227-6844-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.837), Vehicle(0.119), Male speech, man speaking(0.112)
- **音频特征**: RMS=0.0098, 频谱重心=935Hz, 场景提示=quiet_indoor

### 样本 1459: tram-barcelona-179-5554-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.532), Train(0.322), Vehicle(0.256)
- **音频特征**: RMS=0.0113, 频谱重心=677Hz, 场景提示=mixed_environment

### 样本 1460: metro_station-paris-79-2149-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.749), Animal(0.229), Clip-clop(0.216)
- **音频特征**: RMS=0.0023, 频谱重心=1421Hz, 场景提示=quiet_indoor

### 样本 1461: shopping_mall-vienna-139-4220-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.301), Vehicle(0.104)
- **音频特征**: RMS=0.0033, 频谱重心=1385Hz, 场景提示=mixed_environment

### 样本 1462: street_pedestrian-vienna-159-4841-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.817), Clip-clop(0.160), Animal(0.120)
- **音频特征**: RMS=0.0013, 频谱重心=1453Hz, 场景提示=mixed_environment

### 样本 1463: tram-prague-1109-41845-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.377), Animal(0.129), Mouse(0.125)
- **音频特征**: RMS=0.0171, 频谱重心=730Hz, 场景提示=mixed_environment

### 样本 1464: street_pedestrian-prague-1037-42868-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.859)
- **音频特征**: RMS=0.0075, 频谱重心=1378Hz, 场景提示=mixed_environment

### 样本 1465: metro_station-barcelona-61-1831-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.361), Vehicle(0.133), Animal(0.117)
- **音频特征**: RMS=0.0019, 频谱重心=1397Hz, 场景提示=quiet_indoor

### 样本 1466: tram-stockholm-283-8556-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.728), Vehicle(0.329), Rumble(0.167)
- **音频特征**: RMS=0.0291, 频谱重心=293Hz, 场景提示=mixed_environment

### 样本 1467: bus-milan-1154-41107-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.521), Car(0.215), Rumble(0.105)
- **音频特征**: RMS=0.0349, 频谱重心=971Hz, 场景提示=mixed_environment

### 样本 1468: metro-barcelona-220-6643-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.797), Vehicle(0.279)
- **音频特征**: RMS=0.0201, 频谱重心=926Hz, 场景提示=mixed_environment

### 样本 1469: metro_station-stockholm-239-7088-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.714), Speech(0.650), Rail transport(0.541)
- **音频特征**: RMS=0.0198, 频谱重心=1318Hz, 场景提示=mixed_environment

### 样本 1470: bus-barcelona-15-619-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.387), Train(0.130)
- **音频特征**: RMS=0.0241, 频谱重心=452Hz, 场景提示=mixed_environment

### 样本 1471: bus-stockholm-36-1080-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.864), Vehicle(0.108), Animal(0.100)
- **音频特征**: RMS=0.0093, 频谱重心=1437Hz, 场景提示=quiet_indoor

### 样本 1472: tram-helsinki-276-8432-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.604), Vehicle(0.410)
- **音频特征**: RMS=0.0142, 频谱重心=741Hz, 场景提示=mixed_environment

### 样本 1473: metro-milan-1143-43882-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.541), Vehicle(0.464), Train(0.138)
- **音频特征**: RMS=0.0204, 频谱重心=528Hz, 场景提示=mixed_environment

### 样本 1474: public_square-milan-1074-43232-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.783), Run(0.240), Outside, urban or manmade(0.133)
- **音频特征**: RMS=0.0032, 频谱重心=1253Hz, 场景提示=quiet_indoor

### 样本 1475: public_square-vienna-123-3633-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **音频特征**: RMS=0.0013, 频谱重心=1240Hz, 场景提示=quiet_indoor

### 样本 1476: metro-lyon-1139-42060-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Speech(0.610), Vehicle(0.509), Aircraft(0.141)
- **音频特征**: RMS=0.0089, 频谱重心=907Hz, 场景提示=quiet_indoor

### 样本 1477: street_pedestrian-helsinki-262-7938-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Animal(0.353), Music(0.333), Clip-clop(0.299)
- **音频特征**: RMS=0.0067, 频谱重心=767Hz, 场景提示=quiet_indoor

### 样本 1478: bus-milan-1078-43958-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.355)
- **音频特征**: RMS=0.0082, 频谱重心=1081Hz, 场景提示=quiet_indoor

### 样本 1479: tram-london-279-8477-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.512), Train(0.132), Vehicle(0.102)
- **音频特征**: RMS=0.0089, 频谱重心=690Hz, 场景提示=quiet_indoor

### 样本 1480: airport-paris-7-342-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.494)
- **音频特征**: RMS=0.0029, 频谱重心=1195Hz, 场景提示=quiet_indoor

### 样本 1481: shopping_mall-lyon-1066-43835-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.149), Animal(0.102)
- **音频特征**: RMS=0.0018, 频谱重心=1515Hz, 场景提示=mixed_environment

### 样本 1482: street_traffic-vienna-176-5440-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.212), Train(0.109)
- **音频特征**: RMS=0.0033, 频谱重心=1153Hz, 场景提示=quiet_indoor

### 样本 1483: metro_station-helsinki-64-1924-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.436), Vehicle(0.103)
- **音频特征**: RMS=0.0056, 频谱重心=723Hz, 场景提示=quiet_indoor

### 样本 1484: metro_station-milan-1127-42202-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.784), Vehicle(0.356), Car(0.123)
- **音频特征**: RMS=0.0126, 频谱重心=1185Hz, 场景提示=mixed_environment

### 样本 1485: shopping_mall-lyon-1196-44888-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.698), Clip-clop(0.601), Horse(0.541)
- **音频特征**: RMS=0.0020, 频谱重心=1523Hz, 场景提示=mixed_environment

### 样本 1486: shopping_mall-lisbon-1002-40192-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Silence(0.150), Speech(0.102)
- **音频特征**: RMS=0.0021, 频谱重心=1048Hz, 场景提示=quiet_indoor

### 样本 1487: metro_station-vienna-86-2356-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.787), Children playing(0.709), Child speech, kid speaking(0.300)
- **音频特征**: RMS=0.0157, 频谱重心=754Hz, 场景提示=mixed_environment

### 样本 1488: street_pedestrian-helsinki-146-4406-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.776), Music(0.356), Clip-clop(0.316)
- **音频特征**: RMS=0.0041, 频谱重心=1145Hz, 场景提示=quiet_indoor

### 样本 1489: shopping_mall-stockholm-136-4121-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.676)
- **音频特征**: RMS=0.0031, 频谱重心=1055Hz, 场景提示=quiet_indoor

### 样本 1490: tram-milan-1134-41334-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.504), Mechanisms(0.344), Creak(0.203)
- **音频特征**: RMS=0.0295, 频谱重心=773Hz, 场景提示=mixed_environment

### 样本 1491: public_square-milan-1074-41663-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.875), Clip-clop(0.237), Animal(0.225)
- **音频特征**: RMS=0.0033, 频谱重心=1220Hz, 场景提示=mixed_environment

### 样本 1492: metro-barcelona-41-1262-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.811), Vehicle(0.510), Car(0.172)
- **音频特征**: RMS=0.0082, 频谱重心=817Hz, 场景提示=quiet_indoor

### 样本 1493: street_pedestrian-stockholm-157-4754-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.755), Animal(0.342), Clip-clop(0.201)
- **音频特征**: RMS=0.0044, 频谱重心=1703Hz, 场景提示=quiet_indoor

### 样本 1494: metro_station-lyon-1028-42154-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.675), Music(0.233)
- **音频特征**: RMS=0.0047, 频谱重心=914Hz, 场景提示=quiet_indoor

### 样本 1495: public_square-milan-1044-40885-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.836), Animal(0.132), Clip-clop(0.128)
- **音频特征**: RMS=0.0034, 频谱重心=1008Hz, 场景提示=quiet_indoor

### 样本 1496: metro_station-helsinki-64-1926-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.130), Animal(0.128), Speech(0.124)
- **音频特征**: RMS=0.0042, 频谱重心=978Hz, 场景提示=quiet_indoor

### 样本 1497: airport-paris-206-6260-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.509), Vehicle(0.156), Animal(0.117)
- **音频特征**: RMS=0.0080, 频谱重心=1088Hz, 场景提示=quiet_indoor

### 样本 1498: shopping_mall-helsinki-128-3829-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.352), Vehicle(0.110)
- **音频特征**: RMS=0.0026, 频谱重心=1263Hz, 场景提示=quiet_indoor

### 样本 1499: airport-london-205-6226-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Vehicle(0.215), Clip-clop(0.122), Animal(0.106)
- **音频特征**: RMS=0.0013, 频谱重心=1661Hz, 场景提示=mixed_environment

### 样本 1500: shopping_mall-lisbon-1176-44623-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.248), Speech(0.133), Train(0.113)
- **音频特征**: RMS=0.0058, 频谱重心=1057Hz, 场景提示=quiet_indoor

### 样本 1501: shopping_mall-helsinki-130-3906-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.740)
- **音频特征**: RMS=0.0040, 频谱重心=1166Hz, 场景提示=quiet_indoor

### 样本 1502: tram-helsinki-183-5701-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.668), Field recording(0.283), Train(0.213)
- **音频特征**: RMS=0.0680, 频谱重心=314Hz, 场景提示=mixed_environment

### 样本 1503: shopping_mall-paris-134-4066-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.467), Animal(0.382), Horse(0.337)
- **音频特征**: RMS=0.0018, 频谱重心=1129Hz, 场景提示=quiet_indoor

### 样本 1504: public_square-lyon-1024-40487-a.wav
- **真实场景**: public_square
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.403), Silence(0.138)
- **音频特征**: RMS=0.0012, 频谱重心=1013Hz, 场景提示=quiet_indoor

### 样本 1505: bus-stockholm-37-1101-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.629), Bird(0.517), Pigeon, dove(0.485)
- **音频特征**: RMS=0.0094, 频谱重心=983Hz, 场景提示=quiet_indoor

### 样本 1506: tram-london-190-5836-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.687), Vehicle(0.358), Emergency vehicle(0.224)
- **音频特征**: RMS=0.0110, 频谱重心=792Hz, 场景提示=mixed_environment

### 样本 1507: street_pedestrian-helsinki-262-7927-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Vehicle(0.185), Speech(0.127)
- **音频特征**: RMS=0.0036, 频谱重心=1026Hz, 场景提示=quiet_indoor

### 样本 1508: street_traffic-paris-171-5244-a.wav
- **真实场景**: street_traffic
- **AE预测**: bus
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.584), Car(0.290)
- **音频特征**: RMS=0.0059, 频谱重心=831Hz, 场景提示=quiet_indoor

### 样本 1509: metro_station-lyon-1167-45465-a.wav
- **真实场景**: metro_station
- **AE预测**: tram
- **AS预测**: public_square
- **检测到的事件**: Music(0.624), Speech(0.368), Vehicle(0.169)
- **音频特征**: RMS=0.0056, 频谱重心=689Hz, 场景提示=quiet_indoor

### 样本 1510: street_pedestrian-prague-1051-43251-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.904), Run(0.350), Outside, urban or manmade(0.270)
- **音频特征**: RMS=0.0048, 频谱重心=1411Hz, 场景提示=mixed_environment

### 样本 1511: shopping_mall-stockholm-136-4108-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Inside, small room(0.106), Speech(0.104)
- **音频特征**: RMS=0.0056, 频谱重心=1040Hz, 场景提示=quiet_indoor

### 样本 1512: public_square-london-113-3291-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.726), Animal(0.249), Clip-clop(0.233)
- **音频特征**: RMS=0.0019, 频谱重心=958Hz, 场景提示=quiet_indoor

### 样本 1513: tram-london-189-5823-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.830), Vehicle(0.583), Rumble(0.242)
- **音频特征**: RMS=0.0379, 频谱重心=484Hz, 场景提示=mixed_environment

### 样本 1514: street_pedestrian-lisbon-1004-43967-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.846), Clip-clop(0.255), Horse(0.226)
- **音频特征**: RMS=0.0026, 频谱重心=1174Hz, 场景提示=quiet_indoor

### 样本 1515: metro-stockholm-227-6836-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.860), Music(0.653)
- **音频特征**: RMS=0.0099, 频谱重心=864Hz, 场景提示=quiet_indoor

### 样本 1516: metro_station-stockholm-239-7090-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.811), Music(0.396)
- **音频特征**: RMS=0.0120, 频谱重心=1440Hz, 场景提示=mixed_environment

### 样本 1517: public_square-vienna-123-3635-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.853), Run(0.258), Clip-clop(0.230)
- **音频特征**: RMS=0.0022, 频谱重心=1373Hz, 场景提示=quiet_indoor

### 样本 1518: bus-barcelona-210-6400-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.798), Vehicle(0.609), Music(0.488)
- **音频特征**: RMS=0.0451, 频谱重心=451Hz, 场景提示=mixed_environment

### 样本 1519: shopping_mall-prague-1009-43429-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.542)
- **音频特征**: RMS=0.0063, 频谱重心=1268Hz, 场景提示=mixed_environment

### 样本 1520: tram-lisbon-1046-43523-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.749), Vehicle(0.643), Train(0.259)
- **音频特征**: RMS=0.0740, 频谱重心=522Hz, 场景提示=mixed_environment

### 样本 1521: airport-vienna-14-564-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.526), Mouse(0.142), Music(0.141)
- **音频特征**: RMS=0.0011, 频谱重心=1887Hz, 场景提示=mixed_environment

### 样本 1522: shopping_mall-paris-132-3967-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.862)
- **音频特征**: RMS=0.0034, 频谱重心=1636Hz, 场景提示=mixed_environment

### 样本 1523: street_pedestrian-lisbon-1098-42261-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.634), Vehicle(0.109)
- **音频特征**: RMS=0.0031, 频谱重心=1021Hz, 场景提示=quiet_indoor

### 样本 1524: public_square-prague-1192-45558-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **音频特征**: RMS=0.0035, 频谱重心=935Hz, 场景提示=quiet_indoor

### 样本 1525: metro_station-stockholm-83-2228-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Train(0.447), Vehicle(0.352), Speech(0.343)
- **音频特征**: RMS=0.0070, 频谱重心=1486Hz, 场景提示=mixed_environment

### 样本 1526: airport-london-6-283-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.628)
- **音频特征**: RMS=0.0019, 频谱重心=1253Hz, 场景提示=quiet_indoor

### 样本 1527: street_pedestrian-lisbon-1004-42477-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.689), Arrow(0.169)
- **音频特征**: RMS=0.0027, 频谱重心=1193Hz, 场景提示=quiet_indoor

### 样本 1528: airport-paris-206-6275-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.164)
- **音频特征**: RMS=0.0091, 频谱重心=1044Hz, 场景提示=quiet_indoor

### 样本 1529: street_traffic-london-270-8214-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.729), Vehicle(0.198)
- **音频特征**: RMS=0.0040, 频谱重心=1765Hz, 场景提示=mixed_environment

### 样本 1530: metro_station-barcelona-63-1894-a.wav
- **真实场景**: metro_station
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.490), Train(0.122), Car(0.101)
- **音频特征**: RMS=0.0397, 频谱重心=1024Hz, 场景提示=mixed_environment

### 样本 1531: airport-vienna-13-545-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: airport
- **检测到的事件**: Speech(0.693), Boat, Water vehicle(0.347), Rowboat, canoe, kayak(0.256)
- **音频特征**: RMS=0.0017, 频谱重心=1480Hz, 场景提示=mixed_environment

### 样本 1532: metro_station-lisbon-1021-42913-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.715), Vehicle(0.268), Outside, urban or manmade(0.125)
- **音频特征**: RMS=0.0097, 频谱重心=1017Hz, 场景提示=quiet_indoor

### 样本 1533: shopping_mall-prague-1009-40930-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.325)
- **音频特征**: RMS=0.0058, 频谱重心=1846Hz, 场景提示=mixed_environment

### 样本 1534: tram-vienna-285-8624-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Sliding door(0.249), Vehicle(0.199), Door(0.180)
- **音频特征**: RMS=0.0052, 频谱重心=931Hz, 场景提示=quiet_indoor

### 样本 1535: metro-lyon-1079-43199-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.718), Vehicle(0.543), Car(0.132)
- **音频特征**: RMS=0.0110, 频谱重心=1056Hz, 场景提示=mixed_environment

### 样本 1536: airport-vienna-13-541-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.736), Clip-clop(0.184), Animal(0.161)
- **音频特征**: RMS=0.0015, 频谱重心=1583Hz, 场景提示=mixed_environment

### 样本 1537: public_square-lyon-1178-44232-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Honk(0.641), Goose(0.581), Fowl(0.356)
- **音频特征**: RMS=0.0017, 频谱重心=1165Hz, 场景提示=quiet_indoor

### 样本 1538: street_pedestrian-milan-1080-41800-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Rain(0.196), Rain on surface(0.178), Raindrop(0.125)
- **音频特征**: RMS=0.0015, 频谱重心=2444Hz, 场景提示=mixed_environment

### 样本 1539: metro_station-lyon-1077-42520-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.679), Vehicle(0.105)
- **音频特征**: RMS=0.0045, 频谱重心=843Hz, 场景提示=quiet_indoor

### 样本 1540: tram-prague-1184-44355-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.559), Train(0.179), Field recording(0.161)
- **音频特征**: RMS=0.0200, 频谱重心=720Hz, 场景提示=mixed_environment

### 样本 1541: public_square-lyon-1178-44752-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.720), Horse(0.552), Clip-clop(0.528)
- **音频特征**: RMS=0.0013, 频谱重心=1209Hz, 场景提示=quiet_indoor

### 样本 1542: airport-vienna-209-6371-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.668), Music(0.184), Clip-clop(0.179)
- **音频特征**: RMS=0.0015, 频谱重心=1484Hz, 场景提示=quiet_indoor

### 样本 1543: street_traffic-vienna-274-8358-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.752), Animal(0.207), Clip-clop(0.128)
- **音频特征**: RMS=0.0034, 频谱重心=1654Hz, 场景提示=quiet_indoor

### 样本 1544: bus-milan-1190-45491-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.778), Vehicle(0.326), Train(0.120)
- **音频特征**: RMS=0.0206, 频谱重心=789Hz, 场景提示=mixed_environment

### 样本 1545: street_pedestrian-prague-1051-40272-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.880), Clip-clop(0.313), Animal(0.256)
- **音频特征**: RMS=0.0044, 频谱重心=1359Hz, 场景提示=mixed_environment

### 样本 1546: shopping_mall-stockholm-137-4174-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.830), Animal(0.162), Clip-clop(0.162)
- **音频特征**: RMS=0.0076, 频谱重心=1038Hz, 场景提示=quiet_indoor

### 样本 1547: street_pedestrian-milan-1205-45325-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.717)
- **音频特征**: RMS=0.0023, 频谱重心=930Hz, 场景提示=quiet_indoor

### 样本 1548: street_pedestrian-london-151-4581-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.768), Clip-clop(0.440), Horse(0.358)
- **音频特征**: RMS=0.0011, 频谱重心=1578Hz, 场景提示=quiet_indoor

### 样本 1549: shopping_mall-vienna-140-4276-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.430), Music(0.147)
- **音频特征**: RMS=0.0014, 频谱重心=1378Hz, 场景提示=mixed_environment

### 样本 1550: park-lisbon-1198-45301-a.wav
- **真实场景**: park
- **AE预测**: street_pedestrian
- **AS预测**: park
- **检测到的事件**: Speech(0.177), Silence(0.147)
- **音频特征**: RMS=0.0023, 频谱重心=748Hz, 场景提示=quiet_indoor

### 样本 1551: metro-barcelona-220-6645-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.746), Vehicle(0.450), Train(0.102)
- **音频特征**: RMS=0.0162, 频谱重心=979Hz, 场景提示=mixed_environment

### 样本 1552: street_pedestrian-paris-265-8047-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.552), Pigeon, dove(0.255), Bird(0.254)
- **音频特征**: RMS=0.0017, 频谱重心=1528Hz, 场景提示=quiet_indoor

### 样本 1553: tram-vienna-202-6114-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.499), Vehicle(0.380), Power windows, electric windows(0.199)
- **音频特征**: RMS=0.0046, 频谱重心=1131Hz, 场景提示=quiet_indoor

### 样本 1554: airport-stockholm-10-420-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.852), Animal(0.219), Clip-clop(0.188)
- **音频特征**: RMS=0.0042, 频谱重心=1034Hz, 场景提示=quiet_indoor

### 样本 1555: metro_station-milan-1187-44654-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro
- **检测到的事件**: Speech(0.788), Music(0.784), Television(0.120)
- **音频特征**: RMS=0.0086, 频谱重心=917Hz, 场景提示=quiet_indoor

### 样本 1556: park-barcelona-91-2529-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.338), Duck(0.235), Bird(0.216)
- **音频特征**: RMS=0.0025, 频谱重心=1820Hz, 场景提示=mixed_environment

### 样本 1557: metro-lyon-1126-43833-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.552), Vehicle(0.491), Rail transport(0.336)
- **音频特征**: RMS=0.0258, 频谱重心=935Hz, 场景提示=mixed_environment

### 样本 1558: tram-barcelona-179-5529-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.692), Vehicle(0.268)
- **音频特征**: RMS=0.0117, 频谱重心=737Hz, 场景提示=mixed_environment

### 样本 1559: metro_station-helsinki-231-6951-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.636), Animal(0.124)
- **音频特征**: RMS=0.0029, 频谱重心=1281Hz, 场景提示=quiet_indoor

### 样本 1560: airport-prague-1034-43125-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.767), Basketball bounce(0.101)
- **音频特征**: RMS=0.0087, 频谱重心=1536Hz, 场景提示=mixed_environment

### 样本 1561: metro-prague-1157-41299-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.521), Vehicle(0.171), Mouse(0.170)
- **音频特征**: RMS=0.0111, 频谱重心=899Hz, 场景提示=mixed_environment

### 样本 1562: public_square-london-115-3373-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.852), Animal(0.194), Horse(0.183)
- **音频特征**: RMS=0.0024, 频谱重心=1105Hz, 场景提示=quiet_indoor

### 样本 1563: street_pedestrian-stockholm-266-8074-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.759), Clip-clop(0.159), Animal(0.158)
- **音频特征**: RMS=0.0038, 频谱重心=1244Hz, 场景提示=quiet_indoor

### 样本 1564: public_square-lyon-1024-43906-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.738), Vehicle(0.146), Silence(0.110)
- **音频特征**: RMS=0.0021, 频谱重心=964Hz, 场景提示=quiet_indoor

### 样本 1565: metro_station-lyon-1167-45751-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.862), Music(0.171), Outside, urban or manmade(0.110)
- **音频特征**: RMS=0.0051, 频谱重心=999Hz, 场景提示=quiet_indoor

### 样本 1566: tram-london-278-8459-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.720), Vehicle(0.505), Train(0.184)
- **音频特征**: RMS=0.0155, 频谱重心=718Hz, 场景提示=mixed_environment

### 样本 1567: metro_station-vienna-88-2405-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.265), Train(0.170)
- **音频特征**: RMS=0.0112, 频谱重心=616Hz, 场景提示=mixed_environment

### 样本 1568: tram-paris-192-5857-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.388)
- **音频特征**: RMS=0.0110, 频谱重心=558Hz, 场景提示=mixed_environment

### 样本 1569: street_pedestrian-vienna-160-4865-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.810), Vehicle(0.215), Bicycle(0.158)
- **音频特征**: RMS=0.0025, 频谱重心=1232Hz, 场景提示=quiet_indoor

### 样本 1570: street_traffic-london-169-5180-a.wav
- **真实场景**: street_traffic
- **AE预测**: metro_station
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.217), Train(0.146), Speech(0.108)
- **音频特征**: RMS=0.0098, 频谱重心=1250Hz, 场景提示=quiet_indoor

### 样本 1571: airport-stockholm-207-6299-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: airport
- **检测到的事件**: Speech(0.751), Animal(0.304), Goat(0.251)
- **音频特征**: RMS=0.0038, 频谱重心=1703Hz, 场景提示=mixed_environment

### 样本 1572: tram-london-278-8470-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.752), Music(0.164), Vehicle(0.134)
- **音频特征**: RMS=0.0100, 频谱重心=1034Hz, 场景提示=mixed_environment

### 样本 1573: metro-lisbon-1119-41220-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.601), Vehicle(0.353), Train(0.162)
- **音频特征**: RMS=0.0112, 频谱重心=796Hz, 场景提示=mixed_environment

### 样本 1574: airport-lisbon-1122-43393-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.355), Animal(0.255), Vehicle(0.198)
- **音频特征**: RMS=0.0047, 频谱重心=1240Hz, 场景提示=quiet_indoor

### 样本 1575: shopping_mall-lisbon-1125-44006-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.390), Music(0.232)
- **音频特征**: RMS=0.0038, 频谱重心=1100Hz, 场景提示=quiet_indoor

### 样本 1576: airport-lyon-1101-41703-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.379)
- **音频特征**: RMS=0.0024, 频谱重心=1300Hz, 场景提示=quiet_indoor

### 样本 1577: street_pedestrian-barcelona-260-7896-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.760), Clip-clop(0.276), Horse(0.230)
- **音频特征**: RMS=0.0019, 频谱重心=1597Hz, 场景提示=mixed_environment

### 样本 1578: public_square-lyon-1178-45363-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.750), Animal(0.144)
- **音频特征**: RMS=0.0021, 频谱重心=1106Hz, 场景提示=quiet_indoor

### 样本 1579: park-lyon-1144-40825-a.wav
- **真实场景**: park
- **AE预测**: street_pedestrian
- **AS预测**: park
- **检测到的事件**: Speech(0.730), Animal(0.115)
- **音频特征**: RMS=0.0008, 频谱重心=1148Hz, 场景提示=quiet_indoor

### 样本 1580: tram-prague-1042-42881-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Pigeon, dove(0.450), Bird(0.385), Speech(0.268)
- **音频特征**: RMS=0.0054, 频谱重心=1323Hz, 场景提示=quiet_indoor

### 样本 1581: metro_station-prague-1019-43970-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.829), Clip-clop(0.318), Horse(0.255)
- **音频特征**: RMS=0.0025, 频谱重心=1421Hz, 场景提示=quiet_indoor

### 样本 1582: metro_station-lyon-1010-42360-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: tram
- **检测到的事件**: Speech(0.826), Music(0.379), Male speech, man speaking(0.114)
- **音频特征**: RMS=0.0032, 频谱重心=1289Hz, 场景提示=quiet_indoor

### 样本 1583: street_pedestrian-vienna-267-8131-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.276), Vehicle(0.111)
- **音频特征**: RMS=0.0038, 频谱重心=975Hz, 场景提示=quiet_indoor

### 样本 1584: airport-paris-7-332-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.518)
- **音频特征**: RMS=0.0026, 频谱重心=1423Hz, 场景提示=mixed_environment

### 样本 1585: street_pedestrian-helsinki-148-4464-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Silence(0.147)
- **音频特征**: RMS=0.0016, 频谱重心=1061Hz, 场景提示=quiet_indoor

### 样本 1586: shopping_mall-paris-257-7800-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.681), Animal(0.434), Clip-clop(0.399)
- **音频特征**: RMS=0.0023, 频谱重心=1554Hz, 场景提示=mixed_environment

### 样本 1587: tram-prague-1161-43834-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.670), Vehicle(0.534), Train(0.287)
- **音频特征**: RMS=0.0600, 频谱重心=361Hz, 场景提示=mixed_environment

### 样本 1588: metro_station-helsinki-232-6985-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.492), Music(0.127), Vehicle(0.124)
- **音频特征**: RMS=0.0046, 频谱重心=755Hz, 场景提示=quiet_indoor

### 样本 1589: shopping_mall-vienna-139-4234-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.227), Vehicle(0.110)
- **音频特征**: RMS=0.0021, 频谱重心=1662Hz, 场景提示=mixed_environment

### 样本 1590: metro-helsinki-221-6684-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.603), Vehicle(0.341), Sliding door(0.210)
- **音频特征**: RMS=0.0191, 频谱重心=545Hz, 场景提示=mixed_environment

### 样本 1591: street_pedestrian-prague-1037-43129-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.661)
- **音频特征**: RMS=0.0022, 频谱重心=1384Hz, 场景提示=mixed_environment

### 样本 1592: metro_station-lyon-1167-44615-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.883), Chatter(0.168), Outside, urban or manmade(0.150)
- **音频特征**: RMS=0.0055, 频谱重心=1331Hz, 场景提示=quiet_indoor

### 样本 1593: street_pedestrian-lyon-1047-43302-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.754), Clip-clop(0.171), Animal(0.150)
- **音频特征**: RMS=0.0019, 频谱重心=1201Hz, 场景提示=quiet_indoor

### 样本 1594: public_square-stockholm-252-7548-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.142), Animal(0.122), Vehicle(0.116)
- **音频特征**: RMS=0.0022, 频谱重心=1051Hz, 场景提示=quiet_indoor

### 样本 1595: shopping_mall-paris-257-7795-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.743), Clip-clop(0.197), Music(0.170)
- **音频特征**: RMS=0.0033, 频谱重心=1350Hz, 场景提示=mixed_environment

### 样本 1596: airport-stockholm-10-435-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.510), Animal(0.120)
- **音频特征**: RMS=0.0014, 频谱重心=1539Hz, 场景提示=quiet_indoor

### 样本 1597: tram-helsinki-276-8404-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.576), Speech(0.431), Car(0.190)
- **音频特征**: RMS=0.0344, 频谱重心=625Hz, 场景提示=mixed_environment

### 样本 1598: airport-helsinki-4-174-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.756), Clip-clop(0.319), Horse(0.220)
- **音频特征**: RMS=0.0020, 频谱重心=1269Hz, 场景提示=quiet_indoor

### 样本 1599: street_pedestrian-london-151-4580-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Animal(0.384), Speech(0.316), Clip-clop(0.290)
- **音频特征**: RMS=0.0014, 频谱重心=1189Hz, 场景提示=quiet_indoor

### 样本 1600: bus-lyon-1159-41285-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.854), Bleat(0.291), Animal(0.288)
- **音频特征**: RMS=0.0080, 频谱重心=919Hz, 场景提示=quiet_indoor

### 样本 1601: bus-prague-1120-42683-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.679), Vehicle(0.575), Car(0.249)
- **音频特征**: RMS=0.0206, 频谱重心=682Hz, 场景提示=mixed_environment

### 样本 1602: tram-stockholm-197-5936-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.776), Music(0.251), Vehicle(0.228)
- **音频特征**: RMS=0.0414, 频谱重心=416Hz, 场景提示=mixed_environment

### 样本 1603: metro-vienna-58-1736-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.437), Animal(0.142)
- **音频特征**: RMS=0.0054, 频谱重心=1352Hz, 场景提示=quiet_indoor

### 样本 1604: bus-vienna-219-6623-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.430), Creak(0.192), Vehicle(0.161)
- **音频特征**: RMS=0.0141, 频谱重心=408Hz, 场景提示=mixed_environment

### 样本 1605: bus-prague-1120-42543-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.580), Vehicle(0.475), Train(0.337)
- **音频特征**: RMS=0.0234, 频谱重心=823Hz, 场景提示=mixed_environment

### 样本 1606: street_traffic-london-168-5132-a.wav
- **真实场景**: street_traffic
- **AE预测**: bus
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.506), Speech(0.258), Animal(0.129)
- **音频特征**: RMS=0.0124, 频谱重心=1057Hz, 场景提示=mixed_environment

### 样本 1607: street_pedestrian-paris-265-8044-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Inside, small room(0.126)
- **音频特征**: RMS=0.0015, 频谱重心=1768Hz, 场景提示=quiet_indoor

### 样本 1608: airport-stockholm-12-491-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.226), Music(0.173), Engine(0.110)
- **音频特征**: RMS=0.0050, 频谱重心=1676Hz, 场景提示=mixed_environment

### 样本 1609: shopping_mall-milan-1084-40845-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.598), Clip-clop(0.361), Animal(0.336)
- **音频特征**: RMS=0.0023, 频谱重心=1737Hz, 场景提示=mixed_environment

### 样本 1610: public_square-stockholm-119-3485-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Clip-clop(0.486), Horse(0.444), Animal(0.378)
- **音频特征**: RMS=0.0070, 频谱重心=1105Hz, 场景提示=quiet_indoor

### 样本 1611: tram-paris-280-8496-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.783), Animal(0.295), Cat(0.294)
- **音频特征**: RMS=0.0082, 频谱重心=737Hz, 场景提示=quiet_indoor

### 样本 1612: metro_station-prague-1130-42687-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.826), Clip-clop(0.202), Horse(0.156)
- **音频特征**: RMS=0.0031, 频谱重心=1331Hz, 场景提示=quiet_indoor

### 样本 1613: shopping_mall-helsinki-130-3885-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.797), Chatter(0.315)
- **音频特征**: RMS=0.0064, 频谱重心=1057Hz, 场景提示=quiet_indoor

### 样本 1614: street_pedestrian-vienna-267-8118-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.177)
- **音频特征**: RMS=0.0035, 频谱重心=843Hz, 场景提示=quiet_indoor

### 样本 1615: shopping_mall-helsinki-129-3870-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.766), Clip-clop(0.149), Animal(0.148)
- **音频特征**: RMS=0.0044, 频谱重心=1077Hz, 场景提示=quiet_indoor

### 样本 1616: street_pedestrian-lisbon-1174-44665-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.756), Outside, urban or manmade(0.120), Vehicle(0.103)
- **音频特征**: RMS=0.0029, 频谱重心=1118Hz, 场景提示=quiet_indoor

### 样本 1617: street_pedestrian-lyon-1162-45745-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.495)
- **音频特征**: RMS=0.0016, 频谱重心=1234Hz, 场景提示=quiet_indoor

### 样本 1618: public_square-london-113-3269-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.839), Run(0.214), Clip-clop(0.201)
- **音频特征**: RMS=0.0028, 频谱重心=1249Hz, 场景提示=quiet_indoor

### 样本 1619: street_pedestrian-vienna-160-4900-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.638), Clip-clop(0.262), Horse(0.225)
- **音频特征**: RMS=0.0029, 频谱重心=1229Hz, 场景提示=quiet_indoor

### 样本 1620: metro_station-vienna-240-7148-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.746), Animal(0.127)
- **音频特征**: RMS=0.0037, 频谱重心=747Hz, 场景提示=quiet_indoor

### 样本 1621: bus-milan-1154-43213-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.515), Speech(0.485), Car(0.126)
- **音频特征**: RMS=0.0164, 频谱重心=1343Hz, 场景提示=mixed_environment

### 样本 1622: street_pedestrian-stockholm-155-4709-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.810), Clip-clop(0.300), Animal(0.268)
- **音频特征**: RMS=0.0067, 频谱重心=970Hz, 场景提示=quiet_indoor

### 样本 1623: shopping_mall-vienna-139-4217-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.483), Vehicle(0.226)
- **音频特征**: RMS=0.0031, 频谱重心=1332Hz, 场景提示=mixed_environment

### 样本 1624: public_square-vienna-124-3673-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.749), Animal(0.166), Clip-clop(0.134)
- **音频特征**: RMS=0.0014, 频谱重心=1198Hz, 场景提示=quiet_indoor

### 样本 1625: shopping_mall-london-131-3947-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Mouse(0.318), Speech(0.238), Animal(0.132)
- **音频特征**: RMS=0.0018, 频谱重心=1216Hz, 场景提示=quiet_indoor

### 样本 1626: metro-lyon-1139-42319-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.699), Music(0.168)
- **音频特征**: RMS=0.0085, 频谱重心=1164Hz, 场景提示=quiet_indoor

### 样本 1627: shopping_mall-stockholm-258-7833-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.855), Clip-clop(0.256), Animal(0.193)
- **音频特征**: RMS=0.0026, 频谱重心=1341Hz, 场景提示=mixed_environment

### 样本 1628: shopping_mall-stockholm-136-4122-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.262)
- **音频特征**: RMS=0.0051, 频谱重心=1033Hz, 场景提示=quiet_indoor

### 样本 1629: shopping_mall-helsinki-129-3874-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.887), Animal(0.188), Clip-clop(0.139)
- **音频特征**: RMS=0.0085, 频谱重心=1155Hz, 场景提示=quiet_indoor

### 样本 1630: public_square-lyon-1024-42305-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.180), Writing(0.141), Inside, small room(0.111)
- **音频特征**: RMS=0.0024, 频谱重心=828Hz, 场景提示=quiet_indoor

### 样本 1631: airport-helsinki-3-164-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.852), Children playing(0.183), Animal(0.158)
- **音频特征**: RMS=0.0025, 频谱重心=1022Hz, 场景提示=quiet_indoor

### 样本 1632: airport-lyon-1041-43878-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.732), Narration, monologue(0.104)
- **音频特征**: RMS=0.0031, 频谱重心=1106Hz, 场景提示=quiet_indoor

### 样本 1633: metro_station-milan-1117-41828-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.848), Clip-clop(0.164), Horse(0.135)
- **音频特征**: RMS=0.0063, 频谱重心=1030Hz, 场景提示=quiet_indoor

### 样本 1634: tram-lisbon-1200-45641-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.772), Vehicle(0.747), Power windows, electric windows(0.395)
- **音频特征**: RMS=0.0095, 频谱重心=945Hz, 场景提示=quiet_indoor

### 样本 1635: tram-paris-280-8500-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.812), Cat(0.699), Domestic animals, pets(0.656)
- **音频特征**: RMS=0.0077, 频谱重心=696Hz, 场景提示=quiet_indoor

### 样本 1636: street_pedestrian-lyon-1003-42656-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.718), Arrow(0.492)
- **音频特征**: RMS=0.0017, 频谱重心=1163Hz, 场景提示=quiet_indoor

### 样本 1637: airport-lisbon-1122-42212-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.258), Speech(0.177), Cricket(0.146)
- **音频特征**: RMS=0.0044, 频谱重心=1576Hz, 场景提示=mixed_environment

### 样本 1638: airport-london-5-226-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.740), Animal(0.207), Mouse(0.177)
- **音频特征**: RMS=0.0013, 频谱重心=1479Hz, 场景提示=mixed_environment

### 样本 1639: metro-vienna-60-1815-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.616), Vehicle(0.332), Train(0.246)
- **音频特征**: RMS=0.0342, 频谱重心=449Hz, 场景提示=mixed_environment

### 样本 1640: metro_station-prague-1170-45481-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.388), Music(0.205)
- **音频特征**: RMS=0.0058, 频谱重心=923Hz, 场景提示=quiet_indoor

### 样本 1641: metro-helsinki-222-6732-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.780), Vehicle(0.585), Bus(0.122)
- **音频特征**: RMS=0.0222, 频谱重心=586Hz, 场景提示=mixed_environment

### 样本 1642: bus-milan-1083-40804-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.741), Vehicle(0.416)
- **音频特征**: RMS=0.0237, 频谱重心=778Hz, 场景提示=mixed_environment

### 样本 1643: metro_station-lyon-1077-40718-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.816), Chatter(0.119), Music(0.116)
- **音频特征**: RMS=0.0051, 频谱重心=1082Hz, 场景提示=quiet_indoor

### 样本 1644: shopping_mall-vienna-139-4245-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.500)
- **音频特征**: RMS=0.0033, 频谱重心=1361Hz, 场景提示=mixed_environment

### 样本 1645: street_pedestrian-prague-1085-41206-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.452), Vehicle(0.285), Boat, Water vehicle(0.262)
- **音频特征**: RMS=0.0020, 频谱重心=1068Hz, 场景提示=quiet_indoor

### 样本 1646: street_pedestrian-helsinki-147-4458-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.814), Vehicle(0.211), Outside, urban or manmade(0.105)
- **音频特征**: RMS=0.0052, 频谱重心=920Hz, 场景提示=quiet_indoor

### 样本 1647: metro-lyon-1064-42253-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.220), Sliding door(0.190), Pigeon, dove(0.186)
- **音频特征**: RMS=0.0079, 频谱重心=913Hz, 场景提示=quiet_indoor

### 样本 1648: shopping_mall-paris-132-3963-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.729), Animal(0.160)
- **音频特征**: RMS=0.0033, 频谱重心=1460Hz, 场景提示=quiet_indoor

### 样本 1649: street_pedestrian-lisbon-1099-40926-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.875), Outside, urban or manmade(0.132), Hubbub, speech noise, speech babble(0.116)
- **音频特征**: RMS=0.0037, 频谱重心=1377Hz, 场景提示=quiet_indoor

### 样本 1650: public_square-vienna-122-3592-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.834), Clip-clop(0.129), Outside, urban or manmade(0.125)
- **音频特征**: RMS=0.0009, 频谱重心=1260Hz, 场景提示=quiet_indoor

### 样本 1651: tram-prague-1135-43933-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.764), Vehicle(0.329), Music(0.124)
- **音频特征**: RMS=0.0143, 频谱重心=826Hz, 场景提示=mixed_environment

### 样本 1652: tram-barcelona-179-5539-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.528), Vehicle(0.303), Train(0.141)
- **音频特征**: RMS=0.0107, 频谱重心=648Hz, 场景提示=mixed_environment

### 样本 1653: bus-paris-29-962-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.416), Vehicle(0.359), Train(0.109)
- **音频特征**: RMS=0.0155, 频谱重心=573Hz, 场景提示=mixed_environment

### 样本 1654: shopping_mall-london-256-7728-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.593), Clip-clop(0.217), Animal(0.179)
- **音频特征**: RMS=0.0019, 频谱重心=1315Hz, 场景提示=mixed_environment

### 样本 1655: shopping_mall-milan-1049-40236-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.784), Basketball bounce(0.136)
- **音频特征**: RMS=0.0038, 频谱重心=1482Hz, 场景提示=mixed_environment

### 样本 1656: public_square-milan-1044-40061-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.851), Run(0.220), Animal(0.177)
- **音频特征**: RMS=0.0040, 频谱重心=953Hz, 场景提示=quiet_indoor

### 样本 1657: street_pedestrian-paris-265-8068-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.730), Animal(0.199), Clip-clop(0.137)
- **音频特征**: RMS=0.0013, 频谱重心=1760Hz, 场景提示=mixed_environment

### 样本 1658: street_pedestrian-lisbon-1004-41607-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.540)
- **音频特征**: RMS=0.0017, 频谱重心=1226Hz, 场景提示=quiet_indoor

### 样本 1659: metro_station-paris-77-2124-a.wav
- **真实场景**: metro_station
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.462), Train(0.423), Rail transport(0.257)
- **音频特征**: RMS=0.0091, 频谱重心=762Hz, 场景提示=quiet_indoor

### 样本 1660: shopping_mall-prague-1031-40669-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.141), Silence(0.113)
- **音频特征**: RMS=0.0051, 频谱重心=689Hz, 场景提示=quiet_indoor

### 样本 1661: metro-prague-1054-41491-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.730), Music(0.215), Vehicle(0.139)
- **音频特征**: RMS=0.0108, 频谱重心=956Hz, 场景提示=mixed_environment

### 样本 1662: metro_station-barcelona-230-6935-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.378), Vehicle(0.181)
- **音频特征**: RMS=0.0062, 频谱重心=1348Hz, 场景提示=quiet_indoor

### 样本 1663: street_pedestrian-london-149-4510-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: metro_station
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.593), Vehicle(0.432)
- **音频特征**: RMS=0.0068, 频谱重心=668Hz, 场景提示=quiet_indoor

### 样本 1664: shopping_mall-london-131-3930-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.614), Mechanisms(0.103)
- **音频特征**: RMS=0.0017, 频谱重心=1707Hz, 场景提示=mixed_environment

### 样本 1665: metro_station-lyon-1077-40816-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.725), Vehicle(0.146)
- **音频特征**: RMS=0.0063, 频谱重心=898Hz, 场景提示=quiet_indoor

### 样本 1666: street_pedestrian-london-149-4511-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.823), Animal(0.249), Clip-clop(0.243)
- **音频特征**: RMS=0.0017, 频谱重心=1174Hz, 场景提示=quiet_indoor

### 样本 1667: tram-milan-1048-41788-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Sliding door(0.300), Vehicle(0.209), Door(0.186)
- **音频特征**: RMS=0.0128, 频谱重心=881Hz, 场景提示=mixed_environment

### 样本 1668: public_square-vienna-122-3625-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.615), Animal(0.237), Clip-clop(0.220)
- **音频特征**: RMS=0.0009, 频谱重心=1066Hz, 场景提示=quiet_indoor

### 样本 1669: metro-prague-1054-43223-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.720), Vehicle(0.165)
- **音频特征**: RMS=0.0066, 频谱重心=883Hz, 场景提示=quiet_indoor

### 样本 1670: metro_station-paris-82-2210-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.262), Speech(0.218), Sliding door(0.163)
- **音频特征**: RMS=0.0097, 频谱重心=2053Hz, 场景提示=mixed_environment

### 样本 1671: park-london-243-7257-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.699), Animal(0.579), Horse(0.324)
- **音频特征**: RMS=0.0026, 频谱重心=784Hz, 场景提示=quiet_indoor

### 样本 1672: metro-stockholm-227-6831-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.780), Animal(0.192), Vehicle(0.189)
- **音频特征**: RMS=0.0071, 频谱重心=1124Hz, 场景提示=quiet_indoor

### 样本 1673: street_pedestrian-lisbon-1098-41902-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.743), Vehicle(0.243)
- **音频特征**: RMS=0.0033, 频谱重心=1218Hz, 场景提示=quiet_indoor

### 样本 1674: airport-milan-1172-44215-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Horse(0.485), Clip-clop(0.479), Speech(0.391)
- **音频特征**: RMS=0.0031, 频谱重心=1466Hz, 场景提示=mixed_environment

### 样本 1675: street_pedestrian-paris-265-8053-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Animal(0.313), Speech(0.201), Clip-clop(0.164)
- **音频特征**: RMS=0.0010, 频谱重心=1823Hz, 场景提示=quiet_indoor

### 样本 1676: bus-milan-1180-45318-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.231)
- **音频特征**: RMS=0.0265, 频谱重心=912Hz, 场景提示=mixed_environment

### 样本 1677: street_pedestrian-stockholm-266-8092-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.473), Idling(0.153), Engine(0.129)
- **音频特征**: RMS=0.0064, 频谱重心=1391Hz, 场景提示=quiet_indoor

### 样本 1678: tram-stockholm-199-5992-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.724), Vehicle(0.539), Sliding door(0.263)
- **音频特征**: RMS=0.0149, 频谱重心=607Hz, 场景提示=mixed_environment

### 样本 1679: metro_station-london-69-2035-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.888)
- **音频特征**: RMS=0.0022, 频谱重心=1849Hz, 场景提示=mixed_environment

### 样本 1680: street_pedestrian-milan-1005-43673-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.734), Horse(0.539), Neigh, whinny(0.490)
- **音频特征**: RMS=0.0023, 频谱重心=1369Hz, 场景提示=mixed_environment

### 样本 1681: public_square-paris-118-3482-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.736), Clip-clop(0.227), Run(0.211)
- **音频特征**: RMS=0.0031, 频谱重心=1412Hz, 场景提示=quiet_indoor

### 样本 1682: bus-lisbon-1156-42486-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.727), Vehicle(0.551), Bus(0.171)
- **音频特征**: RMS=0.0283, 频谱重心=759Hz, 场景提示=mixed_environment

### 样本 1683: shopping_mall-london-256-7770-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.563), Animal(0.433), Cat(0.309)
- **音频特征**: RMS=0.0033, 频谱重心=1831Hz, 场景提示=mixed_environment

### 样本 1684: bus-lyon-1129-42724-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.716), Vehicle(0.496), Bus(0.125)
- **音频特征**: RMS=0.0123, 频谱重心=555Hz, 场景提示=mixed_environment

### 样本 1685: metro_station-paris-238-7065-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.594), Train(0.418), Vehicle(0.341)
- **音频特征**: RMS=0.0102, 频谱重心=1516Hz, 场景提示=mixed_environment

### 样本 1686: street_pedestrian-lyon-1047-41650-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.693), Animal(0.309), Clip-clop(0.274)
- **音频特征**: RMS=0.0027, 频谱重心=1277Hz, 场景提示=quiet_indoor

### 样本 1687: shopping_mall-helsinki-129-3865-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **音频特征**: RMS=0.0025, 频谱重心=1760Hz, 场景提示=mixed_environment

### 样本 1688: tram-barcelona-181-5619-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.920), Chatter(0.213), Male speech, man speaking(0.114)
- **音频特征**: RMS=0.0122, 频谱重心=1090Hz, 场景提示=mixed_environment

### 样本 1689: street_pedestrian-prague-1051-42510-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.809), Clip-clop(0.118), Animal(0.108)
- **音频特征**: RMS=0.0068, 频谱重心=857Hz, 场景提示=quiet_indoor

### 样本 1690: tram-london-278-8464-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.796), Music(0.276), Vehicle(0.157)
- **音频特征**: RMS=0.0092, 频谱重心=1040Hz, 场景提示=quiet_indoor

### 样本 1691: shopping_mall-helsinki-130-3910-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.646), Music(0.159), Animal(0.148)
- **音频特征**: RMS=0.0013, 频谱重心=2048Hz, 场景提示=mixed_environment

### 样本 1692: street_traffic-london-167-5129-a.wav
- **真实场景**: street_traffic
- **AE预测**: bus
- **AS预测**: public_square
- **检测到的事件**: Speech(0.720), Vehicle(0.208), Animal(0.183)
- **音频特征**: RMS=0.0094, 频谱重心=1172Hz, 场景提示=quiet_indoor

### 样本 1693: street_pedestrian-vienna-160-4873-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.778), Clip-clop(0.357), Animal(0.343)
- **音频特征**: RMS=0.0024, 频谱重心=1288Hz, 场景提示=quiet_indoor

### 样本 1694: street_pedestrian-london-263-7981-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.447), Animal(0.108), Vehicle(0.105)
- **音频特征**: RMS=0.0019, 频谱重心=1471Hz, 场景提示=quiet_indoor

### 样本 1695: street_pedestrian-lisbon-1099-40523-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.832), Vehicle(0.199), Outside, urban or manmade(0.103)
- **音频特征**: RMS=0.0034, 频谱重心=1257Hz, 场景提示=quiet_indoor

### 样本 1696: shopping_mall-stockholm-258-7847-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.779), Music(0.164), Chatter(0.131)
- **音频特征**: RMS=0.0048, 频谱重心=1373Hz, 场景提示=mixed_environment

### 样本 1697: street_pedestrian-milan-1080-43286-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Rain(0.168), Rain on surface(0.132), Vehicle(0.108)
- **音频特征**: RMS=0.0018, 频谱重心=2307Hz, 场景提示=mixed_environment

### 样本 1698: bus-lyon-1186-45046-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.785), Vehicle(0.314), Music(0.147)
- **音频特征**: RMS=0.0232, 频谱重心=609Hz, 场景提示=mixed_environment

### 样本 1699: metro_station-barcelona-229-6897-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.675)
- **音频特征**: RMS=0.0025, 频谱重心=911Hz, 场景提示=quiet_indoor

### 样本 1700: metro-barcelona-42-1271-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.248)
- **音频特征**: RMS=0.0096, 频谱重心=791Hz, 场景提示=quiet_indoor

### 样本 1701: airport-paris-7-352-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.802), Animal(0.449), Cat(0.339)
- **音频特征**: RMS=0.0053, 频谱重心=1267Hz, 场景提示=quiet_indoor

### 样本 1702: shopping_mall-helsinki-129-3860-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.598), Animal(0.211), Vehicle(0.164)
- **音频特征**: RMS=0.0041, 频谱重心=1031Hz, 场景提示=quiet_indoor

### 样本 1703: airport-helsinki-4-184-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Music(0.233), Run(0.227), Vehicle(0.167)
- **音频特征**: RMS=0.0020, 频谱重心=1708Hz, 场景提示=mixed_environment

### 样本 1704: street_traffic-helsinki-269-8187-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.360), Boat, Water vehicle(0.119)
- **音频特征**: RMS=0.0089, 频谱重心=634Hz, 场景提示=quiet_indoor

### 样本 1705: metro_station-london-235-7014-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.766), Narration, monologue(0.223), Female speech, woman speaking(0.156)
- **音频特征**: RMS=0.0141, 频谱重心=1198Hz, 场景提示=mixed_environment

### 样本 1706: airport-vienna-14-583-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.874), Female speech, woman speaking(0.626), Narration, monologue(0.502)
- **音频特征**: RMS=0.0059, 频谱重心=1961Hz, 场景提示=mixed_environment

### 样本 1707: metro_station-lisbon-1007-40011-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.782), Animal(0.224), Clip-clop(0.123)
- **音频特征**: RMS=0.0036, 频谱重心=871Hz, 场景提示=quiet_indoor

### 样本 1708: metro-london-48-1461-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.722), Vehicle(0.455), Car(0.137)
- **音频特征**: RMS=0.0073, 频谱重心=961Hz, 场景提示=quiet_indoor

### 样本 1709: street_pedestrian-prague-1203-44208-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.806), Clip-clop(0.248), Horse(0.174)
- **音频特征**: RMS=0.0018, 频谱重心=1576Hz, 场景提示=mixed_environment

### 样本 1710: airport-stockholm-11-477-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.886), Clip-clop(0.341), Run(0.279)
- **音频特征**: RMS=0.0046, 频谱重心=1129Hz, 场景提示=quiet_indoor

### 样本 1711: metro-barcelona-220-6642-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.748), Vehicle(0.207), Animal(0.161)
- **音频特征**: RMS=0.0049, 频谱重心=1550Hz, 场景提示=mixed_environment

### 样本 1712: metro-paris-49-1505-a.wav
- **真实场景**: metro
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Train(0.913), Train wheels squealing(0.888), Rail transport(0.874)
- **音频特征**: RMS=0.0337, 频谱重心=960Hz, 场景提示=mixed_environment

### 样本 1713: bus-lisbon-1223-45244-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.562), Air brake(0.205), Truck(0.107)
- **音频特征**: RMS=0.0157, 频谱重心=608Hz, 场景提示=mixed_environment

### 样本 1714: street_pedestrian-stockholm-157-4760-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.593), Animal(0.204), Bird(0.119)
- **音频特征**: RMS=0.0024, 频谱重心=1886Hz, 场景提示=mixed_environment

### 样本 1715: metro-lisbon-1199-45637-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.273), Speech(0.248)
- **音频特征**: RMS=0.0086, 频谱重心=1070Hz, 场景提示=quiet_indoor

### 样本 1716: airport-prague-1069-40583-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.729), Animal(0.229), Mouse(0.212)
- **音频特征**: RMS=0.0022, 频谱重心=1370Hz, 场景提示=quiet_indoor

### 样本 1717: street_pedestrian-prague-1037-41988-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.864), Clip-clop(0.181), Outside, urban or manmade(0.171)
- **音频特征**: RMS=0.0026, 频谱重心=1535Hz, 场景提示=mixed_environment

### 样本 1718: street_pedestrian-lyon-1072-41081-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.817), Clip-clop(0.147), Animal(0.114)
- **音频特征**: RMS=0.0018, 频谱重心=1579Hz, 场景提示=mixed_environment

### 样本 1719: tram-prague-1088-40204-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.331), Train(0.130)
- **音频特征**: RMS=0.0169, 频谱重心=725Hz, 场景提示=mixed_environment

### 样本 1720: street_pedestrian-barcelona-144-4363-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.767), Animal(0.238), Horse(0.164)
- **音频特征**: RMS=0.0022, 频谱重心=1380Hz, 场景提示=mixed_environment

### 样本 1721: public_square-paris-118-3481-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Animal(0.474), Clip-clop(0.355), Speech(0.333)
- **音频特征**: RMS=0.0017, 频谱重心=1203Hz, 场景提示=quiet_indoor

### 样本 1722: airport-lisbon-1114-40219-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.744), Vehicle(0.160), Animal(0.101)
- **音频特征**: RMS=0.0072, 频谱重心=1502Hz, 场景提示=quiet_indoor

### 样本 1723: street_pedestrian-milan-1096-43580-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.865), Clip-clop(0.357), Horse(0.272)
- **音频特征**: RMS=0.0026, 频谱重心=1356Hz, 场景提示=mixed_environment

### 样本 1724: shopping_mall-stockholm-135-4092-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.893), Horse(0.596), Clip-clop(0.509)
- **音频特征**: RMS=0.0101, 频谱重心=1095Hz, 场景提示=mixed_environment

### 样本 1725: street_traffic-london-270-8218-a.wav
- **真实场景**: street_traffic
- **AE预测**: metro
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.806), Vehicle(0.375)
- **音频特征**: RMS=0.0063, 频谱重心=1376Hz, 场景提示=quiet_indoor

### 样本 1726: street_pedestrian-lisbon-1098-43986-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.821), Clip-clop(0.207), Horse(0.181)
- **音频特征**: RMS=0.0026, 频谱重心=1468Hz, 场景提示=mixed_environment

### 样本 1727: street_pedestrian-prague-1037-41296-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.861), Vehicle(0.162), Outside, urban or manmade(0.150)
- **音频特征**: RMS=0.0079, 频谱重心=1349Hz, 场景提示=mixed_environment

### 样本 1728: street_pedestrian-lyon-1003-41711-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.371), Snake(0.159)
- **音频特征**: RMS=0.0017, 频谱重心=1822Hz, 场景提示=mixed_environment

### 样本 1729: shopping_mall-prague-1031-41364-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: park
- **音频特征**: RMS=0.0043, 频谱重心=666Hz, 场景提示=quiet_indoor

### 样本 1730: metro_station-stockholm-83-2236-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.837), Clip-clop(0.599), Horse(0.494)
- **音频特征**: RMS=0.0054, 频谱重心=981Hz, 场景提示=quiet_indoor

### 样本 1731: shopping_mall-stockholm-137-4140-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: public_square
- **检测到的事件**: Speech(0.535), Clip-clop(0.462), Horse(0.420)
- **音频特征**: RMS=0.0087, 频谱重心=927Hz, 场景提示=quiet_indoor

### 样本 1732: airport-barcelona-1-60-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.691), Animal(0.125)
- **音频特征**: RMS=0.0044, 频谱重心=1095Hz, 场景提示=quiet_indoor

### 样本 1733: street_pedestrian-london-151-4570-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.195), Inside, small room(0.139), Walk, footsteps(0.108)
- **音频特征**: RMS=0.0012, 频谱重心=1060Hz, 场景提示=quiet_indoor

### 样本 1734: park-paris-244-7280-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.302), Animal(0.107)
- **音频特征**: RMS=0.0025, 频谱重心=682Hz, 场景提示=quiet_indoor

### 样本 1735: shopping_mall-stockholm-136-4126-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.766), Vehicle(0.126), Animal(0.126)
- **音频特征**: RMS=0.0032, 频谱重心=1106Hz, 场景提示=quiet_indoor

### 样本 1736: public_square-london-113-3281-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.865), Clip-clop(0.664), Horse(0.628)
- **音频特征**: RMS=0.0037, 频谱重心=1128Hz, 场景提示=quiet_indoor

### 样本 1737: street_pedestrian-lisbon-1099-41591-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.840), Outside, urban or manmade(0.131), Run(0.117)
- **音频特征**: RMS=0.0038, 频谱重心=1231Hz, 场景提示=quiet_indoor

### 样本 1738: street_pedestrian-prague-1085-40983-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.729), Clip-clop(0.329), Horse(0.273)
- **音频特征**: RMS=0.0019, 频谱重心=1232Hz, 场景提示=quiet_indoor

### 样本 1739: public_square-vienna-123-3632-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.862), Run(0.155), Outside, urban or manmade(0.148)
- **音频特征**: RMS=0.0025, 频谱重心=1582Hz, 场景提示=mixed_environment

### 样本 1740: metro_station-london-68-2022-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.760), Animal(0.221), Domestic animals, pets(0.143)
- **音频特征**: RMS=0.0029, 频谱重心=1720Hz, 场景提示=mixed_environment

### 样本 1741: metro_station-london-234-7010-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Silence(0.110), Vehicle(0.107)
- **音频特征**: RMS=0.0041, 频谱重心=1267Hz, 场景提示=quiet_indoor

### 样本 1742: bus-prague-1147-43420-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.617), Vehicle(0.556), Train(0.275)
- **音频特征**: RMS=0.0216, 频谱重心=1387Hz, 场景提示=mixed_environment

### 样本 1743: bus-stockholm-217-6568-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.307), Music(0.120)
- **音频特征**: RMS=0.0170, 频谱重心=542Hz, 场景提示=mixed_environment

### 样本 1744: street_pedestrian-lisbon-1174-45511-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.749), Vehicle(0.190), Animal(0.113)
- **音频特征**: RMS=0.0034, 频谱重心=1123Hz, 场景提示=quiet_indoor

### 样本 1745: tram-vienna-201-6070-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.803), Vehicle(0.116)
- **音频特征**: RMS=0.0055, 频谱重心=1589Hz, 场景提示=quiet_indoor

### 样本 1746: street_pedestrian-barcelona-261-7925-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.610), Music(0.248), Vehicle(0.213)
- **音频特征**: RMS=0.0039, 频谱重心=1170Hz, 场景提示=quiet_indoor

### 样本 1747: shopping_mall-paris-257-7804-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.715), Animal(0.479), Bow-wow(0.411)
- **音频特征**: RMS=0.0025, 频谱重心=1592Hz, 场景提示=mixed_environment

### 样本 1748: metro-milan-1141-40569-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.725), Vehicle(0.111)
- **音频特征**: RMS=0.0088, 频谱重心=1298Hz, 场景提示=quiet_indoor

### 样本 1749: public_square-milan-1168-45716-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.671), Vehicle(0.239), Fire(0.186)
- **音频特征**: RMS=0.0034, 频谱重心=2808Hz, 场景提示=mixed_environment

### 样本 1750: public_square-lyon-1024-40074-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.522), Vehicle(0.212), Animal(0.132)
- **音频特征**: RMS=0.0023, 频谱重心=709Hz, 场景提示=quiet_indoor

### 样本 1751: metro_station-london-75-2101-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.775), Narration, monologue(0.277), Male speech, man speaking(0.259)
- **音频特征**: RMS=0.0078, 频谱重心=1202Hz, 场景提示=quiet_indoor

### 样本 1752: metro_station-vienna-86-2329-a.wav
- **真实场景**: metro_station
- **AE预测**: tram
- **AS预测**: park
- **检测到的事件**: Silence(0.155), Vehicle(0.133)
- **音频特征**: RMS=0.0095, 频谱重心=411Hz, 场景提示=quiet_indoor

### 样本 1753: tram-london-279-8489-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.495), Train(0.180), Aircraft(0.111)
- **音频特征**: RMS=0.0128, 频谱重心=493Hz, 场景提示=mixed_environment

### 样本 1754: airport-barcelona-1-31-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.722)
- **音频特征**: RMS=0.0038, 频谱重心=1374Hz, 场景提示=quiet_indoor

### 样本 1755: metro-vienna-60-1821-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.345), Music(0.144), Car(0.101)
- **音频特征**: RMS=0.0296, 频谱重心=310Hz, 场景提示=mixed_environment

### 样本 1756: airport-milan-1108-42936-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.845), Bow-wow(0.746), Dog(0.712)
- **音频特征**: RMS=0.0027, 频谱重心=1436Hz, 场景提示=mixed_environment

### 样本 1757: metro-prague-1213-45179-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.595), Vehicle(0.483), Train(0.264)
- **音频特征**: RMS=0.0215, 频谱重心=1034Hz, 场景提示=mixed_environment

### 样本 1758: public_square-lyon-1024-40028-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.406), Silence(0.183), Vehicle(0.165)
- **音频特征**: RMS=0.0019, 频谱重心=1070Hz, 场景提示=quiet_indoor

### 样本 1759: metro-helsinki-221-6699-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.505), Field recording(0.192), Ship(0.123)
- **音频特征**: RMS=0.0615, 频谱重心=470Hz, 场景提示=mixed_environment

### 样本 1760: tram-helsinki-184-5712-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Silence(0.118)
- **音频特征**: RMS=0.0082, 频谱重心=596Hz, 场景提示=quiet_indoor

### 样本 1761: street_pedestrian-paris-154-4659-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.620), Run(0.219), Clip-clop(0.195)
- **音频特征**: RMS=0.0015, 频谱重心=1416Hz, 场景提示=quiet_indoor

### 样本 1762: public_square-vienna-122-3616-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.365), Animal(0.238), Silence(0.121)
- **音频特征**: RMS=0.0010, 频谱重心=975Hz, 场景提示=quiet_indoor

### 样本 1763: metro_station-vienna-86-2341-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: park
- **检测到的事件**: Vehicle(0.321), Speech(0.289)
- **音频特征**: RMS=0.0086, 频谱重心=448Hz, 场景提示=quiet_indoor

### 样本 1764: tram-stockholm-284-8597-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.752), Vehicle(0.360), Bus(0.112)
- **音频特征**: RMS=0.0141, 频谱重心=715Hz, 场景提示=mixed_environment

### 样本 1765: airport-prague-1034-43157-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.713), Music(0.114), Animal(0.111)
- **音频特征**: RMS=0.0078, 频谱重心=1611Hz, 场景提示=mixed_environment

### 样本 1766: bus-paris-30-968-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.489)
- **音频特征**: RMS=0.0076, 频谱重心=1261Hz, 场景提示=quiet_indoor

### 样本 1767: tram-lisbon-1131-42888-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.726), Vehicle(0.706), Car(0.332)
- **音频特征**: RMS=0.0921, 频谱重心=521Hz, 场景提示=mixed_environment

### 样本 1768: airport-vienna-13-535-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.739), Clip-clop(0.527), Horse(0.405)
- **音频特征**: RMS=0.0017, 频谱重心=1314Hz, 场景提示=quiet_indoor

### 样本 1769: airport-helsinki-4-186-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Animal(0.243), Keys jangling(0.138), Clip-clop(0.131)
- **音频特征**: RMS=0.0038, 频谱重心=1346Hz, 场景提示=quiet_indoor

### 样本 1770: tram-prague-1086-43438-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.260), Music(0.152)
- **音频特征**: RMS=0.0105, 频谱重心=590Hz, 场景提示=mixed_environment

### 样本 1771: airport-lyon-1041-42942-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Snort(0.112), Speech(0.106)
- **音频特征**: RMS=0.0019, 频谱重心=1004Hz, 场景提示=quiet_indoor

### 样本 1772: park-prague-1185-44666-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Vehicle(0.303)
- **音频特征**: RMS=0.0102, 频谱重心=571Hz, 场景提示=mixed_environment

### 样本 1773: shopping_mall-helsinki-255-7660-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.788)
- **音频特征**: RMS=0.0058, 频谱重心=1191Hz, 场景提示=quiet_indoor

### 样本 1774: airport-paris-9-407-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.659), Music(0.395)
- **音频特征**: RMS=0.0046, 频谱重心=1020Hz, 场景提示=quiet_indoor

### 样本 1775: street_pedestrian-prague-1037-41211-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.862), Run(0.282), Outside, urban or manmade(0.184)
- **音频特征**: RMS=0.0027, 频谱重心=1586Hz, 场景提示=mixed_environment

### 样本 1776: public_square-prague-1075-40404-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.679), Horse(0.629), Animal(0.563)
- **音频特征**: RMS=0.0026, 频谱重心=1025Hz, 场景提示=quiet_indoor

### 样本 1777: airport-prague-1069-41871-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.765), Animal(0.208)
- **音频特征**: RMS=0.0029, 频谱重心=1513Hz, 场景提示=mixed_environment

### 样本 1778: street_pedestrian-lyon-1162-44194-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.614), Animal(0.358), Clip-clop(0.347)
- **音频特征**: RMS=0.0015, 频谱重心=1249Hz, 场景提示=quiet_indoor

### 样本 1779: metro_station-vienna-88-2410-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.331), Vehicle(0.241), Reversing beeps(0.239)
- **音频特征**: RMS=0.0053, 频谱重心=1505Hz, 场景提示=mixed_environment

### 样本 1780: airport-paris-7-314-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.827), Clip-clop(0.363), Horse(0.342)
- **音频特征**: RMS=0.0023, 频谱重心=1375Hz, 场景提示=mixed_environment

### 样本 1781: street_pedestrian-helsinki-148-4475-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.679)
- **音频特征**: RMS=0.0015, 频谱重心=1434Hz, 场景提示=quiet_indoor

### 样本 1782: tram-lyon-1093-40872-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.719), Music(0.169), Vehicle(0.158)
- **音频特征**: RMS=0.0050, 频谱重心=1531Hz, 场景提示=quiet_indoor

### 样本 1783: airport-lyon-1095-43489-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.567), Music(0.198)
- **音频特征**: RMS=0.0018, 频谱重心=1322Hz, 场景提示=quiet_indoor

### 样本 1784: tram-lisbon-1100-40473-a.wav
- **真实场景**: tram
- **AE预测**: street_traffic
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.739), Air brake(0.483), Speech(0.367)
- **音频特征**: RMS=0.0181, 频谱重心=1453Hz, 场景提示=mixed_environment

### 样本 1785: street_pedestrian-lyon-1072-42426-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.416), Animal(0.113)
- **音频特征**: RMS=0.0019, 频谱重心=1170Hz, 场景提示=quiet_indoor

### 样本 1786: metro_station-lisbon-1221-44313-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: tram
- **检测到的事件**: Speech(0.773), Mouse(0.142), Animal(0.103)
- **音频特征**: RMS=0.0038, 频谱重心=1140Hz, 场景提示=quiet_indoor

### 样本 1787: street_pedestrian-helsinki-146-4413-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.850), Clip-clop(0.535), Horse(0.493)
- **音频特征**: RMS=0.0049, 频谱重心=1076Hz, 场景提示=quiet_indoor

### 样本 1788: metro-lyon-1082-42541-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.827), Vehicle(0.411), Music(0.271)
- **音频特征**: RMS=0.0085, 频谱重心=1017Hz, 场景提示=quiet_indoor

### 样本 1789: public_square-paris-118-3456-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.105), Animal(0.102)
- **音频特征**: RMS=0.0016, 频谱重心=1647Hz, 场景提示=mixed_environment

### 样本 1790: airport-lyon-1169-45672-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.804), Run(0.581), Clip-clop(0.258)
- **音频特征**: RMS=0.0023, 频谱重心=1351Hz, 场景提示=mixed_environment

### 样本 1791: bus-barcelona-210-6409-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.787), Car(0.482), Rumble(0.278)
- **音频特征**: RMS=0.0963, 频谱重心=345Hz, 场景提示=mixed_environment

### 样本 1792: metro_station-vienna-86-2337-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.854), Children playing(0.584), Child speech, kid speaking(0.172)
- **音频特征**: RMS=0.0018, 频谱重心=1710Hz, 场景提示=mixed_environment

### 样本 1793: airport-prague-1034-42685-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.731), Clip-clop(0.220), Animal(0.169)
- **音频特征**: RMS=0.0076, 频谱重心=1466Hz, 场景提示=mixed_environment

### 样本 1794: metro-lyon-1201-45581-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.539), Animal(0.202), Quack(0.164)
- **音频特征**: RMS=0.0092, 频谱重心=860Hz, 场景提示=quiet_indoor

### 样本 1795: street_pedestrian-helsinki-147-4443-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: public_square
- **检测到的事件**: Music(0.508), Speech(0.133)
- **音频特征**: RMS=0.0040, 频谱重心=1023Hz, 场景提示=quiet_indoor

### 样本 1796: shopping_mall-stockholm-136-4123-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.642)
- **音频特征**: RMS=0.0033, 频谱重心=1157Hz, 场景提示=quiet_indoor

### 样本 1797: tram-lisbon-1100-42554-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.586), Train(0.564), Rail transport(0.475)
- **音频特征**: RMS=0.0284, 频谱重心=1117Hz, 场景提示=mixed_environment

### 样本 1798: public_square-stockholm-252-7554-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.211), Animal(0.156), Bird(0.127)
- **音频特征**: RMS=0.0017, 频谱重心=1154Hz, 场景提示=quiet_indoor

### 样本 1799: metro_station-prague-1118-40283-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Silence(0.211), Speech(0.150)
- **音频特征**: RMS=0.0028, 频谱重心=866Hz, 场景提示=quiet_indoor

### 样本 1800: bus-milan-1078-41458-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.755), Vehicle(0.624), Train(0.231)
- **音频特征**: RMS=0.0236, 频谱重心=813Hz, 场景提示=mixed_environment

### 样本 1801: public_square-stockholm-120-3540-a.wav
- **真实场景**: public_square
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.269), Train(0.131)
- **音频特征**: RMS=0.0088, 频谱重心=738Hz, 场景提示=quiet_indoor

### 样本 1802: airport-stockholm-11-462-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Animal(0.416), Horse(0.296), Clip-clop(0.260)
- **音频特征**: RMS=0.0041, 频谱重心=1113Hz, 场景提示=quiet_indoor

### 样本 1803: metro-lyon-1181-44269-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.764), Vehicle(0.334), Music(0.196)
- **音频特征**: RMS=0.0093, 频谱重心=1086Hz, 场景提示=quiet_indoor

### 样本 1804: public_square-prague-1152-40840-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.833), Vehicle(0.237), Boat, Water vehicle(0.179)
- **音频特征**: RMS=0.0022, 频谱重心=1408Hz, 场景提示=mixed_environment

### 样本 1805: bus-lyon-1073-42985-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.781), Vehicle(0.260), Mouse(0.123)
- **音频特征**: RMS=0.0196, 频谱重心=601Hz, 场景提示=mixed_environment

### 样本 1806: metro-prague-1157-41051-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.602), Train(0.588), Rail transport(0.383)
- **音频特征**: RMS=0.0160, 频谱重心=926Hz, 场景提示=mixed_environment

### 样本 1807: metro-paris-54-1594-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.888), Vehicle(0.275), Car(0.136)
- **音频特征**: RMS=0.0068, 频谱重心=867Hz, 场景提示=quiet_indoor

### 样本 1808: metro_station-lyon-1010-42321-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.772), Music(0.104)
- **音频特征**: RMS=0.0029, 频谱重心=1325Hz, 场景提示=quiet_indoor

### 样本 1809: public_square-paris-118-3454-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.692), Animal(0.248), Clip-clop(0.168)
- **音频特征**: RMS=0.0015, 频谱重心=1438Hz, 场景提示=quiet_indoor

### 样本 1810: street_pedestrian-prague-1051-43622-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.865), Clip-clop(0.162), Horse(0.125)
- **音频特征**: RMS=0.0045, 频谱重心=1272Hz, 场景提示=mixed_environment

### 样本 1811: tram-barcelona-179-5527-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.795), Door(0.190), Cupboard open or close(0.180)
- **音频特征**: RMS=0.0119, 频谱重心=1320Hz, 场景提示=mixed_environment

### 样本 1812: bus-prague-1215-45332-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.455), Music(0.206), Train(0.200)
- **音频特征**: RMS=0.0365, 频谱重心=442Hz, 场景提示=mixed_environment

### 样本 1813: metro-stockholm-57-1688-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.814), Inside, small room(0.132), Vehicle(0.117)
- **音频特征**: RMS=0.0090, 频谱重心=685Hz, 场景提示=quiet_indoor

### 样本 1814: metro-barcelona-220-6653-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.781), Vehicle(0.311)
- **音频特征**: RMS=0.0101, 频谱重心=1119Hz, 场景提示=mixed_environment

### 样本 1815: airport-milan-1172-44925-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.468), Clip-clop(0.256), Horse(0.232)
- **音频特征**: RMS=0.0030, 频谱重心=1428Hz, 场景提示=mixed_environment

### 样本 1816: shopping_mall-helsinki-130-3909-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.821), Music(0.296), Clip-clop(0.160)
- **音频特征**: RMS=0.0027, 频谱重心=1406Hz, 场景提示=mixed_environment

### 样本 1817: airport-milan-1172-44524-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.769), Clip-clop(0.510), Horse(0.427)
- **音频特征**: RMS=0.0031, 频谱重心=1414Hz, 场景提示=mixed_environment

### 样本 1818: metro-stockholm-57-1695-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.259), Sliding door(0.124)
- **音频特征**: RMS=0.0170, 频谱重心=458Hz, 场景提示=mixed_environment

### 样本 1819: street_traffic-stockholm-175-5396-a.wav
- **真实场景**: street_traffic
- **AE预测**: metro_station
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.699), Car(0.151), Aircraft(0.137)
- **音频特征**: RMS=0.0346, 频谱重心=1304Hz, 场景提示=mixed_environment

### 样本 1820: tram-barcelona-181-5599-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.854), Vehicle(0.304), Hubbub, speech noise, speech babble(0.109)
- **音频特征**: RMS=0.0139, 频谱重心=1242Hz, 场景提示=mixed_environment

### 样本 1821: street_traffic-london-167-5128-a.wav
- **真实场景**: street_traffic
- **AE预测**: bus
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.693), Vehicle(0.331), Animal(0.110)
- **音频特征**: RMS=0.0092, 频谱重心=1342Hz, 场景提示=quiet_indoor

### 样本 1822: metro_station-milan-1117-40314-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.693), Vehicle(0.163)
- **音频特征**: RMS=0.0073, 频谱重心=866Hz, 场景提示=quiet_indoor

### 样本 1823: public_square-paris-117-3438-a.wav
- **真实场景**: public_square
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.235), Speech(0.138)
- **音频特征**: RMS=0.0052, 频谱重心=1056Hz, 场景提示=quiet_indoor

### 样本 1824: tram-helsinki-182-5661-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.508), Train(0.208), Field recording(0.202)
- **音频特征**: RMS=0.0272, 频谱重心=547Hz, 场景提示=mixed_environment

### 样本 1825: metro-lisbon-1224-45017-a.wav
- **真实场景**: metro
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.643), Vehicle(0.488), Train(0.318)
- **音频特征**: RMS=0.0138, 频谱重心=745Hz, 场景提示=mixed_environment

### 样本 1826: public_square-paris-251-7502-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.163), Vehicle(0.150)
- **音频特征**: RMS=0.0041, 频谱重心=963Hz, 场景提示=quiet_indoor

### 样本 1827: street_pedestrian-lisbon-1004-41249-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.434), Music(0.105)
- **音频特征**: RMS=0.0024, 频谱重心=1187Hz, 场景提示=quiet_indoor

### 样本 1828: street_pedestrian-barcelona-141-4290-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.840), Animal(0.172), Outside, urban or manmade(0.108)
- **音频特征**: RMS=0.0051, 频谱重心=1641Hz, 场景提示=mixed_environment

### 样本 1829: metro-milan-1141-40730-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.822), Vehicle(0.269)
- **音频特征**: RMS=0.0290, 频谱重心=611Hz, 场景提示=mixed_environment

### 样本 1830: tram-milan-1182-45383-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.133)
- **音频特征**: RMS=0.0124, 频谱重心=1151Hz, 场景提示=mixed_environment

### 样本 1831: metro_station-london-70-2038-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.720), Vehicle(0.132), Animal(0.102)
- **音频特征**: RMS=0.0076, 频谱重心=1265Hz, 场景提示=mixed_environment

### 样本 1832: public_square-stockholm-121-3569-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.681), Animal(0.312), Clip-clop(0.186)
- **音频特征**: RMS=0.0068, 频谱重心=1156Hz, 场景提示=quiet_indoor

### 样本 1833: street_pedestrian-lyon-1003-42432-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.317)
- **音频特征**: RMS=0.0017, 频谱重心=1065Hz, 场景提示=quiet_indoor

### 样本 1834: bus-london-212-6480-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.755), Vehicle(0.271)
- **音频特征**: RMS=0.0034, 频谱重心=809Hz, 场景提示=quiet_indoor

### 样本 1835: metro-paris-54-1570-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.740), Door(0.202), Animal(0.147)
- **音频特征**: RMS=0.0063, 频谱重心=1413Hz, 场景提示=quiet_indoor

### 样本 1836: street_pedestrian-prague-1203-45726-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.699), Vehicle(0.124)
- **音频特征**: RMS=0.0019, 频谱重心=1050Hz, 场景提示=quiet_indoor

### 样本 1837: metro-stockholm-56-1666-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.679), Vehicle(0.309), Doorbell(0.180)
- **音频特征**: RMS=0.0198, 频谱重心=737Hz, 场景提示=mixed_environment

### 样本 1838: airport-stockholm-10-429-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.777), Animal(0.303), Clip-clop(0.170)
- **音频特征**: RMS=0.0041, 频谱重心=1060Hz, 场景提示=quiet_indoor

### 样本 1839: tram-prague-1189-45733-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.685), Music(0.369), Vehicle(0.303)
- **音频特征**: RMS=0.0297, 频谱重心=613Hz, 场景提示=mixed_environment

### 样本 1840: airport-paris-206-6269-a.wav
- **真实场景**: airport
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.273), Vehicle(0.119)
- **音频特征**: RMS=0.0059, 频谱重心=1012Hz, 场景提示=quiet_indoor

### 样本 1841: park-paris-99-2803-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.278)
- **音频特征**: RMS=0.0015, 频谱重心=937Hz, 场景提示=quiet_indoor

### 样本 1842: airport-milan-1089-40755-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.760)
- **音频特征**: RMS=0.0024, 频谱重心=1670Hz, 场景提示=mixed_environment

### 样本 1843: metro_station-stockholm-85-2314-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.866)
- **音频特征**: RMS=0.0137, 频谱重心=1411Hz, 场景提示=mixed_environment

### 样本 1844: public_square-prague-1214-44516-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.781), Clip-clop(0.210), Run(0.178)
- **音频特征**: RMS=0.0027, 频谱重心=1113Hz, 场景提示=quiet_indoor

### 样本 1845: airport-barcelona-0-15-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.844), Clip-clop(0.152), Animal(0.144)
- **音频特征**: RMS=0.0023, 频谱重心=1322Hz, 场景提示=quiet_indoor

### 样本 1846: airport-lyon-1095-42436-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.742), Clip-clop(0.106)
- **音频特征**: RMS=0.0024, 频谱重心=1526Hz, 场景提示=mixed_environment

### 样本 1847: tram-stockholm-198-5972-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.813), Vehicle(0.151)
- **音频特征**: RMS=0.0081, 频谱重心=1218Hz, 场景提示=quiet_indoor

### 样本 1848: street_pedestrian-barcelona-142-4313-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.798)
- **音频特征**: RMS=0.0025, 频谱重心=1647Hz, 场景提示=mixed_environment

### 样本 1849: airport-milan-1089-42696-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.832), Clip-clop(0.429), Horse(0.357)
- **音频特征**: RMS=0.0021, 频谱重心=1474Hz, 场景提示=mixed_environment

### 样本 1850: metro_station-lyon-1167-44554-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.831), Vehicle(0.142), Outside, urban or manmade(0.141)
- **音频特征**: RMS=0.0057, 频谱重心=1602Hz, 场景提示=mixed_environment

### 样本 1851: tram-lisbon-1100-41838-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.454), Boat, Water vehicle(0.434), Wind(0.329)
- **音频特征**: RMS=0.0235, 频谱重心=1133Hz, 场景提示=mixed_environment

### 样本 1852: metro_station-lisbon-1021-42189-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.607), Train(0.497), Speech(0.393)
- **音频特征**: RMS=0.0410, 频谱重心=763Hz, 场景提示=mixed_environment

### 样本 1853: shopping_mall-prague-1031-41125-a.wav
- **真实场景**: shopping_mall
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Music(0.263), Musical instrument(0.123)
- **音频特征**: RMS=0.0018, 频谱重心=1077Hz, 场景提示=quiet_indoor

### 样本 1854: tram-lyon-1103-40733-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.771), Vehicle(0.349)
- **音频特征**: RMS=0.0100, 频谱重心=598Hz, 场景提示=mixed_environment

### 样本 1855: street_pedestrian-milan-1080-40565-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.612), Chink, clink(0.130), Animal(0.107)
- **音频特征**: RMS=0.0019, 频谱重心=1596Hz, 场景提示=mixed_environment

### 样本 1856: park-london-97-2743-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.772), Animal(0.272), Vehicle(0.161)
- **音频特征**: RMS=0.0027, 频谱重心=666Hz, 场景提示=quiet_indoor

### 样本 1857: airport-barcelona-1-54-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.778), Outside, urban or manmade(0.119)
- **音频特征**: RMS=0.0032, 频谱重心=971Hz, 场景提示=quiet_indoor

### 样本 1858: bus-prague-1030-40034-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Telephone bell ringing(0.333), Alarm clock(0.211), Alarm(0.131)
- **音频特征**: RMS=0.0521, 频谱重心=1084Hz, 场景提示=mixed_environment

### 样本 1859: shopping_mall-london-131-3922-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.682)
- **音频特征**: RMS=0.0020, 频谱重心=1246Hz, 场景提示=quiet_indoor

### 样本 1860: airport-prague-1069-43322-a.wav
- **真实场景**: airport
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.681)
- **音频特征**: RMS=0.0025, 频谱重心=1493Hz, 场景提示=mixed_environment

### 样本 1861: airport-london-5-244-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.783), Animal(0.230), Clip-clop(0.190)
- **音频特征**: RMS=0.0013, 频谱重心=1432Hz, 场景提示=mixed_environment

### 样本 1862: public_square-stockholm-121-3572-a.wav
- **真实场景**: public_square
- **AE预测**: metro_station
- **AS预测**: public_square
- **检测到的事件**: Speech(0.413), Vehicle(0.253), Animal(0.113)
- **音频特征**: RMS=0.0055, 频谱重心=1196Hz, 场景提示=quiet_indoor

### 样本 1863: metro_station-lyon-1010-43911-a.wav
- **真实场景**: metro_station
- **AE预测**: tram
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.821), Male speech, man speaking(0.176), Music(0.169)
- **音频特征**: RMS=0.0042, 频谱重心=1172Hz, 场景提示=quiet_indoor

### 样本 1864: park-paris-244-7277-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.843), Animal(0.203), Clip-clop(0.177)
- **音频特征**: RMS=0.0024, 频谱重心=1172Hz, 场景提示=quiet_indoor

### 样本 1865: tram-stockholm-283-8551-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Cupboard open or close(0.245), Sliding door(0.229), Door(0.177)
- **音频特征**: RMS=0.0080, 频谱重心=564Hz, 场景提示=quiet_indoor

### 样本 1866: metro-paris-52-1544-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.285), Inside, small room(0.117), Mouse(0.117)
- **音频特征**: RMS=0.0068, 频谱重心=1320Hz, 场景提示=quiet_indoor

### 样本 1867: public_square-milan-1074-42719-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.852), Animal(0.321), Clip-clop(0.173)
- **音频特征**: RMS=0.0028, 频谱重心=1157Hz, 场景提示=quiet_indoor

### 样本 1868: tram-milan-1182-44906-a.wav
- **真实场景**: tram
- **AE预测**: metro_station
- **AS预测**: tram
- **检测到的事件**: Sliding door(0.653), Door(0.587), Vehicle(0.295)
- **音频特征**: RMS=0.0121, 频谱重心=1370Hz, 场景提示=mixed_environment

### 样本 1869: street_pedestrian-lyon-1162-45438-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.674), Animal(0.462), Clip-clop(0.452)
- **音频特征**: RMS=0.0013, 频谱重心=1380Hz, 场景提示=quiet_indoor

### 样本 1870: airport-paris-206-6264-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.139)
- **音频特征**: RMS=0.0101, 频谱重心=1073Hz, 场景提示=mixed_environment

### 样本 1871: airport-london-6-278-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Animal(0.120), Vehicle(0.119), Mouse(0.106)
- **音频特征**: RMS=0.0030, 频谱重心=970Hz, 场景提示=quiet_indoor

### 样本 1872: metro_station-paris-81-2191-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Music(0.246), Musical instrument(0.139)
- **音频特征**: RMS=0.0022, 频谱重心=1584Hz, 场景提示=quiet_indoor

### 样本 1873: tram-helsinki-184-5721-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.624), Vehicle(0.121), Cupboard open or close(0.107)
- **音频特征**: RMS=0.0074, 频谱重心=1121Hz, 场景提示=quiet_indoor

### 样本 1874: airport-helsinki-3-136-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.837), Run(0.359), Animal(0.233)
- **音频特征**: RMS=0.0030, 频谱重心=1260Hz, 场景提示=quiet_indoor

### 样本 1875: airport-london-205-6179-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Cat(0.598), Animal(0.520), Meow(0.464)
- **音频特征**: RMS=0.0011, 频谱重心=1520Hz, 场景提示=mixed_environment

### 样本 1876: public_square-vienna-122-3612-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.416), Animal(0.226), Clip-clop(0.171)
- **音频特征**: RMS=0.0011, 频谱重心=937Hz, 场景提示=quiet_indoor

### 样本 1877: metro_station-lyon-1028-42814-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.295), Train(0.100)
- **音频特征**: RMS=0.0102, 频谱重心=918Hz, 场景提示=mixed_environment

### 样本 1878: airport-lisbon-1122-43685-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.814), Animal(0.356), Clip-clop(0.203)
- **音频特征**: RMS=0.0040, 频谱重心=1277Hz, 场景提示=mixed_environment

### 样本 1879: street_pedestrian-milan-1205-44726-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.440)
- **音频特征**: RMS=0.0011, 频谱重心=1272Hz, 场景提示=quiet_indoor

### 样本 1880: metro_station-paris-82-2202-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.278), Vehicle(0.142), Mouse(0.140)
- **音频特征**: RMS=0.0119, 频谱重心=2078Hz, 场景提示=mixed_environment

### 样本 1881: metro_station-vienna-87-2382-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Vehicle(0.324)
- **音频特征**: RMS=0.0052, 频谱重心=1341Hz, 场景提示=quiet_indoor

### 样本 1882: public_square-prague-1192-45141-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.151)
- **音频特征**: RMS=0.0031, 频谱重心=1025Hz, 场景提示=quiet_indoor

### 样本 1883: bus-milan-1078-40649-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.387), White noise(0.101)
- **音频特征**: RMS=0.0087, 频谱重心=1046Hz, 场景提示=quiet_indoor

### 样本 1884: public_square-london-113-3285-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: airport
- **检测到的事件**: Speech(0.723), Clip-clop(0.330), Animal(0.281)
- **音频特征**: RMS=0.0018, 频谱重心=1002Hz, 场景提示=quiet_indoor

### 样本 1885: tram-helsinki-276-8424-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.449), Vehicle(0.422), Field recording(0.115)
- **音频特征**: RMS=0.0164, 频谱重心=705Hz, 场景提示=mixed_environment

### 样本 1886: street_traffic-stockholm-273-8323-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.775), Vehicle(0.524), Boat, Water vehicle(0.169)
- **音频特征**: RMS=0.0156, 频谱重心=1116Hz, 场景提示=mixed_environment

### 样本 1887: airport-lisbon-1000-43069-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.826), Chatter(0.122)
- **音频特征**: RMS=0.0046, 频谱重心=1450Hz, 场景提示=mixed_environment

### 样本 1888: park-prague-1185-44706-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Vehicle(0.276), Speech(0.154)
- **音频特征**: RMS=0.0064, 频谱重心=589Hz, 场景提示=quiet_indoor

### 样本 1889: metro-milan-1218-44438-a.wav
- **真实场景**: metro
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.694), Music(0.194)
- **音频特征**: RMS=0.0206, 频谱重心=797Hz, 场景提示=mixed_environment

### 样本 1890: public_square-vienna-124-3665-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.789), Clip-clop(0.371), Animal(0.294)
- **音频特征**: RMS=0.0018, 频谱重心=1157Hz, 场景提示=quiet_indoor

### 样本 1891: street_pedestrian-barcelona-260-7892-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.847)
- **音频特征**: RMS=0.0027, 频谱重心=1576Hz, 场景提示=mixed_environment

### 样本 1892: street_pedestrian-lisbon-1004-43024-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.849), Outside, urban or manmade(0.129), Male speech, man speaking(0.111)
- **音频特征**: RMS=0.0026, 频谱重心=1268Hz, 场景提示=quiet_indoor

### 样本 1893: tram-london-188-5806-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.435), Speech(0.314), Train(0.151)
- **音频特征**: RMS=0.0124, 频谱重心=713Hz, 场景提示=mixed_environment

### 样本 1894: metro_station-vienna-240-7131-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.518), Field recording(0.264), Train(0.232)
- **音频特征**: RMS=0.0334, 频谱重心=471Hz, 场景提示=mixed_environment

### 样本 1895: metro-stockholm-227-6837-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.812), Vehicle(0.368)
- **音频特征**: RMS=0.0122, 频谱重心=751Hz, 场景提示=mixed_environment

### 样本 1896: street_traffic-milan-1087-40737-a.wav
- **真实场景**: street_traffic
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.174)
- **音频特征**: RMS=0.0017, 频谱重心=862Hz, 场景提示=quiet_indoor

### 样本 1897: street_pedestrian-prague-1051-41593-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.859), Clip-clop(0.150), Animal(0.120)
- **音频特征**: RMS=0.0046, 频谱重心=1019Hz, 场景提示=quiet_indoor

### 样本 1898: tram-lyon-1112-43973-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.709), Vehicle(0.641), Train(0.214)
- **音频特征**: RMS=0.0129, 频谱重心=544Hz, 场景提示=mixed_environment

### 样本 1899: metro_station-vienna-87-2390-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.155)
- **音频特征**: RMS=0.0037, 频谱重心=1011Hz, 场景提示=quiet_indoor

### 样本 1900: tram-prague-1184-44604-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Train(0.620), Vehicle(0.491), Rail transport(0.472)
- **音频特征**: RMS=0.0373, 频谱重心=467Hz, 场景提示=mixed_environment

### 样本 1901: street_pedestrian-milan-1165-44660-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.872), Clip-clop(0.240), Animal(0.219)
- **音频特征**: RMS=0.0037, 频谱重心=1188Hz, 场景提示=quiet_indoor

### 样本 1902: shopping_mall-barcelona-126-3766-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.818), Narration, monologue(0.155), Animal(0.140)
- **音频特征**: RMS=0.0052, 频谱重心=1668Hz, 场景提示=mixed_environment

### 样本 1903: street_pedestrian-barcelona-143-4334-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.828), Clip-clop(0.323), Animal(0.248)
- **音频特征**: RMS=0.0028, 频谱重心=1132Hz, 场景提示=quiet_indoor

### 样本 1904: street_pedestrian-vienna-158-4817-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.372), Arrow(0.111)
- **音频特征**: RMS=0.0016, 频谱重心=1349Hz, 场景提示=quiet_indoor

### 样本 1905: bus-barcelona-210-6404-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.800), Speech(0.738), Car(0.354)
- **音频特征**: RMS=0.0462, 频谱重心=483Hz, 场景提示=mixed_environment

### 样本 1906: bus-barcelona-16-647-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.628), Vehicle(0.264)
- **音频特征**: RMS=0.0079, 频谱重心=990Hz, 场景提示=quiet_indoor

### 样本 1907: shopping_mall-prague-1219-45097-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.815), Clip-clop(0.277), Horse(0.217)
- **音频特征**: RMS=0.0029, 频谱重心=1702Hz, 场景提示=mixed_environment

### 样本 1908: metro_station-lyon-1077-42424-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.359), Vehicle(0.345), Train(0.312)
- **音频特征**: RMS=0.0046, 频谱重心=1016Hz, 场景提示=quiet_indoor

### 样本 1909: bus-milan-1154-41234-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.476), Vehicle(0.439), Car(0.106)
- **音频特征**: RMS=0.0353, 频谱重心=975Hz, 场景提示=mixed_environment

### 样本 1910: shopping_mall-lisbon-1002-42072-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.792)
- **音频特征**: RMS=0.0021, 频谱重心=1122Hz, 场景提示=quiet_indoor

### 样本 1911: shopping_mall-stockholm-137-4167-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.744), Music(0.139), Animal(0.133)
- **音频特征**: RMS=0.0079, 频谱重心=981Hz, 场景提示=quiet_indoor

### 样本 1912: shopping_mall-lisbon-1176-45605-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.234)
- **音频特征**: RMS=0.0014, 频谱重心=1231Hz, 场景提示=quiet_indoor

### 样本 1913: shopping_mall-lyon-1066-40395-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.366)
- **音频特征**: RMS=0.0014, 频谱重心=1549Hz, 场景提示=mixed_environment

### 样本 1914: street_pedestrian-barcelona-260-7901-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.736), Clip-clop(0.251), Horse(0.178)
- **音频特征**: RMS=0.0028, 频谱重心=1707Hz, 场景提示=mixed_environment

### 样本 1915: bus-lisbon-1106-42268-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.864), Vehicle(0.181)
- **音频特征**: RMS=0.0185, 频谱重心=639Hz, 场景提示=mixed_environment

### 样本 1916: metro_station-milan-1117-43845-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.585), Clip-clop(0.156), Horse(0.155)
- **音频特征**: RMS=0.0063, 频谱重心=982Hz, 场景提示=quiet_indoor

### 样本 1917: metro_station-barcelona-230-6924-a.wav
- **真实场景**: metro_station
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.185)
- **音频特征**: RMS=0.0063, 频谱重心=1321Hz, 场景提示=quiet_indoor

### 样本 1918: street_pedestrian-stockholm-155-4691-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.811), Clip-clop(0.205), Run(0.180)
- **音频特征**: RMS=0.0044, 频谱重心=1130Hz, 场景提示=quiet_indoor

### 样本 1919: airport-lisbon-1122-42593-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Animal(0.174), Speech(0.169), Vehicle(0.135)
- **音频特征**: RMS=0.0035, 频谱重心=1267Hz, 场景提示=mixed_environment

### 样本 1920: metro_station-london-74-2090-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.814), Snake(0.349), Children playing(0.203)
- **音频特征**: RMS=0.0066, 频谱重心=1833Hz, 场景提示=mixed_environment

### 样本 1921: metro-barcelona-220-6673-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.806), Vehicle(0.241), Train(0.132)
- **音频特征**: RMS=0.0208, 频谱重心=917Hz, 场景提示=mixed_environment

### 样本 1922: metro-stockholm-57-1697-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.479), Vehicle(0.131)
- **音频特征**: RMS=0.0096, 频谱重心=580Hz, 场景提示=quiet_indoor

### 样本 1923: street_traffic-london-271-8249-a.wav
- **真实场景**: street_traffic
- **AE预测**: metro_station
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.670), Vehicle(0.305)
- **音频特征**: RMS=0.0060, 频谱重心=1397Hz, 场景提示=quiet_indoor

### 样本 1924: bus-lisbon-1226-45085-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.732), Music(0.373), Vehicle(0.143)
- **音频特征**: RMS=0.0079, 频谱重心=1673Hz, 场景提示=quiet_indoor

### 样本 1925: metro_station-milan-1117-40345-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.166), Vehicle(0.150)
- **音频特征**: RMS=0.0058, 频谱重心=973Hz, 场景提示=quiet_indoor

### 样本 1926: tram-prague-1151-42051-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.592), Field recording(0.282), Speech(0.232)
- **音频特征**: RMS=0.0340, 频谱重心=507Hz, 场景提示=mixed_environment

### 样本 1927: shopping_mall-helsinki-129-3871-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.760), Music(0.132)
- **音频特征**: RMS=0.0064, 频谱重心=1064Hz, 场景提示=quiet_indoor

### 样本 1928: shopping_mall-helsinki-130-3913-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.840), Chatter(0.144)
- **音频特征**: RMS=0.0043, 频谱重心=1299Hz, 场景提示=mixed_environment

### 样本 1929: public_square-prague-1152-42323-a.wav
- **真实场景**: public_square
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.731), Clip-clop(0.224), Horse(0.165)
- **音频特征**: RMS=0.0024, 频谱重心=1261Hz, 场景提示=mixed_environment

### 样本 1930: airport-barcelona-1-25-a.wav
- **真实场景**: airport
- **AE预测**: metro_station
- **AS预测**: airport
- **检测到的事件**: Speech(0.889), Male speech, man speaking(0.252), Narration, monologue(0.154)
- **音频特征**: RMS=0.0063, 频谱重心=1220Hz, 场景提示=mixed_environment

### 样本 1931: street_pedestrian-paris-265-8039-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.821), Clip-clop(0.253), Horse(0.208)
- **音频特征**: RMS=0.0017, 频谱重心=1393Hz, 场景提示=quiet_indoor

### 样本 1932: bus-lisbon-1212-45601-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.780), Vehicle(0.381)
- **音频特征**: RMS=0.0167, 频谱重心=1079Hz, 场景提示=mixed_environment

### 样本 1933: metro-barcelona-220-6665-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.788), Vehicle(0.624), Field recording(0.250)
- **音频特征**: RMS=0.0302, 频谱重心=664Hz, 场景提示=mixed_environment

### 样本 1934: airport-vienna-14-576-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.766)
- **音频特征**: RMS=0.0010, 频谱重心=1600Hz, 场景提示=quiet_indoor

### 样本 1935: shopping_mall-vienna-139-4231-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.220), Vehicle(0.147), Animal(0.142)
- **音频特征**: RMS=0.0029, 频谱重心=1278Hz, 场景提示=quiet_indoor

### 样本 1936: metro_station-stockholm-239-7108-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.645), Train(0.256), Vehicle(0.232)
- **音频特征**: RMS=0.0086, 频谱重心=1534Hz, 场景提示=mixed_environment

### 样本 1937: street_pedestrian-london-149-4524-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.832), Clip-clop(0.244), Horse(0.193)
- **音频特征**: RMS=0.0020, 频谱重心=1194Hz, 场景提示=quiet_indoor

### 样本 1938: public_square-lyon-1056-40600-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.811), Run(0.176), Outside, urban or manmade(0.173)
- **音频特征**: RMS=0.0029, 频谱重心=1150Hz, 场景提示=quiet_indoor

### 样本 1939: public_square-lyon-1056-40078-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.717), Vehicle(0.116)
- **音频特征**: RMS=0.0034, 频谱重心=1105Hz, 场景提示=quiet_indoor

### 样本 1940: shopping_mall-milan-1084-41849-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.675), Mouse(0.194), Animal(0.124)
- **音频特征**: RMS=0.0024, 频谱重心=1444Hz, 场景提示=mixed_environment

### 样本 1941: public_square-prague-1214-44267-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.743), Animal(0.142)
- **音频特征**: RMS=0.0015, 频谱重心=1155Hz, 场景提示=quiet_indoor

### 样本 1942: public_square-stockholm-121-3589-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.262), Boat, Water vehicle(0.159), Clip-clop(0.103)
- **音频特征**: RMS=0.0058, 频谱重心=894Hz, 场景提示=quiet_indoor

### 样本 1943: street_traffic-vienna-176-5415-a.wav
- **真实场景**: street_traffic
- **AE预测**: metro_station
- **AS预测**: public_square
- **音频特征**: RMS=0.0030, 频谱重心=1323Hz, 场景提示=quiet_indoor

### 样本 1944: shopping_mall-prague-1219-45410-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.786)
- **音频特征**: RMS=0.0039, 频谱重心=1509Hz, 场景提示=mixed_environment

### 样本 1945: airport-london-6-262-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.640), Vehicle(0.106)
- **音频特征**: RMS=0.0018, 频谱重心=1222Hz, 场景提示=quiet_indoor

### 样本 1946: metro-paris-225-6802-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.277), Vehicle(0.243)
- **音频特征**: RMS=0.0126, 频谱重心=1432Hz, 场景提示=mixed_environment

### 样本 1947: airport-paris-206-6255-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.147)
- **音频特征**: RMS=0.0088, 频谱重心=957Hz, 场景提示=quiet_indoor

### 样本 1948: street_pedestrian-vienna-159-4860-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.674), Horse(0.542), Clip-clop(0.489)
- **音频特征**: RMS=0.0011, 频谱重心=1347Hz, 场景提示=mixed_environment

### 样本 1949: metro-lyon-1082-40313-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.723), Vehicle(0.503), Car(0.138)
- **音频特征**: RMS=0.0159, 频谱重心=1463Hz, 场景提示=mixed_environment

### 样本 1950: tram-lisbon-1200-45464-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.757), Vehicle(0.356), Bus(0.184)
- **音频特征**: RMS=0.0120, 频谱重心=917Hz, 场景提示=mixed_environment

### 样本 1951: airport-lyon-1169-44330-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.857), Clip-clop(0.584), Animal(0.422)
- **音频特征**: RMS=0.0020, 频谱重心=1505Hz, 场景提示=mixed_environment

### 样本 1952: tram-lyon-1150-41169-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.757), Sliding door(0.259), Door(0.225)
- **音频特征**: RMS=0.0069, 频谱重心=1094Hz, 场景提示=quiet_indoor

### 样本 1953: metro-stockholm-57-1706-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Train(0.396), Vehicle(0.368), Railroad car, train wagon(0.282)
- **音频特征**: RMS=0.0116, 频谱重心=581Hz, 场景提示=mixed_environment

### 样本 1954: shopping_mall-london-256-7715-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.830), Clip-clop(0.238), Horse(0.178)
- **音频特征**: RMS=0.0026, 频谱重心=1469Hz, 场景提示=mixed_environment

### 样本 1955: airport-milan-1172-45409-a.wav
- **真实场景**: airport
- **AE预测**: metro_station
- **AS预测**: public_square
- **检测到的事件**: Speech(0.562), Vehicle(0.266), Reversing beeps(0.118)
- **音频特征**: RMS=0.0054, 频谱重心=1578Hz, 场景提示=mixed_environment

### 样本 1956: tram-paris-194-5885-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.633), Vehicle(0.310), Car(0.129)
- **音频特征**: RMS=0.0057, 频谱重心=821Hz, 场景提示=quiet_indoor

### 样本 1957: public_square-lyon-1208-45562-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_traffic
- **音频特征**: RMS=0.0034, 频谱重心=1516Hz, 场景提示=quiet_indoor

### 样本 1958: metro-helsinki-222-6730-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.711), Vehicle(0.261), Music(0.114)
- **音频特征**: RMS=0.0202, 频谱重心=661Hz, 场景提示=mixed_environment

### 样本 1959: metro-barcelona-42-1297-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.161)
- **音频特征**: RMS=0.0082, 频谱重心=829Hz, 场景提示=quiet_indoor

### 样本 1960: street_pedestrian-helsinki-147-4438-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.201)
- **音频特征**: RMS=0.0052, 频谱重心=598Hz, 场景提示=quiet_indoor

### 样本 1961: metro_station-prague-1130-40875-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.683), Arrow(0.287), Vehicle(0.204)
- **音频特征**: RMS=0.0076, 频谱重心=972Hz, 场景提示=quiet_indoor

### 样本 1962: metro_station-helsinki-67-1994-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_pedestrian
- **检测到的事件**: Vehicle(0.215), Music(0.183), Train(0.166)
- **音频特征**: RMS=0.0023, 频谱重心=1159Hz, 场景提示=quiet_indoor

### 样本 1963: shopping_mall-milan-1049-42361-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.724)
- **音频特征**: RMS=0.0028, 频谱重心=1575Hz, 场景提示=mixed_environment

### 样本 1964: public_square-paris-116-3404-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.825), Clip-clop(0.347), Horse(0.289)
- **音频特征**: RMS=0.0024, 频谱重心=870Hz, 场景提示=quiet_indoor

### 样本 1965: metro-prague-1163-44202-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.812), Rail transport(0.664), Railroad car, train wagon(0.659)
- **音频特征**: RMS=0.0317, 频谱重心=664Hz, 场景提示=mixed_environment

### 样本 1966: street_pedestrian-paris-265-8042-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.794), Animal(0.164), Clip-clop(0.157)
- **音频特征**: RMS=0.0014, 频谱重心=1400Hz, 场景提示=quiet_indoor

### 样本 1967: airport-prague-1015-41221-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.201), Vehicle(0.190), Clip-clop(0.114)
- **音频特征**: RMS=0.0053, 频谱重心=1088Hz, 场景提示=quiet_indoor

### 样本 1968: metro-london-48-1496-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.779), Animal(0.312), Bird(0.194)
- **音频特征**: RMS=0.0101, 频谱重心=1007Hz, 场景提示=mixed_environment

### 样本 1969: tram-prague-1189-44992-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.773), Vehicle(0.514), Car(0.130)
- **音频特征**: RMS=0.0554, 频谱重心=412Hz, 场景提示=mixed_environment

### 样本 1970: public_square-vienna-122-3602-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.691), Animal(0.243), Clip-clop(0.114)
- **音频特征**: RMS=0.0010, 频谱重心=1088Hz, 场景提示=quiet_indoor

### 样本 1971: tram-prague-1088-43434-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.388), Train(0.163), Railroad car, train wagon(0.101)
- **音频特征**: RMS=0.0220, 频谱重心=546Hz, 场景提示=mixed_environment

### 样本 1972: street_pedestrian-london-263-7974-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.564)
- **音频特征**: RMS=0.0018, 频谱重心=1523Hz, 场景提示=mixed_environment

### 样本 1973: metro_station-lyon-1179-44230-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.720)
- **音频特征**: RMS=0.0035, 频谱重心=1207Hz, 场景提示=quiet_indoor

### 样本 1974: park-lyon-1144-43245-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.738), Whispering(0.178)
- **音频特征**: RMS=0.0009, 频谱重心=1498Hz, 场景提示=quiet_indoor

### 样本 1975: tram-lisbon-1035-42518-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.266), Microwave oven(0.110)
- **音频特征**: RMS=0.0148, 频谱重心=762Hz, 场景提示=mixed_environment

### 样本 1976: public_square-prague-1152-41372-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.794), Clip-clop(0.137), Outside, urban or manmade(0.135)
- **音频特征**: RMS=0.0024, 频谱重心=1362Hz, 场景提示=mixed_environment

### 样本 1977: metro_station-stockholm-239-7099-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Train(0.694), Rail transport(0.549), Railroad car, train wagon(0.538)
- **音频特征**: RMS=0.0067, 频谱重心=1176Hz, 场景提示=mixed_environment

### 样本 1978: public_square-milan-1014-42553-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.682), Vehicle(0.294), Boat, Water vehicle(0.167)
- **音频特征**: RMS=0.0052, 频谱重心=1051Hz, 场景提示=quiet_indoor

### 样本 1979: metro-milan-1141-42004-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.854), Vehicle(0.328)
- **音频特征**: RMS=0.0111, 频谱重心=879Hz, 场景提示=mixed_environment

### 样本 1980: airport-vienna-209-6365-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.720), Clip-clop(0.237), Horse(0.180)
- **音频特征**: RMS=0.0020, 频谱重心=1380Hz, 场景提示=quiet_indoor

### 样本 1981: metro-milan-1197-44875-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.488), Vehicle(0.470), Railroad car, train wagon(0.354)
- **音频特征**: RMS=0.0829, 频谱重心=672Hz, 场景提示=mixed_environment

### 样本 1982: metro-barcelona-220-6631-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.777), Music(0.360), Vehicle(0.203)
- **音频特征**: RMS=0.0085, 频谱重心=1305Hz, 场景提示=quiet_indoor

### 样本 1983: shopping_mall-milan-1084-42167-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.766), Basketball bounce(0.199), Clip-clop(0.106)
- **音频特征**: RMS=0.0027, 频谱重心=1822Hz, 场景提示=mixed_environment

### 样本 1984: street_pedestrian-lyon-1003-40003-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.753)
- **音频特征**: RMS=0.0019, 频谱重心=1289Hz, 场景提示=quiet_indoor

### 样本 1985: street_pedestrian-lisbon-1099-40169-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.681)
- **音频特征**: RMS=0.0033, 频谱重心=1230Hz, 场景提示=quiet_indoor

### 样本 1986: airport-vienna-13-555-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.466), Animal(0.194), Clip-clop(0.192)
- **音频特征**: RMS=0.0015, 频谱重心=1279Hz, 场景提示=quiet_indoor

### 样本 1987: tram-milan-1065-43407-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.566), Vehicle(0.321), Train(0.299)
- **音频特征**: RMS=0.0103, 频谱重心=739Hz, 场景提示=mixed_environment

### 样本 1988: street_traffic-paris-172-5299-a.wav
- **真实场景**: street_traffic
- **AE预测**: park
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.191)
- **音频特征**: RMS=0.0027, 频谱重心=1378Hz, 场景提示=quiet_indoor

### 样本 1989: street_pedestrian-barcelona-260-7905-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.343), Animal(0.138)
- **音频特征**: RMS=0.0022, 频谱重心=1500Hz, 场景提示=mixed_environment

### 样本 1990: street_pedestrian-vienna-160-4875-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.657), Animal(0.175), Clip-clop(0.162)
- **音频特征**: RMS=0.0019, 频谱重心=1355Hz, 场景提示=mixed_environment

### 样本 1991: shopping_mall-london-256-7729-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.830), Chatter(0.204), Inside, public space(0.132)
- **音频特征**: RMS=0.0036, 频谱重心=1478Hz, 场景提示=mixed_environment

### 样本 1992: tram-milan-1036-40559-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.596), Train(0.558), Vehicle(0.399)
- **音频特征**: RMS=0.0220, 频谱重心=566Hz, 场景提示=mixed_environment

### 样本 1993: bus-london-22-831-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.809), Vehicle(0.458), Car(0.171)
- **音频特征**: RMS=0.0216, 频谱重心=459Hz, 场景提示=mixed_environment

### 样本 1994: metro_station-lyon-1010-40010-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.761)
- **音频特征**: RMS=0.0027, 频谱重心=1306Hz, 场景提示=quiet_indoor

### 样本 1995: metro_station-lyon-1010-42857-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.804), Vehicle(0.100)
- **音频特征**: RMS=0.0044, 频谱重心=1189Hz, 场景提示=quiet_indoor

### 样本 1996: bus-stockholm-36-1088-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.854), Vehicle(0.272), Hubbub, speech noise, speech babble(0.131)
- **音频特征**: RMS=0.0110, 频谱重心=1077Hz, 场景提示=mixed_environment

### 样本 1997: airport-milan-1172-45420-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.622), Clip-clop(0.433), Horse(0.383)
- **音频特征**: RMS=0.0029, 频谱重心=1554Hz, 场景提示=mixed_environment

### 样本 1998: tram-helsinki-183-5695-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.336), Train(0.114)
- **音频特征**: RMS=0.0159, 频谱重心=631Hz, 场景提示=mixed_environment

### 样本 1999: airport-prague-1034-40148-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.836), Clip-clop(0.178), Outside, urban or manmade(0.137)
- **音频特征**: RMS=0.0092, 频谱重心=1226Hz, 场景提示=mixed_environment

### 样本 2000: airport-paris-206-6273-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.689), Music(0.135)
- **音频特征**: RMS=0.0069, 频谱重心=1060Hz, 场景提示=quiet_indoor

### 样本 2001: street_pedestrian-lisbon-1174-44367-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.841), Vehicle(0.152), Outside, urban or manmade(0.111)
- **音频特征**: RMS=0.0042, 频谱重心=999Hz, 场景提示=quiet_indoor

### 样本 2002: street_pedestrian-barcelona-144-4365-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Clip-clop(0.766), Horse(0.759), Speech(0.728)
- **音频特征**: RMS=0.0024, 频谱重心=1476Hz, 场景提示=quiet_indoor

### 样本 2003: street_pedestrian-london-263-7989-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.759), Animal(0.347), Clip-clop(0.278)
- **音频特征**: RMS=0.0026, 频谱重心=1421Hz, 场景提示=quiet_indoor

### 样本 2004: bus-stockholm-217-6563-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Siren(0.238), Howl(0.130), Vehicle(0.124)
- **音频特征**: RMS=0.0175, 频谱重心=514Hz, 场景提示=mixed_environment

### 样本 2005: metro_station-helsinki-66-1983-a.wav
- **真实场景**: metro_station
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.645)
- **音频特征**: RMS=0.0013, 频谱重心=1506Hz, 场景提示=quiet_indoor

### 样本 2006: public_square-prague-1075-41468-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.878), Run(0.673), Outside, urban or manmade(0.350)
- **音频特征**: RMS=0.0030, 频谱重心=1299Hz, 场景提示=quiet_indoor

### 样本 2007: airport-london-6-266-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.105), Animal(0.105), Vehicle(0.100)
- **音频特征**: RMS=0.0018, 频谱重心=1253Hz, 场景提示=quiet_indoor

### 样本 2008: shopping_mall-helsinki-255-7656-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.844), Clip-clop(0.209), Animal(0.169)
- **音频特征**: RMS=0.0055, 频谱重心=1341Hz, 场景提示=quiet_indoor

### 样本 2009: bus-lisbon-1128-43215-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.818), Vehicle(0.248)
- **音频特征**: RMS=0.0282, 频谱重心=711Hz, 场景提示=mixed_environment

### 样本 2010: park-prague-1185-44905-a.wav
- **真实场景**: park
- **AE预测**: street_traffic
- **AS预测**: park
- **检测到的事件**: Speech(0.445), Vehicle(0.212), Animal(0.160)
- **音频特征**: RMS=0.0065, 频谱重心=658Hz, 场景提示=quiet_indoor

### 样本 2011: public_square-lyon-1024-40770-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Animal(0.176), Silence(0.163), Mouse(0.161)
- **音频特征**: RMS=0.0019, 频谱重心=922Hz, 场景提示=quiet_indoor

### 样本 2012: street_pedestrian-barcelona-260-7900-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.825), Horse(0.446), Clip-clop(0.425)
- **音频特征**: RMS=0.0019, 频谱重心=1589Hz, 场景提示=mixed_environment

### 样本 2013: metro-vienna-59-1757-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.176)
- **音频特征**: RMS=0.0058, 频谱重心=1220Hz, 场景提示=quiet_indoor

### 样本 2014: bus-prague-1032-41827-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.800), Vehicle(0.660), Car(0.227)
- **音频特征**: RMS=0.0437, 频谱重心=738Hz, 场景提示=mixed_environment

### 样本 2015: tram-stockholm-284-8600-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.733), Vehicle(0.535), Music(0.348)
- **音频特征**: RMS=0.0502, 频谱重心=413Hz, 场景提示=mixed_environment

### 样本 2016: metro-prague-1026-41579-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.778), Rail transport(0.655), Railroad car, train wagon(0.653)
- **音频特征**: RMS=0.0591, 频谱重心=816Hz, 场景提示=mixed_environment

### 样本 2017: street_pedestrian-prague-1203-44804-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.654), Run(0.275), Vehicle(0.121)
- **音频特征**: RMS=0.0033, 频谱重心=1491Hz, 场景提示=mixed_environment

### 样本 2018: tram-barcelona-275-8393-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.880), Male speech, man speaking(0.353), Narration, monologue(0.176)
- **音频特征**: RMS=0.0091, 频谱重心=759Hz, 场景提示=quiet_indoor

### 样本 2019: airport-lisbon-1175-44703-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.776), Clip-clop(0.127), Vehicle(0.109)
- **音频特征**: RMS=0.0039, 频谱重心=1520Hz, 场景提示=mixed_environment

### 样本 2020: public_square-lyon-1178-45398-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Animal(0.294), Speech(0.267), Clip-clop(0.253)
- **音频特征**: RMS=0.0015, 频谱重心=1479Hz, 场景提示=quiet_indoor

### 样本 2021: airport-lisbon-1000-41312-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.845), Outside, urban or manmade(0.135), Hubbub, speech noise, speech babble(0.111)
- **音频特征**: RMS=0.0055, 频谱重心=1511Hz, 场景提示=mixed_environment

### 样本 2022: bus-milan-1083-43422-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.767), Vehicle(0.525), Bus(0.130)
- **音频特征**: RMS=0.0221, 频谱重心=859Hz, 场景提示=mixed_environment

### 样本 2023: street_pedestrian-stockholm-157-4757-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.261), Sewing machine(0.198)
- **音频特征**: RMS=0.0062, 频谱重心=1427Hz, 场景提示=mixed_environment

### 样本 2024: metro_station-barcelona-229-6909-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.825), Vehicle(0.110)
- **音频特征**: RMS=0.0030, 频谱重心=1024Hz, 场景提示=quiet_indoor

### 样本 2025: airport-london-6-302-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Vehicle(0.162)
- **音频特征**: RMS=0.0020, 频谱重心=1018Hz, 场景提示=quiet_indoor

### 样本 2026: bus-milan-1154-43356-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.392), Car(0.113)
- **音频特征**: RMS=0.0133, 频谱重心=1407Hz, 场景提示=mixed_environment

### 样本 2027: park-helsinki-94-2607-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.711), Walk, footsteps(0.298), Outside, rural or natural(0.221)
- **音频特征**: RMS=0.0017, 频谱重心=1730Hz, 场景提示=mixed_environment

### 样本 2028: airport-paris-9-373-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.404), Animal(0.337), Domestic animals, pets(0.185)
- **音频特征**: RMS=0.0026, 频谱重心=1288Hz, 场景提示=quiet_indoor

### 样本 2029: metro-milan-1141-42061-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.778), Vehicle(0.375)
- **音频特征**: RMS=0.0205, 频谱重心=635Hz, 场景提示=mixed_environment

### 样本 2030: bus-lyon-1073-41889-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.613), Vehicle(0.147)
- **音频特征**: RMS=0.0109, 频谱重心=630Hz, 场景提示=mixed_environment

### 样本 2031: public_square-lyon-1208-44382-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.325), Vehicle(0.220), Silence(0.104)
- **音频特征**: RMS=0.0028, 频谱重心=1732Hz, 场景提示=mixed_environment

### 样本 2032: street_pedestrian-lyon-1047-42628-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.649), Clip-clop(0.180), Horse(0.156)
- **音频特征**: RMS=0.0019, 频谱重心=1198Hz, 场景提示=quiet_indoor

### 样本 2033: shopping_mall-london-131-3933-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.611), Music(0.294), Sliding door(0.176)
- **音频特征**: RMS=0.0020, 频谱重心=1852Hz, 场景提示=mixed_environment

### 样本 2034: shopping_mall-helsinki-129-3861-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.781), Clip-clop(0.309), Horse(0.236)
- **音频特征**: RMS=0.0024, 频谱重心=1333Hz, 场景提示=quiet_indoor

### 样本 2035: public_square-vienna-124-3694-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Bow-wow(0.688), Dog(0.650), Animal(0.647)
- **音频特征**: RMS=0.0017, 频谱重心=1201Hz, 场景提示=quiet_indoor

### 样本 2036: street_pedestrian-lyon-1003-42767-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.657), Animal(0.156), Clip-clop(0.123)
- **音频特征**: RMS=0.0017, 频谱重心=1316Hz, 场景提示=quiet_indoor

### 样本 2037: shopping_mall-paris-257-7784-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.762), Animal(0.219), Clip-clop(0.133)
- **音频特征**: RMS=0.0022, 频谱重心=1603Hz, 场景提示=mixed_environment

### 样本 2038: metro-lisbon-1121-43879-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.678), Train(0.533), Railroad car, train wagon(0.318)
- **音频特征**: RMS=0.0339, 频谱重心=648Hz, 场景提示=mixed_environment

### 样本 2039: metro_station-milan-1187-45045-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.590), Speech(0.447), Field recording(0.430)
- **音频特征**: RMS=0.0409, 频谱重心=504Hz, 场景提示=mixed_environment

### 样本 2040: metro_station-vienna-87-2367-a.wav
- **真实场景**: metro_station
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Vehicle(0.160), White noise(0.151)
- **音频特征**: RMS=0.0047, 频谱重心=1527Hz, 场景提示=mixed_environment

### 样本 2041: metro_station-london-233-6990-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Speech(0.565), Music(0.106)
- **音频特征**: RMS=0.0045, 频谱重心=1670Hz, 场景提示=mixed_environment

### 样本 2042: metro-barcelona-220-6634-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.766), Vehicle(0.270)
- **音频特征**: RMS=0.0115, 频谱重心=1109Hz, 场景提示=mixed_environment

### 样本 2043: metro_station-stockholm-83-2240-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.851), Animal(0.510), Horse(0.385)
- **音频特征**: RMS=0.0058, 频谱重心=1018Hz, 场景提示=quiet_indoor

### 样本 2044: street_pedestrian-vienna-160-4876-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.573), Animal(0.231), Clip-clop(0.102)
- **音频特征**: RMS=0.0027, 频谱重心=1258Hz, 场景提示=quiet_indoor

### 样本 2045: shopping_mall-london-131-3931-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.477)
- **音频特征**: RMS=0.0019, 频谱重心=1137Hz, 场景提示=quiet_indoor

### 样本 2046: metro_station-barcelona-63-1887-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.498)
- **音频特征**: RMS=0.0359, 频谱重心=904Hz, 场景提示=mixed_environment

### 样本 2047: public_square-stockholm-252-7556-a.wav
- **真实场景**: public_square
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Animal(0.180), Speech(0.171), Vehicle(0.121)
- **音频特征**: RMS=0.0035, 频谱重心=963Hz, 场景提示=quiet_indoor

### 样本 2048: bus-stockholm-217-6565-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: metro
- **音频特征**: RMS=0.0108, 频谱重心=645Hz, 场景提示=mixed_environment

### 样本 2049: public_square-london-114-3318-a.wav
- **真实场景**: public_square
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.724), Music(0.113)
- **音频特征**: RMS=0.0027, 频谱重心=1321Hz, 场景提示=quiet_indoor

### 样本 2050: street_pedestrian-lisbon-1098-42704-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.863), Vehicle(0.123), Outside, urban or manmade(0.116)
- **音频特征**: RMS=0.0032, 频谱重心=1582Hz, 场景提示=mixed_environment

### 样本 2051: metro_station-prague-1130-43319-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.748), Children playing(0.151), Animal(0.144)
- **音频特征**: RMS=0.0033, 频谱重心=1406Hz, 场景提示=mixed_environment

### 样本 2052: shopping_mall-lisbon-1002-42772-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Mouse(0.124)
- **音频特征**: RMS=0.0024, 频谱重心=1149Hz, 场景提示=quiet_indoor

### 样本 2053: tram-london-185-5757-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.523), Music(0.327), Car(0.241)
- **音频特征**: RMS=0.0184, 频谱重心=621Hz, 场景提示=mixed_environment

### 样本 2054: shopping_mall-stockholm-137-4156-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.823), Clip-clop(0.544), Horse(0.437)
- **音频特征**: RMS=0.0079, 频谱重心=910Hz, 场景提示=quiet_indoor

### 样本 2055: public_square-prague-1192-44200-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.821), Outside, urban or manmade(0.134), Clip-clop(0.130)
- **音频特征**: RMS=0.0067, 频谱重心=745Hz, 场景提示=quiet_indoor

### 样本 2056: metro-vienna-228-6861-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.336), Train(0.164)
- **音频特征**: RMS=0.0088, 频谱重心=513Hz, 场景提示=quiet_indoor

### 样本 2057: airport-paris-206-6239-a.wav
- **真实场景**: airport
- **AE预测**: metro_station
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.307), Vehicle(0.227), Train(0.188)
- **音频特征**: RMS=0.0062, 频谱重心=862Hz, 场景提示=quiet_indoor

### 样本 2058: metro_station-milan-1127-41792-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Train(0.806), Vehicle(0.633), Railroad car, train wagon(0.631)
- **音频特征**: RMS=0.0319, 频谱重心=1287Hz, 场景提示=mixed_environment

### 样本 2059: bus-prague-1147-43067-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.440), Train(0.171), Speech(0.105)
- **音频特征**: RMS=0.0192, 频谱重心=925Hz, 场景提示=mixed_environment

### 样本 2060: bus-stockholm-217-6547-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.276), Music(0.146), Rumble(0.113)
- **音频特征**: RMS=0.0250, 频谱重心=430Hz, 场景提示=mixed_environment

### 样本 2061: metro_station-lyon-1028-41278-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Music(0.401), Vehicle(0.390), Speech(0.375)
- **音频特征**: RMS=0.0067, 频谱重心=1367Hz, 场景提示=quiet_indoor

### 样本 2062: public_square-prague-1027-41770-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.721), Vehicle(0.222), Fire(0.131)
- **音频特征**: RMS=0.0071, 频谱重心=1128Hz, 场景提示=quiet_indoor

### 样本 2063: tram-helsinki-182-5648-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Vehicle(0.237)
- **音频特征**: RMS=0.0387, 频谱重心=565Hz, 场景提示=mixed_environment

### 样本 2064: airport-london-205-6213-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.838), Run(0.209), Outside, urban or manmade(0.186)
- **音频特征**: RMS=0.0024, 频谱重心=1520Hz, 场景提示=quiet_indoor

### 样本 2065: street_pedestrian-lyon-1003-43555-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.735), Clip-clop(0.128), Animal(0.113)
- **音频特征**: RMS=0.0016, 频谱重心=1270Hz, 场景提示=quiet_indoor

### 样本 2066: airport-stockholm-208-6337-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.806), Clip-clop(0.462), Horse(0.370)
- **音频特征**: RMS=0.0047, 频谱重心=1295Hz, 场景提示=quiet_indoor

### 样本 2067: airport-stockholm-207-6297-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.875), Clip-clop(0.242), Animal(0.236)
- **音频特征**: RMS=0.0031, 频谱重心=1553Hz, 场景提示=mixed_environment

### 样本 2068: street_pedestrian-paris-154-4674-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Animal(0.285), Speech(0.119), Chewing, mastication(0.105)
- **音频特征**: RMS=0.0018, 频谱重心=1406Hz, 场景提示=quiet_indoor

### 样本 2069: public_square-london-113-3283-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.127), Animal(0.116)
- **音频特征**: RMS=0.0019, 频谱重心=1048Hz, 场景提示=quiet_indoor

### 样本 2070: airport-vienna-13-548-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.328), Animal(0.183), Clip-clop(0.142)
- **音频特征**: RMS=0.0012, 频谱重心=1615Hz, 场景提示=mixed_environment

### 样本 2071: airport-lisbon-1114-40725-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.769), Vehicle(0.162), Animal(0.101)
- **音频特征**: RMS=0.0073, 频谱重心=1400Hz, 场景提示=quiet_indoor

### 样本 2072: street_pedestrian-barcelona-142-4305-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.860), Outside, urban or manmade(0.185), Children playing(0.179)
- **音频特征**: RMS=0.0025, 频谱重心=1755Hz, 场景提示=mixed_environment

### 样本 2073: airport-barcelona-2-101-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.810), Clip-clop(0.189), Outside, urban or manmade(0.175)
- **音频特征**: RMS=0.0027, 频谱重心=1303Hz, 场景提示=quiet_indoor

### 样本 2074: metro_station-paris-80-2169-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.372), Train(0.309), Rail transport(0.176)
- **音频特征**: RMS=0.0317, 频谱重心=973Hz, 场景提示=mixed_environment

### 样本 2075: tram-milan-1182-45685-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Vehicle(0.311), Train(0.206), Speech(0.192)
- **音频特征**: RMS=0.0140, 频谱重心=913Hz, 场景提示=mixed_environment

### 样本 2076: bus-lyon-1159-43352-a.wav
- **真实场景**: bus
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.834), Vehicle(0.387), Car(0.118)
- **音频特征**: RMS=0.0152, 频谱重心=641Hz, 场景提示=mixed_environment

### 样本 2077: airport-paris-206-6247-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.244)
- **音频特征**: RMS=0.0083, 频谱重心=989Hz, 场景提示=quiet_indoor

### 样本 2078: shopping_mall-stockholm-258-7816-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.794), Music(0.287), Chatter(0.236)
- **音频特征**: RMS=0.0036, 频谱重心=1271Hz, 场景提示=mixed_environment

### 样本 2079: airport-helsinki-4-220-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Clicking(0.245), Speech(0.219)
- **音频特征**: RMS=0.0015, 频谱重心=1385Hz, 场景提示=quiet_indoor

### 样本 2080: shopping_mall-london-256-7702-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.803), Chatter(0.106)
- **音频特征**: RMS=0.0022, 频谱重心=1572Hz, 场景提示=mixed_environment

### 样本 2081: airport-vienna-209-6347-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Silence(0.184)
- **音频特征**: RMS=0.0016, 频谱重心=894Hz, 场景提示=quiet_indoor

### 样本 2082: bus-milan-1083-40552-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.806), Vehicle(0.359)
- **音频特征**: RMS=0.0222, 频谱重心=876Hz, 场景提示=mixed_environment

### 样本 2083: metro_station-prague-1130-40960-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.820), Horse(0.285), Clip-clop(0.284)
- **音频特征**: RMS=0.0032, 频谱重心=1461Hz, 场景提示=mixed_environment

### 样本 2084: street_pedestrian-stockholm-155-4715-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Run(0.426), Speech(0.397), Walk, footsteps(0.324)
- **音频特征**: RMS=0.0059, 频谱重心=924Hz, 场景提示=quiet_indoor

### 样本 2085: bus-paris-32-994-a.wav
- **真实场景**: bus
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.725), Vehicle(0.402), Music(0.119)
- **音频特征**: RMS=0.0181, 频谱重心=1100Hz, 场景提示=mixed_environment

### 样本 2086: metro-helsinki-222-6749-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.693), Vehicle(0.237), Train(0.136)
- **音频特征**: RMS=0.0145, 频谱重心=846Hz, 场景提示=mixed_environment

### 样本 2087: public_square-stockholm-121-3560-a.wav
- **真实场景**: public_square
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.701), Vehicle(0.169)
- **音频特征**: RMS=0.0053, 频谱重心=1207Hz, 场景提示=quiet_indoor

### 样本 2088: park-prague-1185-44522-a.wav
- **真实场景**: park
- **AE预测**: street_traffic
- **AS预测**: park
- **检测到的事件**: Vehicle(0.237), Speech(0.179)
- **音频特征**: RMS=0.0071, 频谱重心=620Hz, 场景提示=quiet_indoor

### 样本 2089: shopping_mall-stockholm-137-4151-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.639), Clip-clop(0.177), Horse(0.158)
- **音频特征**: RMS=0.0035, 频谱重心=1165Hz, 场景提示=quiet_indoor

### 样本 2090: park-lyon-1144-42608-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.725), Animal(0.166), Silence(0.155)
- **音频特征**: RMS=0.0007, 频谱重心=1067Hz, 场景提示=quiet_indoor

### 样本 2091: public_square-london-113-3284-a.wav
- **真实场景**: public_square
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.743), Clip-clop(0.201), Music(0.188)
- **音频特征**: RMS=0.0021, 频谱重心=1117Hz, 场景提示=quiet_indoor

### 样本 2092: tram-barcelona-275-8391-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.736), Sliding door(0.158), Door(0.148)
- **音频特征**: RMS=0.0073, 频谱重心=1080Hz, 场景提示=quiet_indoor

### 样本 2093: street_pedestrian-london-149-4499-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.756), Run(0.193), Animal(0.159)
- **音频特征**: RMS=0.0016, 频谱重心=1109Hz, 场景提示=quiet_indoor

### 样本 2094: bus-lisbon-1123-41297-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.687), Vehicle(0.212)
- **音频特征**: RMS=0.0082, 频谱重心=1054Hz, 场景提示=quiet_indoor

### 样本 2095: public_square-london-113-3273-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.416), Animal(0.133), Clip-clop(0.105)
- **音频特征**: RMS=0.0027, 频谱重心=1170Hz, 场景提示=quiet_indoor

### 样本 2096: airport-lisbon-1122-40344-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.723), Clip-clop(0.219), Animal(0.178)
- **音频特征**: RMS=0.0040, 频谱重心=1390Hz, 场景提示=mixed_environment

### 样本 2097: tram-paris-195-5908-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.757), Vehicle(0.718), Field recording(0.375)
- **音频特征**: RMS=0.0235, 频谱重心=382Hz, 场景提示=mixed_environment

### 样本 2098: street_pedestrian-lisbon-1174-44260-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.597), Animal(0.152), Clip-clop(0.114)
- **音频特征**: RMS=0.0033, 频谱重心=1042Hz, 场景提示=quiet_indoor

### 样本 2099: shopping_mall-paris-257-7809-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.769)
- **音频特征**: RMS=0.0033, 频谱重心=1402Hz, 场景提示=mixed_environment

### 样本 2100: shopping_mall-paris-133-4001-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.551), Music(0.476)
- **音频特征**: RMS=0.0032, 频谱重心=1366Hz, 场景提示=mixed_environment

### 样本 2101: airport-stockholm-207-6288-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.644), Animal(0.362), Sheep(0.239)
- **音频特征**: RMS=0.0035, 频谱重心=1399Hz, 场景提示=mixed_environment

### 样本 2102: metro-lyon-1201-44608-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.615), Air brake(0.189), Bus(0.120)
- **音频特征**: RMS=0.0170, 频谱重心=1447Hz, 场景提示=mixed_environment

### 样本 2103: metro-lisbon-1119-41979-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.628), Train(0.573), Speech(0.428)
- **音频特征**: RMS=0.0223, 频谱重心=641Hz, 场景提示=mixed_environment

### 样本 2104: metro_station-lyon-1077-44062-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.773), Chatter(0.179), Music(0.146)
- **音频特征**: RMS=0.0035, 频谱重心=1289Hz, 场景提示=mixed_environment

### 样本 2105: airport-london-6-300-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.571), Clicking(0.157), Typing(0.105)
- **音频特征**: RMS=0.0020, 频谱重心=1112Hz, 场景提示=quiet_indoor

### 样本 2106: metro-milan-1218-45486-a.wav
- **真实场景**: metro
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.624), Vehicle(0.275), Music(0.161)
- **音频特征**: RMS=0.0168, 频谱重心=790Hz, 场景提示=mixed_environment

### 样本 2107: tram-lyon-1103-41716-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.802), Bird(0.332), Pigeon, dove(0.281)
- **音频特征**: RMS=0.0062, 频谱重心=1157Hz, 场景提示=quiet_indoor

### 样本 2108: airport-lisbon-1000-41411-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.811), Chatter(0.157)
- **音频特征**: RMS=0.0045, 频谱重心=1489Hz, 场景提示=mixed_environment

### 样本 2109: park-paris-99-2810-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Speech(0.763), Outside, urban or manmade(0.138), Music(0.121)
- **音频特征**: RMS=0.0030, 频谱重心=1138Hz, 场景提示=quiet_indoor

### 样本 2110: street_pedestrian-barcelona-261-7911-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.785), Keys jangling(0.106), Vehicle(0.103)
- **音频特征**: RMS=0.0046, 频谱重心=1161Hz, 场景提示=quiet_indoor

### 样本 2111: tram-milan-1146-42519-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.747), Vehicle(0.324)
- **音频特征**: RMS=0.0096, 频谱重心=712Hz, 场景提示=quiet_indoor

### 样本 2112: public_square-stockholm-119-3502-a.wav
- **真实场景**: public_square
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Speech(0.456), Vehicle(0.341), Fire(0.211)
- **音频特征**: RMS=0.0078, 频谱重心=1376Hz, 场景提示=quiet_indoor

### 样本 2113: park-barcelona-89-2447-a.wav
- **真实场景**: park
- **AE预测**: park
- **AS预测**: public_square
- **检测到的事件**: Animal(0.515), Speech(0.298), Horse(0.291)
- **音频特征**: RMS=0.0021, 频谱重心=869Hz, 场景提示=quiet_indoor

### 样本 2114: street_pedestrian-milan-1080-41306-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.493), Chink, clink(0.124)
- **音频特征**: RMS=0.0015, 频谱重心=1087Hz, 场景提示=quiet_indoor

### 样本 2115: street_pedestrian-prague-1085-41608-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.476), Clip-clop(0.328), Horse(0.318)
- **音频特征**: RMS=0.0021, 频谱重心=1020Hz, 场景提示=quiet_indoor

### 样本 2116: metro-helsinki-44-1326-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.636), Vehicle(0.444), Rumble(0.279)
- **音频特征**: RMS=0.0456, 频谱重心=458Hz, 场景提示=mixed_environment

### 样本 2117: park-prague-1092-42220-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.713), Vehicle(0.310)
- **音频特征**: RMS=0.0055, 频谱重心=629Hz, 场景提示=quiet_indoor

### 样本 2118: metro_station-lisbon-1020-41753-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.886), Vehicle(0.148), Outside, urban or manmade(0.135)
- **音频特征**: RMS=0.0183, 频谱重心=1069Hz, 场景提示=mixed_environment

### 样本 2119: tram-london-190-5829-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.621), Vehicle(0.599), Train(0.588)
- **音频特征**: RMS=0.0133, 频谱重心=706Hz, 场景提示=mixed_environment

### 样本 2120: street_pedestrian-stockholm-156-4738-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.808), Outside, urban or manmade(0.146), Run(0.114)
- **音频特征**: RMS=0.0096, 频谱重心=1028Hz, 场景提示=quiet_indoor

### 样本 2121: shopping_mall-lyon-1196-45621-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.539), Clip-clop(0.238), Horse(0.211)
- **音频特征**: RMS=0.0022, 频谱重心=1626Hz, 场景提示=mixed_environment

### 样本 2122: shopping_mall-helsinki-129-3856-a.wav
- **真实场景**: shopping_mall
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.829), Animal(0.152), Clip-clop(0.105)
- **音频特征**: RMS=0.0027, 频谱重心=1514Hz, 场景提示=mixed_environment

### 样本 2123: metro-paris-53-1560-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Speech(0.417), Sliding door(0.244), Vehicle(0.218)
- **音频特征**: RMS=0.0082, 频谱重心=1173Hz, 场景提示=quiet_indoor

### 样本 2124: airport-milan-1108-43385-a.wav
- **真实场景**: airport
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.674)
- **音频特征**: RMS=0.0019, 频谱重心=1335Hz, 场景提示=quiet_indoor

### 样本 2125: metro_station-vienna-87-2368-a.wav
- **真实场景**: metro_station
- **AE预测**: metro_station
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.790), Vehicle(0.258)
- **音频特征**: RMS=0.0072, 频谱重心=801Hz, 场景提示=quiet_indoor

### 样本 2126: airport-milan-1172-45082-a.wav
- **真实场景**: airport
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.543), Animal(0.149), Vehicle(0.123)
- **音频特征**: RMS=0.0029, 频谱重心=1682Hz, 场景提示=mixed_environment

### 样本 2127: public_square-vienna-122-3620-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.552), Animal(0.186), Silence(0.179)
- **音频特征**: RMS=0.0013, 频谱重心=804Hz, 场景提示=quiet_indoor

### 样本 2128: street_traffic-london-270-8222-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Speech(0.636), Animal(0.206), Vehicle(0.179)
- **音频特征**: RMS=0.0041, 频谱重心=1317Hz, 场景提示=quiet_indoor

### 样本 2129: street_traffic-lyon-1029-40200-a.wav
- **真实场景**: street_traffic
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Animal(0.302), Speech(0.268), Bird(0.179)
- **音频特征**: RMS=0.0128, 频谱重心=528Hz, 场景提示=mixed_environment

### 样本 2130: airport-paris-206-6249-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Horse(0.205), Clip-clop(0.181), Animal(0.171)
- **音频特征**: RMS=0.0093, 频谱重心=1009Hz, 场景提示=quiet_indoor

### 样本 2131: street_pedestrian-lisbon-1174-45273-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: public_square
- **检测到的事件**: Speech(0.863), Clip-clop(0.180), Animal(0.145)
- **音频特征**: RMS=0.0032, 频谱重心=1076Hz, 场景提示=quiet_indoor

### 样本 2132: bus-prague-1120-41266-a.wav
- **真实场景**: bus
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.463), Vehicle(0.173)
- **音频特征**: RMS=0.0130, 频谱重心=1091Hz, 场景提示=mixed_environment

### 样本 2133: street_pedestrian-stockholm-156-4746-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.858), Run(0.447), Outside, urban or manmade(0.249)
- **音频特征**: RMS=0.0070, 频谱重心=1193Hz, 场景提示=quiet_indoor

### 样本 2134: street_pedestrian-milan-1005-40762-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: airport
- **检测到的事件**: Speech(0.820), Outside, urban or manmade(0.107)
- **音频特征**: RMS=0.0023, 频谱重心=1205Hz, 场景提示=quiet_indoor

### 样本 2135: park-helsinki-94-2630-a.wav
- **真实场景**: park
- **AE预测**: public_square
- **AS预测**: park
- **检测到的事件**: Speech(0.551), Boat, Water vehicle(0.324), Vehicle(0.253)
- **音频特征**: RMS=0.0022, 频谱重心=1175Hz, 场景提示=quiet_indoor

### 样本 2136: metro_station-prague-1118-40369-a.wav
- **真实场景**: metro_station
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Patter(0.226)
- **音频特征**: RMS=0.0032, 频谱重心=1165Hz, 场景提示=quiet_indoor

### 样本 2137: tram-barcelona-180-5592-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: tram
- **检测到的事件**: Speech(0.742), Music(0.264), Vehicle(0.239)
- **音频特征**: RMS=0.0258, 频谱重心=543Hz, 场景提示=mixed_environment

### 样本 2138: airport-prague-1015-40987-a.wav
- **真实场景**: airport
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Speech(0.798), Animal(0.299), Clip-clop(0.294)
- **音频特征**: RMS=0.0053, 频谱重心=1215Hz, 场景提示=quiet_indoor

### 样本 2139: shopping_mall-prague-1031-43107-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: shopping_mall
- **检测到的事件**: Silence(0.122)
- **音频特征**: RMS=0.0019, 频谱重心=1073Hz, 场景提示=quiet_indoor

### 样本 2140: shopping_mall-lisbon-1176-45569-a.wav
- **真实场景**: shopping_mall
- **AE预测**: airport
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.358), Vehicle(0.108)
- **音频特征**: RMS=0.0014, 频谱重心=1165Hz, 场景提示=quiet_indoor

### 样本 2141: tram-london-279-8475-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: tram
- **检测到的事件**: Speech(0.780), Vehicle(0.142)
- **音频特征**: RMS=0.0023, 频谱重心=1051Hz, 场景提示=quiet_indoor

### 样本 2142: metro_station-barcelona-63-1886-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Vehicle(0.339), Ship(0.131)
- **音频特征**: RMS=0.0212, 频谱重心=1150Hz, 场景提示=mixed_environment

### 样本 2143: tram-milan-1065-41575-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.643), Vehicle(0.335), Train(0.283)
- **音频特征**: RMS=0.0193, 频谱重心=587Hz, 场景提示=mixed_environment

### 样本 2144: metro_station-london-235-7015-a.wav
- **真实场景**: metro_station
- **AE预测**: shopping_mall
- **AS预测**: airport
- **检测到的事件**: Speech(0.756), Mouse(0.171)
- **音频特征**: RMS=0.0048, 频谱重心=1625Hz, 场景提示=mixed_environment

### 样本 2145: tram-stockholm-284-8588-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.758), Vehicle(0.692), Car(0.338)
- **音频特征**: RMS=0.0432, 频谱重心=381Hz, 场景提示=mixed_environment

### 样本 2146: street_traffic-london-169-5175-a.wav
- **真实场景**: street_traffic
- **AE预测**: street_traffic
- **AS预测**: public_square
- **检测到的事件**: Vehicle(0.280), Animal(0.154), Keys jangling(0.144)
- **音频特征**: RMS=0.0069, 频谱重心=1146Hz, 场景提示=quiet_indoor

### 样本 2147: street_pedestrian-prague-1051-41335-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.871), Outside, urban or manmade(0.130), Animal(0.124)
- **音频特征**: RMS=0.0047, 频谱重心=1306Hz, 场景提示=mixed_environment

### 样本 2148: metro_station-lyon-1167-45030-a.wav
- **真实场景**: metro_station
- **AE预测**: metro
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.350), Vehicle(0.195), Train(0.121)
- **音频特征**: RMS=0.0061, 频谱重心=1108Hz, 场景提示=quiet_indoor

### 样本 2149: tram-lisbon-1191-45384-a.wav
- **真实场景**: tram
- **AE预测**: bus
- **AS预测**: metro
- **检测到的事件**: Speech(0.848), Vehicle(0.382), Music(0.200)
- **音频特征**: RMS=0.0077, 频谱重心=1292Hz, 场景提示=quiet_indoor

### 样本 2150: airport-vienna-13-536-a.wav
- **真实场景**: airport
- **AE预测**: public_square
- **AS预测**: street_pedestrian
- **检测到的事件**: Inside, small room(0.143), Scissors(0.123), Speech(0.117)
- **音频特征**: RMS=0.0014, 频谱重心=1413Hz, 场景提示=quiet_indoor

### 样本 2151: tram-lyon-1091-43169-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.790), Vehicle(0.586), Bus(0.184)
- **音频特征**: RMS=0.0120, 频谱重心=652Hz, 场景提示=mixed_environment

### 样本 2152: tram-prague-1151-43916-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.568), Vehicle(0.507), Field recording(0.124)
- **音频特征**: RMS=0.0232, 频谱重心=656Hz, 场景提示=mixed_environment

### 样本 2153: street_pedestrian-prague-1085-40630-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: airport
- **AS预测**: street_pedestrian
- **检测到的事件**: Animal(0.145)
- **音频特征**: RMS=0.0019, 频谱重心=1096Hz, 场景提示=quiet_indoor

### 样本 2154: tram-prague-1109-41829-a.wav
- **真实场景**: tram
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Train(0.528), Vehicle(0.416), Rail transport(0.414)
- **音频特征**: RMS=0.0364, 频谱重心=612Hz, 场景提示=mixed_environment

### 样本 2155: shopping_mall-helsinki-130-3914-a.wav
- **真实场景**: shopping_mall
- **AE预测**: shopping_mall
- **AS预测**: street_pedestrian
- **检测到的事件**: Speech(0.824), Clip-clop(0.107), Outside, urban or manmade(0.105)
- **音频特征**: RMS=0.0031, 频谱重心=1547Hz, 场景提示=mixed_environment

### 样本 2156: metro-paris-54-1578-a.wav
- **真实场景**: metro
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.750), Vehicle(0.226)
- **音频特征**: RMS=0.0062, 频谱重心=737Hz, 场景提示=quiet_indoor

### 样本 2157: metro-prague-1016-40633-a.wav
- **真实场景**: metro
- **AE预测**: metro
- **AS预测**: bus
- **检测到的事件**: Vehicle(0.348), Train(0.301), Railroad car, train wagon(0.211)
- **音频特征**: RMS=0.0147, 频谱重心=916Hz, 场景提示=mixed_environment

### 样本 2158: tram-lyon-1112-41192-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: metro
- **检测到的事件**: Speech(0.684), Vehicle(0.271)
- **音频特征**: RMS=0.0086, 频谱重心=516Hz, 场景提示=quiet_indoor

### 样本 2159: street_pedestrian-paris-265-8066-a.wav
- **真实场景**: street_pedestrian
- **AE预测**: street_pedestrian
- **AS预测**: metro_station
- **检测到的事件**: Speech(0.151), Silence(0.127), Animal(0.120)
- **音频特征**: RMS=0.0024, 频谱重心=945Hz, 场景提示=quiet_indoor

### 样本 2160: public_square-prague-1111-41309-a.wav
- **真实场景**: public_square
- **AE预测**: public_square
- **AS预测**: street_traffic
- **检测到的事件**: Silence(0.178)
- **音频特征**: RMS=0.0057, 频谱重心=1359Hz, 场景提示=quiet_indoor

### 样本 2161: tram-paris-196-5915-a.wav
- **真实场景**: tram
- **AE预测**: tram
- **AS预测**: bus
- **检测到的事件**: Speech(0.661), Music(0.284), Vehicle(0.276)
- **音频特征**: RMS=0.0078, 频谱重心=667Hz, 场景提示=quiet_indoor
