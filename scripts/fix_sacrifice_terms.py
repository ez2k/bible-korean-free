#!/usr/bin/env python3
"""
어린이 성경 번역 - 제사 관련 용어 쉽게 변경
대상 연령: 8-10세
"""

import os

korean_dir = 'korean'

# 제사 관련 용어 대체
sacrifice_terms = [
    # 제사 종류
    ('번제를 드리', '다 태워 드리는 제사를 드리'),
    ('번제를', '다 태워 드리는 제사를'),
    ('번제', '다 태워 드리는 제사'),

    ('화목제를 드리', '하나님과 화해하는 제사를 드리'),
    ('화목제를', '하나님과 화해하는 제사를'),
    ('화목제', '화해 제사'),

    ('속죄제를 드리', '죄 용서를 위한 제사를 드리'),
    ('속죄제를', '죄 용서를 위한 제사를'),
    ('속죄제', '죄 용서 제사'),

    ('소제를 드리', '곡식으로 드리는 제사를 드리'),
    ('소제를', '곡식으로 드리는 제사를'),
    ('소제', '곡식 제사'),

    ('속건제를 드리', '빚을 갚는 제사를 드리'),
    ('속건제를', '빚을 갚는 제사를'),
    ('속건제', '빚 갚는 제사'),

    ('요제', '흔들어 드리는 제물'),
    ('거제', '들어올려 드리는 제물'),

    # 제사 장소/도구
    ('제단 위에', '제사 드리는 곳 위에'),
    ('제단에서', '제사 드리는 곳에서'),
    ('제단을', '제사 드리는 곳을'),
    ('제단에', '제사 드리는 곳에'),
    ('제단', '제사 드리는 곳'),

    # 제물
    ('희생제물을', '제사 드리는 짐승을'),
    ('희생제물', '제사 드리는 짐승'),
    ('제물을 드리', '하나님께 바치'),
    ('제물을', '바치는 것을'),
    ('제물', '바치는 것'),

    # 기타 종교 용어
    ('지성소', '가장 거룩한 곳'),
    ('성소', '거룩한 곳'),
    ('성막', '하나님을 만나는 천막'),
    ('회막', '하나님을 만나는 천막'),

    ('언약궤', '하나님과의 약속 상자'),
    ('법궤', '하나님의 법 상자'),

    ('대제사장', '가장 높은 제사장'),

    ('선지자들', '하나님 말씀 전하는 사람들'),
    ('선지자', '하나님 말씀 전하는 사람'),

    # 고대 측정 단위 (간단히)
    ('규빗', '팔꿈치 길이'),  # 약 45cm
    ('세겔', '돈'),
    ('달란트', '큰 돈'),

    # 어려운 단어
    ('역청', '검은 끈끈한 것'),
    ('타작마당', '곡식 떠는 마당'),
    ('진설병', '하나님께 놓는 빵'),
    ('문설주', '문 옆'),

    # 은혜/언약/율법/속죄 - 핵심 용어
    ('은혜를 베풀', '사랑을 베풀'),
    ('은혜를', '사랑과 도움을'),
    ('은혜가', '사랑과 도움이'),
    ('은혜', '사랑과 도움'),

    ('언약을 세우', '약속을 하'),
    ('언약을 맺', '약속을 하'),
    ('언약을 지키', '약속을 지키'),
    ('언약을', '약속을'),
    ('언약의', '약속의'),
    ('언약이', '약속이'),
    ('언약', '약속'),

    ('율법을 지키', '하나님의 법을 지키'),
    ('율법을', '하나님의 법을'),
    ('율법의', '하나님의 법의'),
    ('율법이', '하나님의 법이'),
    ('율법', '하나님의 법'),

    ('속죄하', '죄를 용서받'),
    ('속죄', '죄 용서'),

    # 추가 어려운 용어
    ('거룩하게 하', '특별하게 구별하'),
    ('거룩히', '특별하게'),
    # 거룩한은 유지 - 아이들도 알 수 있는 표현

    ('대적', '적'),
]

def apply_replacements(content, counts):
    """패턴 기반 대체 적용"""
    for old, new in sacrifice_terms:
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            key = f'{old} → {new}'
            counts[key] = counts.get(key, 0) + count
    return content

def fix_file(filepath):
    """단일 파일 수정"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    counts = {}

    content = apply_replacements(content, counts)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return counts
    return {}

def main():
    total_counts = {}
    files_modified = []

    for filename in sorted(os.listdir(korean_dir)):
        if not filename.endswith('.json'):
            continue

        filepath = os.path.join(korean_dir, filename)
        counts = fix_file(filepath)

        if counts:
            files_modified.append(filename)
            for key, count in counts.items():
                total_counts[key] = total_counts.get(key, 0) + count

    print(f"\n=== 제사/종교 용어 수정 완료 ===")
    print(f"수정된 파일: {len(files_modified)}개\n")

    print("변경 내역 (상위 30개):")
    sorted_counts = sorted(total_counts.items(), key=lambda x: x[1], reverse=True)
    total = 0
    for i, (change, count) in enumerate(sorted_counts):
        if i < 30:
            print(f"  {change}: {count}건")
        total += count

    if len(sorted_counts) > 30:
        print(f"  ... 외 {len(sorted_counts) - 30}개 패턴")

    print(f"\n총 {total}건 수정")
    return total

if __name__ == '__main__':
    main()
