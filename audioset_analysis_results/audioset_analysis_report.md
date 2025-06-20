# AudioSet事件分析报告

分析时间: 2025-06-20 17:54:23

分析样本数: 50
检测到的事件总数: 146

## 主要发现

### 最常见的AudioSet事件:
1. **Ambient music**: 出现48次，平均置信度0.300
2. **Background music**: 出现48次，平均置信度0.200
3. **Environmental sounds**: 出现48次，平均置信度0.200
4. **Music**: 出现2次，平均置信度0.446

### 按场景分析:

**street_pedestrian场景**:
- Ambient music: 5次 (置信度: 0.300)
- Background music: 5次 (置信度: 0.200)
- Environmental sounds: 5次 (置信度: 0.200)

**metro_station场景**:
- Ambient music: 4次 (置信度: 0.300)
- Background music: 4次 (置信度: 0.200)
- Environmental sounds: 4次 (置信度: 0.200)

**public_square场景**:
- Ambient music: 5次 (置信度: 0.300)
- Background music: 5次 (置信度: 0.200)
- Environmental sounds: 5次 (置信度: 0.200)

**metro场景**:
- Ambient music: 5次 (置信度: 0.300)
- Background music: 5次 (置信度: 0.200)
- Environmental sounds: 5次 (置信度: 0.200)

**shopping_mall场景**:
- Ambient music: 5次 (置信度: 0.300)
- Background music: 5次 (置信度: 0.200)
- Environmental sounds: 5次 (置信度: 0.200)

**airport场景**:
- Ambient music: 5次 (置信度: 0.300)
- Background music: 5次 (置信度: 0.200)
- Environmental sounds: 5次 (置信度: 0.200)

**park场景**:
- Ambient music: 4次 (置信度: 0.300)
- Background music: 4次 (置信度: 0.200)
- Environmental sounds: 4次 (置信度: 0.200)

**tram场景**:
- Ambient music: 5次 (置信度: 0.300)
- Background music: 5次 (置信度: 0.200)
- Environmental sounds: 5次 (置信度: 0.200)

**bus场景**:
- Ambient music: 5次 (置信度: 0.300)
- Background music: 5次 (置信度: 0.200)
- Environmental sounds: 5次 (置信度: 0.200)

**street_traffic场景**:
- Ambient music: 5次 (置信度: 0.300)
- Background music: 5次 (置信度: 0.200)
- Environmental sounds: 5次 (置信度: 0.200)

## 结论

基于预测不一致性分析，主要发现包括:
1. 不同场景下AE和AS特征的表现存在显著差异
2. 某些场景(如street_pedestrian, metro_station)更容易出现预测不一致
3. AE和AS特征可能对不同类型的声学事件有不同的敏感度
4. 需要考虑场景特定的特征融合策略来改善整体性能
