#!/usr/bin/env python3
"""
어투 일관성 수정 스크립트 (6차)
남은 ~입니다, ~한다 패턴 수정
"""

import glob
import re

def fix_speech_style_6():
    files = glob.glob('/root/bible-korean-free/korean/*.json')

    stats = {
        '것입니다." → 거예요."': 0,
        '말씀하신다." → 말씀하세요."': 0,
        '때문입니다." → 때문이에요."': 0,
        '분이십니다." → 분이세요."': 0,
        '사람입니다." → 사람이에요."': 0,
        '백성입니다." → 백성이에요."': 0,
        '하나입니다." → 하나예요."': 0,
        '이것입니다." → 이거예요."': 0,
        '하나님다." → 하나님이에요."': 0,
        '아니다." → 아니에요."': 0,
        '필요하다." → 필요해요."': 0,
        '두렵다." → 두려워요."': 0,
        '옳다." → 옳아요."': 0,
        '바란다." → 바라요."': 0,
        '더럽힌다." → 더럽혀요."': 0,
        '꾸민다." → 꾸며요."': 0,
        '베푼다." → 베풀어요."': 0,
        '거두신다." → 거두세요."': 0,
        '헐뜯는다." → 헐뜯어요."': 0,
        '합니다." → 해요."': 0,
        '더럽혔다." → 더럽혔어요."': 0,
        '꾸몄다." → 꾸몄어요."': 0,
        '썼다." → 썼어요."': 0,
        '보냈다." → 보냈어요."': 0,
        '멸망시켰다." → 멸망시켰어요."': 0,
        '다녔다." → 다녔어요."': 0,
        '예수다." → 예수예요."': 0,
        '자다." → 자요."': 0,
    }

    modified_files = []

    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 입니다 → 이에요
        count = len(re.findall(r'것입니다\."', content))
        stats['것입니다." → 거예요."'] += count
        content = content.replace('것입니다."', '거예요."')

        count = len(re.findall(r'때문입니다\."', content))
        stats['때문입니다." → 때문이에요."'] += count
        content = content.replace('때문입니다."', '때문이에요."')

        count = len(re.findall(r'분이십니다\."', content))
        stats['분이십니다." → 분이세요."'] += count
        content = content.replace('분이십니다."', '분이세요."')

        count = len(re.findall(r'사람입니다\."', content))
        stats['사람입니다." → 사람이에요."'] += count
        content = content.replace('사람입니다."', '사람이에요."')

        count = len(re.findall(r'백성입니다\."', content))
        stats['백성입니다." → 백성이에요."'] += count
        content = content.replace('백성입니다."', '백성이에요."')

        count = len(re.findall(r'하나입니다\."', content))
        stats['하나입니다." → 하나예요."'] += count
        content = content.replace('하나입니다."', '하나예요."')

        count = len(re.findall(r'이것입니다\."', content))
        stats['이것입니다." → 이거예요."'] += count
        content = content.replace('이것입니다."', '이거예요."')

        count = len(re.findall(r'하나님다\."', content))
        stats['하나님다." → 하나님이에요."'] += count
        content = content.replace('하나님다."', '하나님이에요."')

        count = len(re.findall(r'합니다\."', content))
        stats['합니다." → 해요."'] += count
        content = content.replace('합니다."', '해요."')

        # 다 → 아요/어요
        count = len(re.findall(r'말씀하신다\."', content))
        stats['말씀하신다." → 말씀하세요."'] += count
        content = content.replace('말씀하신다."', '말씀하세요."')

        count = len(re.findall(r'아니다\."', content))
        stats['아니다." → 아니에요."'] += count
        content = content.replace('아니다."', '아니에요."')

        count = len(re.findall(r'필요하다\."', content))
        stats['필요하다." → 필요해요."'] += count
        content = content.replace('필요하다."', '필요해요."')

        count = len(re.findall(r'두렵다\."', content))
        stats['두렵다." → 두려워요."'] += count
        content = content.replace('두렵다."', '두려워요."')

        count = len(re.findall(r'옳다\."', content))
        stats['옳다." → 옳아요."'] += count
        content = content.replace('옳다."', '옳아요."')

        count = len(re.findall(r'바란다\."', content))
        stats['바란다." → 바라요."'] += count
        content = content.replace('바란다."', '바라요."')

        count = len(re.findall(r'더럽힌다\."', content))
        stats['더럽힌다." → 더럽혀요."'] += count
        content = content.replace('더럽힌다."', '더럽혀요."')

        count = len(re.findall(r'꾸민다\."', content))
        stats['꾸민다." → 꾸며요."'] += count
        content = content.replace('꾸민다."', '꾸며요."')

        count = len(re.findall(r'베푼다\."', content))
        stats['베푼다." → 베풀어요."'] += count
        content = content.replace('베푼다."', '베풀어요."')

        count = len(re.findall(r'거두신다\."', content))
        stats['거두신다." → 거두세요."'] += count
        content = content.replace('거두신다."', '거두세요."')

        count = len(re.findall(r'헐뜯는다\."', content))
        stats['헐뜯는다." → 헐뜯어요."'] += count
        content = content.replace('헐뜯는다."', '헐뜯어요."')

        # 과거형 추가
        count = len(re.findall(r'더럽혔다\."', content))
        stats['더럽혔다." → 더럽혔어요."'] += count
        content = content.replace('더럽혔다."', '더럽혔어요."')

        count = len(re.findall(r'꾸몄다\."', content))
        stats['꾸몄다." → 꾸몄어요."'] += count
        content = content.replace('꾸몄다."', '꾸몄어요."')

        count = len(re.findall(r'썼다\."', content))
        stats['썼다." → 썼어요."'] += count
        content = content.replace('썼다."', '썼어요."')

        count = len(re.findall(r'보냈다\."', content))
        stats['보냈다." → 보냈어요."'] += count
        content = content.replace('보냈다."', '보냈어요."')

        count = len(re.findall(r'멸망시켰다\."', content))
        stats['멸망시켰다." → 멸망시켰어요."'] += count
        content = content.replace('멸망시켰다."', '멸망시켰어요."')

        count = len(re.findall(r'다녔다\."', content))
        stats['다녔다." → 다녔어요."'] += count
        content = content.replace('다녔다."', '다녔어요."')

        count = len(re.findall(r'예수다\."', content))
        stats['예수다." → 예수예요."'] += count
        content = content.replace('예수다."', '예수예요."')

        count = len(re.findall(r'자다\."', content))
        stats['자다." → 자요."'] += count
        content = content.replace('자다."', '자요."')

        # 변경된 경우에만 저장
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_files.append(filepath.split('/')[-1])

    return stats, modified_files

if __name__ == '__main__':
    print("어투 일관성 수정 (6차) 시작...")
    print("남은 ~입니다, ~한다 패턴 수정\n")

    stats, modified_files = fix_speech_style_6()

    print("수정 통계:")
    total = 0
    for pattern, count in stats.items():
        if count > 0:
            print(f"  {pattern}: {count}건")
            total += count
    print(f"  ─────────────────")
    print(f"  총계: {total}건")

    print(f"\n수정된 파일: {len(modified_files)}개")
    for f in sorted(modified_files):
        print(f"  - {f}")

    print("\n완료!")
