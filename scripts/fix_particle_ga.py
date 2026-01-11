#!/usr/bin/env python3
"""
조사 오류 수정 스크립트 (문맥별 정교한 수정)
- "나 하나님가" → "나 하나님이" (1인칭 주어)
- "하나님가 하나님" → "하나님이 하나님" (선언문)
- "하나님가 누구" → "하나님이 누구" (의문문)
- "하나님가 아니" → "하나님이 아니" (부정/의문)
- "네/너희 하나님가" → "네/너희 하나님께서" (소유격 + 존칭)
- 그 외 "하나님가" → "하나님께서" (일반 서술문)
"""

import glob
import re

def fix_particle_ga():
    files = glob.glob('/root/bible-korean-free/korean/*.json')

    stats = {
        '나 하나님가 → 나 하나님이': 0,
        '하나님가 하나님 → 하나님이 하나님': 0,
        '하나님가 누구 → 하나님이 누구': 0,
        '하나님가 아니 → 하나님이 아니': 0,
        '소유격 하나님가 → 하나님께서': 0,
        '기타 하나님가 → 하나님께서': 0
    }

    modified_files = []

    for filepath in sorted(files):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 1. "나 하나님가" → "나 하나님이" (1인칭 주어)
        count = len(re.findall(r'나 하나님가', content))
        stats['나 하나님가 → 나 하나님이'] += count
        content = content.replace('나 하나님가', '나 하나님이')

        # 2. "하나님가 하나님" → "하나님이 하나님" (선언문)
        count = len(re.findall(r'하나님가 하나님', content))
        stats['하나님가 하나님 → 하나님이 하나님'] += count
        content = content.replace('하나님가 하나님', '하나님이 하나님')

        # 3. "하나님가 누구" → "하나님이 누구" (의문문)
        count = len(re.findall(r'하나님가 누구', content))
        stats['하나님가 누구 → 하나님이 누구'] += count
        content = content.replace('하나님가 누구', '하나님이 누구')

        # 4. "하나님가 아니" → "하나님이 아니" (부정/의문)
        count = len(re.findall(r'하나님가 아니', content))
        stats['하나님가 아니 → 하나님이 아니'] += count
        content = content.replace('하나님가 아니', '하나님이 아니')

        # 5. 소유격 뒤 "하나님가" → "하나님께서"
        # 패턴: "네 하나님가", "너희 하나님가", "우리 하나님가" 등
        patterns = [
            (r'네 하나님가', '네 하나님께서'),
            (r'너희 하나님가', '너희 하나님께서'),
            (r'우리 하나님가', '우리 하나님께서'),
            (r'그들의 하나님가', '그들의 하나님께서'),
        ]
        for pattern, replacement in patterns:
            count = len(re.findall(pattern, content))
            stats['소유격 하나님가 → 하나님께서'] += count
            content = content.replace(pattern.replace(r'', ''), replacement)

        # 6. 그 외 남은 "하나님가" → "하나님께서"
        count = content.count('하나님가')
        stats['기타 하나님가 → 하나님께서'] += count
        content = content.replace('하나님가', '하나님께서')

        # 변경된 경우에만 저장
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            modified_files.append(filepath.split('/')[-1])

    return stats, modified_files

if __name__ == '__main__':
    print("조사 오류 수정 시작...")
    stats, modified_files = fix_particle_ga()

    print("\n수정 통계:")
    total = 0
    for pattern, count in stats.items():
        if count > 0:
            print(f"  {pattern}: {count}건")
            total += count
    print(f"  총계: {total}건")

    print(f"\n수정된 파일: {len(modified_files)}개")
    for f in modified_files:
        print(f"  - {f}")

    print("\n완료!")
